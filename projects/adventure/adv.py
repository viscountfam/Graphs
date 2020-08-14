from room import Room
from player import Player
from world import World
from pathlib import Path
import random, sys
from ast import literal_eval

sys.setrecursionlimit(3000)
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"
initialPath = Path("projects/adventure")
import_path = Path("projects/graph")
map_file = initialPath / "maps/main_maze.txt"
# map_file = initialPath / "maps/test_line.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
s = []
traversal_path = []
backtrack = []
visited = {}
untraversed = {}
# last = []
def traverse_maze():
    def opposite(direction):
        if direction == "n":
            return "s"
        elif direction == "s":
            return "n"
        elif direction == "e":
            return "w"
        elif direction == "w":
            return "e"
    #check to see if you've visited all the rooms
    while len(visited) < len(room_graph):
        room = player.current_room.id 
        # check if you've visited the room
        if room not in visited:
            # mark that the room has been visited
            visited[room] = player.current_room.get_exits()
            # mark that you haven't explored the exits to the room
            untraversed[room] = player.current_room.get_exits()
        # explore the exits
        while len(untraversed[player.current_room.id]) < 1:
            back = backtrack.pop()
            traversal_path.append(back)
            player.travel(back)
        
        move = untraversed[player.current_room.id].pop()
        traversal_path.append(move)
        backtrack.append(opposite(move))
        player.travel(move)
traverse_maze()                    
print("travesal_path", traversal_path)
                

            


    
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


######
# UNCOMMENT TO WALK AROUND
######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
