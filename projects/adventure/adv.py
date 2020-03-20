from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
#map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# ################################


def go_travel():
    visited = {
      0: {'w': '?', 's': '?', 'n': '?', 'e': '?' }
    }
    s = Stack()
    prev_room = 0
    direction_traveled = ''

    s.push(0)
    while s.size() > 0:
        cur_room = s.pop()
        map_it(player.current_room.id, prev_room, visited, direction_traveled)
        if '?' in visited[cur_room].values():
            for key, value in visited[cur_room].items():
                if value == '?':
                    player.travel(key)
                    s.push(player.current_room.id)
                    direction_traveled = key
                    traversal_path.append(direction_traveled)
                    prev_room = cur_room
                    break
        else:
            if bfs(cur_room, visited) is None:
                return
            path_to_exit = bfs(cur_room, visited)
            new_traverse = []
            for index, room in enumerate(path_to_exit):
                if index < len(path_to_exit) - 1 and path_to_exit[index + 1] in visited[room].values():
                    for key, value in visited[room].items():
                        if value == path_to_exit[index + 1]:
                            new_traverse.append(key)
            # Move there
            for move in new_traverse:
                prev_room = player.current_room.id
                player.travel(move)
                direction_traveled = move
                traversal_path.append(move)
            if '?' in visited[player.current_room.id].values():
                s.push(player.current_room.id)



def map_it(cur_room, prev_room, visited, direction_traveled):
    if cur_room not in visited:
        exits_array = player.current_room.get_exits()
        new_room_exits = {}

        for direction in exits_array:
            new_room_exits[direction] = '?'
        if direction_traveled == 's':
            new_room_exits['n'] = prev_room
        if direction_traveled == 'n':
            new_room_exits['s'] = prev_room
        if direction_traveled == 'e':
            new_room_exits['w'] = prev_room
        if direction_traveled == 'w':
            new_room_exits['e'] = prev_room
        visited[cur_room] = new_room_exits
        visited[prev_room][direction_traveled] = cur_room

    else:
        if direction_traveled == 's':
            visited[cur_room]['n'] = prev_room
        if direction_traveled == 'n':
            visited[cur_room]['s'] = prev_room
        if direction_traveled == 'e':
            visited[cur_room]['w'] = prev_room
        if direction_traveled == 'w':
            visited[cur_room]['e'] = prev_room

def bfs(starting_vertex, visited):
    q = Queue()
    q.enqueue([starting_vertex])
    visited_rooms = set()

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if v not in visited_rooms:
            if '?' in visited[v].values():
                return path
            visited_rooms.add(v)
            for key, value in visited[v].items():
                path_copy = path.copy()
                path_copy.append(value)
                q.enqueue(path_copy)    

####################################
# TRAVERSAL TEST

go_travel()

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
