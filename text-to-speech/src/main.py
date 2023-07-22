"""
    This is the home function for the app
"""

import os
from gtts import gTTS
from flask import Flask, render_template, request

import pyttsx3

engine = pyttsx3.init()
app = Flask(__name__)



@app.get("/")
def home():
    return render_template('index.html')



@app.route('/tts', methods=['POST'])
def tts():
    text = request.form['text']
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    return render_template('index.html', audio_file='output.mp3')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
