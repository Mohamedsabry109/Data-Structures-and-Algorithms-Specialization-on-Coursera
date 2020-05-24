#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    dist = [len(adj)+1]*len(adj)
    dist[s] = 0
    queue = []
    queue.append(s)
    while len(queue):
        u = queue.pop(0)
        for v in adj[u]:
            if dist[v] == len(adj) + 1:
                queue.append(v)
                dist[v] = dist[u] + 1

    if dist[t] != len(adj) + 1:
        return dist[t]
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
