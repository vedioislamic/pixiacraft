# main.py
# main.py
from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from text2image.main import generate_image

app = FastAPI()

@app.get("/generate")
def generate(prompt: str = Query(..., description="Enter your image prompt")):
    output_file = generate_image(prompt)
    return FileResponse(output_file, media_type="image/png")