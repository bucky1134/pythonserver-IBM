from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench",methods=['GET'])
def englishToFrench():
    textToTranslate = request.args.get("text")
    french_text=translator.englis_to_french(textToTranslate)
    return french_text

@app.route("/frenchToEnglish",methods=['GET'])
def frenchToEnglish():
    textToTranslate = request.args.get("text")
    english_text=translator.french_to_english(textToTranslate)
    return english_text

@app.route("/")
def renderIndexPage():
    return 
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
