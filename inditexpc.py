from transformers import ViTImageProcessor, ViTForImageClassification, ViTModel
from PIL import Image
from io import BytesIO
import requests
from datasets import load_dataset
import torch

# Selecciona el dispositiu
device = "cuda" if torch.cuda.is_available() else "cpu"

# Carregar el model i el processador
#Genera els tokens per a la primer capa del grafs bipartits
tokenizer = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
#Serveix per processar els tokens inicials al estat final.
model = ViTModel.from_pretrained('google/vit-base-patch16-224-in21k').to(device)

url = 'https://static.zara.net/photos///2024/V/0/3/p/0208/600/620/2/w/2048/0208600620_6_1_1.jpg?ts=1700650087558'

img = None
try:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content)).convert("RGB")
except Exception as e:
    print(f"Error loading image {url}: {e}")

encoding = tokenizer(img, return_tensors="pt")
#print(encoding)

pt_outputs = model(**encoding)
last_hidden_states = pt_outputs.last_hidden_state

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
        print(f"Error loading image {url1}: {e}")
    return img

def getEmbedingsImage(img):
    encoding = tokenizer(img, return_tensors="pt")
    with torch.no_grad():
        pt_outputs1 = model(**encoding)
    embeding = pt_outputs1.last_hidden_state
    return embeding

def compara(url1, url2):
    img1=getImage(url1)
    img2=getImage(url2)
    
    if(img1!=None and img2!=None):
        emb1 = getEmbedingsImage(img1)
        emb2 = getEmbedingsImage(img2)
        print(compute_similarity(emb1,emb2))


def fetch_similar(image, top_k=5):
    """Fetches the `top_k` similar images with `image` as the query."""
    # Prepare the input query image for embedding computation.
    image_transformed = transformation_chain(image).unsqueeze(0)
    new_batch = {"pixel_values": image_transformed.to(device)}

    # Comute the embedding.
    with torch.no_grad():
        query_embeddings = model(**new_batch).last_hidden_state[:, 0].cpu()

    # Compute similarity scores with all the candidate images at one go.
    # We also create a mapping between the candidate image identifiers
    # and their similarity scores with the query image.
    sim_scores = compute_scores(all_candidate_embeddings, query_embeddings)
    similarity_mapping = dict(zip(candidate_ids, sim_scores))
 
    # Sort the mapping dictionary and return `top_k` candidates.
    similarity_mapping_sorted = dict(
        sorted(similarity_mapping.items(), key=lambda x: x[1], reverse=True)
    )
    id_entries = list(similarity_mapping_sorted.keys())[:top_k]

    ids = list(map(lambda x: int(x.split("_")[0]), id_entries))

    return ids, label


url1 = 'https://static.zara.net/photos///2024/V/0/2/p/0679/416/251/2/w/2048/0679416251_6_2_1.jpg?ts=1714473877883'
url2 = 'https://static.zara.net/photos///2024/V/0/2/p/0679/416/251/2/w/2048/0679416251_3_1_1.jpg?ts=1714473877592'
url3 = 'https://static.zara.net/photos///2024/V/0/1/p/4786/055/802/2/w/2048/4786055802_3_1_1.jpg?ts=1712743908341'

compara(url1,url3)
