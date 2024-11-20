def solution(n, wires):
    answer = -1
    for wire in wires:
        new_tree = wires[:]
        new_tree.remove(wire)
        separated_graph = undi_graph(new_tree)
        separated_graph_size = separated_graph.dfs()
        new_answer = abs(2 * separated_graph_size - n)
        if answer == -1:
            answer = new_answer
        else:
            if answer > new_answer:
                answer = new_answer
    return answer

class undi_graph():
    def __init__(self, graph):
        self.V = sorted(list(set(sum(graph, []))))
        self.neighbor = {}
        self.graph_size = 0
        for v in self.V:
            self.neighbor[v] = []
        for (v, w) in graph:
            self.neighbor[v].append(w)
            self.neighbor[w].append(v)
    def dfs(self):
        if self.V:
            visited = {}
            for v in self.V:
                visited[v] = False
            self.__dfsrun(visited, self.V[0])
            return self.graph_size
    def __dfsrun(self, visited, v):
        if not visited[v]:
            visited[v] = True
            self.graph_size += 1
            for w in self.neighbor[v]:
                self.__dfsrun(visited, w)