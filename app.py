from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():  # put application's code here
    return render_template("index.html", string=string)


@app.route("/wordCount", methods=["POST", "GET"])
def register():
    string = request.form.get("string")
    return render_template("wordCount.html")


if __name__ == '__main__':
    app.run()