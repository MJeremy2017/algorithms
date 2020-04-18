class Graph:
    def __init__(self):
        self.graph = dict()
        self.path_all = []
        self.n = 0
        
    def add_edge(self, u, v):
        if u not in self.graph.keys():
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
            
    def bfs(self, start, end):
        queue = [ [start, [start]] ]  # current node, current path
        while queue:
            curr_node, curr_path = queue.pop(0)
            if curr_node == end:
                print("find path", curr_path)
            
            if curr_node not in self.graph.keys():
                continue
            
            children = self.graph[curr_node]
            for child in children:
                # must copy so that each child path is independent
                path = curr_path.copy()
                if child not in curr_path:
                    path.append(child)
                    queue.append([child, path.copy()])