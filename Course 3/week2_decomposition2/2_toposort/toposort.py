#Uses python3

import sys


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

#we can also run dfs on the whole graph then sort the vertices according to the post times
#we can build post time as a min heap to get O(log(n)) insertion, and extracting vertices in O(1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    global clock
    clock = 1
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

