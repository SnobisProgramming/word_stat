from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():  # put application's code here
    return render_template("index.html")


@app.route("/wordCount", methods=["POST", "GET"])
def wordCount():
    string = request.args.get("string")
    wordCount = len(string.split())

    totalCharCount = 0
    for word in string.split(" "):
        totalCharCount += len(word)

    averageWordLength = totalCharCount / wordCount

    return render_template("wordCount.html", charCount=len(string),
                           wordCount=wordCount, averageWordLength=averageWordLength)


if __name__ == '__main__':
    app.run()