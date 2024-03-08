import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_1(self):
        input = Program([VarDecl("a", IntegerType()), VarDecl("c", FloatType())])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 401))
    def test_2(self):
        input = Program([VarDecl("a", IntegerType(), IntegerLit(5)), VarDecl("c", AutoType())])
        expect = "Invalid Variable: c"
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test_3(self):
        input = Program([VarDecl("a", IntegerType(), IntegerLit(5)), VarDecl("c", AutoType(),BinExpr("+",IntegerLit(5),IntegerLit(5)))])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 403))
    def test_4(self):
        input = Program([VarDecl("a", IntegerType(), IntegerLit(5)), VarDecl("c", AutoType(),BinExpr("+",BooleanLit(True),IntegerLit(5)))])
        expect = "Type mismatch in expression: BinExpr(+, BooleanLit(True), IntegerLit(5))"
        self.assertTrue(TestChecker.test(input, expect, 404))
    def test_5(self):
        input = Program([VarDecl("a", IntegerType(), IntegerLit(5)), VarDecl("c", AutoType(),UnExpr('!',BooleanLit(True)))])
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 405))
    def test_6(self):
        input = Program([VarDecl("a", IntegerType(), IntegerLit(5)), VarDecl("c", AutoType(),UnExpr("*",Id("a")))])
        expect = "Type mismatch in expression: UnExpr(*, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 406))
    def test_7(self):
        input = Program([
	VarDecl("x", IntegerType(), IntegerLit(1)),
	VarDecl("y", IntegerType(), IntegerLit(2)),
	VarDecl("x", IntegerType(), IntegerLit(3))
])
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 407))
    def test_8(self):
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([]))
])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 408))
    def test_9(self):
        input = Program([FuncDecl('dbs', VoidType(), [], 'dsa', BlockStmt([]))])
        expect = "Undeclared Function: dsa" 
        self.assertTrue(TestChecker.test(input, expect, 409))
    def test_10(self):
        input = Program([VarDecl('x',FloatType()),FuncDecl('dbs',IntegerType(), [], 'dsa', BlockStmt([])),FuncDecl('abc',IntegerType(), [], 'abc', BlockStmt([AssignStmt(Id('x'),IntegerLit(5))]))])
        expect = "Undeclared Function: dsa"
        self.assertTrue(TestChecker.test(input, expect, 410)) 
    def test_11(self):
        input =""" sumNumbers: function integer( ) {
                        sum: integer = 0;
                        i: integer = 1;
                        n: integer= 10;
                        do {
                            sum =  sum +i;
                            i = i + 1;
                        } while (i <= n);
                        return sum;
                        return i;
                        if (sum + 10)
                        {
                            i = true;
                        }
                    }"""
        expect = "Type mismatch in statement: IfStmt(BinExpr(+, Id(sum), IntegerLit(10)), BlockStmt([AssignStmt(Id(i), BooleanLit(True))]))"
        self.assertTrue(TestChecker.test(input, expect, 411)) 
#     def test_12(self):
#         input = """foo1: function auto (a: integer, a: integer) inherit foo
#         {
#             super(2,3);
#             if (a == 1) return 1;
#             a = 1;
#             b= a+b;
#             a: float;
#         } 
#         foo: function void (inherit a: integer, inherit b: integer)
#         {
            
#         } """
#         expect="Redeclared Parameter: a"
#         self.assertTrue(TestChecker.test(input, expect, 412)) 
#     def test_13(self):
#         input = """ foo1: function auto (c: integer, c: integer) inherit foo
#         {
#             super(2,3);
#             if (a == 1) return 1;
#             a = 1;
#             b= a+b;
#             a: float;
#         } 
#         foo: function void (inherit a: integer, inherit b: integer)
#         {
            
#         } """
#         expect="Redeclared Parameter: c"
#         self.assertTrue(TestChecker.test(input, expect, 413)) 
#     def test_14(self):
#         input = """        r: integer;
#         foo1: function auto (a: integer, d: integer) inherit foo
#         {
#             super(2,3);
#             if (a == 1) return 1;
#             a = 1;
#             b= a+b;
#             a: float;
#         } 
#         foo: function void (inherit a: integer, inherit b: integer)
#         {
            
#         } 
#         """
#         expect="Invalid Parameter: a"
#         self.assertTrue(TestChecker.test(input, expect, 414))
#     def test_15(self):
#         input = """        arr: array[2,1] of integer = {{1},{2}};
#         m: integer;
    
#         foo1: function auto (c: integer, d: integer) inherit foo
#         {
#             super(2,3);
#             if (a == 1) return 1;
#             a = 1;
#             b = a+b;
#             r: integer;
#             r = arr[0,0.0];
 
#         } 
#         foo: function void (inherit a: integer, inherit b: integer)
#         {
            
#         } 
#         """
#         expect="Type mismatch in expression: ArrayCell(arr, [IntegerLit(0), FloatLit(0.0)])"
#         self.assertTrue(TestChecker.test(input, expect, 415)) 
#     def test_16(self):
#         input = """            
#         arr: array[2,1] of integer = {{1},{2}};
#         m: integer;

#         n: integer ;
#         foo1: function auto (c: integer, d: integer) inherit foo
#         {
#             super(2,3);
#             if (a == 1) return 1;
#             a = 1;
#             b = a+b;
#             r: integer;
#             r = arr[0,0];
 
#         } 
#         foo: function auto (inherit a: integer, inherit b: integer)
#         {
#             return a;
#         } 
#         """
#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 416))  

#     def test_17(self):
#         input ="""
      
      
#        arr: array [2,2,2,2] of integer = {
#             {
#                 { {1, 2}, {3, 4} },
#                 { {5, 6}, {7, 8} }
#             },
#             {
#                 { {9, 10}, {11, 12} },
#                 { {13, 14}, {15, 16} }
#             }
#            };
#         m: integer;

#         n: float = readInteger();
#         foo1: function auto (c: integer, d: integer) inherit foo
#         {
#             super(2.0,3);
#             printInteger(1);
#             if (b == 1) return 1;
#             a = 1;
#             a = a+b;
#             r: integer;
#             r = arr[0,0];
 
#         } 
#         foo: function auto (inherit a: float, inherit b: integer)
#         {
#             return a;
#         } 
        
# """



#         expect="Type mismatch in statement: AssignStmt(Id(r), ArrayCell(arr, [IntegerLit(0), IntegerLit(0)]))"
#         self.assertTrue(TestChecker.test(input, expect, 417))
        
#     def test_18(self):
#         input ="""
      
#       var : integer = true;
#     main: function void(){}
 
        
# """



#         expect="Type mismatch in Variable Declaration: VarDecl(var, IntegerType, BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 418))
#     def test_19(self):
#         input ="""
      
#        var : float = "hello";
#     main: function void(){}
 
        
# """



#         expect="Type mismatch in Variable Declaration: VarDecl(var, FloatType, StringLit(hello))"
#         self.assertTrue(TestChecker.test(input, expect, 419))

#     def test_20(self):
#         input ="""
      
#        var : boolean = 123;
#     main: function void(){}
 
        
# """



#         expect="Type mismatch in Variable Declaration: VarDecl(var, BooleanType, IntegerLit(123))"
#         self.assertTrue(TestChecker.test(input, expect, 420))

#     def test_21(self):
#         input ="""
#       arr: array[2,1] of integer = {{1},{2}};
#     m: integer;

#     n: integer ;
#     foo1: function auto (c: integer, d: integer) inherit foo
#     {
#         if (a == 1) return 1;
#         a = 1;
#         b = a+b;
#         r: integer;
#         r = arr[0,0];
#         return r;
#     } 
#     foo: function auto (a: integer, b: integer)
#     {
#         super(2,3);
#         return a;
#     } 
      
 
        
# """



#         expect="Invalid statement in function: foo1"
#         self.assertTrue(TestChecker.test(input, expect, 421))
#     def test_22(self):
#         input ="""
      
#       arr: array[2,1] of integer = {{1},{2}};
#     m: integer;

#     n: integer ;
#     foo1: function auto (c: integer, d: integer) inherit foo
#     {
#         if (a == 1) return 1;
#         a = 1;
#         b = a+b;
#         r: integer;
#         r = arr[0,0];
#         return r;
#     } 
#     foo: function auto ()
#     {
#         return 1;
#     } 
 
        
# """



#         expect="Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 422))
#     def test_23(self):
#         input ="""
      
      
#  arr: array[2,1] of integer = {{1},{2}};
#     m: integer;

#     n: integer ;
#     foo1: function auto (c: integer, d: integer) inherit foo
#     {
#         if (a == 1) return 1;
#         a = 1;
#         b = a+b;
#         r: integer;
#         r = arr[0,0];
#         return r;
#     } 
        
# """



#         expect="Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 423))
#     def test_24(self):
#         input ="""
      
#       arr: array[2,1] of integer = {{1},{2}};
#     m: integer;

#     n: integer ;
#     foo1: function auto (c: integer, d: integer) inherit foo
#     {
#         super(2,3);
#         if (a == 1) return 1;
#         a = 1;
#         b = a+b;
#         r: integer;
#         r = arr[0,0];
#         return r;
#     } 
#     foo: function auto ()
#     {
#         super(2,3);
#         return 1;
#     } 
 
        
# """



#         expect="Type mismatch in expression: IntegerLit(2)"
#         self.assertTrue(TestChecker.test(input, expect, 424))   
#     def test_25(self):
#         input ="""
      
#        var : string = "abc";
#         a : integer = 1;
#         func: function void(alpha : string, delta : integer){
#             b = a + 1;
#         }
#         main: function void(){}
#         func2 : function void (alpha : string, delta : integer){}
#         func3 : function void (alpha : string, delta : integer) {}
 
        
# """



#         expect="Undeclared Identifier: b"
#         self.assertTrue(TestChecker.test(input, expect, 425))
#     def test_26(self):
#         input ="""
      
#       var : integer = "abc";
#         a : integer = 1;
#         func: function void(alpha : string, delta : integer){
#             b = a + 1;
#         }
#         main: function void(){}
#         func2 : function void (alpha : string, delta : integer){}
#         func3 : function void (alpha : string, delta : integer) {}
 
        
# """



#         expect="Type mismatch in Variable Declaration: VarDecl(var, IntegerType, StringLit(abc))"
#         self.assertTrue(TestChecker.test(input, expect, 426))    
#     def test_27(self):
#         input ="""
      
#        var : string = "abc";
#         a : integer = 1;
#         func: function void(alpha : string, delta : integer){
#             a = a + 1;
#         }
#         main: function void(){
#             b = a + 2;
#         }
#         func2 : function void (alpha : string, delta : integer){}
#         func3 : function void (alpha : string, delta : integer) {}
 
        
# """



#         expect="Undeclared Identifier: b"
#         self.assertTrue(TestChecker.test(input, expect, 427))
#     def test_28(self):
#         input ="""
      
#          var : string = "abc";
#         a : integer = 1;
#         func: function void(alpha : string, delta : integer){
#             a = a + 1;
#         }
#         main: function void(){
#             a = a + 2;
#         }
#         func2 : function void (alpha : string, delta : integer){}
#         func3 : function void (alpha : string, delta : integer) {}
 
        
# """



#         expect=""
#         self.assertTrue(TestChecker.test(input, expect, 428))
#     def test_29(self):
#         input ="""
      
#       var : string = "abc";
#         a : integer = 1;
#         func: function void(alpha : string, delta : integer){
#             a = a + 1;
#         }
#         main: function void(){
#             a = a + 2;
#             b = func(alpha, delta);
#         }
#         func2 : function void (alpha : string, delta : integer){}
#         func3 : function void (alpha : string, delta : integer) {}
 
        
# """



#         expect="Type mismatch in expression: FuncCall(func, [Id(alpha), Id(delta)])"
#         self.assertTrue(TestChecker.test(input, expect, 429))
#     def test_30(self):
#         input ="""
      
#       sumNumbers: function integer() {
#             sum: integer = 0;
#             i: integer = 1;
#             n: integer= 20;
#             do {
#                 sum = sum + i;
#                 i = i + 1;
#             } while (i <= n);
#             return sum;
#         }
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 430))
#     def test_31(self):
#         input ="""
      
#        findMax: function integer(a: array[5] of integer) {
           
#             max: integer = a[0];
#             i: integer;
#             for (i=1, i<= 4, i+1)
#             {
#                 z: integer = 0;
#                 z= 10;



#                 if (a[i] > max) 
#                 {
                    
#                     return;
                    
                    
#                 }
#                     max = a[i];
               
                
#             }
#             return max;
                
            
#         }
 
        
# """











#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 431))
#     def test32(self):
#         input ="""
      
#        isEven: function boolean(n: integer) {
#             if ((n%2)==0) 
#                 return true;
#             else
#                 return false;
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 432))
#     def test_33(self):
#         input ="""
      
#       isEven: function boolean(n: integer) {
#             if (n * 2 == 0) 
#                 return true;
#             else
#                 return false;
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 433))
#     def test_34(self):
#         input ="""
#       factorial: function integer(n: integer) {
#             if (n == 0) 
#                 return 1;
#             else
#                 return n * factorial(n - 1);
#         }
      
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 434))
#     def test_35(self):
#         input ="""
#         gcd: function integer(a: integer, b: integer) {
#              r: integer = a % b;
#             while (b != 0) {
             
#                 a = b;
#                 b = r;
#             }
                
#             return a;
#         }
      
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 435))

#     def test_36(self):
#         input ="""
      
#       convertToBinary: function string(n: integer) {
#             s: string = "";
#             while (n > 0) 
#             {
#              if (n % 2 == 0) 
#                     s = "0" + s;
#                 else
#                     s = "1" + s;
#                 n = n / 2;
            
#             }
               
#             return s;
#         }
 
        
# """



#         expect="Type mismatch in expression: BinExpr(+, StringLit(0), Id(s))"
#         self.assertTrue(TestChecker.test(input, expect, 436))

#     def test_37(self):
#         input ="""
      
#        printMultiplicationTable: function void(i: integer) {
#             for (i=1, i<10,i + 1)
#              {
#                 for (j=1, j<10,j + 1)
#                     {
#                     write(i*j + " ");
#                     }
#              } 
                
#                 writeln("");
#         }
 
        
# """



#         expect="Undeclared Identifier: j"
#         self.assertTrue(TestChecker.test(input, expect, 437))
#     def test_38(self):
#         input ="""
#       fibonacci: function integer(n: integer) {
#             if (n == 0) 
#                 return 0;
#             else
#                 if (n == 1) 
#                     return 1;
#                 else
#                     return fibonacci(n - 1) + fibonacci(n - 2);
#         }
      
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 438))
#     def test_39(self):
#         input ="""
      
#        isPrime: function boolean(n: integer) {
#             if (n <= 1) 
#                 return false;
#             else
#                   for (i=1, i<10,i + 1)
#              {
#                 for (j=1, j<10,j + 1)
#                     {
#                     write(i*j + " ");
#                     }
#              }
#             return true;
#         }
    
 
        
# """



#         expect="Undeclared Identifier: i"
#         self.assertTrue(TestChecker.test(input, expect, 439))

#     def test_40(self): # xem lại testcase  này
#         input ="""
      
#       findMin: function integer(a: array[5] of integer) {
#             min: integer = a[0];
#             i: float; 
#             for (i=1,i<10,i+1)
#              {
#              if (a[i] < min) 
#                     min = a[i];
             
#              } 
                
#             return min;
#         }
 
        
# """



#         expect="Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(a, [Id(i)]), Id(min)), AssignStmt(Id(min), ArrayCell(a, [Id(i)])))]))"
#         self.assertTrue(TestChecker.test(input, expect, 440))
#     def test_41(self):
#         input ="""
      
#       foo1: function auto (a: integer, a: integer) inherit foo
#     {
#         super(2,3);
#         if (a == 1) return 1;
#         a = 1;
#         b= a+b;
#         a: float;
#     } 
#     foo: function void (inherit a: integer, inherit b: integer)
#     {
        
#     }
 
        
# """



#         expect="Redeclared Parameter: a"
#         self.assertTrue(TestChecker.test(input, expect, 441))
#     def test_42(self):
#         input ="""
      
#       foo1: function auto (a: integer, b: integer) inherit foo
#     {
#         super(2,3);
#         if (a == 1) return 1;
#         a = 1;
#         b= a+b;
#         a: float;
#     } 
#     foo: function void (a: integer, b: integer)
#     {
        
#     }
 
        
# """



#         expect="Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 442))
#     def test_43(self):
#         input ="""
      
      
#  foo1: function auto (a: integer, b: integer) inherit foo
#     {
#         super(2,3);
#         if (a == 1) return 1;
#         a = 1;
#         b= a+b;
#         a: float;
#     } 
#     foo: function void (a: integer, b: integer) inherit t
#     {
        
#     }
        
# """



#         expect="Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 443))
#     def test_44(self):
#         input ="""
      
#       foo1: function integer (a: integer, b: integer) inherit foo
#     {
#         super(2,3);
#         if (a == 1) return 1;
#         a = 1;
#         b= a+b;
#         a: float;
#         return true;
#     } 
#     foo: function void (a: integer, b: integer)
#     {
        
#     } 
 
        
# """



#         expect="Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 444))
#     def test_45(self):
#         input ="""
      
#       foo1: function integer (a: integer, b: integer) inherit foo
#     {
#         super(2,3);
#         if (a == 1) return 1;
#         a = 1;
#         b= a+b;
#         a: float;
#         return b;
#     } 
#     foo: function void (a: integer, b: integer)
#     {
#         c: integer;
#         c = foo1(3, 4);
#     }
 
        
# """



#         expect="Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 445))   
#     def test_46(self):
#         input ="""
      
#       foo1: function integer (a: integer, b: integer) inherit foo
#     {
#         super(2,3);
#         if (a == 1) return 1;
#         a = 1;
#         b= a+b;
#         a: float;
#         return b;
#     } 
#     foo: function void (a: integer, b: integer)
#     {
#         c: float;
#         c = foo1(3, 4);
#     }
 
        
# """



#         expect="Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 446))
#     def test_47(self):
#         input ="""
      
#       foo1: function integer(a: integer, b: integer) inherit foo {
#     super(2, 3);
#     if (a == 1) return 1;
#     a = 1;
#     b = a + b;
#      c: float;
#     for (b=1, b<=c, b + 2)
#     {
#      if (a==b) return 1;
#      else break;
#     }
#     return b;
# }

# foo: function void(a: integer, b: integer) {
#     // function body here
# }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 447))    
#     def test_48(self):
#         input ="""
      
#       foo1: function integer(a: integer, b: integer) inherit foo {
#             super(2, 3);
#             if (a == 1) return 1;
#             a = 1;
#             b = a + b;
#             c: float;
#             for (b=1, b<=c, b + 2)
#             {
#                 if (a==b) return 1;
#                 else break;
#             }
#             return b;
#         }
#         foo: function void(a: integer, b: integer) {
#             // function body here
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 448))
#     def test_49(self):
#         input ="""
      
#       foo1: function integer(a: integer, b: integer) inherit foo {
#             super(2, 3);
#             if (a == 1) return 1;
#             a = 1;
#             b = a + b;
#             c: float;
#             for (b=1, b<=c, b + 2)
#             {
#                 if (a==b) return 1;
#                 else break;
#             }
#             return b;
#         }
#         foo: function void(a: integer, b: integer) {
#             // function body here
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 449))
#     def test_50(self):
#         input ="""
      
#       foo1: function integer(a: integer, b: integer) inherit foo {
#             super(2, 3.1);
#             if (a == 1) return 1;
#             a = 1;
#             b = a + b;
#             c: float;
#             for (b=1, b<=c, b + 2)
#             {
#                 if (a==b) return 1;
#                 else break;
#             }
#             return b;
#         }
#         foo: function void(a: integer, b: integer) {
#             // function body here
#         }
 
        
# """



#         expect="Type mismatch in expression: FloatLit(3.1)"
#         self.assertTrue(TestChecker.test(input, expect, 450))
#     def test51(self):
#         input ="""
      
#       func1: function void(a: integer, b: float) {
#             if (a < b) {
#                 return;
#             } else {
#                 b = a;
#             }
#         }
#         func2: function void() {
#              x: integer = 1;
#              y: float = 2.0;
#             func1(x, y);
#             func1(y, x);
#         }
 
        
# """



#         expect="Type mismatch in statement: CallStmt(func1, Id(y), Id(x))"
#         self.assertTrue(TestChecker.test(input, expect, 451))
#     def test_52(self):
#         input ="""
      
#        func1: function void(a: integer, b: float) {
#             if (a < b) {
#                 return;
#             } else {
#                 b = a;
#             }
#         }
#         func2: function void() {
#             x: integer = 1;
#              y: float = 2.0;
#             func1(x, y);
#             func1(y, y);
#         }
 
        
# """



#         expect="Type mismatch in statement: CallStmt(func1, Id(y), Id(y))"
#         self.assertTrue(TestChecker.test(input, expect, 452))
#     def test53(self):
#         input ="""
      
#        func1: function void(a: integer, b: float) {
#             if (a < b) {
#                 return;
#             } else {
#                 b = a;
#             }
#         }
#         func2: function void() {
#              x: integer = 1;
#              y: string = "abc";
#             func1(x, y);
#         }
 
        
# """



#         expect="Type mismatch in statement: CallStmt(func1, Id(x), Id(y))"
#         self.assertTrue(TestChecker.test(input, expect, 453))
#     def test_54(self):
#         input ="""
      
#       func1: function void(a: integer, b: float) {
#             if (a < b) {
#                 return;
#             } else {
#                 b = a;
#             }
#         }
#         func2: function void() {
#              x: integer = 1;
#              y: float = 2.0;
#              z: boolean = true;
#             func1(x, y);
#             func1(z, y);
#         }
 
        
# """



#         expect="Type mismatch in statement: CallStmt(func1, Id(z), Id(y))"
#         self.assertTrue(TestChecker.test(input, expect, 454))
#     def test_55(self):
#         input ="""
      
#       func1: function void(a: integer, b: float) {
#             if (a < b) {
#                 return;
#             } else {
#                 b = a;
#             }
#         }
#         func2: function void() {
#              x: integer = 1;
#             func1(x);
#         }
 
        
# """



#         expect="Type mismatch in expression: CallStmt(func1, Id(x))"
#         self.assertTrue(TestChecker.test(input, expect, 455))
#     def test_56(self):
#         input ="""
      
#       func1: function void(a: integer, b: float) {
#             if (a < b) {
#                 return;
#             } else {
#                 b = a;
#             }
#         }
#         func2: function void() {
#              x: integer = 1;
#              y: float = 2.0;
#             func1(x, y, x);
#         }
 
        
# """



#         expect="Type mismatch in expression: CallStmt(func1, Id(x), Id(y), Id(x))"
#         self.assertTrue(TestChecker.test(input, expect, 456))

#     def test_57(self):
#         input ="""
      
#        func1: function void(a: integer, b: float) {
#             if (a < b) {
#                 return;
#             } else {
#                 b = a;
#             }
#         }
#         func2: function void() {
#             x: integer = 1;
#              y: float = 2.0;
#             func1(x);
#         }
 
        
# """



#         expect="Type mismatch in expression: CallStmt(func1, Id(x))"
#         self.assertTrue(TestChecker.test(input, expect, 457))

#     def test_58(self):
#         input ="""
      
#        foo1: function integer(a: integer, b: integer) inherit foo {
#             super(2, 3);
#             if (a == 1) return 1;
#             a = 1;
#             b = a + b;
#              c: float;
#             do
#             {
#                 z: integer= 10;
#             }
#             while(b==1);
#             for (b=1, b<=c, b + 2)
#             {
#             continue;
#                 if (a==b) return 1;
#                 else break;
#             }
#             return b;
#         }
#         foo: function void(a: integer, b: integer) {
#             // function body here
#         }
 
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 458))
#     def test_59(self):
#         input ="""
      
#       foo: function void() {
#             return;
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 459))
#     def test_60(self):
#         input ="""
      
#        foo: function void() {
#             x: integer = 1;
#             y: float = 2.5;
#             return;
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 460))

#     def test_61(self):
#         input ="""
      
#        foo1: function void() {
#             foo2();
#             return;
#         }

#         foo2: function void() {
#             return;
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 461))
#     def test_62(self):
#         input ="""
      
#        foo1: function void() {
#             if (1 == 1) {
#                 return;
#             }
#             return;
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 462))
#     def test_63(self):
#         input ="""
#       foo1: function void() {
#             foo2();
#             return;
#         }

#         foo2: function void() {
#             foo1();
#             return;
#         }
      
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 463))
#     def test_64(self):
#         input ="""
      
#        foo: function void(a: integer, b: integer) {
#             // function body here
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 464))
#     def test_65(self):
#         input ="""
      
      
#  foo1: function integer(a: integer, b: integer) {
#             return a + b;
#         }

#         foo2: function integer(a: integer, b: integer) {
#             x: integer = foo1(a, b);
#             return x;
#         }
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 465))
#     def test_66(self):
#         input ="""
      
#        foo1: function integer(a: integer, b: integer) {
#             x: integer = 1;
#             y: float = 2.5;
#             return a + b;
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 466))   
#     def test_67(self):
#         input ="""
      
#        foo1: function void() {
#             foo2();
#             return;
#         }

#         foo2: function void() {
#             foo3();
#             return;
#         }

#         foo3: function void() {
#             return;
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 467))
#     def test_68(self):
#         input ="""
      
      
#       foo: function integer(a: integer, b: integer) {
#             x: integer = a + b;
#             return x;
#         }
      
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 468))    
#     def test_69(self):
#         input ="""
#        foo1: function void() {
#             x: integer = 1;
#             y: float = 2.5;
#             return;
#         }

#         foo2: function integer(a: integer, b: integer) {
#             x: integer = a + b;
#             return x;
#         }
      
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 469))
#     def test_70(self):
#         input ="""
      
#        foo: function integer(a: integer, b: integer) {
#             if (a > b) {
#                 return a;
#             } else {
#                 return b;
#             }
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 470))
#     def test_71(self):
#         input ="""
      
#        foo1: function void() {
#             foo2();
#             return;
#         }

#         foo2: function void() {
#             foo1();
#             return;
#         }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 471))
#     def test_72(self):
#         input ="""
#        var : auto = "abc";
#             B : auto = 1;
#             func: function void(alpha : string, delta : integer){
#                 if(B > 0){
#                     B = 0;
#                 } else {
#                     B = 1;
#                 }
#                 i : integer;
#                 for (i = 0, i < 10 , i + 1){
#                     var : auto = "abc";
#                     c : auto = 12314;
#                     var = var :: "abc";
#                     break;
#                     continue;
#                 }
#                 z : integer;
#                 return;
#             }
#             main: function void(){}
      
 
        
# """



#         expect=""
#         self.assertTrue(TestChecker.test(input, expect, 472))
#     def test_73(self):
#         input ="""
      
#         var : auto = 5.5;
#             B : auto = 2;
#             func: function string(alpha : string, delta : integer){
#                 if(B > 1){
#                     B = 0;
#                 } else {
#                     B = 1;
#                 }
#                 i : integer;
#                 for (i = 0, i < 5 , i + 1){
#                     var : auto = "def";
#                     c : auto = 12314;
#                     var = var :: "def";
#                     break;
#                     continue;
#                 }
#                 z : string;
#                 return "Hello, World!";
#             }
#             main: function void(){}
            
 
        
# """



#         expect=""
#         self.assertTrue(TestChecker.test(input, expect, 473))
#     def test_74(self):
#         input ="""
#       var : auto = true;
#             B : auto = 0;
#             func: function void(alpha : string, delta : integer){
#                 if(B > 0){
#                     B = 0;
#                 } else {
#                     B = 1;
#                 }
#                 i : integer;
#                 for (i = 0, i < 3 , i + 1){
#                     var : auto = false;
#                     c : auto = 12314;
#                     var = var :: true;
#                     break;
#                     continue;
#                 }
#                 z : boolean;
#                 return;
#             }
#             main: function void(){}
      
 
        
# """



#         expect="Type mismatch in expression: BinExpr(::, Id(var), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 474))
#     def test_75(self):
#         input ="""
      
#       var : auto = 100;
#             B : auto = -1;
#             func: function integer(alpha : string, delta : integer){
#                 if(B > 0){
#                     B = 0;
#                 } else {
#                     B = 1;
#                 }
#                 i : integer;
#                 for (i = 0, i < 7 , i + 1){
#                     var : auto = 5.5;
#                     c : auto = 12314;
#                     var = var + 2.5;
#                     break;
#                     continue;
#                 }
#                 z : integer;
#                 return 999;
#             }
#             main: function void(){}

 
        
# """



#         expect=""
#         self.assertTrue(TestChecker.test(input, expect, 475))
#     def test_76(self):
#         input ="""
#        var : auto = "Hello";
#             B : auto = 1;
#             func: function boolean(alpha : string, delta : integer){
#                 if(B > 0){
#                     B = 0;
#                 } else {
#                     B = 1;
#                 }
#                 i : integer;
#                 for (i = 0, i < 4 , i + 1){
#                     var : auto = true;
#                     c : auto = 12314;
#                     var = var :: false;
#                     break;
#                     continue;
#                 }
#                 z : boolean;
#                 return false;
#             }
#             main: function void(){}
      
 
        
# """



#         expect="Type mismatch in expression: BinExpr(::, Id(var), BooleanLit(False))"
#         self.assertTrue(TestChecker.test(input, expect, 476))

#     def test_77(self): #????????
#         input ="""
      
#             var : auto = 3.14;
#             B : auto = 0;
#             func: function float(alpha : string, delta : integer)inherit foo{
                
#               super(1,1);
#                 i : integer;
               
#                 for (i = 0, i < 3 , i + 1){
#                  m: float;
#                     var: float = 100;
#                     c : auto = 12314;
#                     var = var + 2.5;
#                     break;
#                     continue;
#                 }
#                 z : float;
#                 return 3.141592653589793;
#             }
#             foo: function void (inherit m: integer, n:integer){}
#             main: function void(){}
 
        
# """



#         expect=""
#         self.assertTrue(TestChecker.test(input, expect, 477))

#     def test_78(self):
#         input ="""
      
#       var : auto = "abc";
#             B : auto = -1;
#             func: function void(alpha : string, delta : integer){
#                 if(B > 0){
#                     B = 0;
#                 } else {
#                     B = 1;
#                 }
#                 i : integer;
#                 for (i = 0, i < 6 , i + 1){
#                     var : auto = "abc";
#                     c : auto = 12314;
#                     var = var :: "def";
#                     break;
#                     continue;
#                 }
#                 z : integer;
#                 return;
#             }
#             main: function void(){}
 
        
# """



#         expect=""
#         self.assertTrue(TestChecker.test(input, expect, 478))
#     def test_79(self):
#         input ="""
#        var : auto = false;
#             B : auto = 1;
#             func: function void(alpha : string, delta : integer){
#                 if(B > 0){
#                     B = 0;
#                 } else {
#                     B = 1;
#                 }
#                 i : integer;
#                 for (i = 0, i < 2 , i + 1){
#                     var : auto = true;
#                     c : auto = 12314;
#                     var = var :: false;
#                     break;
#                     continue;
#                 }
#                 z : boolean;
#                 return;
#             }
#             main: function void(){}
      
 
        
# """



#         expect="Type mismatch in expression: BinExpr(::, Id(var), BooleanLit(False))"
#         self.assertTrue(TestChecker.test(input, expect, 479))
#     def test_80(self):
#         input ="""
      
#       var : auto = 999;
#             B : auto = -1;
#             func: function integer(alpha : string, delta : integer){
#                 if(B > 0){
#                     B = 0;
#                 } else {
#                     B = 1;
#                 }
#                 i : integer;
#                 for (i = 0, i < 8 , i + 1){
#                     var : auto = 5.5;
#                     c : auto = 12314;
#                     var = var + 2.5;
#                     break;
#                     continue;
#                 }
#                 z : integer;
#                 return -999;
#             }
#             main: function void(){}
 
        
# """



#         expect=""
#         self.assertTrue(TestChecker.test(input, expect, 480))

#     def test_81(self):
#         input ="""
#       var : auto = true;
#             B : auto = 0;
#             func: function boolean(alpha : string, delta : integer){
#                 if(B > 0){
#                     B = 0;
#                 } else {
#                     B = 1;
#                 }
#                 i : integer;
#                 for (i = 0, i < 5 , i + 1){
#                     var : auto = false;
#                     c : auto = 12314;
#                     var = var :: true;
#                     break;
#                     continue;
#                 }
#                 z : boolean;
#                 return true;
#             }
#             main: function void(){}
      
 
        
# """



#         expect="Type mismatch in expression: BinExpr(::, Id(var), BooleanLit(True))"
#         self.assertTrue(TestChecker.test(input, expect, 481))
#     def test_82(self):
#         input ="""
      
#     a: integer = 10;
#     b: boolean = true;

#     foo1:function integer(){
#         if b  return a;
#         else return -1;
#     }

#     foo2:function float(x: float){
#         if x > 0  return foo1() + x;
#         else return foo1() - x;
#     }

#     main:function void(){
#         writeFloat(foo2(-5));
#         writeFloat(foo2(5));
#     }
 
        
# """



#         expect="Undeclared Function: writeFloat"
#         self.assertTrue(TestChecker.test(input, expect, 482))
#     def test_83(self):
#         input ="""
      
      
#      a: integer = 10;
#     b: boolean = true;

#     foo1:function integer(){
#         if b  return a;
#         else return -1;
#     }

#     foo2:function float(x: float){
#         if x > 0  return foo1() + x;
#         else return foo1() - x;
#     }

#     main:function void(){
#          i: integer;
#         for (i = 0,i <a, i+ 1)
#          {
#          printFloat(foo2(i-5));
#          } 
            
#     }
        
# """



#         expect=""
#         self.assertTrue(TestChecker.test(input, expect, 483))
#     def test_84(self):
#         input ="""
      
#        a: integer = 10;
#     b: boolean = true;

#     foo1:function integer(){
#         if b  return a;
#         else return -1;
#     }

#     foo2:function float(x: float){
#         if x > 0  return foo1() + x;
#         else return foo1() - x;
#     }

#     main:function void(){
#          for (i = 0,i <a, i+ 1)
#          {
#          printInteger(foo2(i-5));
#          } 
#     }
 
        
# """



#         expect="Undeclared Identifier: i"
#         self.assertTrue(TestChecker.test(input, expect, 484))
#     def test_85(self):
#         input ="""
      
#        arr: array [2,2,2,2] of integer = {
#             {
#                 { {1, 2}, {3, 4} },
#                 { {5, 6}, {7, 8} }
#             },
#             {
#                 { {9, 10}, {11, 12} },
#                 { {13, 14}, {15, 16} }
#             }
#            };
#         m: integer;

#         n: float = foo(1,2);
#         foo1: function auto (c: integer, d: integer) inherit foo
#         {
#             super(2.0,3);
#             if (b == 1) return 1;
#             a = 1;
#             a = a+b;
#             r: integer;
#             r = arr[0,0];
 
#         } 
#         foo: function auto (inherit a: float, inherit b: integer)
#         {
#             return a;
#         } 
 
        
# """



#         expect="Type mismatch in statement: AssignStmt(Id(r), ArrayCell(arr, [IntegerLit(0), IntegerLit(0)]))"
#         self.assertTrue(TestChecker.test(input, expect, 485))
  
#     def test_86(self):
#         input ="""
      
      
#  foo1: function auto (c: integer, d: integer) inherit foo
# {
#     if (b == 1) return 1;
#     a = 1;
#     a = a+b;
#     return foo(2.0,3);
# } 
        
# """



#         expect="Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 486))
#     def test_87(self):
#         input ="""
      
#       foo: function auto (inherit a: float, inherit b: integer)
# {
#     return a;
# }

# foo: function auto (c: integer, d: integer)
# {
#     return c + d;
# }
 
        
# """



#         expect="Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 487))    
#     def test_88(self):
#         input ="""
      
      
#  arr: array [2,2,2,2] of integer = {
#     {
#         { {1, 2}, {3, 4} },
#         { {5, 6}, {7, 8} }
#     },
#     {
#         { {9, 10}, {11, 12} },
#         { {13, 14}, {15, 16} }
#     }
# };

# r: integer=arr[0,0];
        
# """



#         expect="Type mismatch in Variable Declaration: VarDecl(r, IntegerType, ArrayCell(arr, [IntegerLit(0), IntegerLit(0)]))"
#         self.assertTrue(TestChecker.test(input, expect, 488))
#     def test_89(self):
#         input ="""
      
#       foo: function auto (inherit a: float, inherit b: integer)
# {
#     return a;
# }

# m: integer = foo(1,2);
 
        
# """



#         expect="Type mismatch in Variable Declaration: VarDecl(m, IntegerType, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]))"
#         self.assertTrue(TestChecker.test(input, expect, 489))
#     def test_90(self):
#         input ="""
      
#       arr: array [2,2,2,2] of integer = {
#     {
#         { {1, 2}, {3, 4} },
#         { {5, 6}, {7, 8} }
#     },
#     {
#         { {9, 10}, {11, 12} },
#         { {13, 14}, {15, 16} }
#     }
# };

# r: integer;
# r: float;
 
        
# """



#         expect="Redeclared Variable: r"
#         self.assertTrue(TestChecker.test(input, expect, 490))
#     def test_91(self):
#         input ="""
      
#       foo: function auto ()
# {
#     if (1 > 2) return 1;
# }
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 491))
#     def test_92(self):
#         input ="""
      
#       foo: function auto ()
# {
#     continue;
# }
 
        
# """



#         expect="Must in loop: ContinueStmt()"
#         self.assertTrue(TestChecker.test(input, expect, 492))
   
#     def test_93(self):
#         input ="""
      
#       foo: integer = foo();
 
        
# """



#         expect="Undeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 493))
#     def test_94(self):
#         input ="""
      
      
#  arr: array [1,5] of integer;
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 494))
#     def test_95(self):
#         input ="""
#          a: integer = 5;
#     b: float = 3.14;
#     c: boolean = true;
#     d: string = "hello";
#     e: array [5] of integer = {1, 2, 3, 4, 5};
#     f: array [2, 3] of boolean = {{true, false, true}, {false, true, false}};

#     x: integer = a + e[2] * 2;
#     y: float = b / x;
  
      
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 495))

#     def test_96(self):
#         input ="""
#         b: float = 2.5;
#     c: boolean = false;
#     d: string = "world";
#     e: array [3] of integer = {7, 8, 9};
#     f: array [2, 2] of boolean = {{true, false}, {false, true}};

#     x: integer = a + e[1] * 3;
#     y: float = b * x;
      
 
        
# """



#         expect="Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 496))

#     def test_97(self):
#         input ="""
      
      
#  b: float = 1.5;
#     c: boolean = true;
#     d: string = "hello";
#     e: array [4] of integer = {2, 4, 6, 8};
#     f: array [3, 3] of boolean = {{true, false, true}, {false, true, false}, {true, true, false}};

#     x: integer = a + e[3] * 2;
#     y: float = b / x;
        
# """



#         expect="Undeclared Identifier: a"
#         self.assertTrue(TestChecker.test(input, expect, 497))
#     def test_98(self):
#         input ="""
      
#       a: integer = 0;
#     b: float = 1.0;
#     c: boolean = false;
#     d: string = "world";
#     e: array [5] of integer = {5, 4, 3, 2, 1};
#     f: array [2, 2] of boolean = {{false, true}, {true, false}};

#     x: integer = a + e[0] * 2;
#     y: float = b * x;
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 498))
#     def test_99(self):
#         input ="""
      
#         a: integer = 7;
#     b: float = 2.0;
#     c: boolean = true;
#     d: string = "hello";
#     e: array [6] of integer = {1, 3, 5, 7, 9, 11};
#     f: array [3, 2] of boolean = {{false, true}, {true, false}, {false, true}};

#     x: integer = a + e[4] * 2;
 
        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 499))

#     def test_100(self):
#         input ="""
      
      
#     a: integer = 6;
#     b: float = 0.2;
#     c: boolean = true;
#     d: string = "hello";
#     e: array [5] of integer = {5, 3, 1, -1, -3};
#     f: array [3, 3] of boolean = {{false, true, false}, {true, false, true}, {false, true, false}};

        
# """



#         expect="No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 500))
   
# # Testcases of Hieu Kien
#     def test_400 (self):
#         input = """
#         foo1: function void (c: integer) inherit foo
#         {
#             super(b, c);
#         }
#         foo: function void (a: integer, inherit b: auto) {
        
#         }
#         foo2: function void (x: integer) inherit foo1
#         {
#             super(b);
#         }
#         main: function void() {
        
#         }"""
#         expect = "Undeclared Identifier: b"
#         self.assertTrue(TestChecker.test(input, expect, 400))
#     def test_401 (self):
#         input = """
#         a: integer = foo(1, 2) + 1;
#         foo: function auto (a: auto, b: auto)
#         {
#             return a + b;
#         }"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 401))
#     def test_402 (self):
#         input = input = """i, j, t: string = \"20\", \"30\", \"40\";
#         main: function void()
#         {
#             k = j :: (i :: t);
#             printString(k);
#         }"""
#         expect = "Undeclared Identifier: k"
#         self.assertTrue(TestChecker.test(input, expect, 402))
#     def test_403 (self):
#         input = """x: integer = 65;
#         fact: function integer (n: integer) {
#             if (n == 0) return 1;
#             else return n * fact(n - 1);
#         }
#         inc: function void(out n: integer, delta: integer) {
#             n = n + delta;
#         }
#         main: function void() {
#             delta: integer = fact(3);
#             inc(x, delta);
#             printInteger(x);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 403))
#     def test_404 (self):
#         input = """
#         foo: function integer (inherit x: integer, y: integer)
#         {
            
#         }
#         foo1: function integer(z: string) inherit foo
#         {
#             super(x, y);
#         }
#         main: function void() {
        
#         }"""
#         expect = "Undeclared Identifier: y"
#         self.assertTrue(TestChecker.test(input, expect, 404))
#     def test_405 (self):
#         input = """x, y: boolean = true, foo(1, 2);
#         foo: function auto (x: auto, y: integer)
#         {
#             return x == y;
#         }
#         goo: function void(a: auto)
#         {
            
#         }
#         main: function void() {
#             goo(2018);
#             goo(3.75);
#         }"""
#         expect = "Type mismatch in statement: CallStmt(goo, FloatLit(3.75))"
#         self.assertTrue(TestChecker.test(input, expect, 405))
#     def test_406 (self):
#         input = """
#         foo: function auto (a: auto, b: integer)
#         {
#             a = a + b;
#             return a;
#         }
#         main: function void() {
#             x: integer = foo(1.7, 2);
#         }"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, [FloatLit(1.7), IntegerLit(2)]))"
#         self.assertTrue(TestChecker.test(input, expect, 406))
#     def test_407 (self):
#         input = """
#         foo: function auto (a: auto, b: integer)
#         {
#             a = a + b;
#             return a;
#         }
#         goo: function void()
#         {
#             x: integer = foo(1.7, 2);
#         }
#         main: function void() {
        
#         }"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(x, IntegerType, FuncCall(foo, [FloatLit(1.7), IntegerLit(2)]))"
#         self.assertTrue(TestChecker.test(input, expect, 407))
#     def test_408 (self):
#         input = """
#         foo: function auto (a: auto, b: integer)
#         {
#             a = a + b;
#             return a;
#         }
#         goo: function void() inherit foo
#         {
#             a: integer = 1;
#             super(1, 2);
#         }
#         main: function void() {
        
#         }"""
#         expect = "Invalid statement in function: goo"
#         self.assertTrue(TestChecker.test(input, expect, 408))
#     def test_409 (self):
#         input = """
#         inc : function void (out n : integer, a: float) inherit foo {} 
#         foo : function auto (inherit n: float, n: integer){} 
#         main: function void()
#         {
        
#         }"""
#         expect = "Redeclared Parameter: n"
#         self.assertTrue(TestChecker.test(input, expect, 409))
#     def test_410 (self):
#         input = """
#         foo: function void (inherit a: integer, a: float) inherit bar {}
#         main: function void()
#         {
        
#         }"""
#         expect = "Undeclared Function: bar"
#         self.assertTrue(TestChecker.test(input, expect, 410))
#     def test_411 (self):
#         input = """
#         foo: function void() inherit foo1{
#             super("HCMUT", true);
#             x = 7;
#         }
#         foo1: function void (inherit x: string, inherit x: boolean) {}
#         main: function void() {}"""
#         expect = "Redeclared Parameter: x"
#         self.assertTrue(TestChecker.test(input, expect, 411))
#     def test_412 (self):
#         input = """
#         foo: function integer() {
#             foo: integer = 2018;
#         }
#         main: function void() {
# 	        foo: integer = foo();
#         }
#         """
#         expect = "Type mismatch in expression: FuncCall(foo, [])"
#         self.assertTrue(TestChecker.test(input, expect, 412))
#     def test_413 (self):
#         input = """
#         foo: function auto (a: auto, b: integer)
#         {
#             return a + b;
#         }
#         a: integer = foo(1, 2) + 1;
#         main: function void() {
#             a = foo(1.1, 2);
#         }"""
#         expect = "Type mismatch in expression: FuncCall(foo, [FloatLit(1.1), IntegerLit(2)])"
#         self.assertTrue(TestChecker.test(input, expect, 413))
#     def test_414 (self):
#         input = """
#         x: auto = x + 4.7;
#         foo: function void(a: integer) {}
#         main: function void() {
#             foo(x);
#         }"""
#         expect = "Type mismatch in statement: CallStmt(foo, Id(x))"
#         self.assertTrue(TestChecker.test(input, expect, 414))
#     def test_415 (self):
#         input = """
#         foo: function void(a: integer) {}
#         foo: integer = 2;
#         main: function void() {
        
#         }"""
#         expect = "Redeclared Variable: foo"
#         self.assertTrue(TestChecker.test(input, expect, 415))
#     def test_416 (self):
#         input = """
#         foo: function void (b: integer) inherit a {
#             preventDefault();
#         }
#         a: function string (inherit c: string) {}
#         a: integer = 1;
#         main: function void() {}"""
#         expect = "Redeclared Variable: a"
#         self.assertTrue(TestChecker.test(input, expect, 416))
#     def test_417 (self):
#         input = """
#         foo: function auto (a: integer) {
#             if (a < 10)
#             {
#                 return a;
#             }
#             else
#             {
#                 return 3.25;
#             }
#         }
#         main: function void() {}
#         """
#         expect = "Type mismatch in statement: ReturnStmt(FloatLit(3.25))"
#         self.assertTrue(TestChecker.test(input, expect, 417))
#     def test_418 (self):
#         input = """
#         main: function void(){
#             a: integer = func1() + 2.2;
#         }
#         func1: function auto(){
#             return "string";
#         }
#         """
#         expect = "Type mismatch in statement: ReturnStmt(StringLit(string))"
#         self.assertTrue(TestChecker.test(input, expect, 418))
#     def test_419 (self):
#         input = """
#         main: function void(){
#             a: integer = func1() + 2;
#         }
#         func1: function auto() inherit foo {
#             return 0;
#         }
#         foo: function integer(){
#             return 1;
#         }
#         """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 419))
#     def test_420 (self):
#         input = """
#         func1: function auto() inherit foo {
#             super(20);
#             x: integer = 20;
#         }
#         foo: function integer(inherit x: integer) {
            
#         }
#         main: function void(){
#             a: integer = func1() + 2;
#         }"""
#         expect = "Redeclared Variable: x"
#         self.assertTrue(TestChecker.test(input, expect, 420))
#     def test_421 (self):
#         input = """
#         func1: function auto(a: integer) inherit foo {
#             super(20);
#             return a;
#         }
#         foo: function integer(inherit x: integer) {
            
#         }
#         main: function void(){
#             a: integer = func1() + 2;
#         }"""
#         expect = "Type mismatch in expression: FuncCall(func1, [])"
#         self.assertTrue(TestChecker.test(input, expect, 421))
#     def test_422 (self):
#         input = """
#         fact: function integer (n: integer) {
#             fact(2018);
#         }
#         main: function void() {
#             delta: integer = fact(3);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 422))
#     def test_423 (self):
#         input = """
#         fact: function integer (n: integer) {
#             if (n <= 1)
#             {
#                 return 1;
#             }
#             return fact(n - 1) + fact(n - 2);
#         }
#         main: function void() {
#             delta: integer = fact(3);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 423))
#     def test_424 (self):
#         input = """
#         foo: function auto () {
#             return 2018;
#         }
#         main: function void() {
#             delta: integer = foo();
#             printInteger(delta);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 424))
#     def test_425 (self):
#         input = """
#         x: boolean = true;
#         foo: function auto () {
#             return x;
#         }
#         main: function void() {
#             delta: integer = foo();
#             printInteger(delta);
#         }"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(delta, IntegerType, FuncCall(foo, []))"
#         self.assertTrue(TestChecker.test(input, expect, 425))
#     def test_426 (self):
#         input = """
#         x: boolean = true;
#         foo: function auto () {
#             return x;
#         }"""
#         expect = "No entry point"
#         self.assertTrue(TestChecker.test(input, expect, 426))
#     def test_427 (self):
#         input = """
#         x: integer = 3;
#         a: integer = readInteger();
#         fact: function integer() 
#         {
            
#         }
#         foo: function auto () {
#             return a;
#         }
#         main: function void() {
#             x = foo();
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 427))
#     def test_428 (self):
#         input = """
#         foo : function void (a : auto){}                  // Line 1
#         main : function void () {
#             foo(true);                                    // Line 3
#             goo();                                        // Line 4
#         }
#         goo : function void (){                           // Line 6                    
#             foo(3);                                       // Line 7
#         } """
#         expect = "Type mismatch in statement: CallStmt(foo, IntegerLit(3))"
#         self.assertTrue(TestChecker.test(input, expect, 428))
#     def test_429 (self):
#         input = """
#         foo: function void (a : auto) {}
#         main: function void () {
#             foo(2018);
#             goo();
#         }
#         goo: function void (){                    
#             foo(3);
#         } """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 429))
#     def test_430 (self):
#         input = """
#         foo: function void (a: auto) inherit goo {
#             preventDefault();
#         }
#         main: function void () {
#             foo(2018);
#             goo(20);
#         }
#         goo: function void (inherit a: integer){                 
#             foo(3);
#         } """
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 430))
#     def test_431 (self):
#         input = """
#         foo: function void (a: auto) inherit goo {
#             preventDefault();
#             b = b + 1;
#         }
#         main: function void () {
#             foo(2018);
#             goo(20, 1998);
#         }
#         goo: function void (inherit a: integer, inherit b: integer){                 
#             foo(3);
#         } """
#         expect = "Undeclared Identifier: b"
#         self.assertTrue(TestChecker.test(input, expect, 431))
#     def test_432 (self):
#         input = """
#         a: array [3, 2] of integer = {{1, "2"}, {1, 2}, {1, 2}};
#         main: function void () {
            
#         }"""
#         expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), StringLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
#         self.assertTrue(TestChecker.test(input, expect, 432))
#     def test_433 (self):
#         input = """
#         foo: function integer(a: auto)
#         {
#             if (a < 20)
#             {
#                 return 1;
#             }
#             return 2.7;
#         }
#         main: function void () {
            
#         }"""
#         expect = "Type mismatch in statement: ReturnStmt(FloatLit(2.7))"
#         self.assertTrue(TestChecker.test(input, expect, 433))
#     def test_434 (self):
#         input = """
#         foo: function integer(a: auto) inherit foo1
#         {
#             preventDefault();
#             if (a < 20)
#             {
#                 x: integer = 5;
#                 return x;
#             }
#             return 3;
#         }
#         foo1: function integer(inherit x: integer)
#         {
#             preventDefault();
#         }
#         main: function void () {
            
#         }"""
#         expect = "Invalid statement in function: foo1"
#         self.assertTrue(TestChecker.test(input, expect, 434))
#     def test_435 (self):
#         input = """
#         foo: function integer(a: auto) inherit foo1
#         {
#             preventDefault();
#             x: integer = 20;
#             if (a < 20)
#             {
#                 x: integer = 5;
#                 return x;
#             }
#             return x;
#         }
#         foo1: function integer(inherit x: integer)
#         {
            
#         }
#         main: function void () {
            
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 435))
#     def test_436 (self):
#         input = """
#         main : function void() inherit foo {
#             super(1.0, 2.0, 3.0);
#             z: integer = foo(1, 2, 3) + 1;
#             x = "abc";
#             y = true;
#         }
#         foo : function auto(inherit x: auto, inherit y: auto, z: auto){
#             return x + y + z;
#         }"""
#         expect = "Type mismatch in statement: ReturnStmt(BinExpr(+, BinExpr(+, Id(x), Id(y)), Id(z)))"
#         self.assertTrue(TestChecker.test(input, expect, 436))
#     def test_437 (self):
#         input = """
#         main:function void() inherit foo {
#             super(12);
#             x:auto = foo(1);
#             foo2();
#             arr: array[2,2] of integer = {{1, 2.7}, {1,2}};
#             arr[1,2] = 1;
#         }
#         foo:function float (x: integer){
#             return x + 1.2;
#         }
#         foo2: function void(){}"""
#         expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(1), FloatLit(2.7)]), ArrayLit([IntegerLit(1), IntegerLit(2)])])"
#         self.assertTrue(TestChecker.test(input, expect, 437))
#     def test_438 (self):
#         input = """
#         foo : function void() {}
#         foo : function auto ( a : integer , b : integer ) inherit bar {}
#         main: function void() {}"""
#         expect = "Redeclared Function: foo"
#         self.assertTrue(TestChecker.test(input, expect, 438))
#     def test_439 (self):
#         input = """
#         a: auto = foo(1, 2);
#         foo: function auto() { }
#         main: function void() {}"""
#         expect = "Type mismatch in expression: FuncCall(foo, [IntegerLit(1), IntegerLit(2)])"
#         self.assertTrue(TestChecker.test(input, expect, 439))
#     def test_440 (self):
#         input = """
#         x: auto = {4,5,6};
#         y: auto = x[1,2];
#         main: function void() {}"""
#         expect = "Type mismatch in expression: ArrayCell(x, [IntegerLit(1), IntegerLit(2)])"
#         self.assertTrue(TestChecker.test(input, expect, 440))
#     def test_441 (self):
#         input = """
#         foo: function float (out z: auto, t: auto)
#         {
#             z = 5;
#             return z + t;
#         }
#         main: function void() {
#             a: auto = foo(2.0, 2);
#             b: auto = foo(3.0, 1);
#             c: float = a + b;
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 441))
#     def test_442 (self):
#         input = """
#         foo: function boolean (n: integer)
#         {
#             if (n < 2)
#             {
#                 return false;
#             }
#             if (n % 2 == 0)
#             {
#                 return n == 2;
#             }
#             i: integer;
#             for (i = 2, i * i <= n, 1)
#             {
#                 if (n % i == 0)
#                 {
#                     return false;
#                 }
#             }
#             return true;
#         }
#         main: function void() {
#             n: integer = readInteger();
#             printBoolean(foo(n));
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 442))
#     def test_443 (self):
#         input = """
#         main: function void() {
#             n: integer = readInteger();
#             printBoolean(foo(n));
#         }
#         foo: function void(n: integer) {}"""
#         expect = "Type mismatch in expression: FuncCall(foo, [Id(n)])"
#         self.assertTrue(TestChecker.test(input, expect, 443))
#     def test_444 (self):
#         input = """
#         main: function void() {
#             n: integer = readInteger();
#             if (foo(n))
#             {
#                 printInteger(n);
#             }
#             else
#             {
#                 printInteger(1 + n);
#             }
#         }
#         foo: function boolean(n: integer) {}"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 444))
#     def test_445 (self):
#         input = """
#         main: function void() {
#             n: float = readInteger();
#             if (foo(n) && foo(n + 1))
#             {
#                 printInteger(n);
#             }
#             else
#             {
#                 printInteger(1 + n);
#             }
#         }
#         foo: function boolean(n: float) {}"""
#         expect = "Type mismatch in statement: CallStmt(printInteger, Id(n))"
#         self.assertTrue(TestChecker.test(input, expect, 445))
#     def test_446 (self):
#         input = """
#         foo: function auto(a: auto, b: string) inherit bar {
#             super(1, a, bar()); // 1
#         }
#         bar: function auto (x: auto, y: boolean, z: float) {}
#         main: function void() {}"""
#         expect = "Type mismatch in expression: FuncCall(bar, [])"
#         self.assertTrue(TestChecker.test(input, expect, 446))
#     def test_447 (self):
#         input = """
#         foo: integer = 2018;
#         foo1: function auto()
#         {
#             return foo;
#         }
#         main: function void()
#         {
#             foo: auto = foo1();
#             printBoolean(foo);
#         }"""
#         expect = "Type mismatch in statement: CallStmt(printBoolean, Id(foo))"
#         self.assertTrue(TestChecker.test(input, expect, 447))
#     def test_448(self):
#         input = """i, j, k: integer = 20, 30, 40;
#         main: function void()
#         {
#             i = j + k;
#             printInteger(i);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 448))
#     def test_449(self):
#         input = """i, j, k: float = 2.75, 1.98, 3.17;
#         main: function void()
#         {
#             t = i + j + k;
#             printFloat(t);
#         }"""
#         expect = """Undeclared Identifier: t"""
#         self.assertTrue(TestChecker.test(input, expect, 449))
#     def test_450(self):
#         input = """i, j: string = \"Baba\", \"Mama\";
#         main: function void()
#         {
#             k = j :: i;
#             t = (k :: j) :: i;
#             l = k :: (j :: i);
#             printString(t);
#             printString(l);
#         }"""
#         expect = """Undeclared Identifier: k"""
#         self.assertTrue(TestChecker.test(input, expect, 450))
#     def test_451(self):
#         input = """main: function void(){
#             a[3 + 5, 2 * x] = y[4] - 7;
#             return;
#         }"""
#         expect = """Undeclared Variable: a"""
#         self.assertTrue(TestChecker.test(input, expect, 451))
#     def test_452(self):
#         input = """
#         a: integer = 20;
#         a: function void() {
#             x: integer = 3;
#         }"""
#         expect = """Redeclared Function: a"""
#         self.assertTrue(TestChecker.test(input, expect, 452))
#     def test_453(self):
#         input = """main: function void(){
#             i: integer = 3;
#             do
#             {
#                 i = i + 1;
#             }   
#             while (i < 200);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 453))
#     def test_454(self):
#         input = """main: function void(){
#             i: integer = 3;
#             do {
#                 i = i + 1;
#             } while (i < 20);
#             printInteger(i);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 454))
#     def test_455(self):
#         input = """a: array[3] of float = {1, 2, 3};
#         main: function void() {
            
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 455))
#     def test_456(self):
#         input = """foo: function void () inherit bar {
#             if (a < b)
#                 if (c < d)
#                     printString("True");
#                 else
#                     printString("False");
#         }
#         main: function void() {}
#         bar: integer = 2;"""
#         expect = """Undeclared Function: bar"""
#         self.assertTrue(TestChecker.test(input, expect, 456))
#     def test_457(self):
#         input = """main: function auto () { return; }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 457))
#     def test_458(self):
#         input = """x: integer = 2018;
#         fact: function integer (n: integer) {
#             if (n == 0) return 1;
#             else return n * fact(n - 1);
#         }
#         decr: function void(out n: integer, delta: integer) {
#             n = n - delta;
#         }
#         main: function void() {
#             delta: integer = fact(3_2);
#             decr(x, delta);
#             printInteger(x);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 458))
#     def test_459(self):
#         input = """main: function void () {
#             a: array [2, 2] of float;
#             i, j: integer;
#             for (i = 0, i < 2, i + 1) {
#                 for (j = 0, j < 2, j + 1) {
#                     a[i, j] = readFloat();
#                 }
#             }
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 459))
#     def test_460(self):
#         input = """main: function void () {
#             a: array [2, 2] of float;
#             i, j: integer;
#             for (i = 0, i < 2, i + 1) {
#                 for (j = 0, j < 2, j + 1) {
#                     a[i, j] = readFloat();
#                 }
#             }
#             for (i = 0, i < 2, i + 1) {
#                 for (j = 0, j < 2, j + 1) {
#                     printFloat(a[i, j]);
#                 }
#             }
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 460))
#     def test_461(self):
#         input = """x: integer = 2018;
#         fibo: function integer (n: integer) {
#             if (n <= 1) return 1;
#             else return fibo(n - 1) + fibo(n - 2);
#         }
#         decr: function void(out n: integer, delta: integer) {
#             n = n - delta;
#         }
#         main: function void() {
#             delta: integer = fibo(100);
#             decr(x, delta);
#             printInteger(x);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 461))
#     def test_462(self):
#         input = """main: function void() {
#             a[0] = b[2, 3] + foo(2) + (b[0, 1] + goo(1));
#             return;
#         }"""
#         expect = """Undeclared Variable: a"""
#         self.assertTrue(TestChecker.test(input, expect, 462))
#     def test_463(self):
#         input = """a: integer = foo();
#         foo: function string() { }
#         main: function void() {}"""
#         expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, FuncCall(foo, []))"""
#         self.assertTrue(TestChecker.test(input, expect, 463))
#     def test_464(self):
#         input = """a : integer = foo(1, 2);
#         foo : function float (a : auto, b: auto) {
#             a = "abc";
#             b = "bcd";
#             return a + b;
#         }
#         main: function void() {}"""
#         expect = """Type mismatch in statement: AssignStmt(Id(a), StringLit(abc))"""
#         self.assertTrue(TestChecker.test(input, expect, 464))
#     def test_465(self):
#         input = """a : integer = foo(1, 2);
#         foo : function integer (a : auto, b: auto) {
#             x: auto = a + b;
#             return x;
#         }
#         main: function void() {}"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 465))
#     def test_466(self):
#         input = """a: auto;
#         main: function void() {}"""
#         expect = """Invalid Variable: a"""
#         self.assertTrue(TestChecker.test(input, expect, 466))
#     def test_467(self):
#         input = """x: integer;
#         y: float;
#         z: boolean;
#         goo: function void(x: integer, y: float) {
        
#         }
#         t: array[10] of float;
#         foo: function auto() {
            
#         }
#         a: string = \"Hello World\";"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 467))
#     def test_468(self):
#         input = """
#         x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
#         y: auto = x[0, 1+1-0];
#         main: function void() {
            
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 468))
#     def test_469(self):
#         input = """
#         goo: function void(a: auto, b: auto)
#         {
#             x: string = a + b;
#         }
#         main: function void() {}
#         foo1: function void(inherit out a: integer) inherit foo {
#             super(x, y, z);
#         }"""
#         expect = """Type mismatch in Variable Declaration: VarDecl(x, StringType, BinExpr(+, Id(a), Id(b)))"""
#         self.assertTrue(TestChecker.test(input, expect, 469))
#     def test_470(self):
#         input = """foo: function integer () {return 1;}
#         x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
#         y: auto = x[1, foo()];"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 470))
#     def test_471(self):
#         input = """x: array [1,2,3] of integer = {{{1, 2, 3}, {4, 5, 6}}};
#         y: auto = x[2 < 3];
#         main: function void() {}"""
#         expect = """Type mismatch in expression: BinExpr(<, IntegerLit(2), IntegerLit(3))"""
#         self.assertTrue(TestChecker.test(input, expect, 471))
#     def test_472(self):
#         input = """
#         a: function integer (a: integer)
#         {
#             if (a <= 1)
#             {
#                 return a;
#             }
#             return a(a - 1) + a(a - 2);
#         }
#         main: function void()
#         {
#             printInteger(a(2018));
#         }"""
#         expect = """Type mismatch in expression: FuncCall(a, [BinExpr(-, Id(a), IntegerLit(1))])"""
#         self.assertTrue(TestChecker.test(input, expect, 472))
#     def test_473(self):
#         input = """
#         a: float = foo(1, 2) + 1.5;
#         foo: function auto(a: integer, b: integer) {
#             return a + b; 
#         }
#         main: function void() {}"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 473))
#     def test_474(self):
#         input = """
#         main: function void () {
#             a: integer = foo();//1
#             b: float = "Error";//2
#         }
#         foo: function auto() {
#             c: float = "Error";//3
#             if("Error")//4
#                 return 123;//5
#             else
#                 return 456;//6
#             return "123"; //7
#         }"""
#         expect = "Type mismatch in Variable Declaration: VarDecl(c, FloatType, StringLit(Error))"
#         self.assertTrue(TestChecker.test(input, expect, 474))
#     def test_475(self):
#         input = """
#         func1: function auto (d: integer, c: integer, e: auto) {
#             g: integer = -e;
#             f: integer = e;
#         }
#         main: function void () {
#             a: integer = func1(2, 3, 2.9);
#         }"""
#         expect = """Type mismatch in Variable Declaration: VarDecl(g, IntegerType, UnExpr(-, Id(e)))"""
#         self.assertTrue(TestChecker.test(input, expect, 475))
#     def test_476(self):
#         input = """foo: function void(b: auto, c: auto)
#         {
#             a: integer = b + c == c;
#         }
#         main: function void() {}"""
#         expect = """Type mismatch in Variable Declaration: VarDecl(a, IntegerType, BinExpr(==, BinExpr(+, Id(b), Id(c)), Id(c)))"""
#         self.assertTrue(TestChecker.test(input, expect, 476))
#     def test_477(self):
#         input = """foo: function void (a: integer, b: integer, c: integer) {
#             printInteger(a + 2 * b + 3 * c);
#         }
#         main: function void() {
#             foo(2, 3, 4);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 477))
#     def test_478(self):
#         input = """foo: function void (a: integer, b: integer) {
#             c: integer = 2018;
#             printInteger(a + 2 * b + 3 * c);
#         }
#         main: function void() {
#             foo(2, 3);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 478))
#     def test_479(self):
#         input = """
#         foo: function auto (b: integer, b: float) { 
# 	        return 3;
# 	        return "hello";
# 	        a: string = 123;
#         }
#         main: function void() {}"""
#         expect = "Redeclared Parameter: b"
#         self.assertTrue(TestChecker.test(input, expect, 479))
#     def test_480(self):
#         input = """foo: function void (a: integer, b: integer) {
#             i: integer;
#             for (i = a, i <= b, i + 1) {
#                 c: integer = a + i;
#                 printInteger(c);
#             }
#         }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 480))
#     def test_481(self):
#         input = """foo: function void () {
#             do
#             {
#                 printInteger(1);
#             }   
#             while (true);
#         }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 481))
#     def test_482(self):
#         input = """foo: function void () {
#             while (true)
#                 break;
#             return;
#         }
#         main: function void() {
            
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 482))
#     def test_483(self):
#         input = """foo: function void () {
#             if (true) {
#                 if (!true) {
                    
#                 }
#                 else return;
#             }
#             return;
#         }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 483))
#     def test_484(self):
#         input = """foo: function void () {
#             if (!true) {
#                 if (true) {
#                     a: integer = 10;
#                     a = a + 1;
#                     return;
#                 }
#                 else
#                     return;
#             }
#             else {
#                 a: integer = 1;
#                 while (a < 20)
#                     a = a + 1;
#                 printInteger(a);
#             }
#         }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 484))
#     def test_485(self):
#         input = """foo: function array [10] of integer(a: array [10] of integer) {
#             i: integer;
#             for (i = 0, i < 10, i + 1) {
#                 a[i] = a[i] * 2 + 1;
#             }
#             return a;
#         }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 485))
#     def test_486(self):
#         input = """foo: function void (out N: integer, i: integer) {
#             j: integer;
#             for (j = 0, j < i, j + 1) {
#                 if (N % j == 0) {
#                     N = N - j;
#                 }
#             }
#         }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 486))
#     def test_487(self):
#         input = """foo1: function void (out N: integer, i: integer) {
#             N = N * i;
#         }
#         main: function void() {
#             N: integer = 2018;
#             foo1(N, 3);
#             printInteger(N);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 487))
#     def test_488(self):
#         input = """foo1: function void (out s: string, N: integer) {
#             i: integer;
#             for (i = 0, i < N, i + 1) {
#                 temp: string = s[N - i - 1];
#                 s[N - i - 1] = s[i];
#                 s[i] = temp;
#             }
#         }
#         main: function void() {}"""
#         expect = """Type mismatch in expression: ArrayCell(s, [BinExpr(-, BinExpr(-, Id(N), Id(i)), IntegerLit(1))])"""
#         self.assertTrue(TestChecker.test(input, expect, 488))
#     def test_489(self):
#         input = """
#         inc : function void (a : integer) inherit foo{
#             super("aa",2);
#             a = 1::2;
#         }
#         foo : function auto (inherit n: float, inherit n: integer){

#         }
#         main: function void() {
            
#         }"""
#         expect = """Redeclared Parameter: n"""
#         self.assertTrue(TestChecker.test(input, expect, 489))
#     def test_490(self):
#         input = """
#         test1 : function string(y : auto) {
#             y = 2; // line 2
#             return "";
#         }
#         main: function void () {
#             x: string = test1(true); // line 6
#         }"""
#         expect = """Type mismatch in statement: AssignStmt(Id(y), IntegerLit(2))"""
#         self.assertTrue(TestChecker.test(input, expect, 490))
#     def test_491(self):
#         input = """foo: function boolean (inherit out a: integer, b: float) inherit goo {}
#         main: function void() {}"""
#         expect = """Undeclared Function: goo"""
#         self.assertTrue(TestChecker.test(input, expect, 491))
#     def test_492(self):
#         input = """foo: function boolean (a: integer, b: float) {
#             i: integer;
#             for (i = 0, i < 5, i + 1) {
#                 x, y, z: integer = 10, 20, 30;
#                 return (x + a + y + b) > (y + a + z + b);
#             }
#         }
#         main: function void() {
            
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 492))
#     def test_493(self):
#         input = """foo1: function void (a: integer, b: float) {
#             c: float = a + b;
#             printFloat(c);
#         }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 493))
#     def test_494(self):
#         input = """foo2: function void (a: integer) {
#             printString(\"Test\");
#             a = a + 1;
#             printInteger(a);
#         }
#         main: function void() {
#             foo2(10);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 494))
#     def test_495(self):
#         input = """a,b,c: boolean = true, false, true;
#         main: function void() {
#             a = b && c;
#             printBoolean(a);
#         }"""
#         expect = ""
#         self.assertTrue(TestChecker.test(input, expect, 495))
#     def test_496(self):
#         input = """foo: function void() {
#             if (true)
#             {
#                 a, b, c: integer = 10, 20, 30;
#                 printInteger(a + b + c);
#             }
#             else
#             {
#                 x, y: float = 2.3e2, -2.3e2;
#                 printFloat(x + y);
#             }   
#         }"""
#         expect = """No entry point"""
#         self.assertTrue(TestChecker.test(input, expect, 496))
#     def test_497(self):
#         input = """a_20: boolean = (2 < 3) < 4;
#         main: function void() {}"""
#         expect = """Type mismatch in expression: BinExpr(<, BinExpr(<, IntegerLit(2), IntegerLit(3)), IntegerLit(4))"""
#         self.assertTrue(TestChecker.test(input, expect, 497))
#     def test_498(self):
#         input = """foo: function string (a: string, b: integer) {
#             return (a :: a[b]);
#         }
#         main: function void() {}"""
#         expect = """Type mismatch in expression: ArrayCell(a, [Id(b)])"""
#         self.assertTrue(TestChecker.test(input, expect, 498))
#     def test_499(self):
#         input = """x: integer = 65;
#         y: function integer(x: integer) {
#             return x + 1;
#         }
#         z: float = 65.20;
#         t: function float(z: float) {
#             return z * 2.0;
#         }
#         main: function void() {
#             y: integer = y(x);
#             t: float = t(z);
#             printInteger(y);
#             printFloat(t);
#         }"""
#         expect = """Type mismatch in expression: FuncCall(y, [Id(x)])"""
#         self.assertTrue(TestChecker.test(input, expect, 499))