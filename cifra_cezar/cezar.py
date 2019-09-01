# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 1key:24:33 2019

@author: Lucas
"""

def encrypt(text, key):

	encripted = ""
	for c in text:
		encripted += chr(ord(c) + (key%255))

	#print(encripted)
	return encripted

def decrypt(text, key):
    
    decrypted = ""
    for c in text:
        decrypted += chr(ord(c) - (key%2255))
        
    #print(decrypted, key)
    return decrypted

def get_key_from_clean_text(clen_text, encrypted_text):
    return ord(encrypted_text[0]) - ord(clen_text[0])

def dictonary_attach(encrypted_text):
    
    dictonary = load_dictonary()
    
    #considera '%' como espaço baseado na criptografia pela ASCII
    encrypted_text = encrypted_text.split('%')
    decrypted_text = '' #string temporaria para obeter a resposta
    
    test_word = encrypted_text[0]   #palavra teste para descritografia
    temp_set_dict = set()   #set temporario de criptografia do dicionario
    
    for key in range(256):
        for word in dictonary:
            temp_set_dict.add(encrypt(word, key))
        
        if test_word in temp_set_dict: #achou a chave
            
            #converte a lista em string
            for w in encrypted_text:
                decrypted_text += (str(w)+str("%")) #concatena o espaço para recontrução do texto
                
            decrypted_text = decrypt(decrypted_text, key)
            
            return 'Chave: '+str(key),  'Texto: '+decrypted_text #retorna chave, texto descritografado
        
    return "Chave não encontrada"
    
def load_dictonary():
    
    arquivo = open('dicionario.txt', 'r')
    dicionario = arquivo.readlines()
    arquivo.close()
    myset = set()
    for line in dicionario:
        line = line.strip().split(' ')
        for word in line:
              myset.add(word)
    
    return myset

def tests_functions():

    text = 'ansiedade é considerada um transtorno'
    key = 5
    
    print('\nTeste de criptografia')
    print('Texto: ', text)
    print('Criptografado: ', encrypt(text, key))
    print()
    
    print('Teste de descriptografia')
    print('Texto: ', encrypt(text, key))
    print('Descriptografado: ', decrypt(encrypt(text, key), key))
    print()
    
    print('Teste de quebra de chave com texto limpo')
    print('Texto limpo: ', text)
    print('Texto criptografado: ', encrypt(text, key))
    print('Chave encontrada: ', get_key_from_clean_text(text, encrypt(text, key)))
    print()
    
    print("Teste de ataque do dicionário")
    print('Texto a ser atacado: ', encrypt(text, key))
    print(dictonary_attach(encrypt(text, key)))
    

tests_functions()