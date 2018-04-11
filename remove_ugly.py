import os
def del_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".git"):
                os.remove(os.path.join(root,name))
                print("Delete File:" + os.path.join(root,name))
if  __name__ == "__main__":
    path = '/Users/pengwu5501/nltk_data/corpora/ptb/wsj'
    del_files(path)