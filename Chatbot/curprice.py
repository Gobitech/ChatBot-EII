import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import dataframe_image as dfi
import json
import html_to_json
import string


def bang_gia_ngoai_te():
    url = "https://www.24h.com.vn/ty-gia-ngoai-te-ttcb-c426.html"
    headers = {
        "User-Agent": "Mozilla/5. (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    rt = soup.find("table", {"class": "gia-vang-search-data-table"})
    for match in rt.findAll("span", {"class": "colorRed"}):
        match.replace_with("")
    for match in rt.findAll("span", {"class": "colorGreen"}):
        match.replace_with("")
    html_string = f"{rt}"
    tables = html_to_json.convert_tables(html_string)

    json = []
    for i in tables[0]:
        i = [k.strip() for k in i]
        json.append(i)
    return json
