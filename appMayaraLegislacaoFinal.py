#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
PF002

Objetivos:
- Facilitar a consulta comparativa de leis a partir do texto obtido pela web
- Indicar a correspondência dos artigos entre a lei nova e as leis antigas, para facilitar a pesquisa dos advogados que trabalham com o tema.
Por exemplo, a pessoa indicaria o art. 10 da lei nova e o programa indicaria quais artigos das outras leis seriam correspondentes e também informaria se não existe correspondência.
'''

import requests
from bs4 import BeautifulSoup

url0 = 'sites/L14133.htm' # Nova Lei de Licitações e Contratos Administrativos (lei principal)
url1 = 'sites/L8666compilado.htm' # Antiga Lei de Licitações e Contratos Administrativos
url2 = 'sites/L10520.htm' # Antiga Lei do Pregão
url3 = 'sites/L12462compilado.htm' # Antiga Lei do RDC

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
def get_arts(text):
    artigos = {}
    iter = 0
    chave = 'Art' + str(iter)
    artigos[chave] = []
    for item in text:
        if 'Art' in item:
            iter += 1
            chave = 'Art' + str(iter)
            artigos[chave]=[]
        artigos[chave].append(item)
    return artigos

lei14133 = get_arts(text0)
lei8666 = get_arts(text1)
lei10520 = get_arts(text2)
lei12462 = get_arts(text3)
            

relacoes = {'lei14133["Art1"]': {'lei8666["Art1"]':lei8666['Art1'],'lei10520["Art1"]':lei10520['Art1'], 'lei12462["Art1"]':lei12462['Art1']}; 'lei14133["Art2"]': {'lei8666["Art2"]':lei8666['Art2']}; 'lei14133["Art5"]': {'lei8666["Art3"]':lei8666['Art3'], 'lei12462["Art3"]': lei12462['Art3']}; 'lei14133["Art7"]': {'lei14133["Art7"]':lei14133['Art7']}}             
            
            
            
            
            
            
            
            