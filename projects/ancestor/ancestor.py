from util import Stack, Queue

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for node in ancestors:
        graph.add_vertex(node[0])
        graph.add_vertex(node[1])
        graph.add_edge(node[1], node[0])
    
    q = Queue()
    q.enqueue([starting_node])

    earliest_ancestor = None
    longest_path = []
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        current_vertex = path[-1]

        if len(path) > len(longest_path):
            earliest_ancestor = current_vertex
            longest_path = path
        if current_vertex not in visited:
            for neighbor in graph.get_neighbors(current_vertex):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
        

    return earliest_ancestor
