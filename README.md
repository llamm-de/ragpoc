# Proof of concept for RAG in a blog application
This is a proof of concept showing the capabilities of RAG LLMs when used with a blog type websystem to index and retrieve data for the postings of the blog. The POC is **not** build for production ready systems and should only be used for demonstrational purpose on a local machine.

## Installation & Set Up
### Prerequisites
In order to get the POC running, some prerequisites must be fulfilled. Mandatory are:
1. [Python 3.11](https://www.python.org/downloads/) or higher installed on your system
2. 

Optional but recommended:
1. [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
2.

### Installing the Large Language Model
In this POC we are using [Ollama](https://ollama.com) as an interface to Llama-3.1 and possible other LLMs. Please follow the installation guide on the [Ollama website](https://ollama.com/download) to get the software up and running.

Next you must install an appropiate LLM that can be used with Ollama. We will proceed here with Llama-3.1 in its 8B parameter version. To d install this, please open a command prompt and type 
```bash 
ollama pull llama3.1:8b
```
This will download the model onto your machine and make it available with Ollama. To check whether it is running properly, type ```ollama run llama3.1:8b```. If everything works fine, you should be asked for a prompt/input to be send to the LLM in order to start the conversation with the chatbot.

Since we want to use an Retrieval Augmented Generation (RAG) Model, we need to also install appropriate embeddings encoder for our LLM. There are various encoders (e.g. OpenAI Ada-002 etc.), but in this case we use the [nomic-embed-text](https://ollama.com/library/nomic-embed-text). It must be installed using Ollama by typing 
```bash
ollama pull nomic-embed-text
```
into the command line.

### Install the required Python packages for the proof on concept
To run the POC, you need to set up the appropriate Python environment and install all packages necessary.

## Running the POC
Yada yada TBC ...
