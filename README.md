==========================================================
                   AI PHONE AGENT 
==========================================================

PROJECT OVERVIEW
----------------
This is a **production-ready AI Phone Agent** for Garage Door, Roofing, and similar service businesses.
The AI agent can:
- Handle calls with natural conversation flow (no robotic tone)
- Book appointments and qualify leads
- Route calls based on time and availability
- Integrate with Workiz CRM and send SMS confirmations
- Preserve accent and tone during speech synthesis (TTS)
- Provide real-time transcription (STT) for debugging and logging

The project demonstrates a full-stack AI solution with a Python backend and a web-based demo interface.

----------------------------------------------------------
FOLDER STRUCTURE
----------------
AI_Phone_Agent_Client/
├── src/                     
│   ├── stt_module.py        # Speech-to-Text module using Google STT or custom API
│   ├── tts_module.py        # Text-to-Speech module, accent-preserving
│   ├── ai_agent.py          # Core AI agent handling calls and generating responses
│   ├── call_routing.py      # Call routing logic (after-hours, voicemail, AI agent)
│   └── crm_integration.py   # CRM & SMS integration logic
│
├── web_demo/                
│   └── app.py               # FastAPI web demo for uploading and processing calls
│
├── config/                 
│   └── config.yaml          # Placeholder for API keys (STT, TTS, CRM, SMS)
│
├── demos/call_demo_examples/  
│   ├── call_demo_1.wav      # Demo call audio 1
│   ├── call_demo_2.wav      # Demo call audio 2
│   └── call_demo_3.wav      # Demo call audio 3
│
├── logs/                    # Folder for storing runtime logs
├── README_Client.md         # Detailed client instructions
├── requirements.txt         # Python dependencies
├── Dockerfile               # Optional container deployment
└── LICENSE                  # MIT License

----------------------------------------------------------
HOW IT WORKS
-------------
1. **Speech-to-Text (STT)**
   - Converts caller audio into text using STT module.
   - Supports multiple accents and handles noisy audio.

2. **AI Agent**
   - Analyzes the text and generates context-aware responses.
   - Handles questions, objections, and scheduling requests.

3. **Text-to-Speech (TTS)**
   - Converts AI-generated text to audio while preserving accent and tone.
   - Output audio returned to caller.

4. **Call Routing**
   - Routes calls depending on business hours and availability.
   - After-hours calls go to voicemail.
   - Business hours calls handled by AI agent.

5. **CRM & SMS Integration**
   - Pushes leads to Workiz CRM.
   - Sends SMS confirmations/follow-ups to clients.

6. **Web Demo**
   - FastAPI app allows uploading demo audio.
   - Processes audio using AI agent pipeline.
   - Returns output audio file and logs transcription.

----------------------------------------------------------
SETUP INSTRUCTIONS
------------------
1. Install dependencies:
2. 2. Update API keys in `config/config.yaml`:STT_API_KEY: "YOUR_STT_KEY_HERE" TTS_API_KEY: "YOUR_TTS_KEY_HERE" CRM_API_KEY: "YOUR_CRM_KEY_HERE" SMS_API_KEY: "YOUR_SMS_KEY_HERE"
   3. Run Web Demo:

uvicorn web_demo.app:app --reload

Open browser at `http://127.0.0.1:8000` to upload demo calls and test the AI agent.

4. Demo Calls:
- Use audio files in `demos/call_demo_examples/` to see AI agent responses.
- 
