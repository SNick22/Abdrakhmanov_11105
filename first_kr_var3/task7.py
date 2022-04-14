# variant 2
import re

with open('input.txt', encoding='utf-8') as input:
    strings = input.readlines()
    with open('output.txt', 'w') as output:
        for string in strings:
            words = re.findall(r'\b[БВГДЖЗЙКЛМНПРСТФХЦЧШЩЬЪьъбвгджзйклмнпрстфхцчшщ]*(?:[ауоыиэяюёеАУОЫИЭЯЮЁЕ]'
                               r'[-БВГДЖЗЙКЛМНПРСТФХЦЧШЩЬЪьъбвгджзйклмнпрстфхцчшщ]*[ауоыиэяюёеАУОЫИЭЯЮЁЕ]'
                               r'[-БВГДЖЗЙКЛМНПРСТФХЦЧШЩЬЪьъбвгджзйклмнпрстфхцчшщ]*)*[ауоыиэяюёеАУОЫИЭЯЮЁЕ]'
                               r'[БВГДЖЗЙКЛМНПРСТФХЦЧШЩЬЪьъбвгджзйклмнпрстфхцчшщ]*[^-w]',
                               string)
            for word in words:
                output.write(word)
