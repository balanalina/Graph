from Domain.Iterators import *
from copy import deepcopy
class Graph:
    def __init__(self,number):
        self.__n = number
        self.__inbound = [[]for i in range(number)]
        self.__outbound = [[] for i in range(number)]
        self.__cost = {}
        for i in range(number):
            self.__inbound[i] = []
            self.__outbound[i] = []
    
    
    """
    This function returns true if there is an edge between the vertices "start" and "end" and False othewise.
    Input: start, end - integers
    Output: True, False
    """
    def isEdge(self,start,end):
        if end in  self.__outbound[start] and start in self.__inbound[end]:
            return True
        return False
    
    """
    The functions adds a new edge to the graph, returns False if the edge already exists, if the edge is added True will be returned.The default value for a cost is 1.
    Input: start(starting vertex of the edge),end(ending vertex of the edge),cost - integers
    Output: True or False
    """
    def addEdge(self,start,end,cost = 1):
        if self.isEdge(start,end):
            return False
        self.__outbound[start].append(end)
        self.__inbound[end].append(start)
        self.__cost[(start,end)] = cost
        
        return True
    
    """
    The function removes an edge and its cost and returns True,if the edge does not exist False is returned.
    Inout: start,end - unsigned integers
    Output: True or False
    """
    def removeEdge(self,start,end):
        if self.isEdge(start, end):
            self.__outbound[start].remove(end)
            self.__inbound[end].remove(start)
            del self.__cost[(start,end)]
            return True
        return False
    
    """
    The funtion returns the cost of the edge between start and end.
    Input: start,end - unsigned integers
    Output: cost - integer
    """
    def getCost(self,start,end):
        return self.__cost[(start,end)]
    
    """
    The functions updates the cost of an edge.
    Input: start, end, newCost - integers
    Output: -
    """
    def setCost(self,start,end,newCost):
        if self.isEdge(start, end):
            self.__cost[(start,end)] = newCost
            return True
        return False
    
    """
    This function returns the number of vertices of the graph.
    Input: - 
    Output: n - integer
    """
    def getVertices(self):
        return self.__n
    
    """
    This function adds a new vertex to our graph, on position n(vertices are indexed from 0) add changes the number of vertices of the graph,adding a list for the new vertex in the list of inbounds and outbounds.
    Input: -
    Output: -
    """
    def addVertex(self):
        self.__n += 1
        self.__outbound.append([])
        self.__inbound.append([])
        
    """
    The function removes an existing vertex and all its aparition,reindexing the vertices  and returns True.If the vertex does not exist, False is returned.
    Input: vertex - unsigned integer
    Output: True or False
    """
    def removeVertex(self,vertex):
        if self.__n <= vertex:
            return False
        self.__n -= 1
        self.__inbound.pop(vertex)
        self.__outbound.pop(vertex)
        for i in range(self.__n):
            if vertex in self.__inbound[i]:
                self.__inbound[i].remove(vertex)
            if vertex in self.__outbound[i]:
                self.__outbound[i].remove(vertex)
        for i in range(self.__n):
            for j in range(len(self.__outbound[i])):
                if self.__outbound[i][j] >= vertex:
                    self.__outbound[i][j] -= 1
            for j in range(len(self.__inbound[i])):
                if self.__inbound[i][j] >= vertex:
                    self.__inbound[i][j] -= 1
        if (i,vertex) in self.__cost:
            del self.__cost[(i,vertex)]
        if (vertex,i) in self.__cost:
            del self.__cost[(vertex,i)]
        return True
        
    """
    The function computes and returns the out degree of a vertex,returns False if the vertex does not exist.
    Input: vertex - unsigned integer
    Outpu: outDegree - unisgned integer, False - inexistent vertex
    """   
    def outDegree(self,vertex):
        if vertex >= self.__n:
            return False
        x = len(self.__outbound[vertex])
        return x
    
    """
    The function computes and returns the in degree of a vertex,returns False if the vertex does not exist.
    Input: vertex - unsigned integer
    Outpu: inDegree - unisgned integer, False - inexistent vertex
    """ 
    def inDegree(self,vertex):
        if vertex >= self.__n:
            return False
        x = len(self.__inbound[vertex])
        return x
    
    """
    The function creates and returns another graph, representing a copy of the initial graph.
    Input: -
    Outpu: g - Graph
    """
    def copyGraph(self):
        graph = Graph(self.__n)
        graph.setOutbound(deepcopy(self.getOutbound()))
        graph.setInbound(deepcopy(self.getInbound()))
        graph.setCosts(deepcopy(self.__cost))
        return graph 
    """
    Setters and getters.
    """
    def getInbound(self):
        return self.__inbound
    
    def getOutbound(self):
        return self.__outbound
    
    def setInbound(self,list):
        self.__inbound = list
        
    def setOutbound(self,list):
        self.__outbound = list
        
    def setCosts(self,dict):
        self.__cost = dict
    
    def getIN(self):
        return self.__inbound
    
    def getOUT(self):
        return self.__outbound
    
    def getCosts(self):
        return self.__cost
    
    """
    This 3 functions return iterators for parsing the graph,parsing inbounds and outbounds.
    """
    def parseOut(self,vertex):
        return vertexIteratorOut(self,vertex)
    
    def parseIn(self,vertex):
        return vertexIteratorIn(self,vertex)
    
    def parse(self):
        return verticesIterator(self)
    """
    Iterator for parsing out a vertex.
    Input: graph - Graph, vertex - integer
    """
class vertexIteratorOut:
    def __init__(self,graph,vertex):
        self.__g = graph
        self.__vertex = vertex
        self.__current = 0
    """
    Checks if there still are elements to parse.
    """  
    def valid(self):
        if self.__current < len(self.__g.getOutbound()[self.__vertex]):
            return True
        return False
    
    """
    Moves to the next element if there is a next element.
    """
    def next(self):
        if self.valid():
            self.__current += 1
        else:
            raise ValueError
    """
    Makes the first element the current element.
    """
    def first(self):
        self.__current = 0 
        
    """
    Returns the current element that was iterated.
    """
    def getCurrent(self):
        if self.valid():
            return self.__g.getOutbound()[self.__vertex][self.__current]
        else:
            raise ValueError
     
    """
    Iterator for parsing in a vertex.
    Input: graph - Graph, vertex - integer
    """   
class vertexIteratorIn:
    def __init__(self,graph,vertex):
        self.__g = graph
        self.__vertex = vertex
        self.__current = 0
    
    """
    Checks if there still are elements  to be iterated.
    """   
    def valid(self):
        if self.__current < len(self.__g.getInbound()[self.__vertex]):
            return True
        return False
    
    """
    Moves the iterator to the next element if there still are elements.
    """
    def next(self):
        if self.valid():
            self.__current += 1
        else:
            raise ValueError
    
    """
    The first element becomes the current one.
    """
    def first(self):
        self.__current = 0 
        
    """
    Return the current element.
    """
    def getCurrent(self):
        if self.valid():
            return self.__g.getInbound()[self.__vertex][self.__current]
        else:
            raise ValueError
     
    """
    Iterator for parsing the graph.
    Input: graph - Graph
    """   
class verticesIterator:
    def __init__(self,graph):
        self.__g = graph
        self.__current = 0
    
    """
    Checks if there still are vertices to be iterated.
    """
    def valid(self):
        if self.__current < self.__g._Graph__n:
            return True
        return False
    
    def first(self):
        self.__current = 0
        
    def next(self):
        if self.valid():
            self.__current += 1
            
            
        return False
    
    def getCurrent(self):
        if self.valid():
            return self.__current
        raise ValueError
    
class myException(Exception):
    def __init__(self,msg):
        self.__msg = msg;
        
    def __str__(self):
        return self.__msg