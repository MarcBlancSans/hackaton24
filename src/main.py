from csvLoader import URLProcessor
from FaissLoader import FaissLoader

from flask import Flask
import flask

def getSimilars(i):
    setID = URLProcessor.getDataURL("../data/inditex_nou.csv", i, 10)
    faiss_loader = FaissLoader()
    setURL = faiss_loader.cargar_faiss(setID)
    return setURL


app = Flask(__name__)

@app.route("/members")
def members():
    
    setURLs = getSimilars(3)
    print(setURLs)
    response = flask.jsonify({"members": [setURLs]})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)

