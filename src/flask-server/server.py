from flask import Flask
import flask

app = Flask(__name__)

@app.route("/members")
def members():
    response = flask.jsonify({"members": ["https://static.zara.net/photos///2024/V/4/1/p/6254/473/820/2/w/2048/6254473820_6_2_1.jpg?ts=1699289279252",
                "https://static.zara.net/photos///2024/V/0/2/p/0679/416/251/2/w/2048/0679416251_6_2_1.jpg?ts=1714473877883", 
                "https://static.zara.net/photos///2024/V/0/1/p/2287/595/800/3/w/2048/2287595800_1_1_1.jpg?ts=1711529251643", 
                "https://static.zara.net/photos///2024/W/0/2/p/7545/534/021/2/w/2048/7545534021_6_2_1.jpg?ts=1704963620252", 
                "https://static.zara.net/photos///2024/V/0/1/p/4786/055/802/2/w/2048/4786055802_3_1_1.jpg?ts=1712743908341",
                "https://static.zara.net/photos///2024/V/4/1/p/7145/091/712/2/w/2048/7145091712_6_1_1.jpg?ts=1708594216876"]})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)
