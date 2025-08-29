from flask import Flask, render_template, request
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    if request.method == "POST":
        text = request.form["text"]
        translated_text = GoogleTranslator(source='en', target='vi').translate(text)
    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
