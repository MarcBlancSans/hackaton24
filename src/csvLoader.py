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
    def get_data_url(csv_path, start_column, num_urls):
        df = pd.read_csv(csv_path)
        data = {}
        urls_count = 0

        for i in range(len(df)):
            if i < start_column:
                continue
            for j in range(len(df.columns)):
                if urls_count >= num_urls:
                    break
                url = str(df.iloc[i, j])
                if url == "":
                    continue
                else:
                    urls_count += 1
                    data[i] = [i, url]
                    break
        return data

# Example usage:

URLProcessor.eliminar_urls_repetits('inditex.csv', 'inditex_nou.csv')
data = URLProcessor.get_data_url('inditex_nou.csv', 2, 50)
print(data)
