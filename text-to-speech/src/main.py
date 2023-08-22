"""
    This is the home function for the app
"""

import os
import uuid
from gtts import gTTS
from flask import Flask, render_template, request


app = Flask(__name__)



@app.get("/")
def home():
    return render_template('./index.html')



@app.route('/tts', methods=['POST'])
def tts():
    text = request.form['text']
    if not bool(text): 
        return render_template('index.html', message = "Please enter some text")
    tts = gTTS(text=text, lang='en')
    output_name = uuid.uuid1().hex + ".mp3"

    static_path = os.path.join(app.root_path, 'static')
    output_path = os.path.join(static_path, output_name)
    tts.save(output_path)
    return render_template('index.html', audio_file="static/"+output_name)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
