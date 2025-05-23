
import sounddevice as sd
from scipy.io.wavfile import write
import whisper
from gtts import gTTS
from playsound import playsound
from local_chatbot import get_sleep_response

def record_audio(filename="user_input.wav", duration=8, fs=16000):
    print("🎤 Listening for 8 seconds... Speak now")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, audio)
    print("✅ Recorded.")

def transcribe_audio(filename="user_input.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    return result["text"]

def speak(text, filename="bot_response.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    playsound(filename)

record_audio()
user_input = transcribe_audio()
bot_reply = get_sleep_response(user_input)
speak(bot_reply)
