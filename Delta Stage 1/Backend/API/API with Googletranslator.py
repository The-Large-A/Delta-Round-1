#API with Googletranslator

from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES, LANGCODES

app = Flask(__name__)
translator = Translator()

def detect_language():
    try:
        text = request.json.get('text', '')
        detected_language = translator.detect(text)
        response_data = {
            "detected_language": LANGUAGES.get(detected_language.lang, "Unknown"),
            #"lang_name" : LANGUAGES.get()
        }
        return jsonify(response_data), 200
    except:
        return jsonify({"error": "Language detection failed. Please check your input."}), 400
    

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        source = request.json.get('source_language', 'auto')
        target = request.json.get('target_language', 'en')
        text = request.json.get('text', '')

        translated_text = translator.translate(text, src=source, dest=target)
        
        response_data = {
            "source_language": LANGUAGES.get(source, "Unknown"),
            "target_language": LANGUAGES.get(target, "Unknown"),
            "translated_text": translated_text.text
        }
        return jsonify(response_data), 200
    except:
        return jsonify({"error": "Translation failed. Please check your input."}), 
    
if __name__ == '__main__': 
   app.run()