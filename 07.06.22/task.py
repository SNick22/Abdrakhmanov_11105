import re
from functools import reduce
from collections import Counter

with open('text.txt', encoding='utf-8') as file:
    text = file.read()
words = re.findall(r'(?:\w+‑\w+)|(?:\w+)', text)
last_words = []
for word in words:
    if word.lower() not in last_words:
        last_words.append(word.lower())
first_letter_words = {}
for word in words:
    try:
        first_letter_words[word[0].lower()] += 1
    except KeyError:
        first_letter_words[word[0].lower()] = 1
sorted_words = sorted(first_letter_words.items(), key=lambda x: x[0])
cnt = Counter(map(lambda x: x.lower(), words))

with open('text.txt', 'a', encoding='utf-8') as file:
    file.write(f'\n\n{len(last_words)}\n')
    for i in sorted_words:
        file.write(f'\n{i[0]}: {i[1]}')
    file.write(f'\n\n{reduce(lambda a, b: a if len(a) > len(b) else b, words)}')
    file.write(f'\n\n{cnt.most_common()[0][0]}')


def shift(word):
    if len(word) > 4:
        if len(word) % 2 == 0:
            return word[-1] + word[:-1]
        else:
            return word[1:] + word[0]
    else:
        return word


for word in words:
    text = text.replace(word, shift(word), 1)

with open('text.txt', 'a', encoding='utf-8') as file:
    file.write(f'\n\n{text}')
