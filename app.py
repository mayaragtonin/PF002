#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
PF002

Objetivos:
- Facilitar a consulta comparativa de leis a partir do texto obtido pela web
- Indicar a correspondência dos artigos entre as leis, para facilitar a pesquisa dos advogados que trabalham com o tema.
Por exemplo, a pessoa indicaria o art. 10 da lei nova e o programa indicaria quais artigos das outras leis seriam correspondentes e também informaria se não existe correspondência.
'''

import requests
from bs4 import BeautifulSoup

url0 = 'sites/L10520.htm'
url1 = 'sites/L12462compilado.htm'
url2 = 'sites/L14133.htm'
url3 = 'sites/L8666compilado.htm'

def get_text(url):
    """
    Parameters
    ----------
    url : string
        url do site que será estudado.
    Returns
    -------
    Soup e lista com todos os parágrafos.
    """
    f = open(url, 'r',encoding='latin-1')
    contents = f.read()
    soup = BeautifulSoup(contents,"lxml")
    f.close()
    texto0 = []
    for tag in soup.find_all('p'):
            texto0.append(tag.text)
    return soup, texto0

soup0, text0 = get_text(url0)
soup1, text1 = get_text(url1)
soup2, text2 = get_text(url2)
soup3, text3 = get_text(url3)

# Comparar os textos dos artigos das sessões
for item in text0:
    print(item)