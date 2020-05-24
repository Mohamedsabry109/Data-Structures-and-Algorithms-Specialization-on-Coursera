#Uses python3

import sys
import queue


def distance(adj, cost, start,end):
    # initialise all distances to be infinity first
    dist=[float('inf')]*len(adj)
    dist[start] = 0
    pq = queue.PriorityQueue()
    pq.put(start)
    while not pq.empty():
        u = pq.get()
        for v in adj[u]:
            v_index = adj[u].index(v)
            if dist[v] > dist[u] + cost[u][v_index]:
                dist[v] = dist[u] + cost[u][v_index]
                pq.put(v)
    if dist[t] == float('inf'):
        return -1
    return dist[t]

if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
