import networkx as nx
from networkx.algorithms import bipartite

if __name__ == "__main__":

    ler = input("")
    casos = int(ler)

    for i in range(0,casos):
      ler = input("")
      camisetas, voluntarios = ler.split(" ")

      numCamisas = int(camisetas)
      voluntarios = int(voluntarios)

      B = nx.Graph()

      camisas = ["XXL","XL","L","M","S","XS"]


      for i in camisas:
        for j in range (0, int(numCamisas/6)):
          B.add_node((i+str(j)), bipartite=0)

      for i in range (0, voluntarios):
        B.add_nodes_from(str(j), bipartite=1)
         #lendo as opções
        ler = input("")
        a, b = ler.split(" ")
        for j in (0, numCamisas/6):
          B.add_edge(a+str(j),i)


      #mostrar o grafo print(B.edges())

      M = nx.maximal_matching(B)

      if len(M) == voluntarios:
        print("YES")
      else:
        print("NO")

      # B.add_edges_from([('A',1), ('B',1), ('C',1), ('C',3), ('D',2), ('E',3),
      # ('E',4)])
