# Going through LangChain's 🦜🔗 Tutorial Docs

## Tutorial 01: Build a Simple LLM Application with LCEL
This application will translate text from English into another language. This is a relatively simple LLM application - it's just a single LLM call plus some prompting

Learning objectives:
- Using language models
- Using PromptTemplates and OutputParsers
- Using LangChain Expression Language (LCEL) to chain components together
- Debugging and tracing your application using LangSmith
- Deploying your application with LangServe

## Tutorial 02: Build a Chatbot
This chatbot will be able to have a conversation and remember previous interactions.


## Tutorial 03: Vector stores and retrievers

Covering the follow concepts:
- Documents
- Vector stores
- Retrievers

### Vector stores

To instantiate a vector store we need to provide an embedding model, in this
example we use OpenAI embeddings

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma.from_documents(
    documents,
    embedding=OpenAIEmbeddings(),
)
```

There are different ways to search vector stores two examples include: `similarity_search()`
(which converts string to vector internally before searching) or `similarity_search_by_vector()`
(where you pass it an embedding which is already a vector).

### Retrievers

`VectorStore` objects do not subclass `Runnable` and so can't be integrated into LangChain Expression Language (LCEL) chains.

LangChain `Retrievers` are Runnables and so can be chained in LCEL.

Example included in Juypter Notebook file on retrieval-augmented generation (RAG)

## Tutorial 04: Build an agent

Agents are systems that use LLMs as reasoning engines to determine which actions to take and the inputs to pass them.
After executing actions, the results can be fed back into the LLM to determine whether more actions are needed, or whether it is okay to finish.

