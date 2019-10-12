# -*- coding: utf-8 -*-
"""
#ESTRUTURA DO ARQUIVO
_____________________
MENSAGEM ORIGINAL
------------------
HASH(MENSAGEM)
------------------
CHAVE PUBLICA
------------------
ASSINATURA DO HASH
------------------

#NECESSARIO INSTALAR
pip install pycryptodome

#EXEMPLO DE USO
Assinar>> python trab4_gpg.py -ass doc1.txt ass.txt
Verificar>> python trab4_gpg.py -ver ass.txt
"""

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import pkcs1_15

import sys
import ast

'''
Comandos de entrada:
-ass <normal text file> <assigned text file> - Para assinar uma mensagem
-ver <assigned text file> - Para verificar assinatura de uma mensagem
'''
arg1 = None
arg2 = None

try:
    command = sys.argv[1]
    arg1 = sys.argv[2]
    if len(sys.argv) == 4:
        arg2 = sys.argv[3]
except:
    print("Comandos de entrada:")
    print("-ass <normal text file> <assigned text file> - Para assinar uma mensagem")
    print("-ver <assigned text file> - Para verificar assinatura de uma mensagem")
    sys.exit()

#Assinar
if  command == "-ass":
    file_n = open(arg1, 'r')
    file_e = arg2
    out = ""

    for line in file_n:
        out += line + '\n'

            
    '''GERAR PAR DE CHAVES'''
    key = RSA.generate(2048)
    private_key = key.export_key()
    file_out = open("private.pem", "wb")
    file_out.write(private_key)

    public_key = key.publickey().export_key()
    file_out = open("receiver.pem", "wb")
    file_out.write(public_key)
    
    '''HASH DA MENSAGEM'''
    hash_msg = SHA256.new(out.encode('utf-8'))
    
    '''ASSINATURA DIGITAL'''
    digitalSign = pkcs1_15.new(key).sign(hash_msg)
    
    if file_e:
        file_e = open(file_e, 'w')
        file_e.write(out)
        file_e.write('Hash: ')
        file_e.write(hash_msg.hexdigest())
        file_e.write('\r\n')
        file_e.write(public_key.decode('utf-8'))
        file_e.write('\r\n')
        file_e.write(str(digitalSign))
    else:
        print(out,'\n')
        print('Hash: ')
        print(hash_msg.hexdigest())
        print('\n')
        print(public_key)
        print('\n')
        print(digitalSign)

#Verificar
elif  command == "-ver":
    file_n = open(arg1, 'r')
    file_e = arg2
    
    if arg2:
        print("ERRO. -ver espera apenas um parametro, foi passado 2.")
        exit()
    
    out = ""
    key = ""
    hash = ""
    signature = ""

    state = 0
    
    for line in file_n:        
        #Ler Hash
        if "Hash: " in line:
            hash = line[6:]
            state = 1
        
        #Ler Chave Publica
        if state == 2:
            key += line 
        if "-----BEGIN PUBLIC KEY-----" in line:
            key += line
            state = 2
        if "-----END PUBLIC KEY-----" in line:
            state = 3
            continue
        #Ler assinatura
        if state == 3:
            signature += line

        #Ler Texto
        if state==0:
            out += line

    key = RSA.import_key(key.encode('utf-8'))
    h = SHA256.new(out.encode('utf-8'))
    signature = ast.literal_eval(signature)
    
    try:
        pkcs1_15.new(key).verify(h, signature)
        print("Assinatura OK.")
    except (ValueError, TypeError) as e:
        print("Falha.",e)
