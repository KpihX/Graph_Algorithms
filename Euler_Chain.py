from k_general_kit.gen_func import *
from k_graph_kit import *

print("Welcome! This program aims to return an eventual Euler chain a  given graph. Refer to 'Graph' help for more information")

while True:
    Vertices = input("\nEnter the graph vertices by separating them with a comma (Ex: A,B,C) : ").split(',')
    if all([vertex != '' for vertex in Vertices]):
        break
    print("\nOne of the vertex entered is an empty string!")

Vertices = set(Vertices)
G = Graph(Vertices, name="Graph")

print("\nYou'll now enter for each couple of vertices, the number of edges between then.\n\
NB: An empty imput means that there is no edge between the considered couple of vertices")
l = len(Vertices)
for i, vertex in zip(range(l), Vertices):
    for i2, vertex2 in zip(range(l), Vertices):
        if i <= i2:
            while True:
                n = input(f"\nEnter the number of non oriented edge(s) between {vertex} & {vertex2} : ")
                if n.strip() == '':
                    break
                if n.isdigit() == False or n == '0':
                    print(f"\n'{n}' is not a strict positive integer!")
                    continue
                G.Edges[fs({vertex, vertex2})] = int(n)
                break
        if i == i2:
            continue
        while True:
            n = input(f"\nEnter the number of the oriented edge(s) {vertex} -> {vertex2} : ")
            if n.strip() == '':
                break
            if n.isdigit() == False or n == '0':
                print(f"\n'{n}' is not a strict positive real integer!")
                continue
            G.Edges[(vertex, vertex2)] = int(n)
            break

print("\nThere, are the datas of the entered graph :\n")
G.printGraph()

if not G.isConnected():
    print("\nThe entered graph is not connected and so, can't have an Euler chain!")
else:
    Chain = G.EulerChain()
    if Chain == ():
        print("\nThe entered graph doesn't have any Euler chain!")
    else:
        Chain = "->".join(Chain)
        print(f"\nThere, is an Euler chain of the graph entered : {Chain}.")

input("\nGlad to have served you! Press 'Enter' to quit.")

