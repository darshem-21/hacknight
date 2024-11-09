import os
from gtts import gTTS
from playsound import playsound

def text_to_speech(text, lang='en'):
    file = gTTS(text=text, lang=lang)
    filename = 'speech.mp3'
    file.save(filename)
    
    # Play the audio file
    playsound(filename)

text_to_speech("Hello, this is error.")