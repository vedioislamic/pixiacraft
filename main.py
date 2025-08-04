# main.py
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4",
    torch_dtype=torch.float16,
    revision="fp16"
).to("cuda")

prompt = "a fantasy landscape with floating islands and waterfalls"
image = pipe(prompt).images[0]
image.save("output.png")