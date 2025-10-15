# src/call_routing.py
import logging
from datetime import datetime

logging.basicConfig(filename='logs/call_routing.log', level=logging.INFO)

class CallRouting:
    def __init__(self):
        self.after_hours_start = 18
        self.after_hours_end = 9

    def route_call(self, current_hour):
        if current_hour >= self.after_hours_start or current_hour < self.after_hours_end:
            logging.info("Call routed to voicemail")
            return "voicemail"
        else:
            logging.info("Call routed to AI agent")
            return "ai_agent"
