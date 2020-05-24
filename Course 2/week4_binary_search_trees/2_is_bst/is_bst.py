#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

def in_order_traversal(i,tree,result):
  if i == -1:
    return
  in_order_traversal(tree[i][1],tree,result)
  result.append(tree[i][0])
  in_order_traversal(tree[i][2],tree,result)


def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  result = []
  in_order_traversal(0,tree,result)
  for i in range(1,len(result)):
    if result[i] < result[i-1]:
      return False

  return True


def main():
  nodes = int(sys.stdin.readline().strip())
  #nodes = int(input())
  tree = []
  for i in range(nodes):
    #tree.append(list(map(int, input().split())))
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if nodes == 0:
    print("CORRECT")
  else:
    
    if IsBinarySearchTree(tree):
      print("CORRECT")
    else:
      print("INCORRECT")

threading.Thread(target=main).start()
