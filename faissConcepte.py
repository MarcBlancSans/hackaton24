import faiss
import numpy as np
# Exemple de dues matrius
A = np.random.random((10, 5)).astype('float32')
B = np.random.random((10, 5)).astype('float32')
C = np.random.random((10, 5)).astype('float32')

print(A)
print(B)
# Indexació de la matriu B
index = faiss.IndexFlatL2(A.shape[1])  # Crear un índex L2
index.add(B)  # Afegir B a l'índex

# Cerca de la similitud
D, I = index.search(A, 2)  # Cercar el vector més proper a A en B
print(D)
print(I)


# Convertir la distància L2 a similitud cosinus
similitud = 1 - (D / 2)

# Calcular el percentatge de similitud
percentatges = similitud * 100

print("Percentatge de similitud entre A i B:", percentatges)