from csvLoader import URLProcessor
from FaissLoader import FaissLoader
import random
from flask import Flask
import flask

def getSimilars(i):
    setID = URLProcessor.getDataURL("../data/inditex_nou.csv", i, 100)
    faiss_loader = FaissLoader()
    setURL = faiss_loader.cargar_faiss(setID)
    return setURL


app = Flask(__name__)

@app.route("/members")
def members():
    i = random.randint(3, 1000)
    setURLs = getSimilars(i)
    print(setURLs)
    response = flask.jsonify({"members": setURLs})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)

