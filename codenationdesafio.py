import json
import requests
from hashlib import sha1
#resumo = sha1(message.encode('utf-8')).hexdigest()

url = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=8e74a0c74448578cf37ff4f839d02039e9400b4b"
answer = requests.get (url) # resposta da URL
print (answer.status_code)
resposta = answer.json()
casas=(resposta['numero_casas'])
cifrado = (resposta['cifrado'])
arquivo = 'answer.json'

alfa = dict(zip("abcdefghijklmnopqrstuvwxyz", range(26)))
alfainv = dict(zip(range(26), "abcdefghijklmnopqrstuvwxyz"))

decifrado = ''
for i in cifrado:
    if i.isalpha(): decifrado += alfainv[( alfa[i] - casas)%26 ]
    else: decifrado += i
with open(arquivo, 'w') as file_object:
    json.dump(resposta, file_object)  
print(decifrado)

