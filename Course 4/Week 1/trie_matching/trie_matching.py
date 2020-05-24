# python3
import sys

NA = -1

class Node:
    def __init__ (self):
        self.next = [NA] * 4

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

def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)
    i = 0
    while i < len(text):
        pattern = prefix_trie_matching(text,trie,i)
        if pattern != NA:
            result.append(i)
        i += 1
    return result

def prefix_trie_matching(text, trie, i):
    symbol = text[i]
    start_index = i
    i += 1
    v = trie[0]
    while True:
        if len(v.keys()) == 0:
            return text[start_index:i-1] 
        elif symbol in v.keys() :
            v = trie[v[symbol]]
            if i < len(text):
                symbol = text[i]
                i += 1
            else:
                 symbol = '$' 
        else:
             return NA 



text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
    patterns += [sys.stdin.readline ().strip ()]

# text = input()
# n = int (input())
# patterns = []
# for i in range (n):
#     patterns += [input()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
