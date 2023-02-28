import pandas as pd


def compara_tabela(tabela1, tabela2):
    hospitais_encontrados = pd.read_csv(tabela1)
    hospitais_faltantes = pd.read_csv(tabela2)

    faltantes = []
    lista_completa = []

    for linha in range(len(hospitais_encontrados)):
        nome_hospital = hospitais_encontrados['nome_estabelecimento_saude'].iloc[linha]
        nome_hospital = nome_hospital.replace("HOSP MUN", "HOSPITAL MUNICIPAL")
        lista_completa.append(nome_hospital)

    for linha in range(len(hospitais_faltantes)):
        nome_faltantes = hospitais_faltantes['NOME'].iloc[linha]
        faltantes.append(nome_faltantes)

    lista_resultante = list(set(lista_completa) - set(faltantes))

    print(len(lista_resultante))

    for linha in range(len(lista_resultante)):
        print(lista_resultante[linha])
    

compara_tabela('hospitais_publicos.csv', 'tabela_completa.csv') 
