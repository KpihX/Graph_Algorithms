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

print("\nYou'll now enter the edges and theirs weights ( > 0 ) following this format 'vertex1=vertex2,weight1,...,weightn', for an  edge between  vertex1 and vertex2.\n\
NB: - There are as many of weights as edges between the vertices of the considered couple.\
    - An empty entry stops the proccess")
while True:
    EdgeWeights = input("\nEnter an edge : ")
    if EdgeWeights.strip() == '':
        break
    index1 = EdgeWeights.find(',')
    index2 = EdgeWeights.find('=')
    if index1 == -1 or index2 == -1:
        print("\nInvalid input!")
        continue
    if  index1 < index2:
        print("\nInvalid input!")
        continue
    
    EdgeWeights = split_iter(EdgeWeights, ",=", False)
    vertex1, vertex2 = EdgeWeights[0], EdgeWeights[1]
    if vertex1 not in G.Vertices or vertex2 not in G.Vertices:
        print("\nAt least one of the given vertex is not in the vertices of the graph defined upstream!")
        continue
    Weights = EdgeWeights[2:]
    if any([not is_u_float(weight) or weight == '0' for weight in Weights]):
        print("\nAt least one of the given weights is not a strict positive real number!")
        continue
    G.Edges[fs({vertex1, vertex2})] = [float(weight) for weight in Weights]

print("\nThere, are the datas of the entered graph :\n")
G.printGraph()

if not G.isRelated():
    print("\nThe entered graph is not related and so can't have even a tree!")
else:
    print("\nThere, is the minimum spanning tree of the graph entered\n")
    G.Krustal().printGraph()

input("\nGlad to have served you! Press 'Enter' to quit.")

