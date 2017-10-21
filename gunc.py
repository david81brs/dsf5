#!/usr/bin/python3
#Quem mais recebe e quem menos recebe na empresa e a média salarial da empresa
#Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área
#A área com mais funcionários e a área com menos funcionários
#Das pessoas que têm o mesmo sobrenome, aquela que recebe mais (não inclua sobrenomes que apenas uma pessoa tem nos resultados)

import json
import os
import pandas as pd

def screenClear():
    os.system('cls' if os.name == 'nt' else 'clear')

def next():
    input("Press Enter...")

file = 'funcionarios.json'

def dao(typef):
    with open(file) as json_data:
        d = json.load(json_data)
    if (typef=="F"):
        k = d['funcionarios']
    if (typef=="A"):
        k = d['areas']
    return k

f = dao("F")

def pandasImport():
    n = dao("F")
    a = dao("A")
    dfpandas = pd.DataFrame.from_dict(n)
    dfarea = pd.DataFrame.from_dict(a)
    print(dfpandas.sort_values(by=['area','salario','nome'], ascending=True).loc[:,["area","salario","nome"]])
    for i  in dfpandas['area'].unique():
        aux = dfpandas[dfpandas['area']==i]
        k=aux.loc[:,['nome','salario']]

        print("\nSalário Máximo na área %s %.2f " % (dfarea[dfarea['codigo']==i]['nome'].unique()[0], aux['salario'].max()) )
        print(k[k['salario']==aux['salario'].max()])

        print("Salário Mínimo na área %s %.2f " % (dfarea[dfarea['codigo']==i]['nome'].unique()[0], aux['salario'].min()) )
        print(k[k['salario']==aux['salario'].min()])

        print("Salário Médio na área  %s %.2f " % (dfarea[dfarea['codigo']==i]['nome'].unique()[0], aux['salario'].mean()) ) 

    return dfpandas

def showSibblings():
	n = dao("F")
	dfpandas = pd.DataFrame.from_dict(n)
	g = dfpandas['nome'].value_counts()
	print("Sibblings: \n%s" % g)

def showTable(f):
    print("id\tarea\tsalario\tnome.sobrenome")
    for i in range(0,len(f)):
        print(i, end="\t")
        print(f[i]['area'],end="\t")
        print(f[i]['salario'],end="\t")
        print(f[i]['nome']+"."+f[i]['sobrenome'])

def checkMaxSal(dd):
    max = 0
    nome = " "
    for i in range(0,len(dd)):
        if (dd[i]['salario'] > max):
            max = dd[i]['salario']
            nome = dd[i]['nome']
    return (nome, max)

def checkMeanSal(dd):
    soma = 0
    for i in range(0,len(dd)):
        soma+=dd[i]['salario']
    return soma/len(dd)

def checkMinSal(dd):
    min = dd[0]['salario']
    nome = " "
    for i in range(0,len(dd)):
        if (dd[i]['salario'] < min):
            min = dd[i]['salario']
            nome = dd[i]['nome']
    return (nome, min)

def checkAreaCount():
    stArea =  dao("A")
    stFunc = dao("F")
    count = []
    for i in range(0,len(stArea)):
        index=0
        for k in range(0,len(stFunc)):
            if stArea[i]['codigo'] == stFunc[k]['area']:
                index+=1
        count.append(index)
    print("Área com (+) integrantes: %i %s" % (max(count), stArea[count.index(max(count))]['nome']) )
    print("Área com (-) integrantes: %i %s" % (min(count), stArea[count.index(min(count))]['nome']) )

def statSal(f):
    print("Maior Salário: %s %.2f " % (checkMaxSal(f)[0], checkMaxSal(f)[1]) )
    print("Média Salários: %.2f" % checkMeanSal(f))
    print("Menor Salário: %s %.2f" % (checkMinSal(f)[0], checkMinSal(f)[1]) )

while(True):
    screenClear()
    print("--{:: Desafio 5 ::}--")
    print("1 - Mostrar Tabela")
    print("2 - Estatística Geral")
    print("3 - Contagem por Área")
    print("4 - Min, Méd, Máx Área")
    print("5 - Sibblings")
    print("6 - Sair")
    ans = int(input())
    if ans == 1:
        screenClear()
        showTable(f)
        next()
    if ans == 2:
        screenClear()
        statSal(f)
        next()
    if ans == 3:
        screenClear()
        checkAreaCount()
        next()
    if ans == 4:
        screenClear()
        pandasImport()
        next()
    if ans == 5:
        screenClear()
        showSibblings()
        next()
    if ans == 6:
        print("Bye!")
        break
