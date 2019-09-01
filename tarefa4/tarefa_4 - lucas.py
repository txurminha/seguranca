# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 13:08:43 2019

@author: Lucas
"""

import time

def mmc(num1, num2):
        
    if num1 > num2:
        maior = num1
    else:
        maior = num2
    while True:
        if maior % num1 == 0 and maior % num2 == 0:
            return maior
        else:
            maior += 1

def fast_sum_multiples(n, m1, m2):
    
    a = (m1 * int(n/m1) * (int(n/m1)+1))/2
    b = (m2 * int(n/m2) * (int(n/m2)+1))/2
    c = (mmc(m1, m2) * int(n/mmc(m1, m2)) * (int(n/mmc(m1, m2))+1))/2
    return a + b - c - n
    

def sum_multiples(n, m1, m2):
    
    sum = 0
    for i in range(n):
        if i%m1==0 or i%m2==0:
            sum+=i
    return sum


inicio = time.time()
x = fast_sum_multiples(10**6, 3, 5)
fim = time.time()
print("Somatório rápido: {} - Tempo {}".format(x, fim - inicio))

inicio = time.time()
x = sum_multiples(10**6, 3, 5)
fim = time.time()
print("Somatório com laço: {} - Tempo {}".format(x, fim - inicio))
