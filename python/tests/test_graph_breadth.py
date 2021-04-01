import pytest
from code_challenges.graph_breadth.graph_breadth import GraphTraverse
from code_challenges.graph.graph import Graph


@pytest.fixture 
def graph_template_directional():
    graph = Graph()
    art = graph.add_vertex('Art')
    space = graph.add_vertex('Space')
    graph.add_edge(art, space)
    
    decorate = graph.add_vertex('Decorate')
    time = graph.add_vertex('Time')
    music = graph.add_vertex('Music')
    graph.add_vertex(space, decorate)
    graph.add_vertex(space, time)
    graph.add_vertex(space, music)

    graph.add_vertex(decorate, time)
    graph.add_vertex(time, music)


def test_breadth_traversal_directional_graph(graph_template_directional):
    graph = graph_template_directional
    actual = graph.GraphTraverse.breadth_first(graph._adjaceny_list.keys()[0])
    expected = ['Art', 'Space', 'Decorate', 'Time', 'Music']
    assert actual == expected

    