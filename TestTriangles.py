 # -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr@
author: rk
"""
import unittest
from Triangle import classifytriangle
# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testEquilateralA(self):
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 is a Equilateral triangle')

    
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
    
    
    def testinvalidTriangles(self):
        self.assertEqual(classifyTriangle(5,12,250),'InvalidInput','5,12,250 is a Invalid triangle')
    
    
    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(150,150,150),'Equilateral','150,150,150 should be equilateral')
    
    
    def testScaleneTriangles(self): 
        self.assertEqual(classifyTriangle(7,8,9),'Scalene','7,8,9 should be scalene')
    
      
    
    def testIsocelesTriangle(self): 
        self.assertEqual(classifyTriangle(7,5,7),'Isoceles','7,5,7 should be isoceles')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
