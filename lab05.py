#!/usr/bin/python

import networkx as nx

if __name__ == "__main__":
    str = input()

    while str != "0 0":
        n, m = str.split(" ")
        n = int(n)
        m = int(m)

        G = nx.Graph()

        for i in range(0, m):
            str = input("")
            u, v, w = str.split(" ")
            G.add_edge(int(u), int(v), weight=int(w))

        T = nx.minimum_spanning_tree(G)                               # Ruas que ficarão com iluminação

        # Calculo da economia feita
        soma = 0
        for i in range(0,n):
            for j in range(0,n):
                if((not T.has_edge(i,j)) and G.has_edge(i,j) and i>j):
                    soma += G[i][j]['weight']

        print(soma)

        str = input()
