import random

class Node: 

    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.marked = False
    
    def __repr__(self):
        return f"({self.left},{self.right})"

steps = 0

def findPath(nodes):
    global steps
    steps = 0
    for node in nodes:
        node.marked = True
        steps += 1
        #print(str(node))
        foundPath = hasPath(nodes, node.left, [node])
        if foundPath:
            return True
        foundPath = hasPath(nodes, node.right, [node])
        if foundPath:
            return True
        node.marked = False
    return False

def hasPath(nodes, value, path):
    global steps
    last = True
    for node in nodes:
        steps += 1

        #print((' '*(len(path)*2)) + str(node))
        if node.marked:
            continue
        last = False
        if node.left == value:
            node.marked = True
            path.append(node)
            foundPath = hasPath(nodes, node.right, path)
            if foundPath:
                return foundPath
            node.marked = False
            path.pop(-1)
        if node.right == value:
            node.marked = True
            path.append(node)
            foundPath = hasPath(nodes, node.left, path)
            if foundPath:
                return foundPath
            node.marked = False
            path.pop(-1)
            
    if last:
        return path
    return []

steps_list = []
for i in range(100):
    nodes = [Node(1,1),Node(1,2),Node(2,3),Node(3,4),Node(4,5),Node(5,6),Node(6,7),Node(7,8),Node(8,9),Node(9,10)]
    random.shuffle(nodes)
    result = findPath(nodes)
    print('Case ', (i+1), ': ',result,' : ',steps)
    steps_list.append(steps)

steps_list.sort(reverse=False)
print('Best case: ', steps_list[0])
print('Worst case: ', steps_list[-1])
