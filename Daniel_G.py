from flask import Flask
from flask import render_template

Daniel_G = Flask(__name__)

@Daniel_G.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    Daniel_G.run(host="0.0.0.0", port=7777)

