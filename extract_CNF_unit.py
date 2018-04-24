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
                line += '\''
                line += subtree
                line += '\''
    return line
"""traversal tree"""
def traversal(tree, lis):
    lis.append(getCFG(tree))
    for subtree in tree:
        if isinstance(subtree, Tree):
            traversal(subtree,lis)
    return lis
"""convert to CNF function"""

def sub_r(sub_rule, list_rule):
    sub = sub_rule.split('_')
    if len(sub) == 2:
        sub_rule += ' '
        sub_rule += '->'
        for item in sub:
            sub_rule += ' '
            sub_rule += item
        list_rule.append(sub_rule)
    else:
        sub_rule += ' '
        sub_rule += '->'
        sub_rule += ' '
        sub_rule += sub[0]
        for item in sub[2:]:
            sub[1] += '_'
            sub[1] += item
        sub_rule += ' '
        sub_rule += sub[1]
        sub_r(sub[1],list_rule)
        list_rule.append(sub_rule)
    l = []
    for i in range(len(list_rule)):
        l.append(list_rule[len(list_rule)-i-1])
    return l
"""process chunk"""
path = '/Users/pengwu5501/Downloads/wsj-2'
files = os.listdir(path)
l = []
grammar = {}
i = 0
dict_word = {}
dict_unit_rule = {}
unit = 0
ter = 0
for file in files:
    sub_path = os.path.join(path, file)
    mrg = os.listdir(sub_path)
    for item in mrg:
        name = os.path.join(sub_path, item)
        tree = ptb.parsed_sents(name)
        for tre in tree:
            list = []
            p = traversal(tre,list)
            for item in p:
                it = item.split('->')
                late = it[1].split()
                if len(late) > 2:
                    for item_ in late:
                        if item_.find('\'') == 0:
                            break
                    it[0] += ' '
                    it[0] += '->'
                    it[0] += ' '
                    it[0] += late[0]
                    it[0] += ' '
                    it[0] += late[1]
                    sub_rule = late[1]
                    for item in late[2:]:
                        it[0] += '_'
                        sub_rule += '_'
                        it[0] += item
                        sub_rule += item
                    #print('original',it[0])
                    if it[0] in grammar:
                        grammar[it[0]] += 1
                    else:
                        grammar[it[0]] = 1
                    list_rule = []
                    sub_list = sub_r(sub_rule, list_rule)
                    for item in sub_list:
                        #print('sub',item)
                        if item in grammar:
                            grammar[item] += 1
                        else:
                            grammar[item] = 1
                elif len(late) == 2:
                    #print('second', item)
                    i += 1
                    if item in grammar:
                        grammar[item] += 1
                    else:
                        grammar[item] = 1
                else:
                    i += 1
                    for item1 in late:
                        if item1.find('\'') == -1:
                            #print('unit', item)
                            if item in dict_unit_rule:
                                dict_unit_rule[item] += 1
                            else:
                                dict_unit_rule[item] = 1
                            list_unit = item.split('->')
                        if item1.find('\'') == 0:
                            #print('terminal', item)
                            word_pro = item.split('->')
                            if item in dict_word:
                                dict_word[item] += 1
                                grammar[item] += 1
                            else:
                                dict_word[item] = 1
                                grammar[item] = 1
#print(count)
print(len(grammar))
print(len(dict_word))
print(len(dict_unit_rule))
for item1 in dict_unit_rule:
    terminal = item1.split('->')
    #print('first',terminal[1])
    for item2 in dict_word:
        FirstNode = terminal[1]
        word = item2.split('->')
        SecondNode = word[1]
        #print('next',word[0])
        if terminal[1].strip() == word[0].strip():
            #print('true', terminal[1], word[0])
            FirstNode += ' '
            FirstNode += '->'
            #FirstNode += ' '
            FirstNode += SecondNode
            #print(FirstNode)
            if FirstNode in grammar:
                grammar[FirstNode] += dict_word[item2]
            else:
                grammar[FirstNode] = dict_word[item2]
print(len(grammar))
for key in grammar:
    print(key)