# web_demo/app.py
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
import shutil
import asyncio
from src.ai_agent import AIAgent

app = FastAPI()
agent = AIAgent()

HTML_CONTENT = '''
<!DOCTYPE html>
<html>
<head>
    <title>AI Phone Agent Demo</title>
</head>
<body>
    <h1>AI Phone Agent Demo</h1>
    <form action="/upload_audio/" enctype="multipart/form-data" method="post">
        <input name="file" type="file" accept="audio/*">
        <input type="submit" value="Upload & Process">
    </form>
</body>
</html>
'''

@app.get("/", response_class=HTMLResponse)
async def root():
    return HTML_CONTENT

@app.post("/upload_audio/")
async def upload_audio(file: UploadFile = File(...)):
    temp_path = f"data/sample_calls/{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    output_audio = await agent.handle_call(temp_path)
    return {"message": "Call processed", "output_audio": output_audio}

@app.get("/demo_audio/{filename}")
async def get_demo_audio(filename: str):
    return FileResponse(f"data/sample_calls/{filename}")
