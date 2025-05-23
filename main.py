
from whisper_transcriber import transcribe_audio
from local_chatbot import get_sleep_response
from tts_generator import speak_response
import os

os.makedirs("input_audio", exist_ok=True)
os.makedirs("output_audio", exist_ok=True)

input_path = "input_audio/query1.wav"
output_path = "output_audio/response1.mp3"

user_query = transcribe_audio(input_path)
bot_reply = get_sleep_response(user_query)
speak_response(bot_reply, output_path)
