#!/usr/bin/python

import networkx as nx

if __name__ == "__main__":

    str = input("")
    n, p, k = str.split(" ")

    n = int(n)
    p = int(p)
    k = int(k)

    G = nx.Graph()
    C = nx.Graph()
    C = G

    while(n != 0):

      for i in range(0, p):
        str = input("")
        u, v = str.split(" ")
        G.add_edge(int(u), int(v))

      remove = True

      while(remove):
        remove = False
        for node in C.nodes():
          if(C.degree(node) < k):
            G.remove_node(node)
            remove = True
            break

      if(len(G)==0 or len(C)==0):
        print(0)
      else:
        M = max(nx.connected_component_subgraphs(G), key=len)
        print(len(M))

      str = input("")
      n, p, k = str.split(" ")

      n = int(n)
      p = int(p)
      k = int(k)
