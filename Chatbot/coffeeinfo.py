import requests
import pandas as pd
import matplotlib.pyplot as pltcoffee_daily_price
from bs4 import BeautifulSoup
import dataframe_image as dfi
import json
import html_to_json


def coffee_daily_price(detail):
    analize = []
    url = "https://vietnambiz.vn/chu-de/ca-phe-34.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    rt = soup.findAll("h3", {"class": "title"})

    for t in rt:
        if "Giá cà phê hôm nay" in t.text:
            children = t.find("a")
            link = "https://vietnambiz.vn" + children["href"]
            n = requests.get(link, headers=headers)
            soup = BeautifulSoup(n.text, "html.parser")
            if detail:
                rt = soup.find("p", {"dir": "ltr"})
                analize.append(rt.text)
                for s in rt.find_next_siblings():
                    if s.name == "p":
                        analize.append(s.text)
                    else:
                        break

                return "\n".join([str(elem) for elem in analize])
            else:
                rt = soup.find("div", {"class": "vnbcbc-sapo"})
                return rt.text


def bang_gia_ca_phe():
    url = "https://giacaphe.com/gia-ca-phe-noi-dia/"
    headers = {
        "User-Agent": "Mozilla/5. (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    rt = soup.find("table", {"id": "gia_trong_nuoc"})

    html_string = f"{rt}"
    tables = html_to_json.convert_tables(html_string)

    for i in tables[0]:
        i["TT nhân xô"] = i["TT nhân xô"].replace("(HCM)", "")
        i["TT nhân xô"] = i["TT nhân xô"].strip()
    return tables[0]


def data_coffee_table():
    coffee_table = bang_gia_ca_phe()
    coffee_name = []
    coffee_average_price = []
    coffee_change = []
    for i in coffee_table:
        coffee_name.append(i.get("TT nhân xô"))
        coffee_average_price.append(i.get("Giá trung bình"))
        coffee_change.append(i.get("Thay đổi"))

    return coffee_name, coffee_average_price, coffee_change

print(data_coffee_table())