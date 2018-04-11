import copy
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
a1 = Node(6)
b1 = Node(5)
b2 = Node(2)
c1 = Node(4)
c2 = Node(1)
c3 = Node(1)
d1 = Node(3)
d2 = Node(0)

a1.left = b1
a1.right = b2
b1.left = c1
b1.right = c2
b2.left = c3
c1.left = d1
c1.right = d2

s = []

def gos(node, path = []):
    if node:
        path.append(node.value)
        if node.left:
            path1 = copy.copy(path)
            gos(node.left, path1)
            if node.right:
                path2 = copy.copy(path)
                gos(node.right, path2)
        else:
            s.append(copy.copy(path))
gos(a1)
for i in s:
    print(i)
