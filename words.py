'''
An analysis of the dialogue in Hamlet

1- Count the frequency of each word
'''


# Count the frequency of each word

# counts = {}
# with open('data/dialogue.txt') as f:
#     for line in f:
#         for word in line.split():
#             counts[word] = counts.get(word,0) + 1
#             # .get good in avoiding if conditions / try-except
#
# # show the first 3 most common words in "Hamlet"
# # best approach: from collections import Counter
# print sorted(counts.items(), key=lambda p: p[1], reverse=True)[:3]

# redone with Counter

from collections import Counter
import random

counts = Counter()
with open('data/dialogue.txt') as f:
    for line in f:
        for word in line.split():
            counts[word] += 1 # the counter class uses the .get(key,0)
# easy way to get the most common #
# print counts.most_common(3)


# task 2
# Organize the unique words by first letter
# words = {} # first letter --> set of words
# with open('data/dialogue.txt') as f:
#     for line in f:
#         for word in line.split():
#             initial = word[0]
#             # we use the set-default
#             words.setdefault(initial, set()).add(word)

# for your convenience
from collections import defaultdict
# warning, the defaultdict will never trigger a KeyError
words = defaultdict(set) # first letter --> set of words
with open('data/dialogue.txt') as f:
    for line in f:
        for word in line.split():
            initial = word[0]
            # we use the set-default
            words[initial].add(word)

'''
task3
word --> list of words that follow
'''

# chain = defaultdict(list)
# last = None


# # Train
# with open('data/dialogue.txt') as f:
#     for line in f:
#         for word in line.split():
#             chain[last].append(word)
#             last = word

# Walk
# word = random.choice(list(chain))
# print word
#
# while word[-1] not in '.?!':
#     word = random.choice(chain[word])
#     print word,

# Improved Train
from collections import defaultdict
import random

def train(filename, size=1):
    chain = defaultdict(list)
    last = (None,) * size
    with open(filename) as f:
        for line in f:
            for word in line.split():
                chain[last].append(word)
                last = last[1:] +  (word,)
    return chain

# Walk
def walk(chain):
    last = random.choice(list(chain))
    for word in last:
        print word,
    while word[-1] not in '.?!':
        word = random.choice(chain[last])
        print word,
        last = last[1:], (word,)

def randomness(chain):
    d = sum(len(set(options)) > 1
        for options in chain.values())
    return float(n) / len(chain)

if __name__ == '__main__':
    chain = train('data/dialogue.txt', 4)
    walk(chain)