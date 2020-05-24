#Uses python3

import sys
import queue



def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    dist = [10**19] * len(adj)
    prev = [-1] * len(adj)
    dist[0] = 0
    relaxed_nodes = []
    #|V| bellman iterations
    for i in range(len(adj)):
        #Bellman ford Algorithm
        for j in range(len(adj)):
            for k_index,k in enumerate(adj[j]):
                if dist[k] > dist[j] + cost[j][k_index]:
                    if (i == len(adj)-1):
                        relaxed_nodes.append(k)
                    dist[k] = dist[j] + cost[j][k_index]
                    prev[k] = j
    distance = dist
    #run bfs on relaxed nodes
    nodes_reached_from_negative_cycles = [-1] * len(adj)
    while(len(relaxed_nodes)):
        u = relaxed_nodes.pop(0)
        nodes_reached_from_negative_cycles[u] = 0
        for v in adj[u]:
            if nodes_reached_from_negative_cycles[v] == -1:
                nodes_reached_from_negative_cycles[v] = 0
                relaxed_nodes.append(v)

    reachable = [0 if x == 10**19 else x for x in dist]
    shortest = nodes_reached_from_negative_cycles

    reachable[s] = -1
    #shortest[s] = -1
    distance[s] = 0

    return distance, reachable, shortest 


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    distance, reachable, shortest = shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

