import os
path = '/Users/pengwu5501/nltk_data/corpora/ptb/wsj'
files = os.listdir(path)
for name in files:
    if name.endswith('.git'):
        os.remove(os.path.join(path, name))
        print("Delete File:" + os.path.join(path, name))

print(files)
#if files.endswith('.idea')