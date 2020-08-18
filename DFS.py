class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()
        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbor(self, vertex_letter):
        neighbor_set = set(self.neighbors)
        if vertex_letter not in neighbor_set:
            self.neighbors.append(vertex_letter)
            self.neighbors.sort()


class Graph:
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices: #check if Object Vertex and in dictionary
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v): #take 2 char values at either end of the edge
        if u in self.vertices and v in self.vertices: #check if they are existing vertices, if not return False
            for key, value in self.vertices.items(): #if exists iterate through the vertices
                if key == u: #when find u add v as a neighbor to it
                    value.add_neighbor(v)
                if key == v: #find v add u as neighbor to it
                    value.add_neighbor(u) #basically setting the neighbors in the vertex class
            return True
        else:
            return False

    def print_graph(self):#print graph to see what it looks like
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + ' ' + str(self.vertices[key].discovery))

    def _dfs(self, vertex):
        global time
        vertex.color = 'red'
        vertex.discovery = time
        time += 1
        for v in vertex.neighbors:
            if self.vertices[v].color == 'black': #if color is black it hasn't been visited yet
                self._dfs(self.vertices[v]) #do call on neighboring vertex
        vertex.color = 'blue' #set color to blue
        vertex.finish = time #set finish time
        time += 1

    def dfs(self, vertex): #pass in the vertex you're starting at
        global time
        time = 1 #set time to 1 everytime we call dfs()
        self._dfs(vertex)

g = Graph()

a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:]) #adds first letter and sends 2nd letter to the add_edge()

g.dfs(a) #call dfs on Vertex a
g.print_graph()