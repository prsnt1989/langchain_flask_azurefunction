import logging
import os

import azure.functions as func
from flask import Flask, redirect, render_template, request, url_for
from langchain import OpenAI
from langchain.docstore.document import Document
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

import requests

app = Flask(__name__)

os.environ["OPENAI_API_KEY"] = "*******"


def get_wiki_data(title, first_paragraph_only):
    url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&explaintext=1&titles={title}"
    if first_paragraph_only:
        url += "&exintro=1"
    data = requests.get(url).json()
    return Document(
        page_content=list(data["query"]["pages"].values())[0]["extract"],
        metadata={"source": f"https://en.wikipedia.org/wiki/{title}"},
    )


sources = [
    get_wiki_data("Unix", True),
    get_wiki_data("Microsoft_Windows", True),
    get_wiki_data("Linux", True),
    get_wiki_data("Seinfeld", True),
]

chain = load_qa_with_sources_chain(OpenAI(temperature=0))


# Code for azure function
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(app.wsgi_app).handle(req, context)


# code for Flask
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = chain(
            {
                "input_documents": sources,
                "question": question,
            },
            return_only_outputs=True,
        )["output_text"]
        return redirect(url_for("index", items=response, question=question))
    result = request.args.get("items")
    question = request.args.get("question")
    return render_template("index.html", items={"question": question, "result": result})
