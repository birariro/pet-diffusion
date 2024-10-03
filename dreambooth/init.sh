git clone https://github.com/huggingface/diffusers
pip install diffusers
pip install -U -r diffusers/examples/dreambooth/requirements.txt
accelerate config default

pip install diffusers transformers accelerate torch
pip install bitsandbytes