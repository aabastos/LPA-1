import networkx as nx
from networkx.algorithms import bipartite

if __name__ == "__main__":

    print("oi")
    str = input("")
    casos = int(str)

    for i in casos:
      str = input("")
      camisetas, voluntarios = str.split(" ")

      camistas = int(camisetas)
      voluntarios = int(voluntarios)

      B = nx.Graph()

      B.add_nodes_from(['XXL','XL','L','M','S','XS'], bipartite=0)

      for j in voluntarios:
        B.add_nodes_from(j, bipartite=1)
        str = input("")
        a, b = str.split(" ")
        B.add_edges_from([(a,j), (b,j)])
