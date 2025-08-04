from fastapi import FastAPI
from huggingface_hub import hf_hub_download

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "PixiaCraft API running"}

# Example: model download
model_file = hf_hub_download(repo_id="stabilityai/stable-diffusion-2-1", filename="model_index.json")