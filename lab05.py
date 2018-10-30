#!/usr/bin/python

import networkx as nx

if __name__ == "__main__":
    str = input("")
    n, m = str.split(" ")

    n = int(n)
    m = int(m)

    while(not(m==0 and n==0)):
      
      G = nx.Graph()
      
      for i in range(0, m):
        str = input("")
        u, v, w = str.split(" ")
        G.add_edge(int(u), int(v), weight=int(w))

      T=nx.minimum_spanning_tree(G)

      soma = 0
      for i in range(0,n):
        for j in range(0,n):
          if((not T.has_edge(i,j)) and G.has_edge(i,j) and i>j):
            soma += G[i][j]['weight']

      print(soma)

      str = input("")
      n, m = str.split(" ")
      
      n = int(n)
      m = int(m)


