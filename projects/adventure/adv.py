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

################################

def go_travel(location):

#DFT for getting to the end of the road
    s = Stack()
    visited = set()
    my_map = {}

    s.push(location)

    while s.size() > 0:
        current_room = s.pop()

        if current_room not in visited:
            visited.add(current_room)
            map_it(my_map, current_room)
            print("current map", my_map)
        

        if "?" in my_map[current_room.id].values():
            for key, value in my_map[current_room.id].items():
                if value == "?":
                    this_room = player.current_room.id
                    print("this room", this_room)
                    previous_room = this_room
                    player.travel(key)
                    my_map[this_room][key] = player.current_room.id
                    s.push(player.current_room)
                    traversal_path.append(key)
                    break
            print("current map", my_map)
        else:
            backtrack = bfs(current_room.id, my_map, traversal_path)
            print("backtrack", backtrack)
            # for item in backtrack:
            #     traversal_path.append(item)
            #     print("traversal path from else statement", traversal_path)
            #What exactly is BFS supposed to be doing here?
            #find the nearest room with a "?"
            #go there


    
    return traversal_path

#BFS to find the next room with a "?"
def bfs(current_room, my_map, traversal_path):
    q = Queue()
    q.enqueue([current_room])
    visited = set()
    while q.size() > 0:
        path = q.dequeue()
        current = path[-1]
        print("PATH", path)
        if current not in visited:
            visited.add(current)
            if "?" in my_map[current].values():
                return path
            for neighbor in my_map[current].items():
                path_copy = path.copy()
                path_copy.append(neighbor[1])
                q.enqueue(path_copy)

#Update my own map
def map_it(maze_map, room):
    maze_map[room.id] = {
        'n': '?',
        'e': '?',
        's': '?',
        'w': '?'
    }
    if "s" not in room.get_exits():
        maze_map[room.id]['s'] = "X"
    if "n" not in room.get_exits():
        maze_map[room.id]['n'] = "X"
    if "e" not in room.get_exits():
        maze_map[room.id]['e'] = "X"
    if "w" not in room.get_exits():
        maze_map[room.id]['w'] = "X"
    
####################################
# TRAVERSAL TEST

go_travel(player.current_room)

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
