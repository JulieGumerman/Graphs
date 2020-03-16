"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
       self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        visited = set()
        #starting node in line
        q.enqueue(starting_vertex)

        while q.size() > 0:
            #get next node out of line
            v = q.dequeue()

            if v not in visited:
                print(v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)



    def dft(self, starting_vertex):
        s = Stack()
        visited = set()

        s.push(starting_vertex)
        while s.size() > 0:
            current_node = s.pop()

            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                edges = self.get_neighbors(current_node)
                for e in edges:
                    s.push(e)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #initialize set; you HAVE to pass visited back down through recursion or it'll loop forever, and you'll be sad
        if visited == None:
            visited = set()
        
        #print starting vertex; if you don't put this, everything else in your code will be right, but your test will fail because nothing got printed
        print(starting_vertex)

        #add your starting_vertex to visited or you'll be off on an infinite loop
        visited.add(starting_vertex)

        #now, look at your neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            #if the neighbor hasn't been visited
            if neighbor not in visited:
                #time for recursion: lines 68 and 71 will take care of the immediate neighbors, and you'll keep going down the line
                self.dft_recursive(neighbor, visited)


        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """


        # Create a queue
        q = Queue()
        # Enqueue A PATH TO the starting vertex
        q.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()    
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            current = path[-1]
            # Check if it's been visited
            if current not in visited:
            # If it hasn't been visited...
                # Mark it as visited
                visited.add(current) 
                # CHECK IF IT'S THE TARGET
                if current == destination_vertex:
                    return path                   
                    # IF SO, RETURN THE PATH

                for neighbor in self.get_neighbors(current):
               # Enqueue A PATH TO all it's neighbors
                    # MAKE A COPY OF THE PATH
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # ENQUEUE THE COPY
                    q.enqueue(path_copy)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        path = []

        s.push(starting_vertex)

        while s.size() > 0:
            current_node = s.pop()
            path.append(current_node)
            if current_node == destination_vertex:
                return path

            if current_node not in visited:
                visited.add(current_node)
                edges = self.get_neighbors(current_node)
                for e in edges:
                    s.push(e)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()


        visited.add(starting_vertex)
        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                do_it_again = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if do_it_again is not None:
                    return do_it_again


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
