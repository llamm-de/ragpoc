"""
A trial script for a simple CLI chatbot based on langchain with Ollama and Llama3.1:8b
"""

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

def main():
    # Static variables
    CONTINUE_CONVERSATION = True
    CONFIG = {"configurable": {"thread_id": "abc123"}}

    # Initialize Model
    workflow = StateGraph(state_schema=MessagesState)
    model = ChatOllama(model="llama3.1:latest")
    def call_model(state:MessagesState):
        response = model.invoke(state["messages"])
        return {"messages": response}
    # Define the (single) node in the graph
    workflow.add_edge(START, "model")
    workflow.add_node("model", call_model)
    # Add memory
    memory = MemorySaver()
    app = workflow.compile(checkpointer=memory)

    # REP Loop
    while CONTINUE_CONVERSATION:
        prompt = input(">>> ")
        if prompt == "/bye":
            print("Good bye!")
            CONTINUE_CONVERSATION = False
            break
        input_messages = [HumanMessage(content=prompt)]
        response = app.invoke({"messages": input_messages}, CONFIG)
        print(f"-> {response['messages'][-1].content}")

if __name__ == "__main__":
    main()