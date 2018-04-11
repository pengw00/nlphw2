from nltk.corpus import treebank
import nltk
t = treebank.parsed_sents('/Users/pengwu5501/nltk_data/corpora/ptb/wsj/00/wsj_0001.mrg')
print(t)
def filter(tree):
    child_nodes = [child.label() for child in tree if isinstance(child, nltk.Tree)]
    return (tree.label() == 'VP') and ('S' in child_nodes)
print(filter(t))
#print([subtree for tree in treebDownload the ptb packageank.parsed_sents() for subtree in tree.subtrees(filter)])