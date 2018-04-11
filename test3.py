from nltk.draw.tree import draw_trees
from nltk import tree, treetransforms
from copy import deepcopy
from nltk.corpus import ptb
from nltk.corpus import treebank
t = ptb.parsed_sents('/Users/pengwu5501/nltk_data/corpora/ptb/wsj/00/wsj_0001.mrg')
for item in t:
    item = treetransforms.chomsky_normal_form(item)
    print(item)
