'''Aplicação de exemplo de utilização da classe get_token,
esta aplicação envia os parâmetros para a classe que faz a
conexão com a API e recebe o access token

Desenvolvido por Thiago M. S. Bueno
thiago.msbueno@gmail.com

Sujestões de melhorias ou melhores práticas são bem vindas :)
'''

import requests
import os
import json

class Token:
    ''' Esta Classe recebe os paramêtros para realizar a autenticação'''

    def __init__(self, url, consumer_key, consumer_secret, code):
        self.url = url
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.code = code

    def get_token(self):
        ''' Este método execuda a chamada da URI, passando os parâmentros para API'''

        payload = {'consumer_key' : self.consumer_key, #Carrega parâmetros
                   'consumer_secret' : self.consumer_secret,
                   'code' : self.code}

        headers = {'Accept' : 'application/json'} #Cria Cabeçalho
        response = requests.post(self.url, json=payload, headers=headers) #Monta URI e chama URI
        response = response.json() #Transofrma em Json
        return(response['access_token']) #Carrega retorno indice token!
        print(response['access_token'])
