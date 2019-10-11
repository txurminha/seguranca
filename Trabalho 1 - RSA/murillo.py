import math

def phi(n):
    amount = 0
    for k in range(1, n+1):
        if math.gcd(n,k) == 1:
            amount += 1
    return amount
    
def multiplicative_inverse(A, M):
    for i in range(0, M):
        if (A*i) % M == 1:
            return i
    return -1

'''
n = 1073
e = 71
c = 436
'''

keyb = input().split(" ")

n = int(keyb[0]) #Chave publica
e = int(keyb[1]) #Expoente da chave publica
c = int(keyb[2]) #mensagem criptografada

#Achar D, que é o inverso multiplicativo de E modulo tot(N)

d = multiplicative_inverse(e, phi(n))
m = pow(c,d)%n
print(m)
