from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Howdy Y'all   <h1>Yeehaw<h1>"


if __name__ == "__main__":
    app.run()