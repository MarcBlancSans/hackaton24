from csvLoader import URLProcessor
from FaissLoader import FaissLoader
from flask import Flask
import flask


faiss_loader = FaissLoader()
faiss_loader.loadEmbeddings(2,10000)
print("JA")

def getSimilars():
    #setID = URLProcessor.getDataURL("../data/inditex_nou.csv", i, 100)
    setURL = faiss_loader.cargar_faiss()
    return setURL




app = Flask(__name__)

@app.route("/members")
def members():
    setURLs = getSimilars()
    print(setURLs)
    response = flask.jsonify({"members": setURLs})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)

