from k_general_kit.gen_func import *
from k_graph_kit import *

print("Welcome! This program aims to return an eventual Hamilton circuit a  given graph. Refer to 'Graph' help for more information")

while True:
    Vertices = input("\nEnter the graph vertices by separating them with a comma (Ex: A,B,C) : ").split(',')
    if all([vertex != '' for vertex in Vertices]):
        break
    print("\nOne of the vertex entered is an empty string!")

Vertices = set(Vertices)
G = Graph(Vertices, name="Graph")

print("\nYou'll now enter the edges and theirs numbers ( integer, > 0 ) following this format 'vertex1-vertex2,number', for an oriented edge from vertex1 to vertex2.\n\
For a non oriented edge, just replace '-' by '='.\n\
NB: An empty entry stops the proccess")
while True:
    EdgeWeights = input("\nEnter an edge : ")
    if EdgeWeights.strip() == '':
        break
    check = 0
    if EdgeWeights.count('-') == 1 and EdgeWeights.count('=') == 0:
        check = 1
        index1 = EdgeWeights.find('-')
    if EdgeWeights.count('-') == 0 and EdgeWeights.count('=') == 1:
        check = 2
        index1 = EdgeWeights.find('=')
    if check == 0:
        print("\nInvalid input!")
        continue
    if ',' not in EdgeWeights:
        print("\nInvalid input!")
        continue
    index2 = EdgeWeights.find(',')
    if index2 < index1:
        print("\nInvalid input!")
        continue
    EdgeWeights = split_iter(EdgeWeights, ",-=", False)
    vertex1, vertex2 = EdgeWeights[0], EdgeWeights[1]
    if vertex1 not in G.Vertices or vertex2 not in G.Vertices:
        print("\nAt least one of the given vertex is not in the vertices of the graph defined upstream!")
        continue
    n = EdgeWeights[2]
    if n.isdigit() == False or n == '0':
        print(f"\n'{n}' is not a strict positive integer!")
        continue
    if check == 1 and vertex1 != vertex2:
        Edge = (vertex1, vertex2)
    else:
        Edge = fs({vertex1, vertex2})
    G.Edges[Edge] = int(n)

print("\nThere, are the datas of the entered graph :\n")
G.printGraph()

if not G.isConnected():
    print("\nThe entered graph is not connected and so, can't have an Hamilton circuit!")
else:
    Circuit = G.HamiltonCircuit()
    if Circuit == ():
        print("\nThe entered graph doesn't have any Hamilton circuit!")
    else:
        Circuit = "->".join(Circuit)
        print(f"\nThere, is an Hamilton circuit of the graph entered : {Circuit}.")

input("\nGlad to have served you! Press 'Enter' to quit.")

