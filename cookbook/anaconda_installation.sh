curl -O https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
bash ~/Anaconda3-2024.10-1-Linux-x86_64.sh
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip3 install datasets timm diffusers transformers lightning peft sentencepiece