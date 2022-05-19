import requests, json
from urllib.request import urlopen

n = int(input())
for k in range(n):
    site = urlopen(f'https://www.thecocktaildb.com/api/json/v1/1/random.php')
    drinks = json.load(site)['drinks'][0]
    for i in range(1, 16):
        if drinks[f'strIngredient{i}'] is None:
            break
        site2 = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?i=' + drinks[f'strIngredient{i}'])
        if site2.json()['ingredients'][0]['strType'] == 'Fruit':
            image_byte = requests.get(drinks['strDrinkThumb'])
            name = drinks['strDrink']
            with open(name + '.jpg', 'wb') as image:
                image.write(image_byte.content)
            break
