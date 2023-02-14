# In this file, we define download_model
# It runs during container build time to get model weights built into the container

# In this example: A Huggingface BERT model

import whisper_timestamped as whisper
import os

def download_model():
    model_name = os.getenv("MODEL_NAME")
    model = whisper.load_model(model_name, in_memory=True)

if __name__ == "__main__":
    download_model()