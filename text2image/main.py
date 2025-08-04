# text2image/main.py
from diffusers import StableDiffusionPipeline
import torch

# Model load karo sirf ek dafa
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16,
    revision="fp16"
).to("cuda")

def generate_image(prompt: str, output_path="output.png"):
    image = pipe(prompt).images[0]
    image.save(output_path)
    return output_path