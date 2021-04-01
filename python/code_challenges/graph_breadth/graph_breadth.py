"""[Extends functionality of Graph class]
"""
from code_challenges.graph.graph import Graph
from code_challenges.stacks_and_queues.stacks_and_queues import Queue


class GraphTraverse(Graph):
    def breadth_first(vert):
        visit = list()
        breadth = list()
        level = Queue()

        while len(visit) < self.size():
            visit.append(vert)
            breadth.append(vert)
            for node in self.get_neighbors(vert):
                if not node[0] in visit:
                    level.enqueue(node[0])
                    continue
                else:
                    continue
                
            vert = self._adjaceny_list[level.dequeue()]

