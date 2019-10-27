# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 22:04:26 2019

@author: Lucas
"""
import math 

#Encriptando  
mensagem = "Se você quiser descobrir os segredos do Universo, pense em termos de energia, frequência e vibração. Nikola Tesla"
chave = 'HACK'

key_list = list()
for i, c in enumerate(chave):
    key_list.append((c, i))    
key_list.sort()
      
clear_msg_table = dict()
len_transposition_dict = math.ceil(len(mensagem)/len(key_list))*len(key_list)
for i in range(len_transposition_dict):
    try:
        clear_msg_table[i] = mensagem[i] 
    except IndexError:
        clear_msg_table[i] = ' '

encrypted_msg = ""    
for i in range(len(key_list)):
    offset = key_list[i][1]
    for j in range(int(len(clear_msg_table)/len(chave))):
        encrypted_msg = encrypted_msg + clear_msg_table[offset]
        offset += len(chave)


#Decriptando
key_list = list()
for i, c in enumerate(chave):
    key_list.append(c)    
key_list.sort()

for i, k in enumerate(key_list):
    key_list[i] = (k, i)

key_for_decrypt = list()
c=0
k=0
while len(key_for_decrypt) != len(chave):
    if chave[c] == key_list[k][0]:
        key_for_decrypt.append(key_list[k])
        k = 0
    else:
        k += 1
        continue
    c += 1
    k = 0
    
        
decrypted_msg_table = dict()
column_len = int(len(encrypted_msg)/len(chave))

temp_decrypt_msg = ''
for k in key_for_decrypt:
    offset = k[1]*(column_len)
    for i in range(column_len):
        temp_decrypt_msg = temp_decrypt_msg + encrypted_msg[i+offset]
        
decrypt_msg = ''
offset = column_len
i = 0
j = 0
while len(decrypt_msg) != len(temp_decrypt_msg):
    i = j  
    for k in range(len(chave)):
        decrypt_msg = decrypt_msg + temp_decrypt_msg[i]
        i = i + offset
    j += 1