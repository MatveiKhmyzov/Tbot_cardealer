import json

word_lst = []

with open('../Tbot_cardealer/blacklist.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            word_lst.append(n)

with open('../Tbot_cardealer/blacklist.json', 'w', encoding='utf-8') as e:
    json.dump(word_lst, e)