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
    node = nodes[0]
    node.marked = True
    steps += 1
    foundPath = hasPath(nodes, node.left, node.right, [node])
    if foundPath:
        return True
    return False

def hasPath(nodes, left, right, path):
    global steps
    last = True
    for node in nodes:
        steps += 1
        if node.marked:
            continue
        last = False

        if node.left == left:
            node.marked = True
            path.append(node)
            fpath = hasPath(nodes, node.right, right, path)
            if fpath:
                return path
            node.marked = False
            path.pop(-1)
        
        if node.right == left:
            node.marked = True
            path.append(node)
            fpath = hasPath(nodes, node.left, right, path)
            if fpath:
                return path
            node.marked = False
            path.pop(-1)
        
        if node.left == right:
            node.marked = True
            path.append(node)
            fpath = hasPath(nodes, left, node.right, path)
            if fpath:
                return path
            node.marked = False
            path.pop(-1)

        if node.right == right:
            node.marked = True
            path.append(node)
            fpath = hasPath(nodes, left, node.left, path)
            if fpath:
                return path
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
