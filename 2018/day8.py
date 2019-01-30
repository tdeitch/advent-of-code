class Node:
    def __init__(self, children, metadata, length):
        self.children = children
        self.metadata = metadata
        self.length = length

def read_input():
    tree = ""
    with open('day8.txt') as f:
        tree = [int(x) for x in "".join(f.readlines()).strip().split(" ")]
#    tree = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
    return tree

def get_root(tree_str):
    num_children = tree_str[0]
    num_metadata = tree_str[1]
    length = 2
    children = []
    for i in range(num_children):
        child = get_root(tree_str[length:])
        children.append(child)
        length += child.length
    metadata = tree_str[length:length + num_metadata]
    length += num_metadata
    return Node(children, metadata, length)

def get_value(node):
    if len(node.children) == 0:
        return sum(node.metadata)
    value = 0
    for md in node.metadata:
        if 0 < md <= len(node.children):
            value += get_value(node.children[md - 1])
    return value

tree_str = read_input()
root = get_root(tree_str)

print(get_value(root))
