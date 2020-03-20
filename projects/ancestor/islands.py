from util import Stack, Queue

islands = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

def island_counter(matrix):
    visited = []
    for i in range(len(matrix)):
        visited.append([[False] * len(matrix[0])])
    #for all nodes
    island_count = 0
    for col in range(len(matrix[0])):
        for row in range(len(matrix)): 
        #if node is not visited
            if not visited[row][col]:
            #if we hit a 1 that has not been visited
                if matrix[row][col] == 1:
                #mark visited
                    visited = dft(row, col, matrix, visited)
                #increment visited count
                #traverse connected nodes
                    island_count += 1
    return island_count

def dft(start_row, start_col, matrix, visited):
    s = Stack()
    s.push((start_row, start_col))

    while s.size() > 0:
        v = s.pop()
        row = v[0]
        col = v[1]
        if not visited[row][col]:
            print(v)
            visited[row][col] = True
            for neighbor in self.get_neighbors(row, col, matrix):
                s.push(neighbor)
    return visited

def get_neighbors(row, col, matrix):
    neighbors = []
    if row > 0 and matrix[row-1][col]:
        neighbors.append((row-1, col))
    #check north
    if row < len(matrix) - 1 and matrix[row-1][col]:
        neighbors.append((row+1, col))
    if col < len(matrix[0] -1) and matrix[row][col+1] == 1:
        neighbors.append((row, col+1))
    if col > 0 and matrix[row][col-1]:
        neighbors.append((row, col+1))
    #check south
    #check east
    #check west

    return neighbors