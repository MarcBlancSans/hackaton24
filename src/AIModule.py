from transformers import ViTImageProcessor, ViTModel
from PIL import Image
from io import BytesIO
import requests
import torch

class AIModule:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
        self.model = ViTModel.from_pretrained('google/vit-base-patch16-224-in21k').to(self.device)

    def get_embeddings_image(self, img):
        encoding = self.tokenizer(img, return_tensors="pt")
        with torch.no_grad():
            pt_outputs1 = self.model(**encoding)
        embedding = pt_outputs1.last_hidden_state[:, 0]
        return embedding

    def getImage(url):
        img = None
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content)).convert("RGB")
        except Exception as e:
            print(f"Error loading image {url}: {e}")
        return img

    #def generateEmbeddings():