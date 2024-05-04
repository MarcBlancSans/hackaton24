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


#build one time the new csv
def csv():

    df = pd.read_csv('inditex.csv')
    fila = df.iloc[2]
    row = fila.iloc[0]  
    #setting the new columns
    new_csv = []
    data = ['year', 'season', 'product type', 'section', 'url']
    new_csv.append(data)

    for i in range(len(df)):

        for j in range(len(df.columns)):
            if j < 1:
                continue
            filera = []
            value = f"{df.iloc[i, j]}"
            str = splitUrl(value)
            for s in range(len(data) - 1):
                filera.append(str[s])
            filera.append(value)
            new_csv.append(filera)

    file_name = 'data.csv'
    df = pd.DataFrame(new_csv)
    df.to_csv(file_name, index=False)

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