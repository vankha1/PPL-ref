import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_1(self):
        input = Program([VarDecl("a", IntegerType()), VarDecl("c", FloatType())])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))