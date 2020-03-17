from util import Stack, Queue

def get_neighbors():
    pass
    

def earliest_ancestor(ancestors, starting_node):
    # queue = Queue()
    # visited = set()
    # queue.enqueue([starting_node])

    # while queue.size > 0:
    #     current_path = queue.dequeue()
    #     current_node = current_path[-1]

    #     if current_node not in visited:
    #         visited.add(current_node)

    #         edges = getNeighbors(current_node)

    #         for edge in edges:
    #             path_copy = list(current_path)
    #             path_copy.append(edge)
    #             queue.enqueue(path.copy)
    # return path_copy[-1]
    path = []
    distant_ancestor = None
    for item in ancestors:
        if item[0] == starting_node:
            distant_ancestor = item[1]
    
    for next_ancestor in ancestors:
        if next_ancestor[0] == distant_ancestor:
            distant_ancestor = next_ancestor[1]

    # for farther_back in ancestors:
    #     if farther_back[0] == distant_ancestor:
    #         distant_ancestor = farther_back[1]
    
    # for prev_gen in ancestors:
    #     if prev_gen[0] == distant_ancestor:
    #         distant_ancestor = prev_gen[1]
    
    return distant_ancestor

    #return ancestors

