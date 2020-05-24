#Uses python3

import sys


def negative_cycle(adj, cost):
    # initiate all distances and previouses to be -1.
    dist = [-1] * len(adj)
    prev = [-1] * len(adj)
    dist[0] = 0
    #|V| bellman iterations
    for i in range(len(adj)):
        #Bellman ford Algorithm
        for j in range(len(adj)):
            for k_index,k in enumerate(adj[j]):
                if dist[k] > dist[j] + cost[j][k_index]:
                    dist[k] = dist[j] + cost[j][k_index]
                    prev[k] = j
        #save values of distances at |v|-1 th itertaions to check at |V|th iteration
        if i == len(adj)-2:
            dist_V_minus_1 = list(dist)
        if i == len(adj)-1:
            dist_V = list(dist)
    #if there are not any changes, then there are not negative cycles
    if dist_V_minus_1 == dist_V:
        return 0
    else:
        return 1


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
    print(negative_cycle(adj, cost))
