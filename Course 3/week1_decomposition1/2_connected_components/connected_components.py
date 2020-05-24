#Uses python3

import sys

def explore(v,visited,adj):
    visited[v] = 1
    for u in adj[v]:
        if not visited[u]:
            explore(u,visited,adj)

def reach(adj, x, y):
    #write your code here
    visited = [0]*len(adj)
    explore(x,visited,adj)
    if visited[y] == 1:
        return 1
    return 0

def number_of_components(adj):
    result = 0
    #write your code here
    visited = [0]*len(adj)
    for v in range(len(adj)):
        if visited[v] == 0:
            explore(v,visited,adj)
            result = result + 1
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
