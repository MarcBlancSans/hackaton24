import pandas as pd
import requests
import os
import csv

class URLProcessor:
    @staticmethod
    def split_url(url):
        atr = url.split("/")
        atr_clean = [a for index, a in enumerate(atr) if index >= 4 and a]
        return atr_clean

    @staticmethod
    def eliminar_urls_repetits(csv_input, csv_output):
        urls_vistes = {}
        with open(csv_input, 'r', newline='') as input_file, open(csv_output, 'w', newline='') as output_file:
            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            for row in reader:
                row_sense_buides = [url for url in row if url.strip()]
                for i, url in enumerate(row_sense_buides):
                    if url not in urls_vistes:
                        urls_vistes[url] = True
                    else:
                        row_sense_buides[i] = ""
                writer.writerow(row_sense_buides)

    @staticmethod
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

    #@staticmethod
    #get the data of the URL from the csv with path 'csvPath', including the URL itself the identification and the column of the url in the csv
    #def createCSV(csvPath, csv):
        