from Graph import*

print("Welcome! This program aims to return the shortest path from a vertex to another one of a given graph.")

while True:
    Vertices = input("\nEnter the graph vertices by separating them with a comma (Ex: A,B,C) : ").split(',')
    if all([vertex != '' for vertex in Vertices]):
        break
    print("\nOne of the vertex entered is an empty string!")

Vertices = set(Vertices)
G = Graph(Vertices, name="Graph")

print("\nYou'll now enter the edges and theirs weights ( > 0 ) following this format 'vertex1-vertex2,weight1,...,weightn', for an oriented edge from vertex1 to vertex2.\n\
For a non oriented edge, just replace '-' by '='.\n\
NB: - There are as many of weights as edges between the vertices of the considered couple.\
    - An empty entry stops the proccess")
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

    EdgeWeights = splitIter(EdgeWeights, ",-=", False)
    vertex1, vertex2 = EdgeWeights[0], EdgeWeights[1]
    if vertex1 not in G.Vertices or vertex2 not in G.Vertices:
        print("\nAt least one of the given vertex is not in the vertices of the graph defined upstream!")
        continue
    Weights = EdgeWeights[2:]
    if any([not isUFloat(weight) or weight == '0' for weight in Weights]):
        print("\nAt least one of the given weights is not a strict positive real number!")
        continue
    if check == 1 and vertex1 != vertex2:
        Edge = (vertex1, vertex2)
    else:
        Edge = fs({vertex1, vertex2})
    G.Edges[Edge] = [float(weight) for weight in Weights]

print("\nThere, are the datas of the entered graph :\n")
G.printGraph()

while True:
    Vertices = input("\nEnter now the starting and the final vertices in the form : start,end (an empty entry interrompt the process) : ")
    if Vertices.strip() == '':
        break
    try:
        start, end = tuple(Vertices.split(','))
    except:
        print("\nInvalid input!")
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

