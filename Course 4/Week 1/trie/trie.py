#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

def build_trie(patterns):
    tree = dict()
    node_counter = 0
    tree[0] = {}
    #each node is a dict
    for pattern in patterns:
        current_node = tree[0]
        for i in pattern:
            if i in current_node.keys():
                current_node = tree[current_node[i]]
            else:
                #adding new node to the trie
                #add new node to new node with label the new symbol
                #current node is the new node
                current_node[i] = node_counter + 1
                node_counter += 1
                tree[node_counter] = {}
                current_node = tree[node_counter]

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    #patterns = input().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
