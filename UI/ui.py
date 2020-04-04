from Domain.graph import Graph
from Domain.Iterators import *
def menu():
    s = "0.Exit. \n"
    s += "1.Get the number of vertices. \n"
    s += "2.Check if there is an edge between two vertices. \n"
    s += "3.Get the out degree of a vertex. \n"
    s += "4.Get the in degree of a vertex. \n"
    s += "5.Change the cost of an edge. \n"
    s += "6.Add an edge. \n"
    s += "7.Remove an edge. \n"
    s += "8.Add a vertex. \n"
    s += "9.Remove a vertex. \n"
    s += "10.Parse the set of outbound edges of a specified vertex. \n"
    s += "11.Parse the set of inbound edges of a specified vertex. \n"
    s += "12.Parse the vertices. \n"
    s += "13.Print the graph. \n"
    return s

def readFile(fileName):
    try:
        f = open(fileName, "r")
        line = f.readline().split(" ")
        g = Graph(int(line[0]))
        line = f.readline()
        while  len(line) > 0:
            line = line.split(" ")
            g.addEdge(int(line[0]),int( line[1]),int( line[2]))
            line = f.readline().strip()
        f.close()
    except IOError as e:
        print("An error occured - " + str(e))
        raise e
    return g
    
def readVertices():
    x = int(input("Enter the starting vertex: "))
    y = int(input("enter the ending vertex: "))
    return x,y

def readVertex():
    x = int(input("Enter the vertex: "))
    return x

def readCost():
    x = int(input("Enter the cost: "))
    return x

def printOut(g):
    vertex = readVertex()
    it = g.parseOut(vertex)
    while(it.valid()):
        print(vertex,"-->",it.getCurrent())
        it.next()
    if len(g.getOutbound()[vertex]) == 0:
        print("Isolated")
            
def printIn(g):
    vertex = readVertex()
    it = g.parseIn(vertex)
    while(it.valid()):
        print(vertex,"<--",it.getCurrent())
        it.next()
    if len(g.getInbound()[vertex]) == 0:
        print("Isolated")
        
def printVertices(g):
    it = g.parse()
    while it.valid():
        print(it.getCurrent())
        it.next()
        
def printGraph(g):
    s1 = "List out: \n"
    for vertice in range(len(g.getOUT())):
        s1 += str(vertice) + " --> " 
        for v in g.getOUT()[vertice]:
            s1+= str(v) + " "
        s1+="\n"
    s2 = "\nList in: \n"
    for vertice in range(len(g.getIN())):
        s2 += str(vertice) + " <-- "
        for v in g.getIN()[vertice]:
            s2+= str(v) + " "
        s2+="\n"
    print(s1)
    print(s2)
        
        
            
        
            
def main():
    g = readFile("graf.txt")
    graph = g.copyGraph()
    command  = 1
    while command != 0:
        print(menu())
        command = int(input("Enter command: "))
        if command == 1:
            print("The number of vertices is: "+str(graph.getVertices()))
        elif command == 2:
            start,end = readVertices()
            if graph.isEdge(start, end):
                print("There is an edge between the vertices.")
            else:
                print("There is no edge between the two vertices.")
        elif command == 3:
            vertex = readVertex()
            print("The out degree of the vertex is " + str(graph.outDegree(vertex)))
        elif command == 4:
            vertex = readVertex()
            print("The in degree of the vertex is " + str(graph.inDegree(vertex)))
        elif command == 5:
            start,end = readVertices()
            newCost = readCost()
            graph.setCost(start, end, newCost)
        elif command == 6:
            start,end = readVertices()
            cost = readCost()
            graph.addEdge(start, end, cost)
        elif command == 7:
            start,end = readVertices()
            graph.removeEdge(start, end)
        elif command == 8:
            graph.addVertex()
        elif command == 9:
            vertex = readVertex()
            graph.removeVertex(vertex)
        elif command == 10:
            printOut(graph)
        elif command == 11:
            printIn(graph)
        elif command == 12:
            printVertices(graph)
        elif command == 13:
            printGraph(graph)
        
main()