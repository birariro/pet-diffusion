export MODEL_NAME="runwayml/stable-diffusion-v1-5"
export INSTANCE_DIR="../images"
export OUTPUT_DIR="../output/models/lora"

accelerate launch ../diffusers/examples/dreambooth/train_dreambooth_lora.py \
  --pretrained_model_name_or_path=$MODEL_NAME  \
  --instance_data_dir=$INSTANCE_DIR \
  --output_dir=$OUTPUT_DIR \
  --instance_prompt="a photo of my pet" \
  --resolution=512 \
  --train_batch_size=1 \
  --gradient_accumulation_steps=1 \
  --checkpointing_steps=100 \
  --learning_rate=1e-4 \
  --lr_scheduler="constant" \
  --lr_warmup_steps=0 \
  --max_train_steps=500 \
  --validation_prompt="A photo of my pet in a bucket" \
  --validation_epochs=50 \
  --seed="0" 
  #--push_to_hub