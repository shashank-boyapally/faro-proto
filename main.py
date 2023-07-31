# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, session, request, jsonify
from flask_cors import CORS, cross_origin
import os
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import DirectoryLoader
from flask_session import Session
from langchain.chat_models import ChatOpenAI
import openai
import chromadb
from chromadb.config import Settings
import time
from langchain.embeddings import GPT4AllEmbeddings

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
app.secret_key = "your_secret_key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
Session(app)


# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.


os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/ask", methods=["GET"])
def hello_world():
    global qa
    query = request.args.get("query")
    chathistory = session.get("chathistory", [])
    session["chathistory"] = []
    # print(qa)
    result = qa({"question": query, "chat_history": chathistory})
    # print(result["chat_history"])
    session["chathistory"] = result["chat_history"]
    print(result["answer"])
    return jsonify({"answer": result["answer"]})


def setqa(abc):
    global qa
    qa = abc


# main driver function
if __name__ == "__main__":
    # run() method of Flask class runs the application
    # on the local development server.
    documents = DirectoryLoader("output").load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    documents = text_splitter.split_documents(documents)
    print("+++++++++1=========")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    print("+++++++++2=========")
    embeddings = OpenAIEmbeddings()
    embeddings = GPT4AllEmbeddings()
    print("+++++++++3=========")

    # client = chromadb.Client(
    #     Settings(
    #         persist_directory="/persist"  # Optional, defaults to .chromadb/ in the current directory
    #     )
    # )

    # vec = client.create_collection(name="newcol")
    # vec.add(documents=documents, ids=["id1"] * len(documents))
    # vec.as
    vectorstore = Chroma.from_documents(
        documents=documents[0:100],
        embedding=embeddings,
        # client=client,
        # collection_name="newcol",
    )
    print("hi")
    for i in range(1, 9):
        print("hi")
        vectorstore.add_documents(documents=documents[i * 10 : (i + 1) * 10])
    vectorstore.aadd_documents(documents=documents[900:])
    print("+++++++++4=========")
    llm = OpenAI(temperature=0.9, model="text-davinci-003")
    print("+++++++++5=========")
    qa = ConversationalRetrievalChain.from_llm(
        llm,
        vectorstore.as_retriever(),
        memory=memory,
    )

    setqa(qa)
    app.run()
