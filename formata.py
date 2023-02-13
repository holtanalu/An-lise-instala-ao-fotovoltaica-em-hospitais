tabela = open('hospitais.txt', 'r')
tabela_final = open('hospitais_com_contorno.csv', 'w')

tabela_final.write('NOME,LATITUDE,LONGITUDE\n')
for linha in tabela.readlines():
    linha_tabela = linha.replace(" -", ",-")
    tabela_final.write(linha_tabela)

tabela.close()
tabela_final.close()

