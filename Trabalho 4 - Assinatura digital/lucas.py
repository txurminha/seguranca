# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 21:25:51 2019

@author: Lucas

MENSAGEM ORIGIANAL
------------------
HASH(MENSAGEM)
------------------
ASSINATURA DO HASH
------------------
CHAVE PUBLICA
------------------
"""

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

''' --------------------------------  GRAVAÇÃO DOS DADOS NO ARQUIVO  ---------------------------- '''
f = open("trabalho4.pem", "wb")

'''MENSAGEM ORIGINAL'''
True_text = "Se você quiser descobrir os segredos do Universo, pense em termos de energia, frequência e vibração. 'Nikola Tesla'"
f.write(True_text.encode())
f.write(b'\n')

'''HASH DA MENSAGEM'''
hash_msg = SHA256.new(True_text.encode()).hexdigest().encode()
#hash_msg = hash_msg.encode('utf-8')
f.write(hash_msg)
f.write(b'\n')

'''CHAVE PUBLICA'''
random_seed = Random.new().read
keyPair = RSA.generate(1024, random_seed)
pubKey = keyPair.publickey()
f.write((pubKey.exportKey('PEM')))
f.write(b'\n')

'''ASSINATURA DIGITAL'''
digitalSign = keyPair.sign(hash_msg, '')
f.write(repr(digitalSign).encode())
f.write(b'\n')

f.close()



''' --------------------------------  LEITURA DO ARQUIVO E SEPARAÇÃO DOS DADOS  ---------------------------- '''
f = open("trabalho4.pem", "rb")
msg_content = f.readlines()
f.close()

fTrueText = msg_content[0].decode()
fHash = msg_content[1].decode()
fPubKey = (msg_content[2]+msg_content[3]+msg_content[4]+
           msg_content[5]+msg_content[6]+msg_content[7]).decode()
fDigitalSign = eval(msg_content[8])


'''------------------------   VERIFICAÇÃO -------------------------------'''
fHash_msg = SHA256.new(fTrueText.encode())

if(pubKey.verify(fHash_msg, fDigitalSign)):
    print(fTrueText)
    print("\nMensagem autentica!")
else:
    print("A mensagem não é autentica.")
    
    
