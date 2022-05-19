import requests


n = int(input())
responce = requests.get(f'http://shibe.online/api/shibes?count={n}')
links = responce.json()
for i in range(len(links)):
    with open(f'image{i}.jpg', 'wb') as image:
        image_bytes = requests.get(links[i]).content
        image.write(image_bytes)
with open('task1.txt', 'w') as file:
    for i in range(len(links)):
        file.write(links[i] + ' ')
        file.write(f'image{i}.jpg\n')
