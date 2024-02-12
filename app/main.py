import logging
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, Query
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import (
    DirectoryLoader,
    UnstructuredMarkdownLoader,
)
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

load_dotenv()
logging.basicConfig(level=logging.INFO)

db_path = './db'

# Load the documents from the data directory
loader = DirectoryLoader('../data/', glob='**/*.md', loader_cls=UnstructuredMarkdownLoader)
docs = loader.load()

# Split the documents into chunks with a maximum size of 1000 characters and an overlap of 0 characters
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

# Split the documents into chunks
texts = text_splitter.split_documents(docs)

# Create the embeddings object
embeddings = OpenAIEmbeddings()


# Create the vector store
if Path(db_path).exists():
    logging.info(f'Loading existing database from {db_path}')
    vectorDB = Chroma(persist_directory=db_path, embedding_function=embeddings)
else:
    logging.info(f'Creating new database at {db_path}')
    vectorDB = Chroma.from_documents(texts, embeddings, persist_directory=db_path)  # Adjust this line accordingly

# Create the retriever
retriever = vectorDB.as_retriever(search_type='similarity', search_kwargs={'k': 2})

# Create the QA model
qa = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name='gpt-3.5-turbo'), chain_type='stuff', retriever=retriever, return_source_documents=True
)

logging.info('Ready to answer questions!')

app = FastAPI()


@app.get(
    '/ask',
    response_model=str,
    tags=['QA'],
    description='Ask a question',
    response_description='The answer to the question based on the documents in the data directory.',
)
async def ask(query: str = Query(..., example='What is EchoVerse?')) -> str:
    """Get the answer to a question based on the documents in the data directory.

    Args:
        query (str, optional): User Question.
          Defaults to Query(..., example="What is EchoVerse?").

    Note:
        The question should be related to the documents in the data directory.
        Otherwise the answer should be "I don't know".

    Example 1: Q: "What is EchoVerse?"
              A: "EchoVerse is ..."

    Example 2: Q: "What is the purpose of FastAPI?"
              A: "I don't know what FastAPI is."

    Returns:
        str: The answer to the question based on the documents
          in the data directory.
    """
    result = qa({'query': query})
    logging.info(f'Q: {query}\nA:{result["result"]}\n')
    return result['result']
