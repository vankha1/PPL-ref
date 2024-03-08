import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl("main",IntegerType(),[],None,BlockStmt([]))]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl("main",IntegerType(),[],None,BlockStmt([FuncCall("putIntLn",[IntegerLit(4)])]))]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl("main",IntegerType(),[],None,BlockStmt([FuncCall("getIntLn",[])]))]))
        self.assertTrue(TestAST.test(input,expect,302))
   