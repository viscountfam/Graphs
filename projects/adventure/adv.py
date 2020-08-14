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
# def traverse_maze(prev_room, current_room):
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
#     if current_room not in visited:
#         potential_paths = player.current_room.get_exits()
#         visited[current_room] = {}
#         for direction in potential_paths:
#             visited[current_room][direction] = "?"
    
#     if len(traversal_path) > 0:
#         opposite_direction = traversal_path[-1]
#     else:
#         opposite_direction = None
    
#     # visited[current_room][opposite(opposite_direction)] = prev_room
#     # visited[prev_room][opposite_direction] = current_room

#     if opposite_direction == 'n':
#         visited[current_room][opposite('n')] = prev_room
#         visited[prev_room]['n'] = current_room
#     elif opposite_direction == 'e':
#         visited[current_room][opposite('e')] = prev_room
#         visited[prev_room]['e'] = current_room
#     elif opposite_direction == 'w':
#         visited[current_room][opposite('w')] = prev_room
#         visited[prev_room]['w'] = current_room
#     elif opposite_direction == 's':
#         visited[current_room][opposite('s')] = prev_room
#         visited[prev_room]['s'] = current_room
    
#     # check possible exits, add them to the stack if the room they exit to is unknown
#     for direction in visited[current_room]:
#         if visited[current_room][direction] == "?":
#             player.travel(direction)
#             next_room = player.current_room.id

#             if (current_room, next_room, direction) not in s:
#                 s.append((current_room, next_room, direction))
            
#             player.travel(opposite(direction))
    
#     # print(f"stack: {s}")
#     if len(s) > 0:
#         next_room_info = s.pop()
#         # print("next_room_info", next_room_info)
#         # print("next_room_info type", type(next_room_info))
#         last.append(next_room_info)
#         current_room_info = next_room_info[0]
#         direction_info = next_room_info[2]
#         next_room_info = next_room_info[1]

#         if direction_info in visited[current_room] and visited[current_room][direction_info] == "?":
#             traversal_path.append(direction_info)
#             player.travel(direction_info)
#             traverse_maze(current_room_info, next_room_info)
        
#         else:
#             # this is where we'll run our bfs
#             def bfs(opposite_direction):
#                 selected_direction = opposite(opposite_direction)
                
#                 q = Queue()
#                 q.enqueue([selected_direction])

#                 while q.size() > 0 and len(visited) < len(room_graph):
#                     path = q.dequeue()
#                     current_room = player.current_room.id 
#                     for direction in path:
#                         player.travel(direction)

#                     player.travel(opposite(path[-1]))
#                     current_room = player.current_room.id 
#                     player.travel(path[-1])

#                     if player.current_room.id not in visited:
#                         for direction in path:
#                             traversal_path.append(direction)
#                         traverse_maze(current_room, player.current_room.id)
#                     else:
#                         for direction in visited[player.current_room.id]:
#                             if direction == "?":
#                                 return path
#                         for direction in visited[player.current_room.id]:
#                             opposite_direction = opposite(path[-1])
#                             if opposite_direction != direction:
#                                 new_path = list(path)
#                                 new_path.append(direction)
#                                 q.enqueue(new_path)

#                         reverse_path = list(path)
#                         reverse_path = reverse_path[:: -1]
#                         for direction in reverse_path:
#                             player.travel(opposite(direction))
                
#                 bfs(opposite_direction)

#             bfs(opposite_direction)
# traverse_maze(None, player.current_room.id)   
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
