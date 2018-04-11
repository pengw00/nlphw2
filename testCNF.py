from nltk.corpus import ptb
from nltk.tree import Tree
t = ptb.parsed_sents('/Users/pengwu5501/nltk_data/corpora/ptb/wsj/00/wsj_0001.mrg')
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
        return line
lis = []
def traversal(tree):
    lis.append(getCFG(tree))
    for subtree in tree:
        if isinstance(subtree, Tree):
            traversal(subtree)
    return lis
p = traversal(t[1])

"""convert to CNF"""
list_rule = []
def sub_r(sub_rule):
    sub = sub_rule.split('_')
    if len(sub) == 2:
        sub_rule += '->'
        for item in sub:
            sub_rule += ' '
            sub_rule += item
        list_rule.append(sub_rule)
    else:
        sub_rule += '->'
        for item in sub[1:-1]:
            sub[0] += '_'
            sub[0] += item
        sub_rule += sub[0]
        sub_rule += ' '
        sub_rule += sub[-1]
        sub_r(sub[0])
        list_rule.append(sub_rule)
    l = []
    for i in range(len(list_rule)):
        l.append(list_rule[len(list_rule)-i-1])
    return l

print('before sperate', p[0])
l = []
print(len(p))
for item in p:
    print(item)
    it = item.split('->')
    late = it[1].split()
    if len(late) > 2:
        it[0] += '->'
        it[0] += ' '
        it[0] += late[0]
        sub_rule = late[0]
        for item in late[1:-1]:
            it[0] += '_'
            sub_rule += '_'
            it[0] += item
            sub_rule += item
        it[0] += ' '
        it[0] += late[-1]
        l.append(it[0])
        sub_list = sub_r(sub_rule)
        for item in sub_list:
            l.append(item)
    else:
        l.append(item)

    #print('sub rule', sub_rule)
    #print('after operate',l)
for item in l:
    print(item)
print(len(l))







