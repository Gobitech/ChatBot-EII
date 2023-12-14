import requests
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import dataframe_image as dfi
import json
import html_to_json


def thuat_ngu():
  url = 'https://www.vcsc.com.vn/tin-tuc/cac-thuat-ngu-chung-khoan-ma-nha-dau-tu-nen-biet'
  headers = {
      'User-Agent': 'Mozilla/5. (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, 'html.parser')

  ds_thuat_ngu = []
  loai = []
  thuat_ngu = []
  rt = soup.find("h3")
  title = rt.text
  for s in rt.find_next_siblings():
    if s.name == 'p':
      if (s.findChildren("img" , recursive=False) or s.findChildren("a" , recursive=False)):
        continue
      elif "Trên đây là tổng hợp " in s.text or "Bộ lọc cổ phiếu" in s.text:
        continue
      id = s.find("em")
      t = id.get_text(strip=True)
      before, sep, after = t.partition('(')
      before, sep, after = before.partition('–')
      before = before.strip()
      thuat_ngu.append((before.lower(), s.get_text(strip=True)))

    elif s.name == 'h3' :
      if "Bộ lọc cổ phiếu" in s.text: continue
      loai.append(title.lower())
      loai.append(thuat_ngu)
      ds_thuat_ngu.append(loai)
      title = s.get_text(strip=True)
      loai = []
      thuat_ngu = []

  loai.append(title.lower())
  loai.append(thuat_ngu)
  ds_thuat_ngu.append(loai)
    
  return ds_thuat_ngu


def data_thuatngu_stock():
    terms = thuat_ngu()
    list_data_terms = []

    for i in terms:
        type_terms = i[0]
        for j in i[1]:
            name_data_terms = j[0]
            data_terms = j[1]
            member_data_terms = []
            member_data_terms.append(name_data_terms)
            member_data_terms.append(data_terms)
            member_data_terms.append(type_terms)
            list_data_terms.append(member_data_terms)
    return list_data_terms
