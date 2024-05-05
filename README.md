# Pick&Fit

Aquest projecte és un exemple d'implementació d'un model ViT (Vision Transformer) de Hugging Face, integrat amb una pàgina web creada amb React. El projecte permet als usuaris introduir una consulta (query) i genera imatges similars a través d'un programa de Python.

## Taula de Continguts

1. [Descripció](#descripció)
2. [Requisits](#requisits)
3. [Instal·lació](#instal·lació)
4. [Ús](#ús)
5. [Arquitectura del Projecte](#arquitectura-del-projecte)
6. [Contribuir](#contribuir)
7. [Llicència](#llicència)
8. [Contacte](#contacte)

## Descripció

Aquest projecte utilitza el model ViT de Hugging Face per generar imatges que són similars a una consulta donada. La interfície d'usuari està construïda amb React, mentre que el backend, que s'encarrega de processar la consulta i generar les imatges, està escrit en Python. El projecte mostra com integrar models de visió amb aplicacions web.

## Requisits

- Python 3.8 o superior
- Node.js 14 o superior
- npm (o yarn)
- Hugging Face Transformers
- OpenCV

## Instal·lació

1. **Backend**

   - Cloneu el repositori:
     ```bash
     git clone https://github.com/usuari/projecte-vithf-react-python.git
     ```
   - Instal·leu les dependències de Python:
     ```bash
     cd backend
     python -m venv venv
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     pip install -r requirements.txt
     ```

2. **Frontend**

   - Instal·leu les dependències de Node.js:
     ```bash
     cd frontend
     npm install
     ```
     
## Ús

1. **Executar el Backend**

   - Assegureu-vos que el vostre entorn virtual està activat:
     ```bash
     source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
     ```
   - Executeu el servidor de Python:
     ```bash
     cd backend
     python app.py
     ```
   - El servidor s'executarà a `http://localhost:5000`.

2. **Executar el Frontend**

   - Executeu l'aplicació de React:
     ```bash
     cd frontend
     npm start
     ```
   - El frontend s'executarà a `http://localhost:3000`.

3. **Ús de l'aplicació**

   - Aneu a `http://localhost:3000` en el vostre navegador.
   - Introduïu una consulta en el camp de text i premeu "Generar".
   - Veureu les imatges generades basades en la vostra consulta.

## Arquitectura del Projecte

El projecte es divideix en dues parts principals:

1. **Backend (Python)**

   - Usa el model ViT de Hugging Face per processar les consultes i generar les imatges.
   - El backend exposa una API RESTful utilitzant Flask.
   - Arxius clau:
     - `app.py`: el servidor Flask.
     - `model.py`: el codi relacionat amb el model ViT.

2. **Frontend (React)**

   - Permet als usuaris introduir una consulta i visualitzar les imatges generades.
   - Usa components de React.
   - Arxius clau:
     - `App.js`: el component principal de React.
     - `ImageGallery.js`: el component que mostra les imatges generades.

## Contribuir

Les contribucions són benvingudes! Si voleu contribuir a aquest projecte, si us plau, feu el següent:

1. Fork el repositori.
2. Creeu una branca (`git checkout -b feature-nom-de-la-branca`).
3. Feu un commit dels vostres canvis (`git commit -am 'Afegit alguna cosa'`).
4. Empenyeu els canvis (`git push origin feature-nom-de-la-branca`).
5. Creeu un Pull Request.

## Llicència

Aquest projecte està llicenciat sota la [Llicència MIT](LICENSE).

## Contacte

Si teniu preguntes o comentaris sobre aquest projecte, si us plau, contacteu-nos a `email@example.com`.
