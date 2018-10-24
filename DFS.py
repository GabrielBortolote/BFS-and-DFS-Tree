import networkx as nx
import matplotlib.pyplot as plt
import sys

G = nx.read_pajek(sys.argv[1]) if (len(sys.argv) > 1) else nx.complete_graph(10)

def DFS(G, s):
	#init
	for node in G.node:
		G.nodes[node]['color'] = 'white'
		G.nodes[node]['pi'] = None
	DFS_Visit(G, s)

	#gerando arvore
	DFS_Tree = nx.Graph()
	for node in G.node:
		DFS_Tree.add_node(node) #copiando nodes
	for node in G.node:
		DFS_Tree.add_edge(node, G.nodes[node]['pi']) #plotando arestas

	return DFS_Tree

def DFS_Visit(G, u):
	G.nodes[u]['color'] = 'gray'
	for node in G.neighbors(u):
		if G.nodes[node]['color'] == 'white':
			G.nodes[node]['pi'] = u
			DFS_Visit(G, node)
	G.nodes[u]['color'] = 'black'


s = sys.argv[2] if (len(sys.argv) > 2) else list(G.nodes)[0]
Tree = DFS(G, s)
nx.draw(G)
plt.show()

nx.draw(Tree)
plt.show()