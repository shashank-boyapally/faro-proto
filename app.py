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
from langchain.embeddings import GPT4AllEmbeddings
from gpt4all import GPT4All

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
app.secret_key = "your_secret_key"
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
# Session(app)



#os.environ["OPENAI_API_KEY"] = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")


# print("+++++++++2=========")
# embeddings = OpenAIEmbeddings()
embeddings = GPT4AllEmbeddings()
# print("+++++++++3=========")
client = chromadb.PersistentClient(path="persist/")
# coll = client.create_collection("newcol")
# vec = client.create_collection(name="newcol")
# vectorstore = Chroma.from_documents(
#     documents=documents,
#     embedding=embeddings,
#     persist_directory="/persist",
#     client=client,
#     collection_name="newcol",
# )
vectorstore = Chroma(
    client=client, collection_name="newcol", embedding_function=embeddings
)
# print("hi")
# for i in range(1, 9):
#     print("hi")
#     vectorstore.add_documents(documents=documents[i * 10 : (i + 1) * 10])
# vectorstore.aadd_documents(documents=documents[900:])


# llm = GPT4All(model="wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin", n_threads=8)


session_manager={}



@app.route("/ask", methods=["GET"])
def hello_world():
    qa=None
    session_id=request.args.get("uuid")
    if session_id not in session_manager:
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        llm = OpenAI(temperature=0.9, model="text-davinci-003")
        qa = ConversationalRetrievalChain.from_llm(
            llm,
            vectorstore.as_retriever(),
            memory=memory,
        )
        session_manager[session_id]=None
    else:
        qa=session_manager[session_id]
    query = request.args.get("query")
    # print(qa)
    result = qa({"question": query})
    print(result["answer"])
    session_manager[session_id]=qa
    return jsonify({"answer": result["answer"]})

# @app.before_app_first_request
# def before_first_request():
#     pass

# @app.before_first_request
# def load_data():
#     embeddings = GPT4AllEmbeddings()
#     client = chromadb.PersistentClient(path="persist/")
#     coll = client.create_collection("newcol")

# main driver function
if __name__ == "__main__":
    
    app.run(host="0.0.0.0",port=int("3000"))