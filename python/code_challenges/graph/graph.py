"""[Module supports implementation of Graph Data-Structure as 
a class]
"""
from linked_list.linked_list import LinkedList


class Vertex:
    """[Node class used in Graph data structure implementation has
    properties ]
    """

    def __init__(self, value):
        self.value = value
        

    def __str__(self):
        return f' instance of graph vertex value of: {self.value} '


    def __repr__(self):
        return self.value



class Edge:
    """[Instance of an edge containing an end vertex  and a weight.
    weight defaults to value of 1]
    """
    def __init__(self,end, weight=1):
        self.end = end
        self.weight = weight


    def __str__(self):
        return f'instance of an edge between to vertices of a Graph instance'



class Graph:
    

    def __init__(self):
        self._adjaceny_list = dict()

    
    def __str__(self):
        return f'instance of a graph as an adjacency list: {self._adjaceny_list}'


    def __repr__(self):
        return self._adjaceny_list


    def add_vertex(self, value):
        vtx = Vertex(value)
        self._adjaceny_list[vtx] = []
        return vtx


    def add_edge(self, start, end, weight=1):
        if start not in self._adjaceny_list:
            raise KeyError('Start vertex not in Graph')
        if end not in self._adjaceny_list:
            raise KeyError('End vertex not in Graph')

        edge = Edge(end, weight)
        adjacency = self._adjaceny_list[start]
        adjacency.append(edge)



    def get_nodes(self):
        vertices = self._adjaceny_list.keys()
        return vertices


    def get_neighbors(self, vertex):
        edges = []
        for pair in self._adjaceny_list[vertex]:
            edges.append((pair.end, pair.weight))
        return edges


    def size(self):
        return len(self._adjaceny_list)



