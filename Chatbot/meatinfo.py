import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import dataframe_image as dfi
import json
import html_to_json


def pig_daily_price(detail):
    analize = []
    url = "https://vietnambiz.vn/gia-thit-heo.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    rt = soup.findAll("h3", {"class": "title"})

    for t in rt:
        if "Giá thịt heo hôm nay" in t.text:
            children = t.find("a")
            link = "https://vietnambiz.vn" + children["href"]
            n = requests.get(link, headers=headers)
            soup = BeautifulSoup(n.text, "html.parser")
            if detail:
                rt = soup.find("p")
                analize.append(rt.text)
                for s in rt.find_next_siblings():
                    if s.name == "p":
                        analize.append(s.text)
                    else:
                        break
                if len(analize) > 3:
                    analize = analize[:4]
                return "\n".join([str(elem) for elem in analize])
            else:
                rt = soup.find("div", {"class": "vnbcbc-sapo"})
                return rt.text
