import unittest
from Domain.graph import Graph

class Test(unittest.TestCase):


    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


    def test(self):
        g = Graph(5)
        g.addEdge(0,1)
        g.addEdge(1,2) 
        g.addEdge(2,4) 
        g.addEdge(3,2) 
        g.addEdge(3,4) 
        g.addEdge(4,3) 
        g.addEdge(4,1)
        gr = g.copyGraph()
        assert g.isEdge(0,4) == False
        g.addEdge(0,4)
        assert g.isEdge(0, 4) == True 
        g.addEdge(0, 2)
        g.removeEdge(0, 2)
        assert g.isEdge(0,2) == False
        assert g.getCost(1, 2) == 1
        assert g.getVertices() == 5
        g.setCost(2, 4, 3)
        assert g.getCost(2, 4) == 3
        g.addVertex()
        assert g.getVertices() == 6
        g.addEdge(0, 5, 2)
        assert g.isEdge(0, 5)
        g.removeVertex(1)
        assert g.isEdge(4,1) == False
        assert g.isEdge(1,2) == False
        assert g.outDegree(4) == 0 
        assert g.inDegree(4) == 1
        assert g.outDegree(0) == 2
        assert g.inDegree(2) == 1
        assert gr.isEdge(0,4) == False
        
        
                              

