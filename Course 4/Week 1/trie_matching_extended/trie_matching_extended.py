# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4
		self.patternEnd = False



def build_trie(patterns):
    tree = dict()
    node_counter = 0
    tree[0] = {}
    #each node is a dict
    for pattern in patterns:
        current_node = tree[0]
        end_flag = 0
        for i in range(len(pattern)):
            if pattern[i] in current_node.keys():
                # if i == len(pattern)-1:
                #     current_node[pattern[i]][1] = 1
                current_node = tree[current_node[pattern[i]][0]]
            else:
                #adding new node to the trie
                #add new node to new node with label the new symbol
                #current node is the new node  
                current_node[pattern[i]] = [node_counter + 1, end_flag]
                node_counter += 1
                tree[node_counter] = {}
                current_node = tree[node_counter]
        current_node['$'] = {}
    return tree

def solve (text, n, patterns):
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
        if not v or '$' in v:
            return text[start_index:i-1] 

        if symbol in v.keys():
            v = trie[v[symbol][0]]

            if i < len(text) :
                symbol = text[i]
                i += 1
                
            elif '$' in v:
                 return text[start_index:i-1]

            else:
                symbol = '$'

        else:
        	return text[start_index:i-1] if '$' in v else -1

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
