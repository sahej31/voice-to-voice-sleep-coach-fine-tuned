
from gtts import gTTS

def speak_response(text, output_path):
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)
