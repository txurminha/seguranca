# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:17:43 2019

@author: Lucas
"""

len_ascii_table = 256    #quantidade de caracteres que deseja analisar da table ascii
offset = 0             #offset para o simbolo inicial (e.g. Alfabato em caixa alta deixar offset em 65)

def generate_vigere_table():
    
    vigenere_table = dict()
    shifter_counter = 0    
    
    for i in range(len_ascii_table):
        shifter_counter = i
        shifter_alphabet_temp = list()
        for j in range(len_ascii_table):
            shifter_alphabet_temp.append(chr(shifter_counter+offset))
            shifter_counter += 1         
            shifter_counter = shifter_counter%(len_ascii_table)
        vigenere_table[chr(i+offset)] = shifter_alphabet_temp
    return vigenere_table


def vigenere_encrypt(vigenere_table, clean_text, key):

    clean_text_list = list()
    for c in clean_text:
        clean_text_list.append(c)

    key_list = list()        
    for k in key:
        key_list.append(ord(k)-offset)
        
    encrypted_text = ""
        
    for i, c in enumerate(clean_text_list):     
        encrypted_text = encrypted_text + vigenere_table[c][key_list[i%len(key_list)]]                           
    
    return encrypted_text



def vigenere_decrypt(vigenere_table, encrypted_text, key):
    
    encrypted_text_list = list()
    for c in encrypted_text:
        encrypted_text_list.append(c)

    key_list = list()        
    for k in key:
        key_list.append(k)
        
    decrypted_text = ""
    
    for i, e in enumerate(encrypted_text_list):
        for j in range(len_ascii_table):
            if vigenere_table[key_list[i%len(key_list)]][j] == encrypted_text_list[i%len(encrypted_text_list)]:
                decrypted_text += chr(j+offset)

    return decrypted_text



mensagem = "Se você quiser descobrir os segredos do Universo, pense em termos de energia, frequência e vibração. Nikola Tesla"
chave = "369111719"

vigenere_table = generate_vigere_table()
encrypted_text = vigenere_encrypt(vigenere_table, mensagem, chave)
decrypted_text = vigenere_decrypt(vigenere_table, encrypted_text, chave)


print("\nQuantidade de caracteres utilizados na tabela de Vigenére: ", len_ascii_table)
print("\nDeslocamento: ", offset)
print("\nTexto Original: ", mensagem)
print("\nChave: ", chave, "Tamanho: ", len(chave))
print("\nTexto Criptografado: ", encrypted_text)
print("\nTexto Descriptografado: ", decrypted_text)






