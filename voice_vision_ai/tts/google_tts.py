from gtts import gTTS
import os

def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")