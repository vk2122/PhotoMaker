from photomaker import PhotoMakerStableDiffusionXLPipeline

from huggingface_hub import hf_hub_download
photomaker_path = hf_hub_download(repo_id="vk2122/PhotoMaker", filename="photomaker-v1.bin", repo_type="model")