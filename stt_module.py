# src/stt_module.py
import speech_recognition as sr
import logging
import asyncio

logging.basicConfig(filename='logs/stt.log', level=logging.INFO)

class STTModule:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.recognizer = sr.Recognizer()

    async def recognize_audio(self, audio_file):
        try:
            with sr.AudioFile(audio_file) as source:
                audio = self.recognizer.record(source)
            text = self.recognizer.recognize_google(audio)
            logging.info(f"STT Success: {text}")
            return text
        except Exception as e:
            logging.error(f"STT Error: {e}")
            return None
