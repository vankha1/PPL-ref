import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):

    def test_case_101(self):

        input = """x: string = "abc"; """
        expect = """Program([
	VarDecl(x, StringType, StringLit(abc))
])"""
        self.assertTrue(TestAST.test(input, expect, 101))

    def test_case_102(self):

        input = """x1z: float;"""
        expect = """Program([
	VarDecl(x1z, FloatType)
])"""
        self.assertTrue(TestAST.test(input, expect, 102))

    def test_case_103(self):

        input = """a_b: boolean;"""
        expect = """Program([
	VarDecl(a_b, BooleanType)
])"""
        self.assertTrue(TestAST.test(input, expect, 103))

    def test_case_104(self):

        input = """x_Y_z: integer;"""
        expect = """Program([
	VarDecl(x_Y_z, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 104))

    def test_case_105(self):

        input = """_Aa: auto;"""
        expect = """Program([
	VarDecl(_Aa, AutoType)
])"""
        self.assertTrue(TestAST.test(input, expect, 105))

    def test_case_106(self):

        input = """Array: array [3] of string;"""
        expect = """Program([
	VarDecl(Array, ArrayType([3], StringType))
])"""
        self.assertTrue(TestAST.test(input, expect, 106))

    def test_case_107(self): #error

        input = """x_Y_z: array[2,2] of integer;"""
        expect = """Program([
	VarDecl(x_Y_z, ArrayType([2, 2], IntegerType))
])"""
        self.assertTrue(TestAST.test(input, expect, 107))

    def test_case_108(self):

        input = """x, y: float = 0, 4_5.e1;"""
        expect = """Program([
	VarDecl(x, FloatType, IntegerLit(0))
	VarDecl(y, FloatType, FloatLit(450.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 108))

    def test_case_109(self):

        input = """z: float = 12 + 2;"""
        expect = """Program([
	VarDecl(z, FloatType, BinExpr(+, IntegerLit(12), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, expect, 109))

    def test_case_110(self):

        input = """chatgpt: string = "uaalo"; """
        expect = """Program([
	VarDecl(chatgpt, StringType, StringLit(uaalo))
])"""
        self.assertTrue(TestAST.test(input, expect, 110))

    def test_case_111(self): 

        input = """x, y: array [1,1] of float = {2}, {"hello"};"""
        expect = """Program([
	VarDecl(x, ArrayType([1, 1], FloatType), ArrayLit([IntegerLit(2)]))
	VarDecl(y, ArrayType([1, 1], FloatType), ArrayLit([StringLit(hello)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 111))

    def test_case_112(self): 

        input = """x, y, z: array [2] of integer = -1.2e8, {1,2}, true;"""
        expect = """Program([
	VarDecl(x, ArrayType([2], IntegerType), UnExpr(-, FloatLit(120000000.0)))
	VarDecl(y, ArrayType([2], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2)]))
	VarDecl(z, ArrayType([2], IntegerType), BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 112))

    def test_case_113(self): 

        input = """x, y, z: boolean= true, false, true && false;"""
        expect = """Program([
	VarDecl(x, BooleanType, BooleanLit(True))
	VarDecl(y, BooleanType, BooleanLit(False))
	VarDecl(z, BooleanType, BinExpr(&&, BooleanLit(True), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 113))

    def test_case_114(self):

        input = """Aee123, _aDC, A_bc: integer = 1 + 1, 2 * 1, -1;"""
        expect = """Program([
	VarDecl(Aee123, IntegerType, BinExpr(+, IntegerLit(1), IntegerLit(1)))
	VarDecl(_aDC, IntegerType, BinExpr(*, IntegerLit(2), IntegerLit(1)))
	VarDecl(A_bc, IntegerType, UnExpr(-, IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 114))

    def test_case_115(self):

        input = """x, x_Y_z, _ADC: array[2] of boolean;"""
        expect = """Program([
	VarDecl(x, ArrayType([2], BooleanType))
	VarDecl(x_Y_z, ArrayType([2], BooleanType))
	VarDecl(_ADC, ArrayType([2], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, expect, 115))

    def test_case_116(self):

        input = """arg1, arg2: integer = 1 - 1, 1 + a ;"""
        expect = """Program([
	VarDecl(arg1, IntegerType, BinExpr(-, IntegerLit(1), IntegerLit(1)))
	VarDecl(arg2, IntegerType, BinExpr(+, IntegerLit(1), Id(a)))
])"""
        self.assertTrue(TestAST.test(input, expect, 116))

    def test_case_117(self):

        input = """a, b: array[1] of float;"""
        expect = """Program([
	VarDecl(a, ArrayType([1], FloatType))
	VarDecl(b, ArrayType([1], FloatType))
])"""
        self.assertTrue(TestAST.test(input, expect, 117))

    def test_case_118(self):

        input = """x: float = writeFloat(1.0); a: integer = -1.5;"""
        expect = """Program([
	VarDecl(x, FloatType, FuncCall(writeFloat, [FloatLit(1.0)]))
	VarDecl(a, IntegerType, UnExpr(-, FloatLit(1.5)))
])"""
        self.assertTrue(TestAST.test(input, expect, 118))

    def test_case_119(self):

        input = """bts: boolean = !true && false; """
        expect = """Program([
	VarDecl(bts, BooleanType, BinExpr(&&, UnExpr(!, BooleanLit(True)), BooleanLit(False)))
])"""
        self.assertTrue(TestAST.test(input, expect, 119))

    def test_case_120(self): #error

        input = """str: string = !!(a && B);"""
        expect = """Program([
	VarDecl(str, StringType, UnExpr(!, UnExpr(!, BinExpr(&&, Id(a), Id(B)))))
])"""
        self.assertTrue(TestAST.test(input, expect, 120))

    def test_case_121(self):

        input = """calculator: integer = (1 - 1) % 2 + 1;"""
        expect = """Program([
	VarDecl(calculator, IntegerType, BinExpr(+, BinExpr(%, BinExpr(-, IntegerLit(1), IntegerLit(1)), IntegerLit(2)), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 121))

    def test_case_122(self):

        input = """java: float = !!a;"""
        expect = """Program([
	VarDecl(java, FloatType, UnExpr(!, UnExpr(!, Id(a))))
])"""
        self.assertTrue(TestAST.test(input, expect, 122))

    def test_case_123(self):

        input = """love: string = "I LOVE YOU";"""
        expect = """Program([
	VarDecl(love, StringType, StringLit(I LOVE YOU))
])"""
        self.assertTrue(TestAST.test(input, expect, 123))

    def test_case_124(self):

        input = """Array: array[3] of float = _A3[31, 12, 2002];"""
        expect = """Program([
	VarDecl(Array, ArrayType([3], FloatType), ArrayCell(_A3, [IntegerLit(31), IntegerLit(12), IntegerLit(2002)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 124))

    def test_case_125(self):

        input = """hate: array[1000] of boolean;"""
        expect = """Program([
	VarDecl(hate, ArrayType([1000], BooleanType))
])"""
        self.assertTrue(TestAST.test(input, expect, 125))

    def test_case_126(self):

        input = """lisa: array[2] of integer =  -1 + 2;"""
        expect = """Program([
	VarDecl(lisa, ArrayType([2], IntegerType), BinExpr(+, UnExpr(-, IntegerLit(1)), IntegerLit(2)))
])"""
        self.assertTrue(TestAST.test(input, expect, 126))

    def test_case_127(self):

        input = """rose: float = str[1];"""
        expect = """Program([
	VarDecl(rose, FloatType, ArrayCell(str, [IntegerLit(1)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 127))

    def test_case_128(self):

        input = """siuuuuuuuuuuuuuuuu: string = "Ronaldo";"""
        expect ="""Program([
	VarDecl(siuuuuuuuuuuuuuuuu, StringType, StringLit(Ronaldo))
])"""
        self.assertTrue(TestAST.test(input, expect, 128))

    def test_case_129(self):

        input = """messi: string = "Linol Messi"; """
        expect = """Program([
	VarDecl(messi, StringType, StringLit(Linol Messi))
])"""
        self.assertTrue(TestAST.test(input, expect, 129))

    def test_case_130(self):

        input = """a, b, c, d, e: integer = a[1], b[2], c[3], d[4], e[-5];"""
        expect = """Program([
	VarDecl(a, IntegerType, ArrayCell(a, [IntegerLit(1)]))
	VarDecl(b, IntegerType, ArrayCell(b, [IntegerLit(2)]))
	VarDecl(c, IntegerType, ArrayCell(c, [IntegerLit(3)]))
	VarDecl(d, IntegerType, ArrayCell(d, [IntegerLit(4)]))
	VarDecl(e, IntegerType, ArrayCell(e, [UnExpr(-, IntegerLit(5))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 130))

    def test_case_131(self):

        input = """func: function integer () {}"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 131))

    def test_case_132(self):

        input = """func: function float () {}"""
        expect = """Program([
	FuncDecl(func, FloatType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 132))

    def test_case_133(self):

        input = """_Func: function array[10, 10] of string () {}"""
        expect = """Program([
	FuncDecl(_Func, ArrayType([10, 10], StringType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 133))

    def test_case_134(self):

        input = """_Func: function void (x: integer) {}"""
        expect = """Program([
	FuncDecl(_Func, VoidType, [Param(x, IntegerType)], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 134))

    def test_case_135(self):

        input = """Func_1: function string (out t: integer, inherit z: float) inherit zzz {}"""
        expect = """Program([
	FuncDecl(Func_1, StringType, [OutParam(t, IntegerType), InheritParam(z, FloatType)], zzz, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 135))

    def test_case_136(self):

        input = """Siuuuuuuuuu_A7: function auto () {{}}"""
        expect = """Program([
	FuncDecl(Siuuuuuuuuu_A7, AutoType, [], None, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 136))

    def test_case_137(self):

        input = """Messssssssssssssssssssi: function array[3] of integer () {}"""
        expect = """Program([
	FuncDecl(Messssssssssssssssssssi, ArrayType([3], IntegerType), [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 137))

    def test_case_138(self):

        input = """Cavani: function void (inherit out a: integer, b: string, c: float) {{}}"""
        expect = """Program([
	FuncDecl(Cavani, VoidType, [InheritOutParam(a, IntegerType), Param(b, StringType), Param(c, FloatType)], None, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 138))

    def test_case_139(self):

        input = """MPAPE_10: function integer () {}"""
        expect = """Program([
	FuncDecl(MPAPE_10, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 139))

    def test_case_140(self):

        input = """a_a: function integer () {}"""
        expect = """Program([
	FuncDecl(a_a, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 140))

    def test_case_141(self):

        input = """Raphinha: function void () {
            {}{}{}{}}"""
        expect = """Program([
	FuncDecl(Raphinha, VoidType, [], None, BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 141))

    def test_case_142(self):

        input = """_Casemiro: function string () {
            {}
            {}
            {
            
            }     
            {}   
        }"""
        expect = """Program([
	FuncDecl(_Casemiro, StringType, [], None, BlockStmt([BlockStmt([]), BlockStmt([]), BlockStmt([]), BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 142))

    def test_case_143(self):

        input = """func: function float () {
            a = 1;
            b = 2;
        }
        """
        expect = """Program([
	FuncDecl(func, FloatType, [], None, BlockStmt([AssignStmt(Id(a), IntegerLit(1)), AssignStmt(Id(b), IntegerLit(2))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 143))

    def test_case_144(self):
        input = """func: function integer () {
            if (n == 1) return 1;
            else break;     
            }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), ReturnStmt(IntegerLit(1)), BreakStmt())]))
])"""
        self.assertTrue(TestAST.test(input, expect, 144))

    def test_case_145(self):

        input = """func: function integer () {
            a[1]= true && false && !a > 1;
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(ArrayCell(a, [IntegerLit(1)]), BinExpr(>, BinExpr(&&, BinExpr(&&, BooleanLit(True), BooleanLit(False)), UnExpr(!, Id(a))), IntegerLit(1)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 145))

    def test_case_146(self):

        input = """func: function array[1] of boolean () {
            continue;
            break;
            printInteger(1);
        }"""
        expect = """Program([
	FuncDecl(func, ArrayType([1], BooleanType), [], None, BlockStmt([ContinueStmt(), BreakStmt(), CallStmt(printInteger, IntegerLit(1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 146))

    def test_case_147(self):

        input = """func: function boolean () {
            {}
            do
            {
                a = 1 + 1;
            }
            while (n == 1);
        }"""
        expect = """Program([
	FuncDecl(func, BooleanType, [], None, BlockStmt([BlockStmt([]), DoWhileStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(1)))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 147))

    def test_case_148(self):

        input = """func: function void () {
            if (n == 1) a = true;
            continue;
            for (i = 0, i < 1, i - 1) a = b && true;
        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(1)), AssignStmt(Id(a), BooleanLit(True))), ContinueStmt(), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(-, Id(i), IntegerLit(1)), AssignStmt(Id(a), BinExpr(&&, Id(b), BooleanLit(True))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 148))

    def test_case_149(self):

        input = """func: function string () {
             for (i = 0, i < 1, i - 1) 
             {
                break;
             }
        }"""
        expect = """Program([
	FuncDecl(func, StringType, [], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(1)), BinExpr(-, Id(i), IntegerLit(1)), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 149))

    def test_case_150(self):

        input = """func: function void () {
            while (i && true) return _a + "uaalo";
        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([WhileStmt(BinExpr(&&, Id(i), BooleanLit(True)), ReturnStmt(BinExpr(+, Id(_a), StringLit(uaalo))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 150))

    def test_case_151(self):

        input = """func: function string () {
            while ( i <= 1) 
                {
                    for (i = 0, v < 10, t + 1)
                    {
                    if (a == 1 ) 
                    {
                        a, b: integer;
                    }
                    
                    a: integer = 10;
                    }
                    a: integer = 10;
                }
        }"""
        expect = """Program([
	FuncDecl(func, StringType, [], None, BlockStmt([WhileStmt(BinExpr(<=, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(v), IntegerLit(10)), BinExpr(+, Id(t), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(==, Id(a), IntegerLit(1)), BlockStmt([VarDecl(a, IntegerType), VarDecl(b, IntegerType)])), VarDecl(a, IntegerType, IntegerLit(10))])), VarDecl(a, IntegerType, IntegerLit(10))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 151))

    def test_case_152(self):

        input = """func: function string () {
            while ( i <= 1) 
                {
                    for (i = 0, v < 10 , t + 1)
                    {
                        break;
                    }
                }
        }"""
        expect = """Program([
	FuncDecl(func, StringType, [], None, BlockStmt([WhileStmt(BinExpr(<=, Id(i), IntegerLit(1)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(v), IntegerLit(10)), BinExpr(+, Id(t), IntegerLit(1)), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 152))

    def test_case_153(self):

        input = """func: function integer () {
            while (a + 1 && true)
                while (a + 1 && true)
                    while (a + 1 && true)
                        while (a + 1 && true)
                            while (a + 1 && true)
                                continue;
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(&&, BinExpr(+, Id(a), IntegerLit(1)), BooleanLit(True)), WhileStmt(BinExpr(&&, BinExpr(+, Id(a), IntegerLit(1)), BooleanLit(True)), WhileStmt(BinExpr(&&, BinExpr(+, Id(a), IntegerLit(1)), BooleanLit(True)), WhileStmt(BinExpr(&&, BinExpr(+, Id(a), IntegerLit(1)), BooleanLit(True)), WhileStmt(BinExpr(&&, BinExpr(+, Id(a), IntegerLit(1)), BooleanLit(True)), ContinueStmt())))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 153))

    def test_case_154(self):

        input = """func: function void () {
            if (i==1) 
                if (i==2)
                    if (i > 3)
                        if (i>=5)
                            printString("I love you");
        }"""
        expect ="""Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([IfStmt(BinExpr(==, Id(i), IntegerLit(1)), IfStmt(BinExpr(==, Id(i), IntegerLit(2)), IfStmt(BinExpr(>, Id(i), IntegerLit(3)), IfStmt(BinExpr(>=, Id(i), IntegerLit(5)), CallStmt(printString, StringLit(I love you))))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 154))

    def test_case_155(self):

        input = """func: function array[1] of integer () {
            break;
            if (true) a = 1 + 1;
            else b = b;
        }"""
        expect = """Program([
	FuncDecl(func, ArrayType([1], IntegerType), [], None, BlockStmt([BreakStmt(), IfStmt(BooleanLit(True), AssignStmt(Id(a), BinExpr(+, IntegerLit(1), IntegerLit(1))), AssignStmt(Id(b), Id(b)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 155))

    def test_case_156(self):

        input = """func: function boolean () {
            if (a[10] >= 100 )
                if (a[1,1] == 10)  printInteger(1);
                else if (a[-1, 10]  || false) b[-1] = 10; 
                   
        }"""
        expect = """Program([
	FuncDecl(func, BooleanType, [], None, BlockStmt([IfStmt(BinExpr(>=, ArrayCell(a, [IntegerLit(10)]), IntegerLit(100)), IfStmt(BinExpr(==, ArrayCell(a, [IntegerLit(1), IntegerLit(1)]), IntegerLit(10)), CallStmt(printInteger, IntegerLit(1)), IfStmt(BinExpr(||, ArrayCell(a, [UnExpr(-, IntegerLit(1)), IntegerLit(10)]), BooleanLit(False)), AssignStmt(ArrayCell(b, [UnExpr(-, IntegerLit(1))]), IntegerLit(10)))))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 156))

    def test_case_157(self):

        input = """func: function void () {
            do {
                str: string = "I LOVE YOU";
             
            }
            while (index == 1);
        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([DoWhileStmt(BinExpr(==, Id(index), IntegerLit(1)), BlockStmt([VarDecl(str, StringType, StringLit(I LOVE YOU))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 157))

    def test_case_158(self):

        input = """func: function string () {
            do {
                
                while( i - 1 == 0)
                {
                    x: integer = 10;
                }
            }
            while ( i  > 100);
        }"""
        expect = """Program([
	FuncDecl(func, StringType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(i), IntegerLit(100)), BlockStmt([WhileStmt(BinExpr(==, BinExpr(-, Id(i), IntegerLit(1)), IntegerLit(0)), BlockStmt([VarDecl(x, IntegerType, IntegerLit(10))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 158))

    def test_case_159(self):

        input = """
        func: function integer () {
            {}}
        """
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([BlockStmt([])]))
])"""
        self.assertTrue(TestAST.test(input, expect, 159))

    def test_case_160(self):

        input = """

        func: function void () {
        
        }"""
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 160))

    def test_case_161(self):

        input = """
        func: function integer () {
            
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([]))
])"""
        self.assertTrue(TestAST.test(input, expect, 161))

    def test_case_162(self):

        input = """func: function integer () {
            while (true) {
            for ( i = 0, i < 2, i + 1)
            {
                continue;
            }
            }
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([WhileStmt(BooleanLit(True), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(2)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([ContinueStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 162))

    def test_case_163(self):

        input = """func: function boolean () {
            break;
             do {
        while (i % 10 == 0) {
             x = 20;
        }
        if (n == 2) {
            return 0;
        } 
    } while (i > 100);
        }"""
        expect = """Program([
	FuncDecl(func, BooleanType, [], None, BlockStmt([BreakStmt(), DoWhileStmt(BinExpr(>, Id(i), IntegerLit(100)), BlockStmt([WhileStmt(BinExpr(==, BinExpr(%, Id(i), IntegerLit(10)), IntegerLit(0)), BlockStmt([AssignStmt(Id(x), IntegerLit(20))])), IfStmt(BinExpr(==, Id(n), IntegerLit(2)), BlockStmt([ReturnStmt(IntegerLit(0))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 163))

    def test_case_164(self):

        input = """func: function integer () {
            continue;
            do {
        while (i + 1 == 2) {
             x = 10;
        }
        if (n == 1) {
            return 0;
        } else {
            break;
        }
    } while (i - 100);
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([ContinueStmt(), DoWhileStmt(BinExpr(-, Id(i), IntegerLit(100)), BlockStmt([WhileStmt(BinExpr(==, BinExpr(+, Id(i), IntegerLit(1)), IntegerLit(2)), BlockStmt([AssignStmt(Id(x), IntegerLit(10))])), IfStmt(BinExpr(==, Id(n), IntegerLit(1)), BlockStmt([ReturnStmt(IntegerLit(0))]), BlockStmt([BreakStmt()]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 164))

    def test_case_165(self):

        input = """func: function integer () {
            while (a < 10) {
        for ( i = 0, i < 5, i - 100) {
            while (i > 2) {
                a = a[i];
            }
        }
    }
    return a;
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([WhileStmt(BinExpr(<, Id(a), IntegerLit(10)), BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(5)), BinExpr(-, Id(i), IntegerLit(100)), BlockStmt([WhileStmt(BinExpr(>, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(a), ArrayCell(a, [Id(i)]))]))]))])), ReturnStmt(Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 165))

    def test_case_166(self):

        input = """func: function integer () {
           do {
        while (b % 2 == 0) {
            b = b / 2;
        }
        for ( i = 0, i < 3, i - a) {
            if (i == b) {
                continue;
            } else {
                b = 1;
            }
        }
    } while (b > 0);
    return b;
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([DoWhileStmt(BinExpr(>, Id(b), IntegerLit(0)), BlockStmt([WhileStmt(BinExpr(==, BinExpr(%, Id(b), IntegerLit(2)), IntegerLit(0)), BlockStmt([AssignStmt(Id(b), BinExpr(/, Id(b), IntegerLit(2)))])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), IntegerLit(3)), BinExpr(-, Id(i), Id(a)), BlockStmt([IfStmt(BinExpr(==, Id(i), Id(b)), BlockStmt([ContinueStmt()]), BlockStmt([AssignStmt(Id(b), IntegerLit(1))]))]))])), ReturnStmt(Id(b))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 166))

    def test_case_167(self):

        input = """func: function integer () {
            preventDefault();
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([CallStmt(preventDefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 167))

    def test_case_168(self):

        input = """func: function float (out a: integer, b: float) {
           a = a[1];
        }"""
        expect = """Program([
	FuncDecl(func, FloatType, [OutParam(a, IntegerType), Param(b, FloatType)], None, BlockStmt([AssignStmt(Id(a), ArrayCell(a, [IntegerLit(1)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 168))

    def test_case_169(self):

        input = """func: function float () {
            readInteger();
        }"""
        expect = """Program([
	FuncDecl(func, FloatType, [], None, BlockStmt([CallStmt(readInteger, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 169))

    def test_case_170(self):

        input = """func: function integer () {
            printFloat("1+1");
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([CallStmt(printFloat, StringLit(1+1))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 170))

    def test_case_171(self):

        input = """func: function array[4] of float () {
          
               printFloat(12.1e45);
        }"""
        expect = """Program([
	FuncDecl(func, ArrayType([4], FloatType), [], None, BlockStmt([CallStmt(printFloat, FloatLit(1.21e+46))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 171))

    def test_case_172(self):

        input = """func: function integer () {
           readFloat();
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([CallStmt(readFloat, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 172))

    def test_case_173(self):

        input = """func: function boolean () {
            readBoolean();
        }"""
        expect = """Program([
	FuncDecl(func, BooleanType, [], None, BlockStmt([CallStmt(readBoolean, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 173))

    def test_case_174(self):

        input = """func: function boolean (a: boolean, b: float) {
            printBoolean(a);    
        }"""
        expect = """Program([
	FuncDecl(func, BooleanType, [Param(a, BooleanType), Param(b, FloatType)], None, BlockStmt([CallStmt(printBoolean, Id(a))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 174))

    def test_case_175(self):

        input = """func: function integer (inherit out a: integer, b: string) {
            readString();
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [InheritOutParam(a, IntegerType), Param(b, StringType)], None, BlockStmt([CallStmt(readString, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 175))

    def test_case_176(self):

        input = """func: function integer () {
        break;
        {
        
        }
            preventdefault();    
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([BreakStmt(), BlockStmt([]), CallStmt(preventdefault, )]))
])"""
        self.assertTrue(TestAST.test(input, expect, 176))

    def test_case_177(self):

        input = """
        func: function integer () {
           if (true) {
            a = 10;
            } else {
                a = 20;
 
            }
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([IfStmt(BooleanLit(True), BlockStmt([AssignStmt(Id(a), IntegerLit(10))]), BlockStmt([AssignStmt(Id(a), IntegerLit(20))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 177))

    def test_case_178(self):

        input = """
        a: integer = func(10);
        """
        expect = """Program([
	VarDecl(a, IntegerType, FuncCall(func, [IntegerLit(10)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 178))

    def test_case_179(self):

        input = """
            integers: array [5] of integer = {1, 2, 3, "a"};
        """
        expect = """Program([
	VarDecl(integers, ArrayType([5], IntegerType), ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), StringLit(a)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 179))

    def test_case_180(self):

        input = """
        func : function boolean ()
        {
            func();
            if (true == a) return 0;
        }
        """
        expect = """Program([
	FuncDecl(func, BooleanType, [], None, BlockStmt([CallStmt(func, ), IfStmt(BinExpr(==, BooleanLit(True), Id(a)), ReturnStmt(IntegerLit(0)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 180))

    def test_case_181(self):

        input = """
        func: function void ()
        {
        arr = {10.5, 20.3, 15.6, 18.9, 25.4};
        n = sizeof(arr) / sizeof(arr[0]);
         average = calculateAverage(arr, n);
        }
        """
        expect = """Program([
	FuncDecl(func, VoidType, [], None, BlockStmt([AssignStmt(Id(arr), ArrayLit([FloatLit(10.5), FloatLit(20.3), FloatLit(15.6), FloatLit(18.9), FloatLit(25.4)])), AssignStmt(Id(n), BinExpr(/, FuncCall(sizeof, [Id(arr)]), FuncCall(sizeof, [ArrayCell(arr, [IntegerLit(0)])]))), AssignStmt(Id(average), FuncCall(calculateAverage, [Id(arr), Id(n)]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 181))

    def test_case_182(self):

        input = """func: function string(str: string) {
            n = strlen(str);
            for (i = 0, i < n / 2, i + 1) {
                swap(str[i], str[n - i - 1]);
            }
            }
        """
        expect = """Program([
	FuncDecl(func, StringType, [Param(str, StringType)], None, BlockStmt([AssignStmt(Id(n), FuncCall(strlen, [Id(str)])), ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(<, Id(i), BinExpr(/, Id(n), IntegerLit(2))), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([CallStmt(swap, ArrayCell(str, [Id(i)]), ArrayCell(str, [BinExpr(-, BinExpr(-, Id(n), Id(i)), IntegerLit(1))]))]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 182))

    def test_case_183(self):

        input = """
            calculateExpApproximation: function float(n: integer) {
            result = 1.0;
            term = 1.0;
            for ( i = 1, i <= n, i + 1) {
                term = (1.0 / n);
                result = term;
            }
            return result;}"""
        expect = """Program([
	FuncDecl(calculateExpApproximation, FloatType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(result), FloatLit(1.0)), AssignStmt(Id(term), FloatLit(1.0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(term), BinExpr(/, FloatLit(1.0), Id(n))), AssignStmt(Id(result), Id(term))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 183))

    def test_case_184(self):

        input = """func: function float () {
            func();
            return expr;
        }"""
        expect = """Program([
	FuncDecl(func, FloatType, [], None, BlockStmt([CallStmt(func, ), ReturnStmt(Id(expr))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 184))

    def test_case_185(self):

        input = """calculateExpression: function string (n: integer) {
             result = 0.0;
            for (i = 1, i <= n, i+2) {
                result =  i / (i + 1);
            }
            return result;
            }
        """
        expect = """Program([
	FuncDecl(calculateExpression, StringType, [Param(n, IntegerType)], None, BlockStmt([AssignStmt(Id(result), FloatLit(0.0)), ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(2)), BlockStmt([AssignStmt(Id(result), BinExpr(/, Id(i), BinExpr(+, Id(i), IntegerLit(1))))])), ReturnStmt(Id(result))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 185))

    def test_case_186(self):

        input = """
        func: function integer () {
           
            c = true * d / 20 ;
         
        }"""
        expect = """Program([
	FuncDecl(func, IntegerType, [], None, BlockStmt([AssignStmt(Id(c), BinExpr(/, BinExpr(*, BooleanLit(True), Id(d)), IntegerLit(20)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 186))

    def test_case_187(self):

        input = """
       
                     sumNumbers: function integer( ) {
                         sum = 0;
                         i = 1;
                        do {
                            sum =  sum +i;
                            i = i + 1;
                        } while (i <= n);
                        return sum;
                    }"""
        expect = """Program([
	FuncDecl(sumNumbers, IntegerType, [], None, BlockStmt([AssignStmt(Id(sum), IntegerLit(0)), AssignStmt(Id(i), IntegerLit(1)), DoWhileStmt(BinExpr(<=, Id(i), Id(n)), BlockStmt([AssignStmt(Id(sum), BinExpr(+, Id(sum), Id(i))), AssignStmt(Id(i), BinExpr(+, Id(i), IntegerLit(1)))])), ReturnStmt(Id(sum))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 187))

    def test_case_188(self):

        input = """printNumbers: function integer (n: integer) {
        for (i = 1, i <= n, i + 10) {
          break;
        }
        }
        """
        expect = """Program([
	FuncDecl(printNumbers, IntegerType, [Param(n, IntegerType)], None, BlockStmt([ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<=, Id(i), Id(n)), BinExpr(+, Id(i), IntegerLit(10)), BlockStmt([BreakStmt()]))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 188))

    def test_case_189(self):

        input = """a: boolean = true;"""
        expect = """Program([
	VarDecl(a, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 189))

    def test_case_190(self):

        input = """a:float = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n * fact(n - 1);
        }
        inc: function void(out n: integer, delta: integer) {
            n = n + delta;
        }
       """
        expect = """Program([
	VarDecl(a, FloatType, IntegerLit(65))
	FuncDecl(fact, IntegerType, [Param(n, IntegerType)], None, BlockStmt([IfStmt(BinExpr(==, Id(n), IntegerLit(0)), ReturnStmt(IntegerLit(1)), ReturnStmt(BinExpr(*, Id(n), FuncCall(fact, [BinExpr(-, Id(n), IntegerLit(1))]))))]))
	FuncDecl(inc, VoidType, [OutParam(n, IntegerType), Param(delta, IntegerType)], None, BlockStmt([AssignStmt(Id(n), BinExpr(+, Id(n), Id(delta)))]))
])"""
        self.assertTrue(TestAST.test(input, expect, 190))

    def test_case_191(self):
        input =	"""a: integer;"""
        expect = """Program([
	VarDecl(a, IntegerType)
])"""
        self.assertTrue(TestAST.test(input, expect, 191))
    def test_case_192(self):
        input =	"""a: integer = 1;"""
        expect = """Program([
	VarDecl(a, IntegerType, IntegerLit(1))
])"""
        self.assertTrue(TestAST.test(input, expect, 192))
    def test_case_193(self):
        input =	"""a: integer = 10.0;"""
        expect = """Program([
	VarDecl(a, IntegerType, FloatLit(10.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 193))
    def test_case_194(self):
        input =	"""a: integer = "str";"""
        expect = """Program([
	VarDecl(a, IntegerType, StringLit(str))
])"""
        self.assertTrue(TestAST.test(input, expect, 194))
    def test_case_195(self):
        input =	"""a: integer = b;"""
        expect = """Program([
	VarDecl(a, IntegerType, Id(b))
])"""
        self.assertTrue(TestAST.test(input, expect, 195))
    def test_case_196(self):
        input =	"""a: boolean = foo(1);"""
        expect = """Program([
	VarDecl(a, BooleanType, FuncCall(foo, [IntegerLit(1)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 196))
    def test_case_197(self):
        input =	"""a: boolean = true;"""
        expect = """Program([
	VarDecl(a, BooleanType, BooleanLit(True))
])"""
        self.assertTrue(TestAST.test(input, expect, 197))
    def test_case_198(self):
        input =	"""a, b: boolean = 1, .e2;"""
        expect = """Program([
	VarDecl(a, BooleanType, IntegerLit(1))
	VarDecl(b, BooleanType, FloatLit(0.0))
])"""
        self.assertTrue(TestAST.test(input, expect, 198))
    def test_case_199(self):
        input =	"""a: boolean = x + 1;"""
        expect = """Program([
	VarDecl(a, BooleanType, BinExpr(+, Id(x), IntegerLit(1)))
])"""
        self.assertTrue(TestAST.test(input, expect, 199))
    def test_case_200(self):
        input =	"""a: array[100] of boolean = a[1];"""
        expect = """Program([
	VarDecl(a, ArrayType([100], BooleanType), ArrayCell(a, [IntegerLit(1)]))
])"""
        self.assertTrue(TestAST.test(input, expect, 200))
