from diffusers import StableDiffusionPipeline
import torch

# Load model from Hugging Face
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", 
    torch_dtype=torch.float16,
    revision="fp16", 
    use_auth_token=True  # Required since it's a gated model
)

pipe = pipe.to("cuda")  # If you have GPU; otherwise use "cpu"

# Your prompt
prompt = "a futuristic city at sunset, high quality, detailed"

# Generate image
image = pipe(prompt).images[0]

# Save image
image.save("output.png")