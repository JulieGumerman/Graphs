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

    for pair in ancestors:
        parent = pair[0]
        child = pair [1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(parent, child)
    
    q = Queue()
    q.enqueue([starting_node])

    earliest_ancestor = -1
    longest_path = []
    longest_path_length = 1
    visited = set()

    while q.size() > 0:
        path = q.dequeue()
        current_vertex = path[-1]

        if len(path) == longest_path_length and current_vertex < earliest_ancestor:
            longest_path_length = len(path)
            earliest_ancestor = current_vertex
        if len(path) > longest_path_length:
            longest_path_length = len(path)
            print(longest_path)
            earliest_ancestor = current_vertex


        neighbors = graph.vertices[current_vertex]

        for ancestor in neighbors:
            path_copy = list(path)
            path_copy.append(ancestor)
            q.enqueue(path_copy)
        
    print("EARLIEST ANCESTOR!!!", earliest_ancestor)
    return earliest_ancestor

