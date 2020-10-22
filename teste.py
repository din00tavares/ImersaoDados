import runSQL



cabecalho = str()
insert = 'INSERT INTO MICRODADOS_ENEM '
n = 0
with open(r'C:\Users\fernandino.tavares\Documents\ImersaoDados\MICRODADOS_ENEM_2019.csv','r') as arq:
    for linha in arq:
        n += 1
        dados = linha.split(';')
        if cabecalho == '':
            insert += '({}) VALUES \n'.format(','.join(dados))
            continue
        valores = str()
        for dado in dados:
            valores += 'Null,' if dado == '' else "'{}',".format(dado)
        valores = '  ({}),\n'.format(valores[:-1])
                
            


        if n % 1000:

        
        