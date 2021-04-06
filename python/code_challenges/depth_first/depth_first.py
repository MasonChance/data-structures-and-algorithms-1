from code_challenges.graph.graph import Graph
from code_challenges.stacks_and_queues.stacks_and_queues import Stack

class DepthTraverse(Graph):

    
    def depth_first():
        visit = list()
        stack = Stack()
        _next = 0

        while len(visit) < self._adjacency_list.size():
            for vert in self._adjaceny_list:
                if len(visit) == 0:
                    visit.append(self._adjacency_list[vert])
                    stack.push(self._adjacency_list[vert])
                if vert[_next][0] not in visit:
                    visit.append(vert[_next][0])
                    stack.push(vert[_next][0])
                    _next += 1
                    continue
                else:
                    continue

        return self.stack_trace(stack)


    @staticmethod
    def stack_trace(stack):
        if not stack.top:
            raise TypeError("TypeError: check that you are passing a <class 'stack'> and that it is not empty")
        try:
            trace = list()
            while stack.top:
                trace.append(stack.pop())
            return trace[::-1] 
        except AttributeError:
            raise AttributeError(f'Input: {stack} must be of type: <class Stack> with at least one element')