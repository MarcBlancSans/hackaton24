import pandas as pd
import requests
import os

#split the url rows in a array of strings (it generates )
def splitUrl(url):
    atr = url.split("/")
    atr_clean = []
    #Clean the url with the empry atr
    for index, a in enumerate(atr):
        if index < 4:
            continue
        if a == "":
            continue
        atr_clean.append(a)
    
    return atr_clean

#download image from url
def download_image(url, filename):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Open the file in binary write mode and write the content of the response
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image from {url}")

import numpy as np

def remove_duplicates(df):
    duplicated_mask = df.duplicated(subset=df.columns[4], keep='first')
    
    # Combinar la máscara de duplicados con una máscara que identifique filas con valores NaN en la columna 'year'
    nan_mask = df[df.columns[0]].isna()
    final_mask = duplicated_mask & ~nan_mask
    
    # Cambiar los valores de las filas duplicadas (excepto NaN) en la columna 'url' a NaN
    df.loc[final_mask, df.columns[4]] = np.nan


    return df



#build one time the new csv
def csv():

    df = pd.read_csv('inditex.csv')
    for index, row in df.iterrows():
    # Crear una llista per emmagatzemar els enllaços únics
        unique_links = []
    # Iterar a través dels enllaços de la fila
        for link in row.dropna():
        # Afegir l'enllaç a la llista si encara no està present
            if link not in unique_links:
                unique_links.append(link)
    # Assignar els enllaços únics a la fila actual
        df.loc[index] = unique_links

    # Guardar el DataFrame modificat com a nou CSV
    df.to_csv("inditex_nodup.csv", index=False)


    #setting the new columns
    new_csv = []
    data = ['year', 'season', 'product_type', 'section', 'url']
    new_csv.append(data)

    for i in range(len(df)):
        if i < 1:
            continue
        for j in range(len(df.columns)):
            filera = []
            value = f"{df.iloc[i, j]}"
            str = splitUrl(value)
            for k, s in enumerate(str):
                if k > len(data) - 2:
                    break
                filera.append(s)
            filera.append(value)
            new_csv.append(filera)

    file_name = 'data.csv'
    df = pd.DataFrame(new_csv)
    df.to_csv(file_name, index=False)

        # Llama a remove_duplicates después de crear el DataFrame desde el archivo CSV
    #df_without_dup = remove_duplicates(df)
    #df_without_dup.to_csv('inditex_nodup.csv', index=False)
    print("CSV file created successfully:", file_name)

def main():
    #df = pd.read_csv('data.csv')
    #fila = df.iloc[2]
    #row = fila.iloc[0]
    #print(f"{row}")
    #download_image(f"{row}", "../data/foto.jpg")
    csv() #JA SHA GENERAT EL NOU CSV


if __name__ == "__main__":
    main()