from k_general_kit.gen_func import *
from k_graph_kit import *

print("Welcome! This program aims to return the shortest path from a vertex to another one of a given graph.")

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
        if i <= i2:
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
        if i == i2:
            continue
        while True:
            Weights = input(f"\nEnter the weight(s) of the oriented edge {vertex} -> {vertex2} : ")
            if Weights.strip() == '':
                break
            Weights = Weights.split(',')
            if any([not is_u_float(weight) or weight == '0' for weight in Weights]):
                print("\nOne of the given weights is not a strict positive real number!")
                continue
            G.Edges[(vertex, vertex2)] = [float(weight) for weight in Weights]
            break

print("\nThere, are the datas of the entered graph :\n")
G.printGraph()

while True:
    Vertices = input("\nEnter now the starting and the final vertices in the form : start,end (an empty entry interrompt the process) : ")
    if Vertices.strip() == '':
        break
    try:
        start, end = tuple(Vertices.split(','))
    except:
        print("\nSaisie invalide!")
        continue
    if start not in G.Vertices or end not in G.Vertices:
        print("\nAt least one of the given vertex is not in the vertices of the graph defined upstream!")
        continue
    Path = G.Djikstra(start, end)
    if Path[1] == inf:
        print(f"\nThere is no possible path from {start} to {end}.")
    else:
        print("\nThe shortest path from {0} to {1} is : {2}.\nIts total weight is : {3}.".format(start, end, "->".join(Path[0]), Path[1]))
    again = input("\nAgain (y or n) : ").lower()
    if again != 'y':
        break

input("\nGlad to have served you! Press 'Enter' to quit.")

