# TalkSync

Real-time multilingual translation solution for client calls supporting English ↔ Hindi / Punjabi.

## Overview

TalkSync is an AI-powered system that converts speech into text, translates it instantly, and generates translated audio output.  
It is designed to help teams communicate effectively with English-speaking clients.

## Features

- Speech-to-Text using Faster-Whisper
- Bidirectional Translation (English ↔ Hindi / Punjabi)
- Text-to-Speech playback
- Transcript and translated output display
- Streamlit-based UI
- Demo audio support

## Tech Stack

- Python
- Streamlit
- Faster-Whisper
- deep-translator (GoogleTranslator)
- gTTS

## Project Structure

TalkSync/   
│    
├── streamlit_app.py     
├── requirements.txt    
├── app/       
│   ├── config.py    
│   ├── services/   
│   └── core/    
├── demo_data/    
    
## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Run the app:

streamlit run streamlit_app.py

3. Open in browser:

http://localhost:8501

## Future Improvements

- Live microphone streaming
- Zoom / Google Meet integration
- Speaker identification
- Role-based audio routing
- Docker & cloud deployment
