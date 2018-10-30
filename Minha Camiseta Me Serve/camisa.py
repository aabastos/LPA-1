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

      camisas = ["XXL","XL","L","M","S","XS"]       # Lista do tamanho de camisas

      for i in camisas:                             # Laço que adiciona um nó para cada camisa.
        for j in range (0, int(numCamisas/6)):      # Se existirem 3 camisas para cada tamanho,
          B.add_node((i+str(j)), bipartite=0)       # serão adicionados 3 nós para cada tamanho de camisa.

      for i in range (0, voluntarios):
        B.add_node(str(j), bipartite=1)

         #lendo as opções
        ler = input("")
        a, b = ler.split(" ")

        for j in range (0, int(numCamisas/6)):
          B.add_edge(a+str(j),i)                    # Liga o voluntário à todas as camisas do tamanho 'a'
          B.add_edge(b+str(j),i)                    # Liga o voluntário à todas as camisas do tamanho 'b'

      #mostrar o grafo print(B.edges())

      M = nx.maximal_matching(B)                    # Casamento máximo do grafo

      if len(M) == voluntarios:                     # Se o tamanho do casamento for igual ao número de funcionários, quer dizer que há camisas suficientes para todos
        print("YES")
      else:
        print("NO")

      # B.add_edges_from([('A',1), ('B',1), ('C',1), ('C',3), ('D',2), ('E',3),
      # ('E',4)])
