# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:37:31 2019

@author: Lucas
"""

def count_sub_graphs(buracos):
    subgraphs = list()
    atual = buracos[0]
    count = 0
    
    for b in enumerate(buracos):
                   
        if atual[1] == False:
            atual[1] = True
            count+=1
            atual = buracos[atual[0]-1]
    
        if atual[1] == True:
            subgraphs.append(count)
            count=0
            
            for i, j in enumerate(buracos):
                if j[1] == False:
                    atual = buracos[i]

                    break
            
    return subgraphs
        
        
def mmc(num1=1, num2=1):
        
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    while True:
        if maior % num1 == 0 and maior % num2 == 0:
            break
        else:
            maior += 1
            
    return maior

#qtd = int(input())
#buracos = input()
buracos = '3 1 5 2 4 8 6 7 10 9 12 13 14 11'

buracos = buracos.split(' ')
buracos = [[int(b), False] for b in buracos] #cast in int each element

subgraphs = count_sub_graphs(buracos)

mmc_temp = 1
for sb in subgraphs:
    mmc_temp = mmc(sb, mmc_temp)
    
print (mmc_temp)            