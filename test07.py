import requests

nick = (input('Digite um Nick: '))
url = f'https://mush.com.br/api/player/{nick}'
response = requests.get(url)
data = response.json()
success = data['success']
clanN = "Nenhum"
ClanTAGN = "Nenhuma"
data2 = data['response']
nick2 = data['response']['account']['username']
type2 = data['response']['account']['type']
vip = data['response']['rank_tag']['name']
if 'clan' in data2:
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
else:
    print(nick2)
    print(type2)
    print('=-=' * 10)
    print(clanN)
    print(ClanTAGN)
    print('=-=' * 10)
    print(vip)
    print('=-=' * 10)




