#Uses python3
import sys
import math



class DisjSet: 
    def __init__(self, n): 
        self.rank = [1] * n 
        self.parent = [i for i in range(n)] 
  
  
    def find(self, x): 
          
        if (self.parent[x] != x): 
            self.parent[x] = self.find(self.parent[x]) 

        return self.parent[x] 
  

    def Union(self, x, y): 
          
        xset = self.find(x) 
        yset = self.find(y) 
  
        if xset == yset: 
            return

        if self.rank[xset] < self.rank[yset]: 
            self.parent[xset] = yset 
  
        elif self.rank[xset] > self.rank[yset]: 
            self.parent[yset] = xset 

        else: 
            self.parent[yset] = xset 
            self.rank[xset] = self.rank[xset] + 1


def distance(x,y,u,v):
    return math.sqrt((x[u]-x[v])**2 +  (y[u]-y[v])**2)

def minimum_distance(x, y):
    result = 0.
    number_vertices = len(x)
    # calculate distances of all edges in the graph
    edges = []
    for i in range(number_vertices):
        for j in range(i,number_vertices):
            if i != j:
                edges.append([i,j,distance(x,y,i,j)])

    edges = sorted(edges , key=lambda x: x[2])
    joint_nodes = [i for i in range(len(x))]
    dis_set = DisjSet(len(x))
    min_distance = 0

    for edge in edges:
        if (dis_set.find(edge[0]) != dis_set.find(edge[1])):
            min_distance += edge[2]
            dis_set.Union(edge[0],edge[1])

    return min_distance


if __name__ == '__main__':
    input = sys.stdin.read()
    #input = input()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
