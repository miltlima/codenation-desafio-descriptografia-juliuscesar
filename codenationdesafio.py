# Milton Lima
#Criptografia de július Cesar desafio da Codenation

import json
import requests
import hashlib

# Consumo da API da Codenation 
url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=token_do_usuário"
answer = requests.get (url) 
print (answer.status_code)
resposta = answer.json()
casas = (resposta['numero_casas'])
cifrado = (resposta['cifrado'])
arquivo = 'answer.json'

# Criçao de dois Dicionários para fazer varredura reversa.
alfa = dict(zip("abcdefghijklmnopqrstuvwxyz", range(26)))
alfainv = dict(zip(range(26), "abcdefghijklmnopqrstuvwxyz"))

#Código de Decifragem 
decifrado = ''
for i in cifrado:
    if i.isalpha(): 
        decifrado += alfainv[( alfa[i] - casas)%26]
    else: 
        decifrado += i

#Hash no Resumo Criptográfico
resumo = hashlib.sha1(decifrado.encode())

# inclusão dos dados de resposta do texto decifrado e da resposta do resumo criptográfio
with open(arquivo, 'w') as arq:
    resposta["decifrado"] = decifrado
    resposta["resumo_criptografico"] = resumo.hexdigest()
    json.dump(resposta, arq)

# Post
token = 'token do usuário'
params = {'token': token}
POST = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution"
answer = {'answer': open('answer.json', 'rb')}
envio = requests.post(POST, files=answer, params=params)
print(envio)