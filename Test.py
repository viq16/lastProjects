import Prim
import PriorityQueue

g = Prim.Graph()

g.add_node(0)
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)
g.add_node(6)
g.add_node(7)

g.add_edge(0, 1, 5)
g.add_edge(0, 6, 3)
g.add_edge(0, 3, 9)
g.add_edge(1, 5, 6)
g.add_edge(1, 4, 8)
g.add_edge(1, 2, 9)
g.add_edge(2, 3, 9)
g.add_edge(2, 4, 4)
g.add_edge(2, 6, 5)
g.add_edge(2, 7, 3)
g.add_edge(3, 6, 8)
g.add_edge(4, 5, 2)
g.add_edge(4, 6, 1)
g.add_edge(5, 6, 6)
g.add_edge(6, 7, 9)

g.algorithm_Prim(0)

print(g.visited)
print(g.visited_history)