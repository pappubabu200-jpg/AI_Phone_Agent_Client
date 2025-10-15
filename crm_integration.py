# src/crm_integration.py
import logging
import requests
import yaml

logging.basicConfig(filename='logs/crm_integration.log', level=logging.INFO)

class CRMIntegration:
    def __init__(self, config_path="config/config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

    def push_lead_to_crm(self, lead_info):
        try:
            api_key = self.config.get("CRM_API_KEY")
            response = requests.post("https://api.workiz.com/leads", headers={"Authorization": f"Bearer {api_key}"}, json=lead_info)
            logging.info(f"CRM push status: {response.status_code}")
            return response.status_code
        except Exception as e:
            logging.error(f"CRM Integration Error: {e}")
            return None

    def send_sms_followup(self, phone, message):
        try:
            sms_key = self.config.get("SMS_API_KEY")
            logging.info(f"SMS sent to {phone}: {message}")
            return True
        except Exception as e:
            logging.error(f"SMS Error: {e}")
            return False
