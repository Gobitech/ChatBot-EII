import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import dataframe_image as dfi
import json
import html_to_json


def gold_daily_price(detail):
    analize = []
    url = "https://vietnambiz.vn/chu-de/vang-52.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    rt = soup.findAll("h3", {"class": "title"})

    for t in rt:
        if "Giá vàng hôm nay" in t.text:
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


def bang_gia_vang():
    url = "https://www.24h.com.vn/gia-vang-hom-nay-c425.html"
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


def data_gold_table():
    gold_name = []
    gold_price_buy_td = []
    gold_price_sell_td = []
    gold_price_buy_yd = []
    gold_price_sell_yd = []
    gold_table = bang_gia_vang()
    for i in gold_table:
        gold_name.append(i[0])
        gold_price_buy_td.append(i[1])
        gold_price_sell_td.append(i[2])
        gold_price_buy_yd.append(i[3])
        gold_price_sell_yd.append(i[4])

    return (
        gold_name,
        gold_price_buy_td,
        gold_price_sell_td,
        gold_price_buy_yd,
        gold_price_sell_yd,
    )


# print(bang_gia_vang())
