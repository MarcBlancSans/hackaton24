import pandas as pd
import requests
import os

import csv

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

def eliminar_urls_repetits(csv_input, csv_output):
    urls_vistes = {}  # Diccionari per fer un seguiment de les URLs vistes
    with open(csv_input, 'r', newline='') as input_file, open(csv_output, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)
        for row in reader:
            row_sense_buides = [url for url in row if url.strip()]  # Eliminem les cel·les buides
            for i, url in enumerate(row_sense_buides):
                if url not in urls_vistes:
                    urls_vistes[url] = True
                else:
                    row_sense_buides[i] = ""  # Substituïm les URLs repetides per una cadena buida
            writer.writerow(row_sense_buides)  # Escrivim la fila amb les URLs repetides eliminades
            
eliminar_urls_repetits('inditex.csv', 'inditex_nou.csv')

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
                row = []
                row.append(i)
                row.append(url)
                if i in data:
                    print("ERROR")
                data[i] = row
                break
    
    return data

data = getDataURL('inditex_nou.csv', 2, 50)
print(data)

'''
    #setting the new columns
df = pd.read_csv('inditex_nou.csv')
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
'''
