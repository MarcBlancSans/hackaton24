from transformers import ViTImageProcessor, ViTModel
from datasets import load_dataset
from PIL import Image
from io import BytesIO
import pandas as pd
import numpy as np
import requests
import torch
import faiss


#get the data of the URL from the csv with path 'csvPath', including the URL itself the identification and the column of the url in the csv
def getDataURL(csvPath, startColumn, numURLs):
    urlsCount = 0
    df = pd.read_csv(csvPath)
    data = {}

    for i in range(len(df)):
        if i < startColumn:
            continue
        for j in range(len(df.columns)):
            if (urlsCount > numURLs):
                break
            url = f"{df.iloc[i, j]}"
            if url == "":
                continue
            else:
                urlsCount += 1

                row = url
                if i in data:
                    print("ERROR")
                data[i] = row
                break
    
    return data

# Selecciona el dispositiu
device = "cuda" if torch.cuda.is_available() else "cpu"

# Carregar el model i el processador
#Genera els tokens per a la primer capa del grafs bipartits
tokenizer = ViTImageProcessor.from_pretrained('google/vit-base-patch16-224-in21k')
#Serveix per processar els tokens inicials al estat final.
model = ViTModel.from_pretrained('google/vit-base-patch16-224-in21k').to(device)
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
    embeding = pt_outputs1.last_hidden_state[:,0]
    return embeding

def cargarFaiss(diccOfURL):

    ids = []
    data = []

    for key, value in diccOfURL.items():
        img = getImage(value)
        if img == None:
            continue
        embeding = getEmbedingsImage(img)
        ids.append(key)
        data.append(embeding[0])
    
    #DATA LENGHT MUST BE GREATHER THAN 0!!!!!!!!!!!!
    array_2d = np.array(data, dtype='float32')
    ids = np.array(ids)

    #index.add(data)

    index = faiss.IndexFlatL2(array_2d.shape[1])  # L2 distance index, assuming Euclidean distance
    index_id_map = faiss.IndexIDMap(index) #IDMap(index)
    index_id_map.add_with_ids(array_2d, ids)

    print("COMPARACIO")
    print(diccOfURL[ids[0]])
    print("-----------")

    xq = array_2d[0]

    k = 5                         # we want 4 similar vectors
    D, I = index_id_map.search(np.expand_dims(xq, axis=0), k)     # actual search
    print("FAISS PROXIMITIES")
    print (I[0])
    for url in I[0]:
        print(diccOfURL[url])






setID = getDataURL("python/inditex_nou.csv", 3, 20)
cargarFaiss(setID)
