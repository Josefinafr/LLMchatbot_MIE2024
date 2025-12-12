from huggingface_hub import snapshot_download

MODEL_NAME = "Qwen/Qwen2-7B-Instruct-AWQ"
TARGET_FOLDER = "./models/Qwen2-7B-Instruct-AWQ"

snapshot_download(
    repo_id=MODEL_NAME,
    local_dir=TARGET_FOLDER,
    local_dir_use_symlinks=False
)

print("Download abgeschlossen:", TARGET_FOLDER)
