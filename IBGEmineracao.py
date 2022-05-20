#NOME: THIAGO ALVES DAMASCENA
#RGM: 2196040-2

import requests #realizar a requisição web
from bs4 import BeautifulSoup

cabecalho = {
  'User-Agent' : "Thiago",
  'From' : "tiga_alves@hotmail.com"
}

cidades = ['sao-paulo', 'guarulhos','santos','poa','pindamonhangaba', 'sorocaba', 'atibaia', 'piracicaba', 'bauru', 'registro', 'franca', 'americana']

for cidade in cidades:
    url = "https://cidades.ibge.gov.br/brasil/sp/"+cidade+"/panorama"
    page = requests.get(url, headers = cabecalho)
    soup = BeautifulSoup(page.text, 'html.parser')

    #busca os indicadores da cidade a partir da classe apontada
    densidade_cidade = soup.find_all(class_ = 'indicador__valor')
    nome_cidade = soup.find_all(class_ = 'h1__mobile__completo')

    #encontra a parte densidade
    densidade = densidade_cidade.__getitem__(1)
    nome = nome_cidade.__getitem__(0)

    #pega somente o valor
    densidade = densidade.contents[0]
    nome = nome.contents[0]

    #substitui as pontuações para transformar em número real
    densidade = densidade.replace(".","")
    densidade = densidade.replace(",",".")
    densidade_d = float(densidade)
    nome = nome.replace("  ","")

    print(nome)

    #questiona se a cidade está apta ou não
    if(densidade_d > 1500):
        print("Densidade: " + densidade +" hab/km²\nA cidade está apta para construir o parque.")
    else:
        print("Densidade: " + densidade +" hab/km²\nA cidade não está apta para construir o parque.")