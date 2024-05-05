from flask import Flask
import flask

app = Flask(__name__)

@app.route("/members")
def members():
    response = flask.jsonify({"members": ["Member 1", "Member 2", "Member 3", "Member 4"]})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)
