"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    def __init__(self):
        self.vertices = {}
        self.seen = set()
    
    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
    
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
    
    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    
    def bft(self, starting_vertex_id):
        # create an empty queue and enqueue a starting  vertex
        q = Queue()
        q.enqueue(starting_vertex_id)

        # create a set to store the visited vertices
        visited = set()

        while q.size() > 0:

            v = q.dequeue()

            if v not in visited:
                visited.add(v)

                print(v)

                for next_vertex in self.get_neighbors(v):
                    q.enqueue(next_vertex)
    
    def dft(self, starting_vertex_id):
        s = Stack()
        s.push(starting_vertex_id)

        visited = set()

        while s.size() > 0:
            v = s.pop()

            if v not in visited:
                visited.add(v)
                print(v)


                for next_vertex in self.get_neighbors(v):
                    s.push(next_vertex)
    
    def bfs(self, starting_vertex_id, target_vertex_id):
        # create an empty queue and enqueue PATH To the Starting Vertex ID
        q = Queue()
        q.enqueue([starting_vertex_id])
        # create a set to store visited vertices
        visited = set()
        collected = []
        # while the queue is not empty
        while q.size() > 0:
            #dequeue the first PATH
            v = q.dequeue()
            collected.append(v[0])
            if v[0] == target_vertex_id:
                return collected
            
            if v[0] not in visited:
                visited.add(v[0])
            
                for next_vertex in self.get_neighbors(v[0]):
                    q.enqueue([next_vertex])
    def dfs(self, starting_vertex_id, target_vertex_id):
        s = Stack()
        s.push([starting_vertex_id])
        visited = set()
        collected = []
        while s.size() > 0:
            v = s.pop()
            collected.append(v[0])
            if v[0] == target_vertex_id:
                return collected

            if v[0] not in visited:
                visited.add(v[0])

                for next_vertex in self.get_neighbors(v[0]):
                    s.push([next_vertex])
    def dfs_recursive(self, starting_vertex_id, target_vertex_id):
        neighbors = self.get_neighbors(starting_vertex_id)
        collected = []
        if starting_vertex_id == target_vertex_id:
            return starting_vertex_id
        if starting_vertex_id not in self.seen:
            self.seen.add(starting_vertex_id)
        if neighbors:
            #call the dftrecursive on all the items in the set
            for val in neighbors:
                if val not in self.seen:
                    collected.append(self.dft_recursive(val))
        return collected
    def dft_recursive(self, starting_vertex_id):
        # use the call stack to function in a way that is similar to a stack
        # last in first out
        # base case
        # the element has no neighbors
        print(starting_vertex_id)
        # if the element has neighbors go to those neighbors
        neighbors = self.get_neighbors(starting_vertex_id)
        # set the current starting vertex to seen
        if starting_vertex_id not in self.seen:
            self.seen.add(starting_vertex_id)
        if neighbors:
            #call the dftrecursive on all the items in the set
            for val in neighbors:
                if val not in self.seen:
                    self.dft_recursive(val)
    def reset_seen(self):
        self.seen = set()
        

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
    graph.reset_seen()
    graph.dft(1)
    # graph.dft_recursive(1)
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
    # print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
