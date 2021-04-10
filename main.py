from flask import Flask, render_template

# Create Flask instance.
app = Flask(__name__)

# Create route decorator.
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


if __name__ == "__main__":
    app.run()