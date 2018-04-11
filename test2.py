from nltk.corpus import ptb
from nltk.tree import Tree
import copy
from nltk.corpus import treebank
#print(ptb.words('/Users/pengwu5501/nltk_data/corpora/ptb/wsj/00/wsj_0001.mrg'))
#print(treebank.fileids())
t = ptb.parsed_sents('/Users/pengwu5501/nltk_data/corpora/ptb/wsj/00/wsj_0001.mrg')
s = []
for tree in t:
    #print(tree.label())
    #print(tree.label())
    #print(tree.subtrees())
    #for subtree in tree.subtrees():
        #print(subtree.label())
    #print(s)
    #for item in s:
        #print(item.label())
    k = tree.productions()
    #chunk = tree.
#for item in k:
    #print(item)
s = []
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
for tree in t:
    traversal(tree)




