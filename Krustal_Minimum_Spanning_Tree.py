from k_general_kit.gen_func import *
from k_graph_kit import *

print("Welcome! This program aims to return the minimum spanning tree of a non oriented given graph. Refer to 'Graph' help for more information")

while True:
    Vertices = input("\nEnter the graph vertices by separating them with a comma (Ex: A,B,C) : ").split(',')
    if all([vertex != '' for vertex in Vertices]):
        break
    print("\nOne of the vertex entered is an empty string!")

Vertices = set(Vertices)
G = Graph(Vertices, name="Graph")

print("\nYou'll now enter the edges and theirs weights ( > 0 ) following this format 'weight1,...,weightn', for a given couple of vertices.\n\
NB: - There are as many of weights as edges between the vertices of the considered couple.\
    - An empty imput means that there is no edge between the considered couple of vertices")
l = len(Vertices)
for i, vertex in zip(range(l), Vertices):
    for i2, vertex2 in zip(range(l), Vertices):
        if i < i2:
            while True:
                Weights = input(f"\nEnter the weight(s) of the non oriented edge(s) between {vertex} & {vertex2} : ")
                if Weights.strip() == '':
                    break
                Weights = Weights.split(',')
                if any([not is_u_float(weight) or weight == '0' for weight in Weights]):
                    print("\nOne of the given weights is not a strict positive real number!")
                    continue
                G.Edges[fs({vertex, vertex2})] = [float(weight) for weight in Weights]
                break

print("\nThere, are the datas of the entered graph :\n")
G.printGraph()

if not G.isRelated():
    print("\nThe entered graph is not related and so can't have even a tree!")
else:
    print("\nThere, is the minimum spanning tree of the graph entered\n")
    G.Krustal().printGraph()

input("\nGlad to have served you! Press 'Enter' to quit.")

