#import numpy as nplocal = geo_localizador.geocode(nome_hospital, timeout=100)
import pandas as pd #biblioteca para lidar com a base de dados (tabela)

from geopy.geocoders import Nominatim #biblioteca para fazer a comunicação com o maps e o openstreetmap


def coordenada_hospitais(tabela):
    hospitais = pd.read_excel(tabela)
    coord_hospitais = []
    hospitais_nominatim = []
    lista_completa = []

    for linha in range(len(hospitais)):
        nome_hospital = hospitais['nome_estabelecimento_saude'].iloc[linha]
        
        nome_hospital = nome_hospital.replace("HOSP MUN", "HOSPITAL MUNICIPAL")

        lista_completa.append(nome_hospital)

        geo_localizador = Nominatim(user_agent="minha_aplicacao")
        local = geo_localizador.geocode(nome_hospital, timeout=100)

        if local:
            cord = (local.latitude, local.longitude)    
            if cord not in coord_hospitais:
                coord_hospitais.append(cord)
                hospitais_nominatim.append(nome_hospital)
                # print(nome_hospital, cord[0], cord[1])

    lista_resultante = list(set(lista_completa) - set(hospitais_nominatim))

    print(len(lista_resultante))

    for linha in range(len(lista_resultante)):
        print(lista_resultante[linha])
    


coordenada_hospitais('hospitais_publicos.csv') 
