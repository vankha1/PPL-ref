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
    def test_12(self):
        input = """foo1: function auto (a: integer, a: integer) inherit foo
        {
            super(2,3);
            if (a == 1) return 1;
            a = 1;
            b= a+b;
            a: float;
        } 
        foo: function void (inherit a: integer, inherit b: integer)
        {
            
        } """
        expect="Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 412)) 
    def test_13(self):
        input = """ foo1: function auto (c: integer, c: integer) inherit foo
        {
            super(2,3);
            if (a == 1) return 1;
            a = 1;
            b= a+b;
            a: float;
        } 
        foo: function void (inherit a: integer, inherit b: integer)
        {
            
        } """
        expect="Redeclared Parameter: c"
        self.assertTrue(TestChecker.test(input, expect, 413)) 
    def test_14(self):
        input = """        r: integer;
        foo1: function auto (a: integer, d: integer) inherit foo
        {
            super(2,3);
            if (a == 1) return 1;
            a = 1;
            b= a+b;
            a: float;
        } 
        foo: function void (inherit a: integer, inherit b: integer)
        {
            
        } 
        """
        expect="Invalid Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 414))
    def test_15(self):
        input = """        arr: array[2,1] of integer = {{1},{2}};
        m: integer;
    
        foo1: function auto (c: integer, d: integer) inherit foo
        {
            super(2,3);
            if (a == 1) return 1;
            a = 1;
            b = a+b;
            r: integer;
            r = arr[0,0.0];
 
        } 
        foo: function void (inherit a: integer, inherit b: integer)
        {
            
        } 
        """
        expect="Type mismatch in expression: ArrayCell(arr, [IntegerLit(0), FloatLit(0.0)])"
        self.assertTrue(TestChecker.test(input, expect, 415)) 
    def test_16(self):
        input = """            
        arr: array[2,1] of integer = {{1},{2}};
        m: integer;

        n: integer ;
        foo1: function auto (c: integer, d: integer) inherit foo
        {
            super(2,3);
            if (a == 1) return 1;
            a = 1;
            b = a+b;
            r: integer;
            r = arr[0,0];
 
        } 
        foo: function auto (inherit a: integer, inherit b: integer)
        {
            return a;
        } 
        """
        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 416))  

    def test_17(self):
        input ="""
      
      
       arr: array [2,2,2,2] of integer = {
            {
                { {1, 2}, {3, 4} },
                { {5, 6}, {7, 8} }
            },
            {
                { {9, 10}, {11, 12} },
                { {13, 14}, {15, 16} }
            }
           };
        m: integer;

        n: float = readInteger();
        foo1: function auto (c: integer, d: integer) inherit foo
        {
            super(2.0,3);
            printInteger(1);
            if (b == 1) return 1;
            a = 1;
            a = a+b;
            r: integer;
            r = arr[0,0];
 
        } 
        foo: function auto (inherit a: float, inherit b: integer)
        {
            return a;
        } 
        
"""



        expect="Type mismatch in statement: AssignStmt(Id(r), ArrayCell(arr, [IntegerLit(0), IntegerLit(0)]))"
        self.assertTrue(TestChecker.test(input, expect, 417))
        
    def test_18(self):
        input ="""
      
      var : integer = true;
    main: function void(){}
 
        
"""



        expect="Type mismatch in Variable Declaration: VarDecl(var, IntegerType, BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 418))
    def test_19(self):
        input ="""
      
       var : float = "hello";
    main: function void(){}
 
        
"""



        expect="Type mismatch in Variable Declaration: VarDecl(var, FloatType, StringLit(hello))"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_20(self):
        input ="""
      
       var : boolean = 123;
    main: function void(){}
 
        
"""



        expect="Type mismatch in Variable Declaration: VarDecl(var, BooleanType, IntegerLit(123))"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_21(self):
        input ="""
      arr: array[2,1] of integer = {{1},{2}};
    m: integer;

    n: integer ;
    foo1: function auto (c: integer, d: integer) inherit foo
    {
        if (a == 1) return 1;
        a = 1;
        b = a+b;
        r: integer;
        r = arr[0,0];
        return r;
    } 
    foo: function auto (a: integer, b: integer)
    {
        super(2,3);
        return a;
    } 
      
 
        
"""



        expect="Invalid statement in function: foo1"
        self.assertTrue(TestChecker.test(input, expect, 421))
    def test_22(self):
        input ="""
      
      arr: array[2,1] of integer = {{1},{2}};
    m: integer;

    n: integer ;
    foo1: function auto (c: integer, d: integer) inherit foo
    {
        if (a == 1) return 1;
        a = 1;
        b = a+b;
        r: integer;
        r = arr[0,0];
        return r;
    } 
    foo: function auto ()
    {
        return 1;
    } 
 
        
"""



        expect="Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 422))
    def test_23(self):
        input ="""
      
      
 arr: array[2,1] of integer = {{1},{2}};
    m: integer;

    n: integer ;
    foo1: function auto (c: integer, d: integer) inherit foo
    {
        if (a == 1) return 1;
        a = 1;
        b = a+b;
        r: integer;
        r = arr[0,0];
        return r;
    } 
        
"""



        expect="Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 423))
    def test_24(self):
        input ="""
      
      arr: array[2,1] of integer = {{1},{2}};
    m: integer;

    n: integer ;
    foo1: function auto (c: integer, d: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b = a+b;
        r: integer;
        r = arr[0,0];
        return r;
    } 
    foo: function auto ()
    {
        super(2,3);
        return 1;
    } 
 
        
"""



        expect="Type mismatch in expression: IntegerLit(2)"
        self.assertTrue(TestChecker.test(input, expect, 424))   
    def test_25(self):
        input ="""
      
       var : string = "abc";
        a : integer = 1;
        func: function void(alpha : string, delta : integer){
            b = a + 1;
        }
        main: function void(){}
        func2 : function void (alpha : string, delta : integer){}
        func3 : function void (alpha : string, delta : integer) {}
 
        
"""



        expect="Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 425))
    def test_26(self):
        input ="""
      
      var : integer = "abc";
        a : integer = 1;
        func: function void(alpha : string, delta : integer){
            b = a + 1;
        }
        main: function void(){}
        func2 : function void (alpha : string, delta : integer){}
        func3 : function void (alpha : string, delta : integer) {}
 
        
"""



        expect="Type mismatch in Variable Declaration: VarDecl(var, IntegerType, StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 426))    
    def test_27(self):
        input ="""
      
       var : string = "abc";
        a : integer = 1;
        func: function void(alpha : string, delta : integer){
            a = a + 1;
        }
        main: function void(){
            b = a + 2;
        }
        func2 : function void (alpha : string, delta : integer){}
        func3 : function void (alpha : string, delta : integer) {}
 
        
"""



        expect="Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test_28(self):
        input ="""
      
         var : string = "abc";
        a : integer = 1;
        func: function void(alpha : string, delta : integer){
            a = a + 1;
        }
        main: function void(){
            a = a + 2;
        }
        func2 : function void (alpha : string, delta : integer){}
        func3 : function void (alpha : string, delta : integer) {}
 
        
"""



        expect=""
        self.assertTrue(TestChecker.test(input, expect, 428))
    def test_29(self):
        input ="""
      
      var : string = "abc";
        a : integer = 1;
        func: function void(alpha : string, delta : integer){
            a = a + 1;
        }
        main: function void(){
            a = a + 2;
            b = func(alpha, delta);
        }
        func2 : function void (alpha : string, delta : integer){}
        func3 : function void (alpha : string, delta : integer) {}
 
        
"""



        expect="Type mismatch in expression: FuncCall(func, [Id(alpha), Id(delta)])"
        self.assertTrue(TestChecker.test(input, expect, 429))
    def test_30(self):
        input ="""
      
      sumNumbers: function integer() {
            sum: integer = 0;
            i: integer = 1;
            n: integer= 20;
            do {
                sum = sum + i;
                i = i + 1;
            } while (i <= n);
            return sum;
        }
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 430))
    def test_31(self):
        input ="""
      
       findMax: function integer(a: array[5] of integer) {
           
            max: integer = a[0];
            i: integer;
            for (i=1, i<= 4, i+1)
            {
                z: integer = 0;
                z= 10;



                if (a[i] > max) 
                {
                    
                    return;
                    
                    
                }
                    max = a[i];
               
                
            }
            return max;
                
            
        }
 
        
"""











        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 431))
    def test32(self):
        input ="""
      
       isEven: function boolean(n: integer) {
            if ((n%2)==0) 
                return true;
            else
                return false;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_33(self):
        input ="""
      
      isEven: function boolean(n: integer) {
            if (n * 2 == 0) 
                return true;
            else
                return false;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 433))
    def test_34(self):
        input ="""
      factorial: function integer(n: integer) {
            if (n == 0) 
                return 1;
            else
                return n * factorial(n - 1);
        }
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 434))
    def test_35(self):
        input ="""
        gcd: function integer(a: integer, b: integer) {
             r: integer = a % b;
            while (b != 0) {
             
                a = b;
                b = r;
            }
                
            return a;
        }
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_36(self):
        input ="""
      
      convertToBinary: function string(n: integer) {
            s: string = "";
            while (n > 0) 
            {
             if (n % 2 == 0) 
                    s = "0" + s;
                else
                    s = "1" + s;
                n = n / 2;
            
            }
               
            return s;
        }
 
        
"""



        expect="Type mismatch in expression: BinExpr(+, StringLit(0), Id(s))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_37(self):
        input ="""
      
       printMultiplicationTable: function void(i: integer) {
            for (i=1, i<10,i + 1)
             {
                for (j=1, j<10,j + 1)
                    {
                    write(i*j + " ");
                    }
             } 
                
                writeln("");
        }
 
        
"""



        expect="Undeclared Identifier: j"
        self.assertTrue(TestChecker.test(input, expect, 437))
    def test_38(self):
        input ="""
      fibonacci: function integer(n: integer) {
            if (n == 0) 
                return 0;
            else
                if (n == 1) 
                    return 1;
                else
                    return fibonacci(n - 1) + fibonacci(n - 2);
        }
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 438))
    def test_39(self):
        input ="""
      
       isPrime: function boolean(n: integer) {
            if (n <= 1) 
                return false;
            else
                  for (i=1, i<10,i + 1)
             {
                for (j=1, j<10,j + 1)
                    {
                    write(i*j + " ");
                    }
             }
            return true;
        }
    
 
        
"""



        expect="Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_40(self): # xem lại testcase  này
        input ="""
      
      findMin: function integer(a: array[5] of integer) {
            min: integer = a[0];
            i: float; 
            for (i=1,i<10,i+1)
             {
             if (a[i] < min) 
                    min = a[i];
             
             } 
                
            return min;
        }
 
        
"""



        expect="Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([IfStmt(BinExpr(<, ArrayCell(a, [Id(i)]), Id(min)), AssignStmt(Id(min), ArrayCell(a, [Id(i)])))]))"
        self.assertTrue(TestChecker.test(input, expect, 440))
    def test_41(self):
        input ="""
      
      foo1: function auto (a: integer, a: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
    } 
    foo: function void (inherit a: integer, inherit b: integer)
    {
        
    }
 
        
"""



        expect="Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input, expect, 441))
    def test_42(self):
        input ="""
      
      foo1: function auto (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
    } 
    foo: function void (a: integer, b: integer)
    {
        
    }
 
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 442))
    def test_43(self):
        input ="""
      
      
 foo1: function auto (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
    } 
    foo: function void (a: integer, b: integer) inherit t
    {
        
    }
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 443))
    def test_44(self):
        input ="""
      
      foo1: function integer (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
        return true;
    } 
    foo: function void (a: integer, b: integer)
    {
        
    } 
 
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 444))
    def test_45(self):
        input ="""
      
      foo1: function integer (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
        return b;
    } 
    foo: function void (a: integer, b: integer)
    {
        c: integer;
        c = foo1(3, 4);
    }
 
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 445))   
    def test_46(self):
        input ="""
      
      foo1: function integer (a: integer, b: integer) inherit foo
    {
        super(2,3);
        if (a == 1) return 1;
        a = 1;
        b= a+b;
        a: float;
        return b;
    } 
    foo: function void (a: integer, b: integer)
    {
        c: float;
        c = foo1(3, 4);
    }
 
        
"""



        expect="Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 446))
    def test_47(self):
        input ="""
      
      foo1: function integer(a: integer, b: integer) inherit foo {
    super(2, 3);
    if (a == 1) return 1;
    a = 1;
    b = a + b;
     c: float;
    for (b=1, b<=c, b + 2)
    {
     if (a==b) return 1;
     else break;
    }
    return b;
}

foo: function void(a: integer, b: integer) {
    // function body here
}
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 447))    
    def test_48(self):
        input ="""
      
      foo1: function integer(a: integer, b: integer) inherit foo {
            super(2, 3);
            if (a == 1) return 1;
            a = 1;
            b = a + b;
            c: float;
            for (b=1, b<=c, b + 2)
            {
                if (a==b) return 1;
                else break;
            }
            return b;
        }
        foo: function void(a: integer, b: integer) {
            // function body here
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 448))
    def test_49(self):
        input ="""
      
      foo1: function integer(a: integer, b: integer) inherit foo {
            super(2, 3);
            if (a == 1) return 1;
            a = 1;
            b = a + b;
            c: float;
            for (b=1, b<=c, b + 2)
            {
                if (a==b) return 1;
                else break;
            }
            return b;
        }
        foo: function void(a: integer, b: integer) {
            // function body here
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 449))
    def test_50(self):
        input ="""
      
      foo1: function integer(a: integer, b: integer) inherit foo {
            super(2, 3.1);
            if (a == 1) return 1;
            a = 1;
            b = a + b;
            c: float;
            for (b=1, b<=c, b + 2)
            {
                if (a==b) return 1;
                else break;
            }
            return b;
        }
        foo: function void(a: integer, b: integer) {
            // function body here
        }
 
        
"""



        expect="Type mismatch in expression: FloatLit(3.1)"
        self.assertTrue(TestChecker.test(input, expect, 450))
    def test51(self):
        input ="""
      
      func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
             y: float = 2.0;
            func1(x, y);
            func1(y, x);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 451))
    def test_52(self):
        input ="""
      
       func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
            x: integer = 1;
             y: float = 2.0;
            func1(x, y);
            func1(y, y);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(y), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 452))
    def test53(self):
        input ="""
      
       func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
             y: string = "abc";
            func1(x, y);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(x), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 453))
    def test_54(self):
        input ="""
      
      func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
             y: float = 2.0;
             z: boolean = true;
            func1(x, y);
            func1(z, y);
        }
 
        
"""



        expect="Type mismatch in statement: CallStmt(func1, Id(z), Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    def test_55(self):
        input ="""
      
      func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
            func1(x);
        }
 
        
"""



        expect="Type mismatch in expression: CallStmt(func1, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 455))
    def test_56(self):
        input ="""
      
      func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
             x: integer = 1;
             y: float = 2.0;
            func1(x, y, x);
        }
 
        
"""



        expect="Type mismatch in expression: CallStmt(func1, Id(x), Id(y), Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_57(self):
        input ="""
      
       func1: function void(a: integer, b: float) {
            if (a < b) {
                return;
            } else {
                b = a;
            }
        }
        func2: function void() {
            x: integer = 1;
             y: float = 2.0;
            func1(x);
        }
 
        
"""



        expect="Type mismatch in expression: CallStmt(func1, Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_58(self):
        input ="""
      
       foo1: function integer(a: integer, b: integer) inherit foo {
            super(2, 3);
            if (a == 1) return 1;
            a = 1;
            b = a + b;
             c: float;
            do
            {
                z: integer= 10;
            }
            while(b==1);
            for (b=1, b<=c, b + 2)
            {
            continue;
                if (a==b) return 1;
                else break;
            }
            return b;
        }
        foo: function void(a: integer, b: integer) {
            // function body here
        }
 
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 458))
    def test_59(self):
        input ="""
      
      foo: function void() {
            return;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 459))
    def test_60(self):
        input ="""
      
       foo: function void() {
            x: integer = 1;
            y: float = 2.5;
            return;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_61(self):
        input ="""
      
       foo1: function void() {
            foo2();
            return;
        }

        foo2: function void() {
            return;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 461))
    def test_62(self):
        input ="""
      
       foo1: function void() {
            if (1 == 1) {
                return;
            }
            return;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 462))
    def test_63(self):
        input ="""
      foo1: function void() {
            foo2();
            return;
        }

        foo2: function void() {
            foo1();
            return;
        }
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 463))
    def test_64(self):
        input ="""
      
       foo: function void(a: integer, b: integer) {
            // function body here
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 464))
    def test_65(self):
        input ="""
      
      
 foo1: function integer(a: integer, b: integer) {
            return a + b;
        }

        foo2: function integer(a: integer, b: integer) {
            x: integer = foo1(a, b);
            return x;
        }
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 465))
    def test_66(self):
        input ="""
      
       foo1: function integer(a: integer, b: integer) {
            x: integer = 1;
            y: float = 2.5;
            return a + b;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 466))   
    def test_67(self):
        input ="""
      
       foo1: function void() {
            foo2();
            return;
        }

        foo2: function void() {
            foo3();
            return;
        }

        foo3: function void() {
            return;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 467))
    def test_68(self):
        input ="""
      
      
      foo: function integer(a: integer, b: integer) {
            x: integer = a + b;
            return x;
        }
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 468))    
    def test_69(self):
        input ="""
       foo1: function void() {
            x: integer = 1;
            y: float = 2.5;
            return;
        }

        foo2: function integer(a: integer, b: integer) {
            x: integer = a + b;
            return x;
        }
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 469))
    def test_70(self):
        input ="""
      
       foo: function integer(a: integer, b: integer) {
            if (a > b) {
                return a;
            } else {
                return b;
            }
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 470))
    def test_71(self):
        input ="""
      
       foo1: function void() {
            foo2();
            return;
        }

        foo2: function void() {
            foo1();
            return;
        }
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 471))
    def test_72(self):
        input ="""
       var : auto = "abc";
            B : auto = 1;
            func: function void(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 10 , i + 1){
                    var : auto = "abc";
                    c : auto = 12314;
                    var = var :: "abc";
                    break;
                    continue;
                }
                z : integer;
                return;
            }
            main: function void(){}
      
 
        
"""



        expect=""
        self.assertTrue(TestChecker.test(input, expect, 472))
    def test_73(self):
        input ="""
      
        var : auto = 5.5;
            B : auto = 2;
            func: function string(alpha : string, delta : integer){
                if(B > 1){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 5 , i + 1){
                    var : auto = "def";
                    c : auto = 12314;
                    var = var :: "def";
                    break;
                    continue;
                }
                z : string;
                return "Hello, World!";
            }
            main: function void(){}
            
 
        
"""



        expect=""
        self.assertTrue(TestChecker.test(input, expect, 473))
    def test_74(self):
        input ="""
      var : auto = true;
            B : auto = 0;
            func: function void(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 3 , i + 1){
                    var : auto = false;
                    c : auto = 12314;
                    var = var :: true;
                    break;
                    continue;
                }
                z : boolean;
                return;
            }
            main: function void(){}
      
 
        
"""



        expect="Type mismatch in expression: BinExpr(::, Id(var), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 474))
    def test_75(self):
        input ="""
      
      var : auto = 100;
            B : auto = -1;
            func: function integer(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 7 , i + 1){
                    var : auto = 5.5;
                    c : auto = 12314;
                    var = var + 2.5;
                    break;
                    continue;
                }
                z : integer;
                return 999;
            }
            main: function void(){}

 
        
"""



        expect=""
        self.assertTrue(TestChecker.test(input, expect, 475))
    def test_76(self):
        input ="""
       var : auto = "Hello";
            B : auto = 1;
            func: function boolean(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 4 , i + 1){
                    var : auto = true;
                    c : auto = 12314;
                    var = var :: false;
                    break;
                    continue;
                }
                z : boolean;
                return false;
            }
            main: function void(){}
      
 
        
"""



        expect="Type mismatch in expression: BinExpr(::, Id(var), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_77(self): #????????
        input ="""
      
            var : auto = 3.14;
            B : auto = 0;
            func: function float(alpha : string, delta : integer)inherit foo{
                
              super(1,1);
                i : integer;
               
                for (i = 0, i < 3 , i + 1){
                 m: float;
                    var: float = 100;
                    c : auto = 12314;
                    var = var + 2.5;
                    break;
                    continue;
                }
                z : float;
                return 3.141592653589793;
            }
            foo: function void (inherit m: integer, n:integer){}
            main: function void(){}
 
        
"""



        expect=""
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_78(self):
        input ="""
      
      var : auto = "abc";
            B : auto = -1;
            func: function void(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 6 , i + 1){
                    var : auto = "abc";
                    c : auto = 12314;
                    var = var :: "def";
                    break;
                    continue;
                }
                z : integer;
                return;
            }
            main: function void(){}
 
        
"""



        expect=""
        self.assertTrue(TestChecker.test(input, expect, 478))
    def test_79(self):
        input ="""
       var : auto = false;
            B : auto = 1;
            func: function void(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 2 , i + 1){
                    var : auto = true;
                    c : auto = 12314;
                    var = var :: false;
                    break;
                    continue;
                }
                z : boolean;
                return;
            }
            main: function void(){}
      
 
        
"""



        expect="Type mismatch in expression: BinExpr(::, Id(var), BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 479))
    def test_80(self):
        input ="""
      
      var : auto = 999;
            B : auto = -1;
            func: function integer(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 8 , i + 1){
                    var : auto = 5.5;
                    c : auto = 12314;
                    var = var + 2.5;
                    break;
                    continue;
                }
                z : integer;
                return -999;
            }
            main: function void(){}
 
        
"""



        expect=""
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_81(self):
        input ="""
      var : auto = true;
            B : auto = 0;
            func: function boolean(alpha : string, delta : integer){
                if(B > 0){
                    B = 0;
                } else {
                    B = 1;
                }
                i : integer;
                for (i = 0, i < 5 , i + 1){
                    var : auto = false;
                    c : auto = 12314;
                    var = var :: true;
                    break;
                    continue;
                }
                z : boolean;
                return true;
            }
            main: function void(){}
      
 
        
"""



        expect="Type mismatch in expression: BinExpr(::, Id(var), BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 481))
    def test_82(self):
        input ="""
      
    a: integer = 10;
    b: boolean = true;

    foo1:function integer(){
        if b  return a;
        else return -1;
    }

    foo2:function float(x: float){
        if x > 0  return foo1() + x;
        else return foo1() - x;
    }

    main:function void(){
        writeFloat(foo2(-5));
        writeFloat(foo2(5));
    }
 
        
"""



        expect="Undeclared Function: writeFloat"
        self.assertTrue(TestChecker.test(input, expect, 482))
    def test_83(self):
        input ="""
      
      
     a: integer = 10;
    b: boolean = true;

    foo1:function integer(){
        if b  return a;
        else return -1;
    }

    foo2:function float(x: float){
        if x > 0  return foo1() + x;
        else return foo1() - x;
    }

    main:function void(){
         i: integer;
        for (i = 0,i <a, i+ 1)
         {
         printFloat(foo2(i-5));
         } 
            
    }
        
"""



        expect=""
        self.assertTrue(TestChecker.test(input, expect, 483))
    def test_84(self):
        input ="""
      
       a: integer = 10;
    b: boolean = true;

    foo1:function integer(){
        if b  return a;
        else return -1;
    }

    foo2:function float(x: float){
        if x > 0  return foo1() + x;
        else return foo1() - x;
    }

    main:function void(){
         for (i = 0,i <a, i+ 1)
         {
         printInteger(foo2(i-5));
         } 
    }
 
        
"""



        expect="Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 484))
    def test_85(self):
        input ="""
      
       arr: array [2,2,2,2] of integer = {
            {
                { {1, 2}, {3, 4} },
                { {5, 6}, {7, 8} }
            },
            {
                { {9, 10}, {11, 12} },
                { {13, 14}, {15, 16} }
            }
           };
        m: integer;

        n: float = foo(1,2);
        foo1: function auto (c: integer, d: integer) inherit foo
        {
            super(2.0,3);
            if (b == 1) return 1;
            a = 1;
            a = a+b;
            r: integer;
            r = arr[0,0];
 
        } 
        foo: function auto (inherit a: float, inherit b: integer)
        {
            return a;
        } 
 
        
"""



        expect="Type mismatch in statement: AssignStmt(Id(r), ArrayCell(arr, [IntegerLit(0), IntegerLit(0)]))"
        self.assertTrue(TestChecker.test(input, expect, 485))
  
    def test_86(self):
        input ="""
      
      
 foo1: function auto (c: integer, d: integer) inherit foo
{
    if (b == 1) return 1;
    a = 1;
    a = a+b;
    return foo(2.0,3);
} 
        
"""



        expect="Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 486))
    def test_87(self):
        input ="""
      
      foo: function auto (inherit a: float, inherit b: integer)
{
    return a;
}

foo: function auto (c: integer, d: integer)
{
    return c + d;
}
 
        
"""



        expect="Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 487))    
    def test_88(self):
        input ="""
      
      
 arr: array [2,2,2,2] of integer = {
    {
        { {1, 2}, {3, 4} },
        { {5, 6}, {7, 8} }
    },
    {
        { {9, 10}, {11, 12} },
        { {13, 14}, {15, 16} }
    }
};

r: integer=arr[0,0];
        
"""



        expect="Type mismatch in Variable Declaration: VarDecl(r, IntegerType, ArrayCell(arr, [IntegerLit(0), IntegerLit(0)]))"
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test_89(self):
        input ="""
      
      foo: function auto (inherit a: float, inherit b: integer)
{
    return a;
}

m: integer = foo(1,2);
 
        
"""



        expect="Type mismatch in Variable Declaration: VarDecl(m, IntegerType, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 489))
    def test_90(self):
        input ="""
      
      arr: array [2,2,2,2] of integer = {
    {
        { {1, 2}, {3, 4} },
        { {5, 6}, {7, 8} }
    },
    {
        { {9, 10}, {11, 12} },
        { {13, 14}, {15, 16} }
    }
};

r: integer;
r: float;
 
        
"""



        expect="Redeclared Variable: r"
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test_91(self):
        input ="""
      
      foo: function auto ()
{
    if (1 > 2) return 1;
}
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test_92(self):
        input ="""
      
      foo: function auto ()
{
    continue;
}
 
        
"""



        expect="Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 492))
   
    def test_93(self):
        input ="""
      
      foo: integer = foo();
 
        
"""



        expect="Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test_94(self):
        input ="""
      
      
 arr: array [1,5] of integer;
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_95(self):
        input ="""
         a: integer = 5;
    b: float = 3.14;
    c: boolean = true;
    d: string = "hello";
    e: array [5] of integer = {1, 2, 3, 4, 5};
    f: array [2, 3] of boolean = {{true, false, true}, {false, true, false}};

    x: integer = a + e[2] * 2;
    y: float = b / x;
  
      
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_96(self):
        input ="""
        b: float = 2.5;
    c: boolean = false;
    d: string = "world";
    e: array [3] of integer = {7, 8, 9};
    f: array [2, 2] of boolean = {{true, false}, {false, true}};

    x: integer = a + e[1] * 3;
    y: float = b * x;
      
 
        
"""



        expect="Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_97(self):
        input ="""
      
      
 b: float = 1.5;
    c: boolean = true;
    d: string = "hello";
    e: array [4] of integer = {2, 4, 6, 8};
    f: array [3, 3] of boolean = {{true, false, true}, {false, true, false}, {true, true, false}};

    x: integer = a + e[3] * 2;
    y: float = b / x;
        
"""



        expect="Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test_98(self):
        input ="""
      
      a: integer = 0;
    b: float = 1.0;
    c: boolean = false;
    d: string = "world";
    e: array [5] of integer = {5, 4, 3, 2, 1};
    f: array [2, 2] of boolean = {{false, true}, {true, false}};

    x: integer = a + e[0] * 2;
    y: float = b * x;
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 498))
    def test_99(self):
        input ="""
      
        a: integer = 7;
    b: float = 2.0;
    c: boolean = true;
    d: string = "hello";
    e: array [6] of integer = {1, 3, 5, 7, 9, 11};
    f: array [3, 2] of boolean = {{false, true}, {true, false}, {false, true}};

    x: integer = a + e[4] * 2;
 
        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_100(self):
        input ="""
      
      
    a: integer = 6;
    b: float = 0.2;
    c: boolean = true;
    d: string = "hello";
    e: array [5] of integer = {5, 3, 1, -1, -3};
    f: array [3, 3] of boolean = {{false, true, false}, {true, false, true}, {false, true, false}};

        
"""



        expect="No entry point"
        self.assertTrue(TestChecker.test(input, expect, 500))
   
