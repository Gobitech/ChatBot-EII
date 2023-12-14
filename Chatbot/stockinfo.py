import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import dataframe_image as dfi
import json
import html_to_json
from vnstock import *
import openpyxl


def stock_daily_analise():
    analize = []
    url = "https://vietstock.vn/nhan-dinh-phan-tich/nhan-dinh-thi-truong.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    rt = soup.findAll("a", {"class": "fontbold"})
    for t in rt:
        if t.getText().find("Vietstock Daily") != -1:
            link = "https://vietstock.vn" + t["href"]
            navigate = requests.get(link, headers=headers)
            soup = BeautifulSoup(navigate.text, "html.parser")
            info = soup.findAll("p", {"class": "pBody"})

            for i in range(int(len(info) * 0.3)):
                analize.append(info[i].getText())

            return "\n".join([str(elem) for elem in analize])


def stock_weekly_analise():
    analize = []
    url = "https://vietstock.vn/nhan-dinh-phan-tich/nhan-dinh-thi-truong.htm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
    }
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    rt = soup.findAll("a", {"class": "fontbold"})
    for t in rt:
        if t.getText().find("Vietstock Weekly") != -1:
            link = "https://vietstock.vn" + t["href"]
            navigate = requests.get(link, headers=headers)
            soup = BeautifulSoup(navigate.text, "html.parser")
            info = soup.findAll("p", {"class": "pBody"})

            for i in range(int(len(info))):
                analize.append(info[i].getText())

            return "\n".join([str(elem) for elem in analize])


def thong_tin_co_ban(ma_co_phieu):
    return ticker_overview(ma_co_phieu)


k = thong_tin_co_ban("VHM")
print(type(k))
