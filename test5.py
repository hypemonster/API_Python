import requests
error = 0
while error != 1:
    try:
        cep = (input('Digite seu CEP: '))
        url = f'https://viacep.com.br/ws/{cep}/json/'
    
        response = requests.get(url)
        data = response.json()
        error = 1
        CEP2 = data['cep']
        logradouro = data['logradouro']
        bairro = data['bairro']
        localidade = data['localidade']
        uf = data['uf']
        estado = data['estado']
        regiao = data['regiao']

        print('=-='*15)
        print(f'CEP: {CEP2}')
        print(f'Logradouro: {logradouro}')
        print(f'Bairro: {bairro}')
        print(f'Localidade: {localidade}')
        print(f'UF: {uf}')
        print(f'Estado: {estado}')
        print(f'Região: {regiao}')
        print('=-='*15)
    
    except requests.exceptions.JSONDecodeError:
        print('CEP inválido. Tente novamente')
        print('-=-' * 10)
        error = 0

