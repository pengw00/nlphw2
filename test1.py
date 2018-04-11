from nltk.corpus import treebank
from nltk.corpus import ptb
import os, string, sys, time, re, math, fileinput, glob, shutil, stat
path = '/Users/pengwu5501/nltk_data/corpora/ptb/wsj'
files = os.listdir(path)
for file in files:
    sub_path = os.path.join(path, file)
    mrg = os.listdir(sub_path)
    for item in mrg:
        name = os.path.join(sub_path, item)
        tree = ptb.parsed_sents(name)
        for tre in tree:
            p = tre.productions()
            print(p)

"""
t = treebank.parsed_sents('/Users/pengwu5501/nltk_data/corpora/ptb/wsj/00/wsj_0001.mrg')
#print(len(t))
for tree in t:
    list = []
    line = ''
    line += tree.label() + '->'
    for child in tree:
        line += child.label() + ' '
    list.append(line)
    print(list)
for child in t.subtrees():
    k = ''
    k += child.label() + '->'
    for item in child:
        k += item.label()
        list.append(k)
        print(list)
        #k = child.productions()
"""