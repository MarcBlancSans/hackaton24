import numpy as np
import faiss
from AIModule import AIModule

class FaissLoader:
    def __init__(self):
        self.image_processor = AIModule()

    def cargar_faiss(self, dicc_of_url):
        ids = []
        data = []

        for key, value in dicc_of_url.items():
            img = AIModule.getImage(value)
            
            if img is None:
                continue
            embedding = self.image_processor.get_embeddings_image(img)
            ids.append(key)
            data.append(embedding[0])

        array_2d = np.array(data, dtype='float32')
        ids = np.array(ids)

        index = faiss.IndexFlatL2(array_2d.shape[1])
        index_id_map = faiss.IndexIDMap(index)
        index_id_map.add_with_ids(array_2d, ids)

        xq = array_2d[0]
        k = 5
        D, I = index_id_map.search(np.expand_dims(xq, axis=0), k)

        print("FAISS PROXIMITIES")
        setURLs = []
        for url in I[0]:
            setURLs.append(dicc_of_url[url])
        return setURLs
