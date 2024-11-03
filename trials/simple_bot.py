"""
A trial script for a simple CLI chatbot based on langchain with Ollama and Llama3.1:8b
"""

from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

def main():
    CONTINUE_CONVERSATION = True

    # Initialize Model
#    workflow = StateGraph(state_schema=MessagesState)
    model = ChatOllama(model="llama3.1:latest")

    # REP Loop
    while CONTINUE_CONVERSATION:
        prompt = input(">>> ")
        response = model.invoke([HumanMessage(content=prompt)])
        if prompt == "/bye":
            print("Good bye!")
            CONTINUE_CONVERSATION = False
        else:
            print(response.content)

if __name__ == "__main__":
    main()