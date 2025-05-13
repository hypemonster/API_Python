import requests

nick = (input('Digite um Nick: '))
url = f'https://mush.com.br/api/player/{nick}'
response = requests.get(url)
data = response.json()
nick2 = data['response']['account']['username']
type2 = data['response']['account']['type']
vip = data['response']['rank_tag']['name']

if data == ['response']['clan']['name']:
    clannome = data['response']['clan']['name']
    clantag = data['response']['clan']['tag']

    print(nick2)
    print(type2)
    print('=-=' * 10)
    print(clannome)
    print(clantag)
    print('=-=' * 10)
    print(vip)
    print('=-=' * 10)