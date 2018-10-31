'''Aplicação de exemplo de utilização da classe get_token,
esta aplicação envia os parâmetros para a classe que faz a
conexão com a API e recebe o access token

Desenvolvido por Thiago M. S. Bueno
thiago.msbueno@gmail.com

Sujestões de melhorias ou melhores práticas são bem vindas :)
'''

from classe import Token #Carregando dados de acesso a API

url = 'https://www.SUAURLDEAUTENTICAÇÃO.com.br/web_api/auth' #Passa parâmetro da URL de autenticação
consumer_key = 'SEU_CONSUMER_KEY_' #Chave de acesso
consumer_secret= 'SEU_CONSUMER_SECRET' #Consumer secret
code = 'SEU_CODIGO_DE_APLICAÇÃO_ATORIZAÇÃO' #Codigo de aplicação


my_token = Token(url, consumer_key, consumer_secret, code).get_token()

print(api)
