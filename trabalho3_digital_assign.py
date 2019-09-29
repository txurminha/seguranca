import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import base64

def rsakeys():  
     length=1024  
     privatekey = RSA.generate(length, Random.new().read)  
     publickey = privatekey.publickey()  
     return privatekey, publickey
 
def encrypt(rsa_publickey,plain_text):
     cipher_text=rsa_publickey.encrypt(plain_text,32)[0]
     b64cipher=base64.b64encode(cipher_text)
     return b64cipher
 
def decrypt(rsa_privatekey,b64cipher):
     decoded_ciphertext = base64.b64decode(b64cipher)
     plaintext = rsa_privatekey.decrypt(decoded_ciphertext)
     return plaintext
 
def sign(privatekey,data):
    return base64.b64encode(str((privatekey.sign(data,''))[0]).encode())

def verify(publickey,data,sign):
     return publickey.verify(data,(int(base64.b64decode(sign)),))
 
privatekey,publickey=rsakeys()
print('Chave privada: ',privatekey)
print('Chave pública: ',publickey) 

text=b"TEXTO TESTE"   

ct=encrypt(publickey,text)
print("Texto cifrado: ", ct)

dt=decrypt(privatekey,ct)
print("Texto decifrado: ", dt)

sing_data = sign(privatekey, dt)

print('Verificação da assinatura: ', verify(publickey, dt, sing_data))