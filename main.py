from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from text2image.main import generate_image

app = FastAPI()

@app.post("/generate")
async def generate(prompt: str = Form(...)):
    generate_image(prompt)
    return FileResponse("output.png", media_type="image/png")