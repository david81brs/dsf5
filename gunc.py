#Quem mais recebe e quem menos recebe na empresa e a média salarial da empresa
#Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área
#A área com mais funcionários e a área com menos funcionários
#Das pessoas que têm o mesmo sobrenome, aquela que recebe mais (não inclua sobrenomes que apenas uma pessoa tem nos resultados)

import json
import os
import pandas as pd

def safeClear():
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
    with open(file) as json_data:
        d = json.load(json_data)
    n = d['funcionarios']
    dfpandas = pd.DataFrame.from_dict(n)
    print(dfpandas)
    byArea = dfpandas.groupby('area')

    print(byArea['nome'])

    print("Média por área:")
    print(byArea.mean())

    print("Mínimos por área:")
    print(byArea.min())

    print("Máximos por área:")
    print(byArea.max())
    return dfpandas

def showTable(f):
    print("id\tnome\tsalario\tarea")
    for i in range(0,len(f)):
        print(i, end="\t")
        print(f[i]['nome'],end="\t")
        print(f[i]['salario'],end="\t")
        print(f[i]['area'], end="\n")

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

def checkAreaSal():
    stArea =  dao("A")
    stFunc = dao("F")
    count = []
    for i in range(0,len(stArea)):
        sum = 0
        index  = 0
        idmax = ""
        idmin = ""
        for k in range(0,len(stFunc)):
            smax = 0
            if stArea[i]['codigo'] == stFunc[k]['area']:
                sum += stFunc[k]['salario']
                index+=1

                if stFunc[k]['salario'] > smax:
                    smax = stFunc[k]['salario']
                    idmax = (stFunc[k]['nome'], stFunc[k]['salario'], stFunc[k]['area'])

                smin = stFunc[k]['salario']

                if stFunc[k]['salario'] < smin:
                    smin = stFunc[k]['salario']
                    idmin = (stFunc[k]['nome'], stFunc[k]['salario'], stFunc[k]['area'])
        count.append(index)
        print("Média Salarial em  %s \t %.2f " % (stArea[i]['nome'], sum/index))
        #print("Funcionário  %s está rico ganhando %.2f na área %s" % (idmax[0], idmax[1], idmax[2]) )
        print("Max: %s %s" %(idmax,smax,))
        print("Min: %s %s" %(idmin,smin,))
        #print("Funcionário  %s está pobre ganhando %.2f na área %s" % (idmin[0], idmin[1], idmin[2]) )
    print("Área com (+) integrantes: %i %s" % (max(count), stArea[count.index(max(count))]['nome']) )
    print("Área com (-) integrantes: %i %s" % (min(count), stArea[count.index(min(count))]['nome']) )

def statSal(f):
    print("Max Sal: %s %.2f " % (checkMaxSal(f)[0], checkMaxSal(f)[1]) )
    print("Mean Sal: %.2f" % checkMeanSal(f))
    print("Min Sal: %s %.2f" % (checkMinSal(f)[0], checkMinSal(f)[1]) )

while(True):
    safeClear()
    print("Desafio 5 - Tada!!!")
    print("1 - Mostrar Tabela")
    print("2 - Estatística Geral")
    print("3 - Estatística Área")
    print("4 - Pandas MODE")
    print("5 - Sair")
    ans = int(input())
    if ans == 1:
        safeClear()
        showTable(f)
        next()
    if ans == 2:
        safeClear()
        statSal(f)
        next()
    if ans == 3:
        safeClear()
        checkAreaSal()
        next()
    if ans == 4:
        safeClear()
        pandasImport()
        next()
    if ans ==5:
        print("Bye!")
        break
