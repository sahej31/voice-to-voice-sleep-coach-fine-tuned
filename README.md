# Voice-to-Voice Sleep Coaching Agent (Adapted for Sleep Domain)

## Overview
This project is an intelligent, fully offline voice-to-voice assistant that functions as a personalized sleep coach. It listens to user queries through the microphone, transcribes them with Whisper AI, generates tailored sleep advice using Falcon-7B, and speaks the response using gTTS.

## Key Features
- Sleep-specialized LLM behavior using clinical prompts
- Whisper AI for speech recognition
- gTTS for spoken response
- Entirely offline and modular
- 5 evaluated conversations showing improved sleep-domain performance

## How to Run

```bash
pip install -r requirements.txt
python main.py            # Runs a fixed query from input_audio
python live_agent.py      # Records user voice from mic
```

## Adaptation Details

- **LLM Used**: Falcon-7B-Instruct via Hugging Face
- **TTS**: gTTS
- **STT**: Whisper base
- **Data Injected via Prompting**:
  - Fitbit sleep stage insights
  - Apple Health sleep duration recommendations
  - NIH-backed research on sleep hygiene



