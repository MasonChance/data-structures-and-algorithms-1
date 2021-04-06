import pytest
from code_challenges.stacks_and_queues.stacks_and_queues import Stack
from code_challenges.graph.graph import Graph
from code_challenges.depth_first.depth_first import DepthTraverse



@pytest.fixture  
def graph():
    graph = Graph()
    a = graph.add_vertex('A')
    b = graph.add_vertex('B')
    c = graph.add_vertex('C')
    d = graph.add_vertex('D')
    e = graph.add_vertex('E')
    f = graph.add_vertex('F')
    g = graph.add_vertex('G')
    h = graph.add_vertex('H')
    graph.add_edge(a, b)
    graph.add_edge(a, d) 
    graph.add_edge(b, c)
    graph.add_edge(b, d) 
    graph.add_edge(c, g)
    graph.add_edge(c, b) 
    graph.add_edge(d, a)
    graph.add_edge(d, b)
    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f) 
    graph.add_edge(f, d)
    graph.add_edge(f, h) 
    graph.add_edge(g, c)
    graph.add_edge(h, d)
    graph.add_edge(h, f)
    return graph


@pytest.fixture  
def stack():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    stack.push('G')
    stack.push('D')
    stack.push('E')
    stack.push('H')
    stack.push('F')
    return stack


def test_stack_trace(stack):
    actual = DepthTraverse.stack_trace(stack)
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert actual == expected


def test_stack_trace_empty_stack():
    empty = Stack()
    with pytest.raises(TypeError) as excinfo:
        DepthTraverse.stack_trace(empty)
    actual = str(excinfo.value)
    expected = "TypeError: check that you are passing a <class 'stack'> and that it is not empty"
    assert actual == expected

def test_stack_trace_invalid_input():
    empty = 'monkey wrench'
    with pytest.raises(AttributeError) as excinfo:
        DepthTraverse.stack_trace(empty)
    actual = str(excinfo.value)
    expected = "'str' object has no attribute 'top'"
    assert actual == expected


def test_depth_first_pass(graph):
    actual = graph.depth_first()
    expected = ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']
    assert actual == expected

