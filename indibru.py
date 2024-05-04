from transformers import ViTImageProcessor, ViTForImageClassification, ViTModel
from PIL import Image
from io import BytesIO
import requests
from datasets import load_dataset
import faiss
import torch
import numpy as np
# Selecciona el dispositiu
device = "cuda" if torch.cuda.is_available() else "cpu"

# Carregar el model i el processador
#Genera els tokens per a la primer capa del grafs bipartits
tokenizer = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
#Serveix per processar els tokens inicials al estat final.
model = ViTModel.from_pretrained('google/vit-base-patch16-224-in21k').to(device)

url = 'https://static.zara.net/photos///2024/V/0/3/p/0208/600/620/2/w/2048/0208600620_6_1_1.jpg?ts=1700650087558'
'''
img = None
try:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
except Exception as e:
    print(f"Error loading image {url}: {e}")
    '''

#encoding = tokenizer(img, return_tensors="pt")
#print(encoding)

#pt_outputs = model(**encoding)
#last_hidden_states = pt_outputs.last_hidden_state

#print(pt_outputs)
#print(last_hidden_states)

def compute_similarity(emb_one, emb_two):
    """Computes average cosine similarity between two vectors and adjusts it to be between 0 and 1."""
    # Compute cosine similarity between the two embeddings
    similarity_scores = torch.nn.functional.cosine_similarity(emb_one, emb_two)
    # Adjust cosine similarity to be between 0 and 1
    adjusted_scores = (1 + similarity_scores) / 2
    # Return the average of the adjusted scores
    return adjusted_scores.mean().item()

def getImage(url):
    img = None
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content)).convert("RGB")
    except Exception as e:
        print(f"Error loading image {url}: {e}")
    return img

def getEmbedingsImage(img):
    encoding = tokenizer(img, return_tensors="pt")
    with torch.no_grad():
        pt_outputs1 = model(**encoding)
    embeding = pt_outputs1.last_hidden_state.squeeze(0)
    return embeding

def compara(url1, url2):
    img1=getImage(url1)
    img2=getImage(url2)
    
    if(img1!=None and img2!=None):
        emb1 = getEmbedingsImage(img1)
        emb2 = getEmbedingsImage(img2)
        print(compute_similarity(emb1,emb2))

def find_similar_embeddings(index, emb, k=2):
    D, I = index.search(emb, k)
    return D, I

# Get the embeddings for a set of URLs
urls = [
    'https://static.zara.net/photos///2024/V/0/2/p/0679/416/251/2/w/2048/0679416251_6_2_1.jpg?ts=1714473877883',
    'https://static.zara.net/photos///2024/V/0/1/p/4786/055/802/2/w/2048/4786055802_3_1_1.jpg?ts=1712743908341',
    'https://static.zara.net/photos///2024/V/0/1/p/2287/595/800/3/w/2048/2287595800_2_1_1.jpg?ts=1711529252148'
    'https://static.zara.net/photos///2023/I/0/3/p/0039/678/800/2/w/2048/0039678800_3_1_1.jpg?ts=1692625464746'
    'https://static.zara.net/photos///2023/V/0/3/p/5507/600/704/2/w/2048/5507600704_6_2_1.jpg?ts=1671119880202'
]

embeddings = []
for url in urls:
    img = getImage(url)
    if img is not None:
        embeddings.append(getEmbedingsImage(img).cpu().numpy())

# Convert embeddings to numpy array
embeddings_np = np.concatenate(embeddings, axis=0)

# Create the FAISS index
d = embeddings_np.shape[1]  # size of the vectors
index = faiss.IndexFlatL2(d)  # build the index
index.add(embeddings_np)  # add vectors to the index

# Find the closest embeddings for a given image
given_url = 'https://static.zara.net/photos///2024/V/0/3/p/0208/600/620/2/w/2048/0208600620_6_1_1.jpg?ts=1700650087558'
given_image = getImage(given_url)
given_emb = getEmbedingsImage(given_image).cpu().numpy()

# Compute similarities
D, I = find_similar_embeddings(index, given_emb, k=1)
print(f"Distances: {D}\nIndices: {I}")

# Output the URLs of the similar images
similar_urls = [urls[i] for i in I.flatten()]  # I.flatten() converteix la matriu a un array 1D
print(f"Similar URLs: {similar_urls}")