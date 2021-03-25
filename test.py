from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/",methods=['POST'])
def hello():
    return jsonify("Hello")

if __name__ == "__main__":
    app.run(port=1000)
