import unittest
from TestUtils import TestCodeGen
from AST import *
class CheckCodeGenSuite(unittest.TestCase):

    def test1(self):
        input = """
            c: integer = 9;
            foo : function integer(b: integer){
                r: integer = 0;
                r = 3 - b;
                return r;
            }
            main : function void(){
                a: auto = 30;
                for (c = 30, c > 10, c - 5) {
                }
                if (!true) printInteger(a);
                else {
                    printInteger(foo(1) + c) ;
                }
            }  
        """
        expect = '12'
        self.assertTrue(TestCodeGen.test(input,expect,801))


