import os
os.environ["PATH"] += os.pathsep + 'C:/Users/Ola/Downloads/release/bin'

from graphviz import Digraph
from PriorityQueue import PriorityQueue

class Graph:

    def __init__(self):
        self.size = 0
        self.nodes = []
        self.edges = []
        self.neighbours = {}
        self.visited = []
        self.visited_history = []

    def add_node(self, node):
        self.nodes.append(node)
        self.neighbours[node] = []
        self.size += 1

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.nodes:
            print('{} is not node of graph'.format(from_node))
            return
        if to_node not in self.nodes:
            print('{} is not node of graph'.format(to_node))
            return

        self.edges.append((from_node, to_node, weight))
        self.neighbours[from_node].append((to_node, weight))
        self.neighbours[to_node].append((from_node, weight))

    def __show_graph__(self):
        g = Digraph(format='png')
        g.attr('edge', arrowhead = 'none')
        for node in self.nodes:
            g.node(str(node))
        for edge in self.edges:
            if (edge[0], edge[1]) in self.visited_history:
                g.edge(str(edge[0]), str(edge[1]), label=str(edge[2]), color="red")
                continue
            if (edge[1], edge[0]) in self.visited_history:
                g.edge(str(edge[0]), str(edge[1]), label=str(edge[2]), color="red")
                continue

            g.edge(str(edge[0]), str(edge[1]), label=str(edge[2]), color="black")
        g.render("Prim_result\graf")
        g.view()

    def algorithm_Prim(self, start_position):
        priority_queue = PriorityQueue(self.size)
        self.visited = [False] * (self.size + 1)
        self.visited[start_position] = True
        self.insert_to_priority_queue_from(start_position, priority_queue)
        while self.visited.count(True) < len(self.nodes):
            target = priority_queue.get()
            self.visited_history.append((target[1], target[0]))
            position = target[0]
            self.visited[position] = True
            self.insert_to_priority_queue_from(position, priority_queue)
        self.__show_graph__()

    def insert_to_priority_queue_from(self, from_node, priority_queue):
        for neighbour in self.neighbours[from_node]:
            if self.visited[neighbour[0]] is False:
                priority_queue.insert(neighbour[0], (from_node, neighbour[1]))