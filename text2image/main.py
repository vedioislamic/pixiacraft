from diffusers import StableDiffusionPipeline
import torch

def generate_image(prompt):
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float16,
        use_auth_token=True  # only if required
    )
    pipe.to("cuda")  # use "cpu" if you don't have GPU

    image = pipe(prompt).images[0]
    image.save("output.png")