import pytest
from code_challenges.graph.graph import Graph, Vertex, Edge

def test_vertex_instantiate():
    actual = Vertex('A').__str__()
    expected = ' instance of graph vertex value of: A '
    assert actual == expected

def test_edge_instantiate():
    actual = Edge('B').__str__()
    expected = 'instance of an edge between to vertices of a Graph instance'
    assert actual == expected


def test_graph_instantiate():
    actual = Graph().__str__()
    expected = 'instance of a graph as an adjacency list: {}'
    assert actual == expected


def test_graph_add_vertex_pass():
    grappy = Graph()
    verty = grappy.add_vertex('A')
    actual = verty.value
    expected = 'A'
    assert actual == expected


def test_graph_add_vertex_fail():
    grappy = Graph()
    with pytest.raises(TypeError) as excinfo:
        grappy.add_vertex()
    actual = str(excinfo.value)
    expected = "add_vertex() missing 1 required positional argument: 'value'"
    assert actual == expected


def test_graph_add_edge_pass():
    grappy = Graph()
    vert_1 = grappy.add_vertex('A')
    vert_2 = grappy.add_vertex('B')
    grappy.add_edge(vert_1, vert_2)
    assert True


def test_graph_get_nodes():
    grappy = Graph()
    vert_1 = grappy.add_vertex('A')
    vert_2 = grappy.add_vertex('B')
    actual = str(grappy.get_nodes())
    expected = f'dict_keys({[vert_1, vert_2]})'
    assert actual == expected


def test_graph_get_neighbors():
    grappy = Graph()
    vert_1 = grappy.add_vertex('A')
    vert_2 = grappy.add_vertex('B')
    grappy.add_edge(vert_1, vert_2)
    actual = grappy.get_neighbors(vert_1)
    expected = [(vert_2, 1)]
    assert actual == expected



