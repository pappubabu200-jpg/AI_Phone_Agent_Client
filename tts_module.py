# src/tts_module.py
import pyttsx3
import logging

logging.basicConfig(filename='logs/tts.log', level=logging.INFO)

class TTSModule:
    def __init__(self, voice_id=None, rate=150):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        if voice_id:
            self.engine.setProperty('voice', voice_id)

    def speak_text(self, text, output_file="output.wav"):
        try:
            self.engine.save_to_file(text, output_file)
            self.engine.runAndWait()
            logging.info(f"TTS Success: {output_file}")
            return output_file
        except Exception as e:
            logging.error(f"TTS Error: {e}")
            return None
