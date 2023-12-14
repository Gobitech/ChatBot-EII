import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import dataframe_image as dfi
import json
import html_to_json


def bang_gia_gas():
    url = "https://vnexpress.net/chu-de/gia-xang-dau-3026"
    headers = {
        "User-Agent": "Mozilla/5. (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    rt = soup.find("table")

    html_string = f"{rt}"
    tables = html_to_json.convert_tables(html_string)

    return tables[0][1:]


def data_gas_table():
    table = bang_gia_gas()
    name = []
    price = []
    change = []

    for i in table:
        name.append(i[0])
        price.append(i[1])
        change.append(i[2])

    return name, price, change
