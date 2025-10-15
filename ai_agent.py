# src/ai_agent.py
import logging
from stt_module import STTModule
from tts_module import TTSModule
import asyncio

logging.basicConfig(filename='logs/ai_agent.log', level=logging.INFO)

class AIAgent:
    def __init__(self):
        self.stt = STTModule()
        self.tts = TTSModule()

    async def handle_call(self, audio_file):
        text = await self.stt.recognize_audio(audio_file)
        if not text:
            return "Error recognizing speech."
        response = self.generate_response(text)
        output_audio = self.tts.speak_text(response)
        return output_audio

    def generate_response(self, user_text):
        user_text = user_text.lower()
        if "price" in user_text:
            return "Our pricing starts at $99. Would you like to schedule a service?"
        elif "schedule" in user_text:
            return "Sure! I can book your appointment. What date works for you?"
        else:
            return "Thank you for calling. How can I assist you today?"
