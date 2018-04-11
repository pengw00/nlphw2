from nltk.corpus import ptb
from nltk.tree import Tree
import os
def getCFG(tree):
    line = ''
    if isinstance(tree, Tree):
        line += tree.label()
        line += ' '
        line += '->'
        for subtree in tree:
            if isinstance(subtree, Tree):
                line += ' '
                line += subtree.label()
            else:
                line += ' '
                line += '"'
                line += subtree
                line += '"'
        print(line)

def traversal(tree):
    getCFG(tree)
    for subtree in tree:
        if isinstance(subtree, Tree):
            traversal(subtree)
path = '/Users/pengwu5501/nltk_data/corpora/ptb/wsj'
files = os.listdir(path)
for file in files:
    sub_path = os.path.join(path, file)
    mrg = os.listdir(sub_path)
    for item in mrg:
        name = os.path.join(sub_path, item)
        tree = ptb.parsed_sents(name)
        for tre in tree:
            traversal(tre)