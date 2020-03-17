from util import Stack, Queue


def earliest_ancestor(ancestors, starting_node):
        s = Stack()
        visited = set()

        s.push(starting_node)
        while s.size() > 0:
            current_node = s.pop()

            if current_node not in visited:
                visited.add(current_node)
                print(current_node)
                edges = self.get_neighbors(current_node)
                for e in edges:
                    s.push(e)