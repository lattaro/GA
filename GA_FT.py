
import pandas as pd
import numpy as np
import random
import heapq
from scipy.stats import entropy

from numpy.random import randint


ind_ref_1 = 1.0000000000000000
ind_ref_2 = 1.5000000000000000
ind_ref_3 = 3.3999999999999999

#Definindo mutação
mutacao_1 = 2
mutacao_2 = 3
mutacao_3 = 1

#Comprimento de onda

total = 1
comprimento = [0.0000015555511]

lambda_arq = open('C:\\Users\\Alex\\Documents\\Python\\GA\\lambdas','w')

k = 0
while k < total:
    lambda_arq.write('{:0d}\n'.format(total)) 
    lambda_arq.write('{:000000000f}\n'.format(comprimento[k]))
    k = k + 1


#Começar do zero - control=0; utlizar melhor otimização - control=1
control=0
	
nmaterfix = 3   #numero de indices fixos
ngeracao = 2   #numero de gerações
nmatcros = 3    #numero de materiais que cada coluna pode assumir
popu_ini = 4   #populacao inicial
conmutacao=10   #Probabilidade de mutação
concrossover=0.9 #Probabilidade de crossover


malha_2 = open('C:\\Users\\Alex\\Documents\\Python\\GA\\Malha_2.txt','r')


linha = malha_2.readline()
valores = linha.split()
x = valores[4]
ntmater = int(x)

Lcromo = ntmater + 1
print('lcromo:',Lcromo)



geracao = 0

while geracao <= ngeracao:
    
    p = 1
    amostra_final = []
    while p <= popu_ini:
        print('Geração = ',geracao)
        print("*")
        print('População = ',p, 'de', popu_ini)
        
        print('*')
        z = 0
        aptidao = []
        while z <= 3:
            malha_3 = open('C:\\Users\\Alex\\Documents\\Python\\GA\\Malha_3.txt','w')

            matriz_aleatoria = []

            i = 0
            k = 1
            while i <= popu_ini/2:
                while k	<= Lcromo:
                    x = random.uniform(0, 1)
                    if x <= 0.33:
                        matriz_aleatoria.append(ind_ref_1)
                        k = k+1
                    elif x > 0.33 and x <= 0.66:
                        matriz_aleatoria.append(ind_ref_2)
                        k = k+1
                    elif x> 0.66 and x <=1:
                        matriz_aleatoria.append(ind_ref_3)
                        k = k+1
                i = i+1
            


            j = 1
            while j < Lcromo:
                if j<10:
                    malha_3.write('            {}   {:.16f}        {:.16f} \n'.format(j,matriz_aleatoria[j],0.0))
                elif j>=10:
                    malha_3.write('           {}   {:.16f}        {:.16f} \n'.format(j,matriz_aleatoria[j],0.0))
                malha_3 
                j = j+1
            print('malha_3:',matriz_aleatoria)
            malha_3.close()    
            # substituir o amostra pelo FEM
            #amostra = subprocess.run(['C:\\Users\\Alex\\Documents\\Python\\GA\\teste_3.py'])
            amostra = np.linalg.norm(matriz_aleatoria)
            
            
            arquivo_amostra = open('C:\\Users\\Alex\\Documents\\Python\\GA\\Arquivo_amostra.txt','w')
            arquivo_amostra.write('{}      {:0000000000000000f} \n'.format(amostra,0.0000000000000000))
            print('\namostra: ',amostra,'\n')
            aptidao.append(amostra)
           #aptidao = aptidao.max()
            
            print('\naptidao: ',aptidao)
            
            
            z = z+1
        aptidao_final = max(aptidao)
        print('aptidao_final: ',aptidao_final)    
        amostra_final.append(aptidao_final)    
            
        p = p+1
    geracao = geracao + 1
    print('\namostra_final: ',amostra_final)
    soma = sum(amostra_final)
    #print('soma: ',soma)
    fitness = []
    i = 0
    while i < popu_ini:
        x = amostra_final[i]/soma
        fitness.append(x)
        i = i+1
    print('\nfitness: ',fitness)

    # seleção do pior indivíduo para o elitismo
    valor_maximo = 1000
    i = 1
    elitismo = 0
    while i < popu_ini:
        if fitness[i] < valor_maximo:
            valor_maximo = fitness[i]
            elitismo = i
        i = i + 1

    
    # Seleção dos melhores pais   
    pais = fitness
    pais = heapq.nlargest(4,pais)
    
    
    print('\npais: ',pais)  
    pai1 = pais[:2]  
    print('\npai1: ',pai1)
    pai2 = pais[2:]
    print('\npai2: ',pai2)


    #Crossover
    c_1 = pai1.copy()
    c_2 = pai2.copy()
    if random.uniform(0,1) <= concrossover:
        cross_over_point = randint(1, 3)
        c_1 = pai1[:cross_over_point] + pai2[cross_over_point:]
        c_2 = pai2[:cross_over_point] + pai2[cross_over_point:]
        print('criança 1:',c_1)
        print('criança 2:',c_2)
    promutacao = random.uniform(0,1)
    print('promutacao: ',promutacao)
    print('Lcromo: ',Lcromo)

    # Mutação
    if promutacao <= conmutacao:
        mutacao = random.uniform(0,1) * Lcromo
        x = int(mutacao)
        print('mutacao: ',mutacao)
        print('x: ',x)
        #amostra_final[x]


    
