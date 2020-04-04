#from Domain.graph import Graph

class vertexIteratorOut:
    def __init__(self,graph,vertex):
        self.__g = graph
        self.__vertex = vertex
        self.__current = 0
        
    def valid(self):
        if self.__current < len(self.__g.getOutbound()[self.__vertex]):
                                return True
        return False
    
    def next(self):
        if self.valid():
            self.__current += 1
        else:
            raise ValueError
        
    def first(self):
        self.__current = 0 
        
    def getCurrent(self):
        if self.valid():
            return self.__g.getOutbound()[self.__vertex][self.__current]
        else:
            raise ValueError

class vertexIteratorIn:
    def __init__(self,graph,vertex):
        self.__g = graph
        self.__vertex = vertex
        self.__current = 0
        
    def valid(self):
        if self.__current < len(self.__g.getInbound()[self.__vertex]):
            return True
        return False
    
    def next(self):
        if self.valid():
            self.__current += 1
        else:
            raise ValueError
        
    def first(self):
        self.__current = 0 
        
    def getCurrent(self):
        if self.valid():
            return self.__g.getInbound()[self.__vertex][self.__current]
        else:
            raise ValueError
        
class verticesIterator:
    def __init__(self,graph):
        self.__g = graph
        self.__current = 0
    
    def valid(self):
        if self.__current < self.__g.__n:
            return True
        return False
    
    def first(self):
        self.__current = 0
        
    def next(self):
        if self.valid():
            self.__current += 1
        raise ValueError
    
    def getCurrent(self):
        if self.valid():
            return self.__current
        raise ValueError