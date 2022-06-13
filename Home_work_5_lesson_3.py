"""
5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
        Например:
>>> get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
"""


from random import choice

def get_jokes(num_jokes, repeate=False):
    all_jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for i in range(num_jokes):
        if not repeate:
            if num_jokes > len(nouns) or num_jokes > len(adverbs) \
                or num_jokes > len(adjectives):
                print('Not enought')
            else:
                noun = choice(nouns)
                adv = choice(adverbs)
                adj = choice(adjectives)

            nouns.remove(noun)
            adverbs.remove(adv)
            adjectives.remove(adj)

            resulting_joke = ' '.join([noun, adv, adj])
        else:
            resulting_joke = ' '.join([choice(nouns), choice(adverbs), choice(adjectives)])
        all_jokes.append(resulting_joke)
    return all_jokes

print(get_jokes(2))