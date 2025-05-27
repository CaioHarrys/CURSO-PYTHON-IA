

import requests #biblioteca de requisição

def buscar_endereco(cep, campo):
    url = f'https://viacep.com.br/ws/{cep}/json/' #rota

    response = requests.get(url) #verifica dentro na rota se a requisição pode ser atendida

    if response.status_code == 200: #verifica se o status code da resposta é 200
        dados = response.json() #pega a informação json que ele devolveu
        endereco = f'{dados['logradouro']}, {dados['bairro']}, {dados['localidade']}, {dados['uf']}' #formata o arquivo json
        campo.value = endereco
        campo.update()
