from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def home():
    translated_text = ""
    original_text = ""
    if request.method == "POST":
        original_text = request.form["text"]
        if original_text.strip() != "":
            result = translator.translate(original_text, src="en", dest="vi")
            translated_text = result.text

    return render_template("index.html", translated=translated_text, original=original_text)

if __name__ == "__main__":
    app.run(debug=True)
