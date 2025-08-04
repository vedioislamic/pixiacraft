from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from diffusers import StableDiffusionPipeline
import torch
import uuid
import os

app = FastAPI()

# Load Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16,
    revision="fp16"
).to("cuda" if torch.cuda.is_available() else "cpu")

# Request body schema
class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_image(request: PromptRequest):
    try:
        prompt = request.prompt
        image = pipe(prompt).images[0]

        # Save the image
        image_id = str(uuid.uuid4())
        image_path = f"outputs/{image_id}.png"
        os.makedirs("outputs", exist_ok=True)
        image.save(image_path)

        return {"status": "success", "image_path": image_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))