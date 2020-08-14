# def traverse_maze(prev_room, current_room):
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