import networkx as nx
import queue as q
import matplotlib.pyplot as plt
import sys

if len(sys.argv) > 1:
	G = nx.read_pajek(sys.argv[1])
else:
	G = nx.complete_graph(10)
	

def BFS(G, s):
	
	#init
	for node in G.node:
		G.nodes[node]['color'] = 'white'
		G.nodes[node]['delta'] = float('inf')
		G.nodes[node]['pi'] = None
	G.nodes[s]['color'] = 'gray'
	G.nodes[s]['delta'] = 0
	queue = q.Queue()
	queue.put(s)

	#calculando
	while queue.qsize()!= 0:
		u = queue.get()
		for node in G.neighbors(u):
			if G.nodes[node]['color'] == 'white':
				G.nodes[node]['color'] = 'gray'
				G.nodes[node]['delta'] = G.node[u]['delta'] + 1
				G.nodes[node]['pi'] = u
				queue.put(node)
		G.nodes[u]['color'] = 'black'

	#gerando Tree
	BFS_Tree = nx.Graph()
	for node in G.node:
		BFS_Tree.add_node(node)
	for node in G.node:
		BFS_Tree.add_edge(node, G.nodes[node]['pi'])

	return BFS_Tree


if (len(sys.argv) > 2):
	s = sys.argv[2]
else:
	s = list(G.nodes)[0]
Tree = BFS(G, s)
nx.draw(G)
plt.show()

nx.draw(Tree)
plt.show()