from nltk.corpus import ptb
import os

def tree2prod(trees):
    prods = []
    for t in trees:
        prods += t.productions()
    return prods
path = '/Users/pengwu5501/nltk_data/corpora/ptb/wsj'
files = os.listdir(path)
productions = []
cnt = 0
for file in files:
    sub_path = os.path.join(path, file)
    sub_file = os.listdir(sub_path)
    for item in sub_file:
        name = os.path.join(sub_path,item)
        tbank = ptb.parsed_sents(name)
        productions += tree2prod(tbank)
        set(productions)
        cnt += 1
        print(len(productions))
gramm = CFG(Nonterminal('S'), productions)
print(gramm)