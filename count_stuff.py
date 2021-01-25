fname = "demo_text.txt"
f = open(fname)

words = []
for line in f:
    for word in line.split():
        words.append(word)

f.close()


# Задача: посчитать какое слово
# сколько раз встретилось в тексте

def default_func():
    # ещё пробовали return [0] и аппендить вместо += 1
    return 0


# minimal python way
words_freqs = dict()
for w in words:
    if w not in words_freqs:
        words_freqs[w] = default_func()
    words_freqs[w] += 1
print(words_freqs)

# defaultdict way
from collections import defaultdict

# дефолтфунк будет вызвана каждый рас
# когда мы полезем в этом словаре по отсутствующему ключу
words_freqs_dd = defaultdict(default_func)
for w in words:
    words_freqs_dd[w] += 1
print(words_freqs_dd)

# Counter -- супертулза для подсчёта

from collections import Counter

words_counted = Counter(words)
print(type(words_counted))
print(words_counted)
print(words_counted.most_common(2))
print(words_counted["ест"])
