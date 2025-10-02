import networkx as nx

G = nx.Graph(name = 'Meu Grafo')

with open("facebook_combined.txt", 'r') as f:
    for line in f:
        u, v = map(int, line.strip().split())
        G.add_edge(u, v)

print(G)
print(f'Nós: {G.number_of_nodes()}')
print(f'Arestas: {G.number_of_edges()}')