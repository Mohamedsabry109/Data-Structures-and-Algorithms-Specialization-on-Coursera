# python3
import queue
class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.residual_capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.

class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].residual_capacity -= flow
        self.edges[id ^ 1].residual_capacity += flow

def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from_, to):
    flow = 0
    while True:
        path_found, path, X = bfs(graph, from_, to)
        if not path_found:
            return flow
        for id in path:
            graph.add_flow(id, X)
        flow += X
    return flow

def bfs(graph, from_, to):

    #define X to be minimum flow in the augmented path, if found
    X = float('inf')
    # flag to indicate if we found an augmenting path
    path_found = False
    #get the number of vertices in the graph
    n = graph.size()
    #define array of distances to all nodes
    dist = [float('inf')]*n
    #list to save the augmenting path
    path = []
    #list of tuples to save parents of nodes upon searching 
    parent = [(None, None)]*n
    #creating queue for bfs
    q = queue.Queue()
    dist[from_] = 0
    q.put(from_)
    while not q.empty():
        current_node = q.get()
        #looping for all neighbours of current node
        for id in graph.get_ids(current_node):
            #get current edge
            current_edge = graph.get_edge(id)
            #only consider a node if it's not visited and the edge has postive capacity
            if float('inf') == dist[current_edge.v] and current_edge.residual_capacity > 0 :
                #update distance to this node
                dist[current_edge.v] = dist[current_node] + 1
                #save parent of this node, where we came to this node v and also the id of the edge by which we arrive 
                parent[current_edge.v] = (current_node, id)
                #save this node for further exploration
                q.put(current_edge.v)
                #if we arrived at the sink node
                if current_edge.v == to:
                    while True:
                        #save id of the edge 
                        path.insert(0, id)
                        #get the capacity of that current edge
                        currX = graph.get_edge(id).residual_capacity
                        #save min capacity while traversing the path
                        X = min(currX, X)
                        #if we arrived at the starting node, break
                        if current_node == from_:
                            break
                        # pick the parent node
                        current_node, id = parent[current_node]
                    path_found = True
                    return path_found, path, X
    return path_found, path, X

if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))