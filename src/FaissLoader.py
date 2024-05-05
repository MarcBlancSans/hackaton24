import numpy as np
import faiss
from AIModule import AIModule
from csvLoader import URLProcessor
import random


class FaissLoader:
    
    def __init__(self):
        self.image_processor = AIModule()

        #['row', 'embedding']
        self.dicc = {}
        self.id = []
        self.embed = []
        

    def loadEmbeddings(self, initialOffset, cant):
        dicc_of_url = URLProcessor.getDataURL("../data/inditex_nou.csv", initialOffset, cant)
        for key, value in dicc_of_url.items():
            img = AIModule.getImage(value)
            if img is None:
                continue
            if img == "nan":
                continue
            
            embedding = self.image_processor.get_embeddings_image(img)
            
            self.dicc[key] = value
            self.id.append(key)
            self.embed.append(embedding[0])

            

    def cargar_faiss(self):

        array_2d = np.array(self.embed, dtype='float32')
        ids = np.array(self.id)

        index = faiss.IndexFlatL2(array_2d.shape[1])
        index_id_map = faiss.IndexIDMap(index)
        index_id_map.add_with_ids(array_2d, ids)

        i = random.randint(0, len(array_2d))

        xq = array_2d[i]
        k = 5
        D, I = index_id_map.search(np.expand_dims(xq, axis=0), k)

        print("FAISS PROXIMITIES")
        setURLs = []
        for url in I[0]:
            setURLs.append(self.dicc[url])
        return setURLs
