import os
os.environ["PATH"] += os.pathsep + 'C:/Users/Ola/Downloads/release/bin'

from decimal import Decimal
from graphviz import Digraph

q = set()
dist = {}
prev = {}

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, length):
        self.to_node = to_node
        self.length = length


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, length):
        edge = Edge(to_node, length)
        if from_node.label in self.edges:
            from_node.edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node.edges = self.edges[from_node.label]
        from_node.edges[to_node.label] = edge

def min_dist(q, dist):
    min_node = None
    for node in q:
        if min_node == None:
            min_node = node
        elif dist[node] < dist[min_node]:
            min_node = node
    return min_node

INFINITY = Decimal('Infinity')

def dijkstra(graph, source):
    dijkstra_initialize(source)
    while q:
        u = min_dist(q, dist)
        q.remove(u)
        if u.label in graph.edges:
            for _, v in graph.edges[u.label].items():
                alt = dist[u] + v.length
                if alt < dist[v.to_node]:
                    dist[v.to_node] = alt
                    prev[v.to_node] = u
    return dist, prev

def dijkstra_initialize(source):
    global q,dist,prev
    for v in graph.nodes:
        dist[v] = INFINITY
        prev[v] = INFINITY
        q.add(v)
    dist[source] = 0

def to_array(prev, from_node):
    previous_node = prev[from_node]
    route = [from_node.label]
    while previous_node != INFINITY:
        route.append(previous_node.label)
        temp = previous_node
        previous_node = prev[temp]
    route.reverse()
    return route

graph = Graph()
node_a = Node("A")
graph.add_node(node_a)
node_b = Node("B")
graph.add_node(node_b)
node_c = Node("C")
graph.add_node(node_c)
node_d = Node("D")
graph.add_node(node_d)
node_e = Node("E")
graph.add_node(node_e)
node_f = Node("F")
graph.add_node(node_f)
node_g = Node("G")
graph.add_node(node_g)

graph.add_edge(node_a, node_b, 4)
graph.add_edge(node_a, node_c, 3)
graph.add_edge(node_a, node_e, 7)
graph.add_edge(node_b, node_d, 5)
graph.add_edge(node_b, node_f, 12)
graph.add_edge(node_c, node_d, 11)
graph.add_edge(node_c, node_e, 8)
graph.add_edge(node_d, node_e, 2)
graph.add_edge(node_d, node_g, 10)
graph.add_edge(node_e, node_g, 5)
graph.add_edge(node_f, node_g, 3)
graph.add_edge(node_g, node_c, 1)

dist, prev = dijkstra(graph, node_a)

dot = Digraph(comment='The Round Table')
nodes = [node_a.label, node_b.label, node_c.label, node_d.label, node_e.label, node_f.label, node_g.label]

def isChosen(x, labels):
    count = int(len(labels)) - 1
    for i in range(0, count):
        if labels[i] == x:
            return True
    return False

def createGraphNode(tabPrev, endNode, nodes):
    for n in nodes:
        arrayTest = to_array(tabPrev, endNode)
        arrayTest.append(endNode.label)
        if isChosen(n, arrayTest):
            dot.node(n, color='red')
        else :
            dot.node(str(n))

createGraphNode(prev, node_g, nodes)

dot.edge(node_a.label, node_b.label, label='4')
dot.edge(node_a.label, node_c.label, label='3')
dot.edge(node_a.label, node_e.label, label='7')
dot.edge(node_b.label, node_d.label, label='5')
dot.edge(node_b.label, node_f.label, label='12')
dot.edge(node_c.label, node_d.label, label='11')
dot.edge(node_c.label, node_e.label, label='8')
dot.edge(node_d.label, node_e.label, label='2')
dot.edge(node_d.label, node_g.label, label='10')
dot.edge(node_e.label, node_g.label, label='5')
dot.edge(node_f.label, node_g.label, label='3')
dot.edge(node_g.label, node_c.label, label='1')

print(dot.source)

dot.render('test-output/round-table.gv.pdf', view=True)
dot.view()