#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree(j, mn, mx):
  #check wether it's a node in the tree by check the index
  if not j in tree: return True
  #check for boundaries in min and max, 
  if tree[j][0] < mn or tree[j][0] > mx: return False
  #check if the chiiilderns are binary trees also, condition on left trees are that the left node is ledd than the parent node
  #condition on the right child is that it can be at most the parent node
  return IsBinarySearchTree(tree[j][1], mn, tree[j][0] - 1)  and IsBinarySearchTree(tree[j][2], tree[j][0], mx)


def main():
  nodes = int(sys.stdin.readline().strip())
  global tree
  tree, int_max, int_min = {}, 2147483647, -2147483648
  for i in range(nodes):
    tree[i] = (list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(0, int_min, int_max):
    print("CORRECT")
  else:
    print("INCORRECT")
threading.Thread(target = main).start()