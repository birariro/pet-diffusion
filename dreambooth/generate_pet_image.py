from diffusers import StableDiffusionPipeline
from datetime import datetime

prompt = "A cute my pet wearing a warm, cozy winter hat, sitting happily with a playful expression, detailed fur, and a soft, comfortable background."

model_id = "./output/model"
pipe = StableDiffusionPipeline.from_pretrained(model_id).to("cuda")
image = pipe(prompt).images[0]

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
image_path = f"./output/images/pet_{timestamp}.png"

# 이미지 저장
image.save(image_path)