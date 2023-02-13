tabela = open('tabela_completa.txt', 'r')
tabela_final = open('tabela_completa.csv', 'w')

tabela_final.write('NOME,LATITUDE,LONGITUDE\n')
for linha in tabela.readlines():
    linha_tabela = linha.replace(" -", ",-")
    tabela_final.write(linha_tabela)

tabela.close()
tabela_final.close()

