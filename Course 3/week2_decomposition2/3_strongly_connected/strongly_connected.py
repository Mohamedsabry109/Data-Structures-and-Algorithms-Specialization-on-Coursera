#Uses python3

import sys

sys.setrecursionlimit(200000)

def explore(v,visited,adj):
    visited[v] = 1
    for u in adj[v]:
        if not visited[u]:
            explore(u,visited,adj)

def dfs(adj, used, order, x):
    used[x] = 1 
    for i in adj[x]:
        if not used[i]:
            dfs(adj,used,order,i)
    order.append(x)
    return


def toposort(adj):
    used = [0] * len(adj)
    order = []
    for x in range(len(adj)):
        if not used[x]:
            dfs(adj,used,order,x)
    return order[::-1]

def number_of_strongly_connected_components(adj,adj_r):
    result = 0
    order = toposort(adj_r)
    visited = [0] * len(adj)
    for v in order:
        if not visited[v]:
            explore(v,visited,adj)
            result += 1

    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_r = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_r[b-1].append(a - 1)
    print(number_of_strongly_connected_components(adj,adj_r))
