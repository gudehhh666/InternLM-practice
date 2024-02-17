import os 
from huggingface_hub import hf_hub_download  # Load model directly 

hf_hub_download(repo_id="internlm/internlm-7b", filename="config.json", local_dir=r'D:\PHD\basics\LLM_practice\tasks\ch2')