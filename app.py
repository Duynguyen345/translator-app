from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Translator API is running 🚀"

@app.route("/translate", methods=["GET"])
def translate():
    text = request.args.get("text", "")
    target = request.args.get("target", "en")
    if not text:
        return jsonify({"error": "Missing text"}), 400
    
    try:
        translated = GoogleTranslator(source="auto", target=target).translate(text)
        return jsonify({"translated": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
