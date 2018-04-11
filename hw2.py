from itertools import product

def get_vocab(tex):
    return set([word for sentence in text for word in sentence])
input1 = [['A', 'B', 'C', 'D', 'E'],
          ['D', 'E', 'C', 'D', 'E'],
          ['A', 'C', 'D', 'D']]
a = product(range(3),repeat=1)