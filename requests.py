import requests
superhero_url = 'https://superheroapi.com/api/2619421814940190/search/name'
superheroes = [{'name': 'Halk'}, {'name': 'Captain America'},{'name': 'Thanos'}]

for hero in superheroes:
    hero_r = requests.get(superhero_url + hero['name'])
    hero['intelligence'] = int(hero_r.json()['results'][0]['powerstats']['intelligence'])
print(sorted(superheroes, key=lambda hero: -hero['intelligence'])[0]['name'])