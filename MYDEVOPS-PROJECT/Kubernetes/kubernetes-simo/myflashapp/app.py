from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Welcome to inspired LLC!</p>"

@app.route("/login")
def hello_login():
    return "<p>Hello, login here !</p>"

@app.route("/signup")
def hello_signup():
    return "<p>Hello, sign up here!</p>"



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
