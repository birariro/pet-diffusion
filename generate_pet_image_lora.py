from diffusers import StableDiffusionPipeline
import torch
from datetime import datetime

prompt = "A cute my pet wearing a warm, cozy winter hat, sitting happily with a playful expression, detailed fur, and a soft, comfortable background."

model_base = "runwayml/stable-diffusion-v1-5"
model_path = "./output/models/lora"
pipe = StableDiffusionPipeline.from_pretrained(model_base, torch_dtype=torch.float16)
pipe.unet.load_attn_procs(model_path)
pipe.to("cuda")

image = pipe(prompt, num_inference_steps=35, guidance_scale=7.5,cross_attention_kwargs={"scale": 0.9}).images[0]


timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
image_path = f"./output/images/pet_lora_{timestamp}.png"

# 이미지 저장
image.save(image_path)