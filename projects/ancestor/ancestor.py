class Graph:
    def __init__(self):
        self.vertices = {}
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print(starting_vertex)

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                self.dft_recursive(v, visited) 

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = [starting_vertex]
        if path[-1] == destination_vertex:
            return path
        neighbors = self.get_neighbors(path[-1])
        if path[-1] not in visited:
            visited.add(path[-1])
            for neighbor in neighbors:
                new_path = list(path) + [neighbor]
                result = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if result:
                    return result

        return None
        
    # def earliest_ancestor(ancestors, starting_node):
    # # create an adjacency list
    # ancestral = {}
    # for ancestor in ancestors:
    #     if ancestral.get(ancestor[1]):
    #         ancestral[ancestor[1]].update({ancestor[0]})
    #     elif ancestral.get(ancestor[1]) is None:
    #         ancestral[ancestor[1]] = {ancestor[0]}       
    # print(ancestral)
    # current_ancestor = ancestral[starting_node]
    # # find the deepest node in the list that is connected to the starting node
    
    # return next_ancestor


def earliest_ancestor(ancestors, starting_node):
    # create an adjacency list
    # ancestral = {}
    # for ancestor in ancestors:
    #     if ancestral.get(ancestor[1]):
    #         ancestral[ancestor[1]].update({ancestor[0]})
    #     elif ancestral.get(ancestor[1]) is None:
    #         ancestral[ancestor[1]] = {ancestor[0]}       
    # print(ancestral)
    # familytree = Graph(ancestral)

    # return familytree.df_recursive(st)
    # graph = Graph()
    # for pair in ancestors:
    #     graph.add_vertex(pair[0])
    #     graph.add_vertex(pair[1])
    #     graph.add_edge(pair[1], pair[0])
    
    # s = []
    # s.append([starting_node])
    # max_path_length = 1
    # earliest_ancestor = -1
    # while len(s) > 0:
    #     path = s.pop(0)
    #     v = path[-1]
    #     if(len(path) >+ max_path_length and v < earliest_ancestor) or (len(path) > max_path_length):
    #         earliest_ancestor = v
    #         max_path_length = len(path)
    #         for neighbor in graph.get_neighbors(v):
    #             path_copy = list(path)
    #             path_copy.append(neighbor)
    #             s.append(path_copy)

    # return earliest_ancestor
    

    # while next_ancestor is not None:
    #     current_ancestor = next_ancestor
    #     next_ancestor = ancestral.get(next_ancestor)
    # return current_ancestor

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 3))#10
# an approach using dictionaries won't work here because we don't have a way to use their levels and return the deeper node
# we want to find the earliest ancestor of any given node
# the best way to do this would be to invert the graph
# doing this makes the parents now the children of the nodes they used to be parents
# this allows us to use dft to find the ancestors
# we want to return the last element that we find not the path
# when we take in values from the ancestors parameter went to switch the 1th element with 0th element
# then run a dft and only return the last element

## How to solve graph problems

# 1. Translate the problem in to graph terminology
#     - Find what parts of the problem can be modeled as nodes / vertices
#     - Find the part of the problem that can be modeled as Edges or Connections
# 2. Build Your Graph
#     - use data from the problem to create a graph based on the way you have chosen to model it's component parts
# 3. Traverse your Graph
#     - think about how you have decided to model your problems solution. look for key words or ideas that could point you toward a specific traversal algorithm. 
#     - look for keywords such as `shortest`, `fastest` or anything that could give you a clue as to what might be a good fit for the problem at hand