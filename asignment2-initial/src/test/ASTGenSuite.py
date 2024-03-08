import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    """
    TESTCASE STRATEGY:
        300-309: Types & Literals
        310-324: Declarations
        325-344: Expressions
        345-374: Statements
        375-399: Mixed Cases
    """

    ##### TYPES & LITERALS #####
    def test300_single_atomic_types(self):
        input = """
            number x
            string y
            bool z
        """
        expect = """Program([VarDecl(NumberType,Id(x)),VarDecl(StringType,Id(y)),VarDecl(BoolType,Id(z))])"""
        self.assertTrue(TestAST.test(input, expect, 300))

    def test301_inferred_types(self):
        input = """
            var x <- 2
            dynamic y
        """
        expect = """Program([VarDecl(var,Id(x),NumLit(2.0)),VarDecl(dynamic,Id(y))])"""
        self.assertTrue(TestAST.test(input, expect, 301))

    def test302_array_types(self):
        input = """number x[5]
        """
        expect = """Program([VarDecl(ArrayType([5],NumberType),Id(x))])"""
        self.assertTrue(TestAST.test(input, expect, 302))

    def test303_atomic_types_with_init(self):
        input = """
            number x <- 5
            number y <- 5.5e5
            string z <- "55"
            bool t <- true
        """
        expect = """Program([VarDecl(NumberType,Id(x),NumLit(5.0)),VarDecl(NumberType,Id(y),NumLit(550000.0)),VarDecl(StringType,Id(z),StringLit(55)),VarDecl(BoolType,Id(t),BooleanLit(True))])"""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test304_array_types_with_init(self):
        input = """number x[5] <- [1,2,3,4,5]
        """
        expect = """Program([VarDecl(ArrayType([5],NumberType),Id(x),[NumLit(1.0),NumLit(2.0),NumLit(3.0),NumLit(4.0),NumLit(5.0)])])"""
        self.assertTrue(TestAST.test(input, expect, 304))

    def test305_inferred_types_with_init(self):
        input = """
            var x <- "vankha"
            dynamic y
        """
        expect = """Program([VarDecl(var,Id(x),StringLit(vankha)),VarDecl(dynamic,Id(y))])"""
        self.assertTrue(TestAST.test(input, expect, 305))

    def test306_assign_with_basic_literal(self):
        input = """
            func main()
            begin
                a <- 1
                b <- 1.1
                c <- "c"
                d <- false
            end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),NumLit(1.0)),AssignStmt(Id(b),NumLit(1.1)),AssignStmt(Id(c),StringLit(c)),AssignStmt(Id(d),BooleanLit(False))]))])"""
        self.assertTrue(TestAST.test(input, expect, 306))

    def test307_assign_with_array_literal(self):
        input = """func main()
            begin
            a <- [1,2,3,4]
            b <- [1,"1", false]
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),[NumLit(1.0),NumLit(2.0),NumLit(3.0),NumLit(4.0)]),AssignStmt(Id(b),[NumLit(1.0),StringLit(1),BooleanLit(False)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 307))

    def test308_assign_with_multiD_array_literal(self):
        input = """func main()
            begin
            a <- [1,[2,[3,4]]]
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),[NumLit(1.0),[NumLit(2.0),[NumLit(3.0),NumLit(4.0)]]])]))])"""
        self.assertTrue(TestAST.test(input, expect, 308))

    def test309_assign_with_mixed_array_literal(self):
        input = """func main()
            begin
            a <- ["1",2,false,abc,abcd()]
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),[StringLit(1),NumLit(2.0),BooleanLit(False),Id(abc),CallExpr(Id(abcd),[])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 309))

    ##### DECLARATIONS #####
    def test310_short_vardecl(self):
        input = """number x
        """
        expect = str(Program([VarDecl(Id('x'), NumberType())]))
        self.assertTrue(TestAST.test(input, expect, 310))

    def test311_full_vardecl(self):
        input = """var x <- 1
                    number y <- 2
                    number z <- 3
        """
        expect = """Program([VarDecl(var,Id(x),NumLit(1.0)),VarDecl(NumberType,Id(y),NumLit(2.0)),VarDecl(NumberType,Id(z),NumLit(3.0))])"""
        self.assertTrue(TestAST.test(input, expect, 311))

    def test312_vardecls(self):
        input = """number x <- 1
                    number y <- 2
                    number z <- 3
                string a
                string b
        """
        expect = """Program([VarDecl(NumberType,Id(x),NumLit(1.0)),VarDecl(NumberType,Id(y),NumLit(2.0)),VarDecl(NumberType,Id(z),NumLit(3.0)),VarDecl(StringType,Id(a)),VarDecl(StringType,Id(b))])"""
        self.assertTrue(TestAST.test(input, expect, 312))

    def test313_full_vardecl_simple_expr(self):
        input = """number x <- a
                number y <- b
                number z <- c
        """
        expect = """Program([VarDecl(NumberType,Id(x),Id(a)),VarDecl(NumberType,Id(y),Id(b)),VarDecl(NumberType,Id(z),Id(c))])"""
        self.assertTrue(TestAST.test(input, expect, 313))

    def test314_full_vardecl_complex_expr(self):
        input = """number x <- hello()
                    number y <- a+5
                    number z <- not b
                """
        expect = """Program([VarDecl(NumberType,Id(x),CallExpr(Id(hello),[])),VarDecl(NumberType,Id(y),BinaryOp(+,Id(a),NumLit(5.0))),VarDecl(NumberType,Id(z),UnaryOp(not,Id(b)))])"""
        self.assertTrue(TestAST.test(input, expect, 314))

    def test315_empty_funcdecl(self):
        input = """func main() begin 
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([]))])"""
        self.assertTrue(TestAST.test(input, expect, 315))

    def test316_simple_empty_params_funcdecl(self):
        input = """func main (number a,string b,bool c,number d) begin 
        end
        """
        expect = """Program([FuncDecl(Id(main),[VarDecl(NumberType,Id(a)),VarDecl(StringType,Id(b)),VarDecl(BoolType,Id(c)),VarDecl(NumberType,Id(d))],Block([]))])"""
        self.assertTrue(TestAST.test(input, expect, 316))

    def test317_inherit_empty_funcdecl(self):
        input = """func main(number a, string b) begin 
        end
        """
        expect = """Program([FuncDecl(Id(main),[VarDecl(NumberType,Id(a)),VarDecl(StringType,Id(b))],Block([]))])"""
        self.assertTrue(TestAST.test(input, expect, 317))

    def test318_normal_funcdecl(self):
        input = """func main()
            begin
                a <- a+1
                writeNumber(a)
            end
            """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(+,Id(a),NumLit(1.0))),Call(Id(writeNumber),[Id(a)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 318))

    def test319_inherit_out_funcdecl(self):
        input = """func main(number c) begin 
        end
        """
        expect = """Program([FuncDecl(Id(main),[VarDecl(NumberType,Id(c))],Block([]))])"""
        self.assertTrue(TestAST.test(input, expect, 319))

    def test320_mixed_decl1(self):
        input = """number x <- 1
        func main()
            begin
                x <- x+1
            end
        """
        expect = """Program([VarDecl(NumberType,Id(x),NumLit(1.0)),FuncDecl(Id(main),[],Block([AssignStmt(Id(x),BinaryOp(+,Id(x),NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 320))

    def test321_mixed_decl2(self):
        input = """number x
        func main()
            begin
                number x <- 2.0
            end
        """
        expect = """Program([VarDecl(NumberType,Id(x)),FuncDecl(Id(main),[],Block([VarDecl(NumberType,Id(x),NumLit(2.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 321))

    def test322_mixed_decl3(self):
        input = """
        func getTotal(number x, number y)
        begin
            return x+y
        end
        func main()
        begin
            number x <- getTotal(1,2)
        end
        """
        expect = """Program([FuncDecl(Id(getTotal),[VarDecl(NumberType,Id(x)),VarDecl(NumberType,Id(y))],Block([Return(BinaryOp(+,Id(x),Id(y)))])),FuncDecl(Id(main),[],Block([VarDecl(NumberType,Id(x),CallExpr(Id(getTotal),[NumLit(1.0),NumLit(2.0)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 322))

    def test323_mixed_decl4(self):
        input = """number x[2] <- [1,2]
        func main()
        begin
            x <- [1,2,3]
        end
        """
        expect = """Program([VarDecl(ArrayType([2],NumberType),Id(x),[NumLit(1.0),NumLit(2.0)]),FuncDecl(Id(main),[],Block([AssignStmt(Id(x),[NumLit(1.0),NumLit(2.0),NumLit(3.0)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 323))

    def test324_mixed_decl5(self):
        input = """number x[2] <- [1,2]
        func main()
        begin
            print(x)
            return
        end
        """
        expect = """Program([VarDecl(ArrayType([2],NumberType),Id(x),[NumLit(1.0),NumLit(2.0)]),FuncDecl(Id(main),[],Block([Call(Id(print),[Id(x)]),Return()]))])"""
        self.assertTrue(TestAST.test(input, expect, 324))

    ##### EXPRESSIONS #####
    def test325_empty_call_expr(self):
        input = """
        func main()
        begin
            hello()
            good_boy()
            are_you_ok()
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Call(Id(hello),[]),Call(Id(good_boy),[]),Call(Id(are_you_ok),[])]))])"""
        self.assertTrue(TestAST.test(input, expect, 325))

    def test326_index_1D_ops(self):
        input = """
        func main()
        begin
            a[0] <- 5
            b[1] <- "string"
            c[3] <- 0.5e6
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(ArrayCell(Id(a),[NumLit(0.0)]),NumLit(5.0)),AssignStmt(ArrayCell(Id(b),[NumLit(1.0)]),StringLit(string)),AssignStmt(ArrayCell(Id(c),[NumLit(3.0)]),NumLit(500000.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 326))

    def test327_index_ND_ops(self):
        input = """
        func main()
        begin
            b[0,1] <- "string"
            c[1,2,3] <- 0.5e6
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(ArrayCell(Id(b),[NumLit(0.0),NumLit(1.0)]),StringLit(string)),AssignStmt(ArrayCell(Id(c),[NumLit(1.0),NumLit(2.0),NumLit(3.0)]),NumLit(500000.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 327))

    def test328_param_lit_call_expr(self):
        input = """
        func main()
        begin
            hello(1)
            good_boy("Sang","Kha")
            are_you_ok(true)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Call(Id(hello),[NumLit(1.0)]),Call(Id(good_boy),[StringLit(Sang),StringLit(Kha)]),Call(Id(are_you_ok),[BooleanLit(True)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 328))

    def test329_param_id_call_expr(self):
        input = """
        func main()
        begin
            hello(a)
            good_boy(b,e)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Call(Id(hello),[Id(a)]),Call(Id(good_boy),[Id(b),Id(e)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 329))

    def test330_nested_func_call(self):
        input = """
        func main()
        begin
            foo(foo(2),5,foo())
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Call(Id(foo),[CallExpr(Id(foo),[NumLit(2.0)]),NumLit(5.0),CallExpr(Id(foo),[])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 330))

    def test331_unary_operator(self):
        input = """
        func main()
        begin
            a <- -4
            a <- --4
            a <- not true
            a <- b[5]
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),UnaryOp(-,NumLit(4.0))),AssignStmt(Id(a),UnaryOp(-,UnaryOp(-,NumLit(4.0)))),AssignStmt(Id(a),UnaryOp(not,BooleanLit(True))),AssignStmt(Id(a),ArrayCell(Id(b),[NumLit(5.0)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 331))

    def test332_nested_array(self):
        input = """
        func main()
        begin
            a <- [1,2,3,[4,5,6]]
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),[NumLit(1.0),NumLit(2.0),NumLit(3.0),[NumLit(4.0),NumLit(5.0),NumLit(6.0)]])]))])"""
        self.assertTrue(TestAST.test(input, expect, 332))

    def test333_multivar_array(self):
        input = """
        func main()
        begin
            b <- a[1,2,3]
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(b),ArrayCell(Id(a),[NumLit(1.0),NumLit(2.0),NumLit(3.0)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 333))

    def test334_binary_operator(self):
        input = """
        func main()
        begin
            a <- 1*b
            a <- true and false
            a <- a==b
            a <- a!=b
            a <- (a...b)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(*,NumLit(1.0),Id(b))),AssignStmt(Id(a),BinaryOp(and,BooleanLit(True),BooleanLit(False))),AssignStmt(Id(a),BinaryOp(==,Id(a),Id(b))),AssignStmt(Id(a),BinaryOp(!=,Id(a),Id(b))),AssignStmt(Id(a),BinaryOp(...,Id(a),Id(b)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 334))

    def test335_complex_binary_operator(self):
        input = """
        func main()
        begin
            a <- a*b*c + a/b/c
            a <- a + b%c + d
            a <- a and b or a
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(*,BinaryOp(*,Id(a),Id(b)),Id(c)),BinaryOp(/,BinaryOp(/,Id(a),Id(b)),Id(c)))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(%,Id(b),Id(c))),Id(d))),AssignStmt(Id(a),BinaryOp(or,BinaryOp(and,Id(a),Id(b)),Id(a)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 335))

    def test336_complex_binary_operator_with_paren1(self):
        input = """
        func main()
        begin
            a <- a*b*(c+a)/b/c
            a <- a + (b%c + d)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(/,BinaryOp(/,BinaryOp(*,BinaryOp(*,Id(a),Id(b)),BinaryOp(+,Id(c),Id(a))),Id(b)),Id(c))),AssignStmt(Id(a),BinaryOp(+,Id(a),BinaryOp(+,BinaryOp(%,Id(b),Id(c)),Id(d))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 336))

    def test337_complex_binary_operator_with_paren2(self):
        input = """
        func main()
        begin
            a <- (a and b) or (a>=b and b)
            a <- (a + (-b - c*(d+e)))*5
            a <- a...((b...c)...d)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(or,BinaryOp(and,Id(a),Id(b)),BinaryOp(>=,Id(a),BinaryOp(and,Id(b),Id(b))))),AssignStmt(Id(a),BinaryOp(*,BinaryOp(+,Id(a),BinaryOp(-,UnaryOp(-,Id(b)),BinaryOp(*,Id(c),BinaryOp(+,Id(d),Id(e))))),NumLit(5.0))),AssignStmt(Id(a),BinaryOp(...,Id(a),BinaryOp(...,BinaryOp(...,Id(b),Id(c)),Id(d))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 337))

    def test338_numeric_left_to_right(self):
        input = """
        func main()
        begin
            a <- b*c/d%e
            a <- b+c-d+e
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(%,BinaryOp(/,BinaryOp(*,Id(b),Id(c)),Id(d)),Id(e))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(-,BinaryOp(+,Id(b),Id(c)),Id(d)),Id(e)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 338))

    def test339_logic_left_to_right(self):
        input = """
        func main()
        begin
            a <- b and c or d
            a <- b or c and d
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(or,BinaryOp(and,Id(b),Id(c)),Id(d))),AssignStmt(Id(a),BinaryOp(and,BinaryOp(or,Id(b),Id(c)),Id(d)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 339))

    def test340_relational_nonassoc(self):
        input = """
        func main()
        begin
            a <- b and c
            a <- b!=c
            a <- b>=c
            a <- b<=c
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(and,Id(b),Id(c))),AssignStmt(Id(a),BinaryOp(!=,Id(b),Id(c))),AssignStmt(Id(a),BinaryOp(>=,Id(b),Id(c))),AssignStmt(Id(a),BinaryOp(<=,Id(b),Id(c)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 340))

    def test341_string_nonassoc(self):
        input = """
        func main()
        begin
            a <- b...c
            a <- b...(c...d)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(...,Id(b),Id(c))),AssignStmt(Id(a),BinaryOp(...,Id(b),BinaryOp(...,Id(c),Id(d))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 341))

    def test342_funccall(self):
        input = """
        func main()
        begin
            t <- getA(a) ... getB(b)
            number x <- getX(x)
            a[1] <- getA1(a[0])
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(t),BinaryOp(...,CallExpr(Id(getA),[Id(a)]),CallExpr(Id(getB),[Id(b)]))),VarDecl(NumberType,Id(x),CallExpr(Id(getX),[Id(x)])),AssignStmt(ArrayCell(Id(a),[NumLit(1.0)]),CallExpr(Id(getA1),[ArrayCell(Id(a),[NumLit(0.0)])]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 342))

    def test343_full_order1(self):
        input = """
        func main()
        begin
            a <- -7+6/3/2*3-4%2
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(-,BinaryOp(+,UnaryOp(-,NumLit(7.0)),BinaryOp(*,BinaryOp(/,BinaryOp(/,NumLit(6.0),NumLit(3.0)),NumLit(2.0)),NumLit(3.0))),BinaryOp(%,NumLit(4.0),NumLit(2.0))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 343))

    def test344_full_order2(self):
        input = """
        func main()
        begin
            a <- (-a + not b) * e[6] and b  >= 6
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),BinaryOp(>=,BinaryOp(and,BinaryOp(*,BinaryOp(+,UnaryOp(-,Id(a)),UnaryOp(not,Id(b))),ArrayCell(Id(e),[NumLit(6.0)])),Id(b)),NumLit(6.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 344))

    ##### STATEMENTS #####
    def test345_scalar_asm(self):
        input = """
        func main()
        begin
            a <- 5
            b <- "ez"
            c <- 0.2e-3
            d <- [a,b,c,d]
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),NumLit(5.0)),AssignStmt(Id(b),StringLit(ez)),AssignStmt(Id(c),NumLit(0.0002)),AssignStmt(Id(d),[Id(a),Id(b),Id(c),Id(d)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 345))

    def test346_indexops_asm(self):
        input = """
        func main()
        begin
            a[0] <- 2
            a[1,2,3] <- 1
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(ArrayCell(Id(a),[NumLit(0.0)]),NumLit(2.0)),AssignStmt(ArrayCell(Id(a),[NumLit(1.0),NumLit(2.0),NumLit(3.0)]),NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 346))

    def test347_complex_asm(self):
        input = """
        func main()
        begin
            a[0] <- foo(1,2,"3")
            a[1,2] <- omg(omg(1))
            ez <- ez*2 + 6*(7-foo())
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(ArrayCell(Id(a),[NumLit(0.0)]),CallExpr(Id(foo),[NumLit(1.0),NumLit(2.0),StringLit(3)])),AssignStmt(ArrayCell(Id(a),[NumLit(1.0),NumLit(2.0)]),CallExpr(Id(omg),[CallExpr(Id(omg),[NumLit(1.0)])])),AssignStmt(Id(ez),BinaryOp(+,BinaryOp(*,Id(ez),NumLit(2.0)),BinaryOp(*,NumLit(6.0),BinaryOp(-,NumLit(7.0),CallExpr(Id(foo),[])))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 347))

    def test348_normal_if(self):
        input = """
        func main()
        begin
            if(is_easy("PPL")==true)
                begin
                    printString("de the co a")
                end
            else begin
                    printString("hoc lai di em")
                end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([If(BinaryOp(==,CallExpr(Id(is_easy),[StringLit(PPL)]),BooleanLit(True)),Block([Call(Id(printString),[StringLit(de the co a)])]),Block([Call(Id(printString),[StringLit(hoc lai di em)])]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 348))

    
    def test349_if_sequence(self):
        input = """
        func main()
        begin
            if(a)
                begin
                end
            elif (b)
                begin
                end
            else begin
                end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([If(Id(a),Block([]),Id(b),Block([]),Block([]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 349))

    def test350_if_nested1(self):
        input = """
        func main()
        begin
            if(calc_score(score)==9)
            begin
                printString("idolll :3")
            end
            else begin
                if (calc_score(score)==5)
                begin
                    printString("vua du qua mon :")
                end
                else begin
                    printString("doan xem")
                end
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([If(BinaryOp(==,CallExpr(Id(calc_score),[Id(score)]),NumLit(9.0)),Block([Call(Id(printString),[StringLit(idolll :3)])]),Block([If(BinaryOp(==,CallExpr(Id(calc_score),[Id(score)]),NumLit(5.0)),Block([Call(Id(printString),[StringLit(vua du qua mon :)])]),Block([Call(Id(printString),[StringLit(doan xem)])]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test351_if_nested2(self):
        input = """
        func main()
        begin
            if(rich==true)
            begin
                if(nice==true)
                begin
                    setState("kind and rich")
                end
                else setState("unkind and rich")
            end 
            else setState("not rich")
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([If(BinaryOp(==,Id(rich),BooleanLit(True)),Block([If(BinaryOp(==,Id(nice),BooleanLit(True)),Block([Call(Id(setState),[StringLit(kind and rich)])]),Call(Id(setState),[StringLit(unkind and rich)]))]),Call(Id(setState),[StringLit(not rich)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 351))

    def test352_if_oneline(self):
        input = """
        func main()
        begin
            if(happy) setHappy(true)
            else setHappy(false)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([If(Id(happy),Call(Id(setHappy),[BooleanLit(True)]),Call(Id(setHappy),[BooleanLit(False)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 352))

    def test353_if_oneline_nested(self):
        input = """
        func main()
        begin
            if(rich==true)
                if(nice==true)
                    setState("kind and rich")
                else setState("unkind and rich")
            else setState("not rich")
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([If(BinaryOp(==,Id(rich),BooleanLit(True)),If(BinaryOp(==,Id(nice),BooleanLit(True)),Call(Id(setState),[StringLit(kind and rich)]),Call(Id(setState),[StringLit(unkind and rich)])),Call(Id(setState),[StringLit(not rich)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 353))

    def test354_normal_loop(self):
        input = """
        func main()
        begin
            for i until i<=5 by i+2
            begin
                printNumber("Yoooo!")
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([For(Id(i),BinaryOp(<=,Id(i),NumLit(5.0)),BinaryOp(+,Id(i),NumLit(2.0)),Block([Call(Id(printNumber),[StringLit(Yoooo!)])]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 354))

    def test355_nested_forloop(self):
        input = """
        func main()
        begin
            for i until i<5*2 by i+2
            begin
                for j until j<5*2 by j+1
                begin
                    printNumber(i+j)
                end
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([For(Id(i),BinaryOp(<,Id(i),BinaryOp(*,NumLit(5.0),NumLit(2.0))),BinaryOp(+,Id(i),NumLit(2.0)),Block([For(Id(j),BinaryOp(<,Id(j),BinaryOp(*,NumLit(5.0),NumLit(2.0))),BinaryOp(+,Id(j),NumLit(1.0)),Block([Call(Id(printNumber),[BinaryOp(+,Id(i),Id(j))])]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 355))

    def test356_normal_while(self):
        input = """
        func main()
        begin
            if (a<5)
            begin
                printNumber(a)
                a <- a+1
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([If(BinaryOp(<,Id(a),NumLit(5.0)),Block([Call(Id(printNumber),[Id(a)]),AssignStmt(Id(a),BinaryOp(+,Id(a),NumLit(1.0)))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 356))

    def test357_nested_while(self):
        input = """
        func main()
        begin
            number a <- 0
            if (match(a)<10)
                printNumber(a)
            elif (match(a)*match(a)<69)
                printNumber(10-a)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([VarDecl(NumberType,Id(a),NumLit(0.0)),If(BinaryOp(<,CallExpr(Id(match),[Id(a)]),NumLit(10.0)),Call(Id(printNumber),[Id(a)]),BinaryOp(<,BinaryOp(*,CallExpr(Id(match),[Id(a)]),CallExpr(Id(match),[Id(a)])),NumLit(69.0)),Call(Id(printNumber),[BinaryOp(-,NumLit(10.0),Id(a))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 357))

    def test358_normal_dowhile(self):
        input = """
        func boolean () 
        begin
            if (a[10] >= 100 ) a <- a + 1
            elif (a[1,1] == 10)  writeNumber(1)
            elif (a[-1, 10]  or false) b[-1] <- 10
            else return foo(2 + 2)
        end
        """
        expect = """Program([FuncDecl(Id(boolean),[],Block([If(BinaryOp(>=,ArrayCell(Id(a),[NumLit(10.0)]),NumLit(100.0)),AssignStmt(Id(a),BinaryOp(+,Id(a),NumLit(1.0))),BinaryOp(==,ArrayCell(Id(a),[NumLit(1.0),NumLit(1.0)]),NumLit(10.0)),Call(Id(writeNumber),[NumLit(1.0)]),BinaryOp(or,ArrayCell(Id(a),[UnaryOp(-,NumLit(1.0)),NumLit(10.0)]),BooleanLit(False)),AssignStmt(ArrayCell(Id(b),[UnaryOp(-,NumLit(1.0))]),NumLit(10.0)),Return(CallExpr(Id(foo),[BinaryOp(+,NumLit(2.0),NumLit(2.0))])))]))])"""
        self.assertTrue(TestAST.test(input, expect, 358))

    def test359_nested_block(self):
        input = """
        ## khai bao ham func
        func integer () 
        begin
            begin
            begin
                if (a[10] >= 100 )
                if (a[1,1] == 10)  printInteger(1)
                else if (a[-1, 10]  or false) b[-1] <- 10
            end
            end
        end
        """
        expect = """Program([FuncDecl(Id(integer),[],Block([Block([Block([If(BinaryOp(>=,ArrayCell(Id(a),[NumLit(10.0)]),NumLit(100.0)),If(BinaryOp(==,ArrayCell(Id(a),[NumLit(1.0),NumLit(1.0)]),NumLit(10.0)),Call(Id(printInteger),[NumLit(1.0)]),If(BinaryOp(or,ArrayCell(Id(a),[UnaryOp(-,NumLit(1.0)),NumLit(10.0)]),BooleanLit(False)),AssignStmt(ArrayCell(Id(b),[UnaryOp(-,NumLit(1.0))]),NumLit(10.0)))))])])]))])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    
    def test360_break_and_return(self):
        input = """
        func main()
        begin
            for i until i<2 by i+1
            begin
                if(i==t)
                    break
                elif(i<0)
                    continue
                else printNumber(i)
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([For(Id(i),BinaryOp(<,Id(i),NumLit(2.0)),BinaryOp(+,Id(i),NumLit(1.0)),Block([If(BinaryOp(==,Id(i),Id(t)),Break,BinaryOp(<,Id(i),NumLit(0.0)),Continue,Call(Id(printNumber),[Id(i)]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    
    def test361_mixed_loop(self):
        input = """
        func main()
        begin
            for i until i<getMax() by i+1
            begin
                if (true)
                begin
                    print("kaka")
                end
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([For(Id(i),BinaryOp(<,Id(i),CallExpr(Id(getMax),[])),BinaryOp(+,Id(i),NumLit(1.0)),Block([If(BooleanLit(True),Block([Call(Id(print),[StringLit(kaka)])]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 361))
        
    def test362_oneline_loop(self):
        input = """
        func main()
        begin
            number k <- 5
            for i until i<getMax() by i+1
                printNumber(i)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([VarDecl(NumberType,Id(k),NumLit(5.0)),For(Id(i),BinaryOp(<,Id(i),CallExpr(Id(getMax),[])),BinaryOp(+,Id(i),NumLit(1.0)),Call(Id(printNumber),[Id(i)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    
    def test363_normal_call(self):
        input = """
        func main()
        begin
            hello()
            hello("Sang")
            hello("Sang","Kha")
            hello(hello("Sang"),"Kha")
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Call(Id(hello),[]),Call(Id(hello),[StringLit(Sang)]),Call(Id(hello),[StringLit(Sang),StringLit(Kha)]),Call(Id(hello),[CallExpr(Id(hello),[StringLit(Sang)]),StringLit(Kha)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 363))

    def test364_nested_call(self):
        input = """
        func main()
        begin
            f(f())
            f(f(f(f(f()))))
            f(f(f(f(f(f())))),f(f(f(f(f())))))
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Call(Id(f),[CallExpr(Id(f),[])]),Call(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[])])])])]),Call(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[])])])])]),CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[CallExpr(Id(f),[])])])])])])]))])"""    
        self.assertTrue(TestAST.test(input, expect, 364))
    
    def test365_expr_call(self):
        input = """
        func main()
        begin   
            f(1*x,_123,"sss"..."aaa",dsa("dsa"),x%5)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Call(Id(f),[BinaryOp(*,NumLit(1.0),Id(x)),Id(_123),BinaryOp(...,StringLit(sss),StringLit(aaa)),CallExpr(Id(dsa),[StringLit(dsa)]),BinaryOp(%,Id(x),NumLit(5.0))])]))])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test366_normal_block(self):
        input = """
        func main()
        begin
            begin
            end
            begin 
                hello()
            end
            begin 
                number a <- 1
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Block([]),Block([Call(Id(hello),[])]),Block([VarDecl(NumberType,Id(a),NumLit(1.0))])]))])"""
        self.assertTrue(TestAST.test(input, expect, 366))

    def test367_normal_return(self):
        input = """
            func hello()
            begin
                printString("hello")
            end
            func one (number x)
            begin
                return 1
            end
        """
        expect = """Program([FuncDecl(Id(hello),[],Block([Call(Id(printString),[StringLit(hello)])])),FuncDecl(Id(one),[VarDecl(NumberType,Id(x))],Block([Return(NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 367))
    
    def test368_complex_return(self):
        input = """
            func isOdd(number x)
            begin
                return x!=0
            end
            func getArr(number x)
            begin
                return [x,x*2,x*3]
            end
        """
        expect = """Program([FuncDecl(Id(isOdd),[VarDecl(NumberType,Id(x))],Block([Return(BinaryOp(!=,Id(x),NumLit(0.0)))])),FuncDecl(Id(getArr),[VarDecl(NumberType,Id(x))],Block([Return([Id(x),BinaryOp(*,Id(x),NumLit(2.0)),BinaryOp(*,Id(x),NumLit(3.0))])]))])"""
        self.assertTrue(TestAST.test(input, expect, 368))
    
    def test369_single_if(self):
        input = """
        func main()
        begin   
            if(a==1) return 1
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([If(BinaryOp(==,Id(a),NumLit(1.0)),Return(NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 369))
    
    def test370_empty_loops(self):
        input = """
        func main()
        begin   
            for i until i<5 by i+1
            begin 
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([For(Id(i),BinaryOp(<,Id(i),NumLit(5.0)),BinaryOp(+,Id(i),NumLit(1.0)),Block([]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 370))
    
    def test371_idx_for_loops(self):
        input = """
        func main()
        begin   
            begin
                for i until v < 10 by 1
                    return a
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Block([For(Id(i),BinaryOp(<,Id(v),NumLit(10.0)),NumLit(1.0),Return(Id(a)))])]))])"""
        self.assertTrue(TestAST.test(input, expect, 371))
    
    def test372_idx_for_loops(self):
        input = """
        func main()
        begin   
            var i <- 5
            for i until i<5 by i+1 
                begin 
                end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([VarDecl(var,Id(i),NumLit(5.0)),For(Id(i),BinaryOp(<,Id(i),NumLit(5.0)),BinaryOp(+,Id(i),NumLit(1.0)),Block([]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 372))
    
    def test373_if_stmt_1(self):
        input = """func integer () 
        begin
            break
            if (true) a <- 1 + 1
            else b <- b
        end
        """
        expect = """Program([FuncDecl(Id(integer),[],Block([Break,If(BooleanLit(True),AssignStmt(Id(a),BinaryOp(+,NumLit(1.0),NumLit(1.0))),AssignStmt(Id(b),Id(b)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 373))
    
    def test374_if_nested_2(self):
        input = """func integer () 
        begin
            if (a + 1 and true)
                if (a + 1 and true)
                    if (a + 1 and true)
                        if (a + 1 and true)
                            if (a + 1 and true)
                                continue
        end
        """
        expect = """Program([FuncDecl(Id(integer),[],Block([If(BinaryOp(and,BinaryOp(+,Id(a),NumLit(1.0)),BooleanLit(True)),If(BinaryOp(and,BinaryOp(+,Id(a),NumLit(1.0)),BooleanLit(True)),If(BinaryOp(and,BinaryOp(+,Id(a),NumLit(1.0)),BooleanLit(True)),If(BinaryOp(and,BinaryOp(+,Id(a),NumLit(1.0)),BooleanLit(True)),If(BinaryOp(and,BinaryOp(+,Id(a),NumLit(1.0)),BooleanLit(True)),Continue)))))]))])"""
        self.assertTrue(TestAST.test(input, expect, 374))

    #### MIXED CASES #####
    def test375_simple_program(self):
        """Simple program"""
        input = """func main ()
        begin
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([]))])"""
        self.assertTrue(TestAST.test(input, expect, 375))

    def test376_more_complex_program(self):
        """More complex program"""
        input = """func main ()
        begin
            printNumber(4)
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([Call(Id(printNumber),[NumLit(4.0)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    
    def test377_full_decl_program(self):
        input = """
        number i <- 6
        func main ()
            begin
                number x <- 7
            end
        number j <- 8
        func foo ()
            begin
                number y <- 8
            end
        """
        expect = """Program([VarDecl(NumberType,Id(i),NumLit(6.0)),FuncDecl(Id(main),[],Block([VarDecl(NumberType,Id(x),NumLit(7.0))])),VarDecl(NumberType,Id(j),NumLit(8.0)),FuncDecl(Id(foo),[],Block([VarDecl(NumberType,Id(y),NumLit(8.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 377))
    
    def test378_full_stmt_program_1(self):
        input = """func main ()
        begin
            ## cond stmt
            if (a>1)
            begin
                a <- 1
            end
            elif (a<1)
            begin
                a <- 0
            end
            else begin
                a <- 0.5
            end
            ## iter stmt
            if (a>0)
            begin
                a <- a*0.4
                print(a)
                if (a<1) break
            end
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([If(BinaryOp(>,Id(a),NumLit(1.0)),Block([AssignStmt(Id(a),NumLit(1.0))]),BinaryOp(<,Id(a),NumLit(1.0)),Block([AssignStmt(Id(a),NumLit(0.0))]),Block([AssignStmt(Id(a),NumLit(0.5))])),If(BinaryOp(>,Id(a),NumLit(0.0)),Block([AssignStmt(Id(a),BinaryOp(*,Id(a),NumLit(0.4))),Call(Id(print),[Id(a)]),If(BinaryOp(<,Id(a),NumLit(1.0)),Break)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test379_full_stmt_program_2(self):
        input = """func main ()
        begin
            number a
            if (a>0)
                for a  until a>0 by a-1
                    if (a>5) print("a>5")
                    else continue
        end
        """
        expect = """Program([FuncDecl(Id(main),[],Block([VarDecl(NumberType,Id(a)),If(BinaryOp(>,Id(a),NumLit(0.0)),For(Id(a),BinaryOp(>,Id(a),NumLit(0.0)),BinaryOp(-,Id(a),NumLit(1.0)),If(BinaryOp(>,Id(a),NumLit(5.0)),Call(Id(print),[StringLit(a>5)]),Continue)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 379))

    def test380_binary_search(self):
        input = """
            func binarySearch (number arr, number x, number low, number high)
            begin
                if (low>high) return -1
                else begin
                    number mid <- (low+high)/2
                    if (x == arr[mid]) return mid
                    else if (x > arr[mid]) return binarySearch(arr,x,mid+1,high)
                    else return binarySearch(arr,x,low,mid-1)
                end
            end
        """
        expect = """Program([FuncDecl(Id(binarySearch),[VarDecl(NumberType,Id(arr)),VarDecl(NumberType,Id(x)),VarDecl(NumberType,Id(low)),VarDecl(NumberType,Id(high))],Block([If(BinaryOp(>,Id(low),Id(high)),Return(UnaryOp(-,NumLit(1.0))),Block([VarDecl(NumberType,Id(mid),BinaryOp(/,BinaryOp(+,Id(low),Id(high)),NumLit(2.0))),If(BinaryOp(==,Id(x),ArrayCell(Id(arr),[Id(mid)])),Return(Id(mid)),If(BinaryOp(>,Id(x),ArrayCell(Id(arr),[Id(mid)])),Return(CallExpr(Id(binarySearch),[Id(arr),Id(x),BinaryOp(+,Id(mid),NumLit(1.0)),Id(high)])),Return(CallExpr(Id(binarySearch),[Id(arr),Id(x),Id(low),BinaryOp(-,Id(mid),NumLit(1.0))]))))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 380))

    def test381_interpolation_search(self):
        input = """
            func interpolationSearch(number arr, number lo, number hi, number x)
            begin
                if ((lo <= hi) and (x >= arr[lo]) and (x <= arr[hi]))
                begin
                    ## Probing the position with keeping
                    ## uniform distribution in mind.
                    pos <- lo + ((hi - lo) / (arr[hi] - arr[lo]) * (x - arr[lo]))
                    
                    ## Condition of target found
                    if (arr[pos] == x)
                        return pos
            
                    ## If x is larger, x is in right subarray
                    if (arr[pos] < x)
                        return interpolationSearch(arr, pos + 1, hi, x)
            
                    ## If x is smaller, x is in left subarray
                    if (arr[pos] > x)
                        return interpolationSearch(arr, lo, pos - 1, x)
                end
            return -1
            end
        """
        expect = """Program([FuncDecl(Id(interpolationSearch),[VarDecl(NumberType,Id(arr)),VarDecl(NumberType,Id(lo)),VarDecl(NumberType,Id(hi)),VarDecl(NumberType,Id(x))],Block([If(BinaryOp(and,BinaryOp(and,BinaryOp(<=,Id(lo),Id(hi)),BinaryOp(>=,Id(x),ArrayCell(Id(arr),[Id(lo)]))),BinaryOp(<=,Id(x),ArrayCell(Id(arr),[Id(hi)]))),Block([AssignStmt(Id(pos),BinaryOp(+,Id(lo),BinaryOp(*,BinaryOp(/,BinaryOp(-,Id(hi),Id(lo)),BinaryOp(-,ArrayCell(Id(arr),[Id(hi)]),ArrayCell(Id(arr),[Id(lo)]))),BinaryOp(-,Id(x),ArrayCell(Id(arr),[Id(lo)]))))),If(BinaryOp(==,ArrayCell(Id(arr),[Id(pos)]),Id(x)),Return(Id(pos))),If(BinaryOp(<,ArrayCell(Id(arr),[Id(pos)]),Id(x)),Return(CallExpr(Id(interpolationSearch),[Id(arr),BinaryOp(+,Id(pos),NumLit(1.0)),Id(hi),Id(x)]))),If(BinaryOp(>,ArrayCell(Id(arr),[Id(pos)]),Id(x)),Return(CallExpr(Id(interpolationSearch),[Id(arr),Id(lo),BinaryOp(-,Id(pos),NumLit(1.0)),Id(x)])))])),Return(UnaryOp(-,NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 381))

    def test382_selection_sort(self):
        input = """
            func selectionSort(number arr, number n)
            begin
                number i 
                number j 
                number min_idx 
                ## One by one move boundary of
                ## unsorted subarray
                for i until i < n-1 by i+1
                begin
                    ## Find the minimum element in
                    ## unsorted array
                    min_idx <- i
                    for j until j < n by j+1
                    begin
                        if (arr[j] < arr[min_idx])
                            min_idx <- j
                    end
                    ## Swap the found minimum element
                    ## with the first element
                    if (min_idx!=i)
                        swap(arr[min_idx], arr[i])
                end
            end
        """
        expect = """Program([FuncDecl(Id(selectionSort),[VarDecl(NumberType,Id(arr)),VarDecl(NumberType,Id(n))],Block([VarDecl(NumberType,Id(i)),VarDecl(NumberType,Id(j)),VarDecl(NumberType,Id(min_idx)),For(Id(i),BinaryOp(<,Id(i),BinaryOp(-,Id(n),NumLit(1.0))),BinaryOp(+,Id(i),NumLit(1.0)),Block([AssignStmt(Id(min_idx),Id(i)),For(Id(j),BinaryOp(<,Id(j),Id(n)),BinaryOp(+,Id(j),NumLit(1.0)),Block([If(BinaryOp(<,ArrayCell(Id(arr),[Id(j)]),ArrayCell(Id(arr),[Id(min_idx)])),AssignStmt(Id(min_idx),Id(j)))])),If(BinaryOp(!=,Id(min_idx),Id(i)),Call(Id(swap),[ArrayCell(Id(arr),[Id(min_idx)]),ArrayCell(Id(arr),[Id(i)])]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 382))

    def test383_merge_sort(self):
        input = """
            func mergeSort (number y[100], number n, number m)
            begin
                if (m > n)
                    return 
                ## Returns recursively
            
                var mid <- m + (n - m) / 2
                mergeSort(arr, m, mid)
                mergeSort(arr, mid + 1, n)
                merge(arr, m, mid, n)
            end
        """
        expect = """Program([FuncDecl(Id(mergeSort),[VarDecl(ArrayType([100],NumberType),Id(y)),VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(m))],Block([If(BinaryOp(>,Id(m),Id(n)),Return()),VarDecl(var,Id(mid),BinaryOp(+,Id(m),BinaryOp(/,BinaryOp(-,Id(n),Id(m)),NumLit(2.0)))),Call(Id(mergeSort),[Id(arr),Id(m),Id(mid)]),Call(Id(mergeSort),[Id(arr),BinaryOp(+,Id(mid),NumLit(1.0)),Id(n)]),Call(Id(merge),[Id(arr),Id(m),Id(mid),Id(n)])]))])"""
        self.assertTrue(TestAST.test(input, expect, 383))

    def test384_quick_sort(self):
        input = """
            func quickSort(number y[100], number n, number m)
            begin
                if (low < high) 
                begin
                    ## pi is partitioning index, arr[p] is now at right place
                    number pi <- partition(arr, low, high)
            
                    ## Separately sort elements before
                    ## partition and after partition
                    quickSort(arr, low, pi - 1)
                    quickSort(arr, pi + 1, high)
                end
            end
        """
        expect = """Program([FuncDecl(Id(quickSort),[VarDecl(ArrayType([100],NumberType),Id(y)),VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(m))],Block([If(BinaryOp(<,Id(low),Id(high)),Block([VarDecl(NumberType,Id(pi),CallExpr(Id(partition),[Id(arr),Id(low),Id(high)])),Call(Id(quickSort),[Id(arr),Id(low),BinaryOp(-,Id(pi),NumLit(1.0))]),Call(Id(quickSort),[Id(arr),BinaryOp(+,Id(pi),NumLit(1.0)),Id(high)])]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 384))

    def test385_heap_sort(self):
        input = """
            func heapSort(number y[100], number n, number m)
            begin
                ## Build heap (rearrange array)
                for i until i >= 0 by i-1
                    heapify(arr, N, i)
            
                ## One by one extract an element
                ## from heap
                for i until i > 0 by i-1 
                begin
                    ## Move current root to end
                    swap(arr[0], arr[i])
            
                    ## call max heapify on the reduced heap
                    heapify(arr, i, 0)
                end
            end
        """
        expect = """Program([FuncDecl(Id(heapSort),[VarDecl(ArrayType([100],NumberType),Id(y)),VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(m))],Block([For(Id(i),BinaryOp(>=,Id(i),NumLit(0.0)),BinaryOp(-,Id(i),NumLit(1.0)),Call(Id(heapify),[Id(arr),Id(N),Id(i)])),For(Id(i),BinaryOp(>,Id(i),NumLit(0.0)),BinaryOp(-,Id(i),NumLit(1.0)),Block([Call(Id(swap),[ArrayCell(Id(arr),[NumLit(0.0)]),ArrayCell(Id(arr),[Id(i)])]),Call(Id(heapify),[Id(arr),Id(i),NumLit(0.0)])]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 385))

    def test386_insertion_sort(self):
        input = """
            func insertionSort(number y[100], number n, number m)
            begin
                number i
                number key
                var j <- 2
                for i until i < n by i+1
                begin
                    key <- arr[i]
                    j <- i - 1
            
                    ## Move elements of arr[0..i-1], 
                    ## that are greater than key, to one
                    ## position ahead of their
                    ## current position
                    if ((j >= 0) and (arr[j] > key))
                    begin
                        arr[j + 1] <- arr[j]
                        j <- j - 1
                    end
                    arr[j + 1] <- key
                end
            end
        """
        expect = """Program([FuncDecl(Id(insertionSort),[VarDecl(ArrayType([100],NumberType),Id(y)),VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(m))],Block([VarDecl(NumberType,Id(i)),VarDecl(NumberType,Id(key)),VarDecl(var,Id(j),NumLit(2.0)),For(Id(i),BinaryOp(<,Id(i),Id(n)),BinaryOp(+,Id(i),NumLit(1.0)),Block([AssignStmt(Id(key),ArrayCell(Id(arr),[Id(i)])),AssignStmt(Id(j),BinaryOp(-,Id(i),NumLit(1.0))),If(BinaryOp(and,BinaryOp(>=,Id(j),NumLit(0.0)),BinaryOp(>,ArrayCell(Id(arr),[Id(j)]),Id(key))),Block([AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),NumLit(1.0))]),ArrayCell(Id(arr),[Id(j)])),AssignStmt(Id(j),BinaryOp(-,Id(j),NumLit(1.0)))])),AssignStmt(ArrayCell(Id(arr),[BinaryOp(+,Id(j),NumLit(1.0))]),Id(key))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 386))

    def test387_find_depth_tree(self):
        input = """
            func findDepthRec(number y[100], number n, number m)
            begin
                if ((index >= n) or (tree[index] == "l"))
                    return 0
            
                ## calc height of left subtree (In preorder
                ## left subtree is processed before right)
                index <- index+1
                number left <-  findDepthRec(tree, n, index)
            
                ## calc height of right subtree
                index <- index+1
                number right  <-  findDepthRec(tree, n, index)
            
                return max(left, right) + 1
            end
            func findDepth(number y[100], number n, number m)
            begin
                number index  <-  0
                return findDepthRec(tree, n, index)
            end
        """
        expect = """Program([FuncDecl(Id(findDepthRec),[VarDecl(ArrayType([100],NumberType),Id(y)),VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(m))],Block([If(BinaryOp(or,BinaryOp(>=,Id(index),Id(n)),BinaryOp(==,ArrayCell(Id(tree),[Id(index)]),StringLit(l))),Return(NumLit(0.0))),AssignStmt(Id(index),BinaryOp(+,Id(index),NumLit(1.0))),VarDecl(NumberType,Id(left),CallExpr(Id(findDepthRec),[Id(tree),Id(n),Id(index)])),AssignStmt(Id(index),BinaryOp(+,Id(index),NumLit(1.0))),VarDecl(NumberType,Id(right),CallExpr(Id(findDepthRec),[Id(tree),Id(n),Id(index)])),Return(BinaryOp(+,CallExpr(Id(max),[Id(left),Id(right)]),NumLit(1.0)))])),FuncDecl(Id(findDepth),[VarDecl(ArrayType([100],NumberType),Id(y)),VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(m))],Block([VarDecl(NumberType,Id(index),NumLit(0.0)),Return(CallExpr(Id(findDepthRec),[Id(tree),Id(n),Id(index)]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 387))

    def test388_lcs(self):
        input = """
            func lcs (number x[100], number y[100], number n, number m)
            begin
                if ((m == 0) or (n == 0))
                    return 0
                if (X[m-1] == Y[n-1])
                    return 1 + lcs(X, Y, m-1, n-1)
                else return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))
            end
        """
        expect = """Program([FuncDecl(Id(lcs),[VarDecl(ArrayType([100],NumberType),Id(x)),VarDecl(ArrayType([100],NumberType),Id(y)),VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(m))],Block([If(BinaryOp(or,BinaryOp(==,Id(m),NumLit(0.0)),BinaryOp(==,Id(n),NumLit(0.0))),Return(NumLit(0.0))),If(BinaryOp(==,ArrayCell(Id(X),[BinaryOp(-,Id(m),NumLit(1.0))]),ArrayCell(Id(Y),[BinaryOp(-,Id(n),NumLit(1.0))])),Return(BinaryOp(+,NumLit(1.0),CallExpr(Id(lcs),[Id(X),Id(Y),BinaryOp(-,Id(m),NumLit(1.0)),BinaryOp(-,Id(n),NumLit(1.0))]))),Return(CallExpr(Id(max),[CallExpr(Id(lcs),[Id(X),Id(Y),Id(m),BinaryOp(-,Id(n),NumLit(1.0))]),CallExpr(Id(lcs),[Id(X),Id(Y),BinaryOp(-,Id(m),NumLit(1.0)),Id(n)])])))]))])"""
        self.assertTrue(TestAST.test(input, expect, 388))

    def test389_spiral_matrix(self):
        input = """
            func spiralPrint(number a[100, 100], number n, number m)
            begin
                number i <- -1
                number k <- 0
                var l <- 0
                ## k - starting row index
                ## m - ending row index
                ## l - starting column index
                ## n - ending column index
                ## i - iterator
                
            
                if ((k < m) and (l < n)) 
                begin
                    ## Print the first row
                    for i until i < n by i+1 
                    begin
                        printString(a[k,i])
                    end
                    k <- k+1
            
                    ## Print the last column
                    for i until i < m by i+1 
                    begin
                        printString(a[i,n-1])
                    end
                    n <- n-1
            
                    ## Print the last row from
                    if (k < m) 
                    begin
                        for i until i >= l by i-1 
                        begin
                            printString(a[m-1,i])
                        end
                        m <- m-1
                    end
            
                    ## Print the first column from
                    if (l < n) 
                    begin
                        for i until i >= k by i-1 
                        begin
                            printString(a[i,l])
                        end
                        l <- l+1
                    end
                end
            end
        """
        expect = """Program([FuncDecl(Id(spiralPrint),[VarDecl(ArrayType([100,100],NumberType),Id(a)),VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(m))],Block([VarDecl(NumberType,Id(i),UnaryOp(-,NumLit(1.0))),VarDecl(NumberType,Id(k),NumLit(0.0)),VarDecl(var,Id(l),NumLit(0.0)),If(BinaryOp(and,BinaryOp(<,Id(k),Id(m)),BinaryOp(<,Id(l),Id(n))),Block([For(Id(i),BinaryOp(<,Id(i),Id(n)),BinaryOp(+,Id(i),NumLit(1.0)),Block([Call(Id(printString),[ArrayCell(Id(a),[Id(k),Id(i)])])])),AssignStmt(Id(k),BinaryOp(+,Id(k),NumLit(1.0))),For(Id(i),BinaryOp(<,Id(i),Id(m)),BinaryOp(+,Id(i),NumLit(1.0)),Block([Call(Id(printString),[ArrayCell(Id(a),[Id(i),BinaryOp(-,Id(n),NumLit(1.0))])])])),AssignStmt(Id(n),BinaryOp(-,Id(n),NumLit(1.0))),If(BinaryOp(<,Id(k),Id(m)),Block([For(Id(i),BinaryOp(>=,Id(i),Id(l)),BinaryOp(-,Id(i),NumLit(1.0)),Block([Call(Id(printString),[ArrayCell(Id(a),[BinaryOp(-,Id(m),NumLit(1.0)),Id(i)])])])),AssignStmt(Id(m),BinaryOp(-,Id(m),NumLit(1.0)))])),If(BinaryOp(<,Id(l),Id(n)),Block([For(Id(i),BinaryOp(>=,Id(i),Id(k)),BinaryOp(-,Id(i),NumLit(1.0)),Block([Call(Id(printString),[ArrayCell(Id(a),[Id(i),Id(l)])])])),AssignStmt(Id(l),BinaryOp(+,Id(l),NumLit(1.0)))]))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 389))
        
    def test390_random_1_empty(self):
        input = """func main ()
        """
        expect = """Program([FuncDecl(Id(main),[])])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    
    def test391_random_2_id(self):
        input = """func main()
            begin
                a <- 1
                a <- b
                a[0] <- 1
            end
            """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),NumLit(1.0)),AssignStmt(Id(a),Id(b)),AssignStmt(ArrayCell(Id(a),[NumLit(0.0)]),NumLit(1.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 391))
        
    def test392_random_Numberlit1(self):
        input = """func main()
            begin
                a <- 1.e23
                b <- 10.21e2
            end
            """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),NumLit(1e+23)),AssignStmt(Id(b),NumLit(1021.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 392))
    
    def test393_random_4_vardecl_single_if(self):
        input = """func main()
            begin
                if (n == 1)  begin
                    number a
                    number b
                end
            end
            """
        expect = """Program([FuncDecl(Id(main),[],Block([If(BinaryOp(==,Id(n),NumLit(1.0)),Block([VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b))]))]))])"""
        self.assertTrue(TestAST.test(input, expect, 393))
    
    def test394_random_Numberlit2(self):
        input = """func main()
            begin
                a <- 1.1e23
                a <- 1.1e-23
                a <- -12.0
            end
            """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),NumLit(1.1e+23)),AssignStmt(Id(a),NumLit(1.1e-23)),AssignStmt(Id(a),UnaryOp(-,NumLit(12.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 394))
    
    def test395_random_stringlit1(self):
        input = """func main()
            begin
                a <- "abc\txyz"
            end
            """
        expect = r"""Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),StringLit(abc	xyz))]))])"""
        self.assertTrue(TestAST.test(input, expect, 395))
    
    def test396_random_stringlit2(self):
        input = r"""func main()
            begin
                a <- "abc\\nxyz"
            end
            """
        expect = r"""Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),StringLit(abc\\nxyz))]))])"""
        self.assertTrue(TestAST.test(input, expect, 396))
    
    def test397_ultimate_001(self):
        input = r"""func main()
            begin
                a <- -1.
            end
            """
        expect = """Program([FuncDecl(Id(main),[],Block([AssignStmt(Id(a),UnaryOp(-,NumLit(1.0)))]))])"""
        self.assertTrue(TestAST.test(input, expect, 397))
    
    def test398_ultimate_002(self):
        input = """number a[3]
        """ 
        expect = """Program([VarDecl(ArrayType([3],NumberType),Id(a))])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test399_ultimate_003(self):
        input = r"""func main()
            begin
                dynamic a <- 6
            end
            """
        expect = """Program([FuncDecl(Id(main),[],Block([VarDecl(dynamic,Id(a),NumLit(6.0))]))])"""
        self.assertTrue(TestAST.test(input, expect, 399))
    def test_AST_400(self):
        input = """func foo ()
        begin
            if (x > 0)
                if (y > 0)
                begin
                    printBoolean(x * y > 0)
                end
                elif (z > 0)
                    printBoolean(x * z > 0)
        end
        """
        expect = """Program([FuncDecl(Id(foo),[],Block([If(BinaryOp(>,Id(x),NumLit(0.0)),If(BinaryOp(>,Id(y),NumLit(0.0)),Block([Call(Id(printBoolean),[BinaryOp(>,BinaryOp(*,Id(x),Id(y)),NumLit(0.0))])]),BinaryOp(>,Id(z),NumLit(0.0)),Call(Id(printBoolean),[BinaryOp(>,BinaryOp(*,Id(x),Id(z)),NumLit(0.0))])))]))])"""
        self.assertTrue(TestAST.test(input, expect, 400))
        
    def test_498(self): 
        input = """var a <- 5
        number b <- 3.24e-2
        string c <- "Hello"
        bool d <- true 
        """
        expect = """Program([\
VarDecl(var,Id(a),NumLit(5.0)),\
VarDecl(NumberType,Id(b),NumLit(0.0324)),\
VarDecl(StringType,Id(c),StringLit(Hello)),\
VarDecl(BoolType,Id(d),BooleanLit(True))\
])"""
        self.assertTrue(TestAST.test(input,expect,498))
    
    def test_401(self): # CHANGED
        input = """string a <- "Hello,World"
        """
        expect = """Program([\
VarDecl(StringType,Id(a),StringLit(Hello,World))\
])"""
        self.assertTrue(TestAST.test(input,expect,401))
    
    def test_402(self): 
        input = """number a <- -123456789
        """
        expect = """Program([\
VarDecl(NumberType,Id(a),UnaryOp(-,NumLit(123456789.0)))\
])"""
        self.assertTrue(TestAST.test(input,expect,402))
    
    def test_403(self): # CHANGED
        input = """func main() begin
            string a <- "Hello"
            string b <- ",world!"
            string c <- a ... b
        end
        """
        expect = """Program([\
FuncDecl(Id(main),[],Block([VarDecl(StringType,Id(a),StringLit(Hello)),\
VarDecl(StringType,Id(b),StringLit(,world!)),\
VarDecl(StringType,Id(c),BinaryOp(...,Id(a),Id(b)))]))])"""
        self.assertTrue(TestAST.test(input,expect,403))
    
    def test_404(self): 
        input = """func foo(number n,number delta) begin
            n <- n + delta
            return
        end
        """
        expect = """Program([FuncDecl(Id(foo),[VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(delta))],Block([AssignStmt(Id(n),BinaryOp(+,Id(n),Id(delta))),Return()]))])"""
        self.assertTrue(TestAST.test(input,expect,404))
    
    def test_405(self): 
        input = """number abc
        """
        expect = """Program([\
VarDecl(NumberType,Id(abc))\
])"""
        self.assertTrue(TestAST.test(input,expect,405))
    
    def test_406(self): 
        input = """number a[2,3]
        """
        expect = """Program([\
VarDecl(ArrayType([2,3],NumberType),Id(a))\
])"""
        self.assertTrue(TestAST.test(input,expect,406))
    
    def test_407(self): 
        input = """number a <- 1
        number b <- 2
        number x <- 1.25
        """
        expect = """Program([\
VarDecl(NumberType,Id(a),NumLit(1.0)),\
VarDecl(NumberType,Id(b),NumLit(2.0)),\
VarDecl(NumberType,Id(x),NumLit(1.25))\
])"""
        self.assertTrue(TestAST.test(input,expect,407))
    def test_408(self): 
        input = """number i <- 0
        """
        expect = """Program([\
VarDecl(NumberType,Id(i),NumLit(0.0))\
])"""
        self.assertTrue(TestAST.test(input,expect,408))
    
    def test_409(self):
        input = """func foo() begin
        return
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[],Block([Return()]))\
])"""
        self.assertTrue(TestAST.test(input,expect,409))
    
    def test_410(self): 
        input = """string a
        number x
        """
        expect = """Program([\
VarDecl(StringType,Id(a)),\
VarDecl(NumberType,Id(x))\
])"""
        self.assertTrue(TestAST.test(input,expect,410))
        
    def test_411(self):
        input = """bool a <- true
        """
        expect = """Program([\
VarDecl(BoolType,Id(a),BooleanLit(True))\
])"""
        self.assertTrue(TestAST.test(input,expect,411))
    
    def test_412(self): 
        input = """number a[1] <- [2]
        """
        expect = """Program([\
VarDecl(ArrayType([1],NumberType),Id(a),[NumLit(2.0)])\
])"""
        self.assertTrue(TestAST.test(input,expect,412)) 
    
    def test_413(self): 
        input = """number a <- 1/2
        number b <- 20 + 30
        """
        expect = """Program([\
VarDecl(NumberType,Id(a),BinaryOp(/,NumLit(1.0),NumLit(2.0))),\
VarDecl(NumberType,Id(b),BinaryOp(+,NumLit(20.0),NumLit(30.0)))\
])"""
        self.assertTrue(TestAST.test(input,expect,413)) 
    
    def test_414(self): 
        input = """number a <- 12.
        number b <- 12e-4
        number c <- 0.23E+7
        """
        expect = """Program([\
VarDecl(NumberType,Id(a),NumLit(12.0)),\
VarDecl(NumberType,Id(b),NumLit(0.0012)),\
VarDecl(NumberType,Id(c),NumLit(2300000.0))\
])"""
        self.assertTrue(TestAST.test(input,expect,414))
    
    def test_415(self): 
        input = """func foo (number a) begin
            somefunc(b,c)
            return a + (-2018)
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a))],Block([Call(Id(somefunc),[Id(b),Id(c)]),Return(BinaryOp(+,Id(a),UnaryOp(-,NumLit(2018.0))))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,415))
    
    def test_416(self): 
        input = """number x
        func foo() begin 
            return 0
        end
        number a <- 10
        """
        expect = """Program([\
VarDecl(NumberType,Id(x)),\
FuncDecl(Id(foo),[],Block([Return(NumLit(0.0))])),\
VarDecl(NumberType,Id(a),NumLit(10.0))\
])"""
        self.assertTrue(TestAST.test(input,expect,416))
    
    def test_417(self): 
        input = """number x
        func foo () begin
            return 0
        end
        func goo () begin
            string i
        end
        """
        expect = """Program([\
VarDecl(NumberType,Id(x)),\
FuncDecl(Id(foo),[],Block([Return(NumLit(0.0))])),\
FuncDecl(Id(goo),[],Block([VarDecl(StringType,Id(i))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,417))
    
    def test_418(self): 
        input = """number x <- 10 - (2 + 3 * 4) / 7
        """
        expect = """Program([\
VarDecl(NumberType,Id(x),\
BinaryOp(-,NumLit(10.0),\
BinaryOp(/,\
BinaryOp(+,NumLit(2.0),\
BinaryOp(*,NumLit(3.0),NumLit(4.0))),NumLit(7.0))))\
])"""
        self.assertTrue(TestAST.test(input,expect,418))
    
    def test_419(self): 
        input = """bool x <- not ((2 < 3) and (3 < 4))
        """
        expect = """Program([\
VarDecl(BoolType,Id(x),\
UnaryOp(not,\
BinaryOp(and,\
BinaryOp(<,NumLit(2.0),NumLit(3.0)),\
BinaryOp(<,NumLit(3.0),NumLit(4.0)))))\
])"""
        self.assertTrue(TestAST.test(input,expect,419))
    
    def test_420(self):
        input = """func fact(number a) begin
            writeNumber(a + 2018)
        end
        func main() begin
            fact(2018)
        end
        """
        expect = """Program([\
FuncDecl(Id(fact),[VarDecl(NumberType,Id(a))],\
Block([Call(Id(writeNumber),[BinaryOp(+,Id(a),NumLit(2018.0))])])),\
FuncDecl(Id(main),[],Block([Call(Id(fact),[NumLit(2018.0)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,420))
    
    def test_421(self): 
        input = """func goo(number a,number b) begin
            var c <- a + 2 * b
            writeNumber(c)
        end
        func main() begin
            goo(3,2.7)
        end
        """
        expect = """Program([\
FuncDecl(Id(goo),[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b))],\
Block([VarDecl(var,Id(c),BinaryOp(+,Id(a),BinaryOp(*,NumLit(2.0),Id(b)))),\
Call(Id(writeNumber),[Id(c)])])),\
FuncDecl(Id(main),[],Block([Call(Id(goo),[NumLit(3.0),NumLit(2.7)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,421))
    
    def test_422(self): 
        input = """func goo(string a,number N) begin
            number i
            string s <- ""
            for i until i >= N by 1 begin
                s <- s ... a[i]
            end
            return s
        end
        func main() 
        begin
        end
        """
        expect = """Program([\
FuncDecl(Id(goo),[VarDecl(StringType,Id(a)),VarDecl(NumberType,Id(N))],\
Block([VarDecl(NumberType,Id(i)),VarDecl(StringType,Id(s),StringLit()),\
For(Id(i),BinaryOp(>=,Id(i),Id(N)),NumLit(1.0),\
Block([AssignStmt(Id(s),BinaryOp(...,Id(s),ArrayCell(Id(a),[Id(i)])))])),\
Return(Id(s))])),\
FuncDecl(Id(main),[],Block([]))\
])"""
        self.assertTrue(TestAST.test(input,expect,422))
        
    def test_499(self):
        input = """func goo() begin
            for i until i >= N by 1 begin
                s <- 1
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(goo),[],\
Block([For(Id(i),BinaryOp(>=,Id(i),Id(N)),NumLit(1.0),\
Block([AssignStmt(Id(s),NumLit(1.0))]))]))])\
"""
        self.assertTrue(TestAST.test(input,expect,499))
    '''
    def test_423(self): # CHANGED
        input = """func abc(number a,number b) begin
            var c <- 2 * a + b
            writeNumber(c)
        end
       func main(number a) begin
            abc(1,"hello")
        end
        """
        expect = """Program([
	FuncDecl(abc,[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b))],Block([VarDecl(var,c,BinaryOp(+,BinaryOp(*,NumLit(2),Id(a)),Id(b))),Call(Id(writeNumber),Id(c))]))
	FuncDecl(main,[VarDecl(NumberType,Id(a))],Block([Call(Id(abc),[NumLit(1),StringLit(hello)])]))
])"""
        self.assertTrue(TestAST.test(input,expect,423))
    '''
    def test_424(self): 
        input = """func main() begin
        end
        """
        expect = """Program([\
FuncDecl(Id(main),[],Block([]))\
])"""
        self.assertTrue(TestAST.test(input,expect,424))
    def test_425(self): 
        input = """bool a29872 <- not((2 < 3) and (3 < 4))
        """
        expect = """Program([\
VarDecl(BoolType,Id(a29872),UnaryOp(not,\
BinaryOp(and,\
BinaryOp(<,NumLit(2.0),NumLit(3.0)),\
BinaryOp(<,NumLit(3.0),NumLit(4.0)))))\
])"""
        self.assertTrue(TestAST.test(input,expect,425))
    
    def test_426(self): 
        input = """number a[12,3]
                   number x
                   """
        expect = """Program([\
VarDecl(ArrayType([12,3],NumberType),Id(a)),\
VarDecl(NumberType,Id(x))\
])"""
        self.assertTrue(TestAST.test(input,expect,426))
    def test_427(self):
        input = """number a[3,4,5]
                  number x <- -2.95
                  """
        expect = """Program([\
VarDecl(ArrayType([3,4,5],NumberType),Id(a)),\
VarDecl(NumberType,Id(x),UnaryOp(-,NumLit(2.95)))\
])"""
        self.assertTrue(TestAST.test(input,expect,427))
    
    def test_428(self): 
        input = """number a[2]
        number b[2]
        func main() begin
            a[0] <- 2018
            a[1] <- -2018
            b[0] <- a[0] + a[1]
            b[1] <- a[0] - a[1]
        end
        """
        expect = """Program([\
VarDecl(ArrayType([2],NumberType),Id(a)),\
VarDecl(ArrayType([2],NumberType),Id(b)),\
FuncDecl(Id(main),[],Block([AssignStmt(ArrayCell(Id(a),[NumLit(0.0)]),NumLit(2018.0)),AssignStmt(ArrayCell(Id(a),[NumLit(1.0)]),UnaryOp(-,NumLit(2018.0))),AssignStmt(ArrayCell(Id(b),[NumLit(0.0)]),BinaryOp(+,ArrayCell(Id(a),[NumLit(0.0)]),ArrayCell(Id(a),[NumLit(1.0)]))),AssignStmt(ArrayCell(Id(b),[NumLit(1.0)]),BinaryOp(-,ArrayCell(Id(a),[NumLit(0.0)]),ArrayCell(Id(a),[NumLit(1.0)])))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,428))
        
    def test_429(self): 
        input = """number i <- 20
        number j <- 30
        number k <- 12.3E-2
        """
        expect = """Program([\
VarDecl(NumberType,Id(i),NumLit(20.0)),\
VarDecl(NumberType,Id(j),NumLit(30.0)),\
VarDecl(NumberType,Id(k),NumLit(0.123))\
])"""
        self.assertTrue(TestAST.test(input,expect,429))
    
    def test_430(self): 
        input = """number i <- 20
        number j <- 30
        """
        expect = """Program([\
VarDecl(NumberType,Id(i),NumLit(20.0)),\
VarDecl(NumberType,Id(j),NumLit(30.0))\
])"""
        self.assertTrue(TestAST.test(input,expect,430))
    def test_431(self): 
        input = """number x <- 20
        dynamic a <- x + 3.7
        """
        expect = """Program([\
VarDecl(NumberType,Id(x),NumLit(20.0)),\
VarDecl(dynamic,Id(a),BinaryOp(+,Id(x),NumLit(3.7)))\
])"""
        self.assertTrue(TestAST.test(input,expect,431))
    
    def test_432(self): 
        input = """func foo(bool a,bool b) begin
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(BoolType,Id(a)),VarDecl(BoolType,Id(b))],Block([]))\
])"""
        self.assertTrue(TestAST.test(input,expect,432))
    def test_433(self): 
        input = """bool test_bool <- false
        """
        expect = """Program([\
VarDecl(BoolType,Id(test_bool),BooleanLit(False))\
])"""
        self.assertTrue(TestAST.test(input,expect,433))
    
    def test_434(self): # Special func error
        input = """number a <- 20
        func foo (number a) begin
            a <- a + 10
        end
        func main() begin
            foo(a_int)
            writeNumber(a_int)
        end
        """
        expect = """Program([\
VarDecl(NumberType,Id(a),NumLit(20.0)),\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a))],\
Block([AssignStmt(Id(a),BinaryOp(+,Id(a),NumLit(10.0)))])),\
FuncDecl(Id(main),[],\
Block([Call(Id(foo),[Id(a_int)]),Call(Id(writeNumber),[Id(a_int)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,434))
    
    def test_435(self): # CHANGED
        input = """number i <- 20
        number j <- 30
        number k <- 40
        func main() 
        begin
            i <- j + k
            writeNumber(i)
        end
        """
        expect = """Program([\
VarDecl(NumberType,Id(i),NumLit(20.0)),\
VarDecl(NumberType,Id(j),NumLit(30.0)),\
VarDecl(NumberType,Id(k),NumLit(40.0)),\
FuncDecl(Id(main),[],Block([AssignStmt(Id(i),BinaryOp(+,Id(j),Id(k))),Call(Id(writeNumber),[Id(i)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,435))
    
    def test_436(self): 
        input = """string i <- \"Hello,\"
        string j <- "'"this '""
        string k <- "'"world!'""
        func main()
        begin
            t <- i ... j
            writeString(t)
        end
        """
        expect = """Program([\
VarDecl(StringType,Id(i),StringLit(Hello,)),\
VarDecl(StringType,Id(j),StringLit('"this '")),\
VarDecl(StringType,Id(k),StringLit('"world!'")),\
FuncDecl(Id(main),[],Block([AssignStmt(Id(t),BinaryOp(...,Id(i),Id(j))),Call(Id(writeString),[Id(t)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,436))
    
    def test_437(self): 
        input = """string i <- "Baba"
        string j <- "Mama"
        func main()
        begin
            k <- j ... i
            t <- (k ... j) ... i
            l <- k ... (j ... i)
            writeString(t)
            writeString(l)
        end
        """
        expect = """Program([\
VarDecl(StringType,Id(i),StringLit(Baba)),\
VarDecl(StringType,Id(j),StringLit(Mama)),\
FuncDecl(Id(main),[],Block([AssignStmt(Id(k),BinaryOp(...,Id(j),Id(i))),\
AssignStmt(Id(t),BinaryOp(...,BinaryOp(...,Id(k),Id(j)),Id(i))),\
AssignStmt(Id(l),BinaryOp(...,Id(k),BinaryOp(...,Id(j),Id(i)))),\
Call(Id(writeString),[Id(t)]),\
Call(Id(writeString),[Id(l)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,437))
    
    def test_438(self): 
        input = """func main() begin
            a[3 + 5,2 * x] <- y[4] - 7
            return
        end
        """
        expect = """Program([\
FuncDecl(Id(main),[],Block([AssignStmt(ArrayCell(Id(a),[BinaryOp(+,NumLit(3.0),NumLit(5.0)),BinaryOp(*,NumLit(2.0),Id(x))]),BinaryOp(-,ArrayCell(Id(y),[NumLit(4.0)]),NumLit(7.0))),Return()]))\
])"""
        self.assertTrue(TestAST.test(input,expect,438))
    
    def test_439(self): 
        input = """func main() begin
            a[0] <- foo(2018) + goo(3)
            return
        end
        """
        expect = """Program([\
FuncDecl(Id(main),[],Block([AssignStmt(ArrayCell(Id(a),[NumLit(0.0)]),BinaryOp(+,CallExpr(Id(foo),[NumLit(2018.0)]),CallExpr(Id(goo),[NumLit(3.0)]))),Return()]))\
])"""
        self.assertTrue(TestAST.test(input,expect,439))

    def test_440(self):
        input = """number i <- 123.45
        number j <- 2.87e+22
        number k <- 2500000000.0
        """
        expect = """Program([\
VarDecl(NumberType,Id(i),NumLit(123.45)),\
VarDecl(NumberType,Id(j),NumLit(2.87e+22)),\
VarDecl(NumberType,Id(k),NumLit(2500000000.0))\
])"""
        self.assertTrue(TestAST.test(input,expect,440))
        
    def test_441(self): 
        input = """func main()
        
        begin
        
        
        
        end
        
        """
        expect = """Program([\
FuncDecl(Id(main),[],Block([]))\
])"""
        self.assertTrue(TestAST.test(input,expect,441))
        
    def test_442(self): 
        input = """func main() begin
            a[0] <- b[2,3] + foo(2) + (b[0,1] + goo(1))
            return
        end
        """
        expect = """Program([\
FuncDecl(Id(main),[],Block([AssignStmt(ArrayCell(Id(a),[NumLit(0.0)]),BinaryOp(+,BinaryOp(+,ArrayCell(Id(b),[NumLit(2.0),NumLit(3.0)]),CallExpr(Id(foo),[NumLit(2.0)])),BinaryOp(+,ArrayCell(Id(b),[NumLit(0.0),NumLit(1.0)]),CallExpr(Id(goo),[NumLit(1.0)])))),Return()]))\
])"""
        self.assertTrue(TestAST.test(input,expect,442))
    
    def test_443(self):
        input = """number a <- 20
                   var b <- a
                   """
        expect = """Program([\
VarDecl(NumberType,Id(a),NumLit(20.0)),\
VarDecl(var,Id(b),Id(a))\
])"""
        self.assertTrue(TestAST.test(input,expect,443))
    def test_444(self): 
        input = """number x[3] <- [1.0,2.0,3.0]
                   number a <- x[0] + x[1] + x[2]
                   """
        expect = """Program([\
VarDecl(ArrayType([3],NumberType),Id(x),[NumLit(1.0),NumLit(2.0),NumLit(3.0)]),\
VarDecl(NumberType,Id(a),BinaryOp(+,BinaryOp(+,ArrayCell(Id(x),[NumLit(0.0)]),ArrayCell(Id(x),[NumLit(1.0)])),ArrayCell(Id(x),[NumLit(2.0)])))\
])"""
        self.assertTrue(TestAST.test(input,expect,444))
    def test_445(self):
        input = """number x[2,3] <- [[1,5,8],[2,9,6]]
                   number a <- x[0,0] + x[0,1] + x[0,2] - x[1,0] - x[1,1] - x[1,2]
                   """
        expect = """Program([\
VarDecl(ArrayType([2,3],NumberType),Id(x),[[NumLit(1.0),NumLit(5.0),NumLit(8.0)],[NumLit(2.0),NumLit(9.0),NumLit(6.0)]]),\
VarDecl(NumberType,Id(a),BinaryOp(-,BinaryOp(-,BinaryOp(-,BinaryOp(+,BinaryOp(+,ArrayCell(Id(x),[NumLit(0.0),NumLit(0.0)]),ArrayCell(Id(x),[NumLit(0.0),NumLit(1.0)])),ArrayCell(Id(x),[NumLit(0.0),NumLit(2.0)])),ArrayCell(Id(x),[NumLit(1.0),NumLit(0.0)])),ArrayCell(Id(x),[NumLit(1.0),NumLit(1.0)])),ArrayCell(Id(x),[NumLit(1.0),NumLit(2.0)])))\
])"""
        self.assertTrue(TestAST.test(input,expect,445))
        
    def test_446(self): 
        input = """dynamic a
        """
        expect = """Program([\
VarDecl(dynamic,Id(a))\
])"""
        self.assertTrue(TestAST.test(input,expect,446))
    
    def test_447(self): 
        input = """number x
        number y
        bool z
        func goo(number x,number y) begin
        
        end
        number t[10]
        func foo() begin
            
        end
        string a <- "Hello World"
        """
        expect = """Program([\
VarDecl(NumberType,Id(x)),\
VarDecl(NumberType,Id(y)),\
VarDecl(BoolType,Id(z)),\
FuncDecl(Id(goo),[VarDecl(NumberType,Id(x)),\
VarDecl(NumberType,Id(y))],Block([])),\
VarDecl(ArrayType([10],NumberType),Id(t)),\
FuncDecl(Id(foo),[],Block([])),\
VarDecl(StringType,Id(a),StringLit(Hello World))\
])"""
        self.assertTrue(TestAST.test(input,expect,447))
    def test_448(self): 
        input = """var a <- 29.5e4
        var b <- true
        var c <- "Hello" 
        """
        expect = """Program([\
VarDecl(var,Id(a),NumLit(295000.0)),\
VarDecl(var,Id(b),BooleanLit(True)),\
VarDecl(var,Id(c),StringLit(Hello))\
])"""
        self.assertTrue(TestAST.test(input,expect,448))
    def test_449(self): 
        input = """func foo1(number a) begin
            super(x,y,z)
        end
        """
        expect = """Program([\
FuncDecl(Id(foo1),[VarDecl(NumberType,Id(a))],Block([Call(Id(super),[Id(x),Id(y),Id(z)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,449))
    def test_450(self):
        input = """number x <- 20
        number y <- 2 * x + 1
        """
        expect = """Program([\
VarDecl(NumberType,Id(x),NumLit(20.0)),\
VarDecl(NumberType,Id(y),BinaryOp(+,BinaryOp(*,NumLit(2.0),Id(x)),NumLit(1.0)))\
])"""
        self.assertTrue(TestAST.test(input,expect,450))
    
    def test_451(self):
        input = """string i <- "20"
        string j <- "30"
        string k <- "40"
        func main() 
        begin
            k <- j ... (i ... t)
            writeString(k)
        end
        """
        expect = """Program([\
VarDecl(StringType,Id(i),StringLit(20)),\
VarDecl(StringType,Id(j),StringLit(30)),\
VarDecl(StringType,Id(k),StringLit(40)),\
FuncDecl(Id(main),[],Block([AssignStmt(Id(k),BinaryOp(...,Id(j),BinaryOp(...,Id(i),Id(t)))),Call(Id(writeString),[Id(k)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,451))
    def test_452(self):
        input = """number x <- 65
        func fact(number n) begin
            if (n == 0) return 1
            else return n * fact(n - 1)
        end
        func inc(number n,number delta) begin
            n <- n + delta
        end
        func main() begin
            number delta <- fact(3)
            inc(x,delta)
            writeNumber(x)
        end
        """
        expect = """Program([\
VarDecl(NumberType,Id(x),NumLit(65.0)),\
FuncDecl(Id(fact),[VarDecl(NumberType,Id(n))],Block([If(BinaryOp(==,Id(n),NumLit(0.0)),Return(NumLit(1.0)),Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),NumLit(1.0))]))))])),\
FuncDecl(Id(inc),[VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(delta))],Block([AssignStmt(Id(n),BinaryOp(+,Id(n),Id(delta)))])),\
FuncDecl(Id(main),[],Block([VarDecl(NumberType,Id(delta),CallExpr(Id(fact),[NumLit(3.0)])),Call(Id(inc),[Id(x),Id(delta)]),Call(Id(writeNumber),[Id(x)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,452))

    def test_453(self):
        input = """number a[2,3] <- [[1,2,3],[4,5,6]]
        """
        expect = """Program([\
VarDecl(ArrayType([2,3],NumberType),Id(a),[[NumLit(1.0),NumLit(2.0),NumLit(3.0)],[NumLit(4.0),NumLit(5.0),NumLit(6.0)]])\
])"""
        self.assertTrue(TestAST.test(input,expect,453))
    
    def test_454(self):
        input = """func fibo(number n) begin
            if (n <= 2) return 1
            else return fibo(n - 1) + fibo(n - 2)
        end
            func main() begin
                writeNumber(fibo(20))
        end
        """
        expect = """Program([\
FuncDecl(Id(fibo),[VarDecl(NumberType,Id(n))],\
Block([If(BinaryOp(<=,Id(n),NumLit(2.0)),Return(NumLit(1.0)),\
Return(BinaryOp(+,\
CallExpr(Id(fibo),[BinaryOp(-,Id(n),NumLit(1.0))]),\
CallExpr(Id(fibo),[BinaryOp(-,Id(n),NumLit(2.0))]))))])),\
FuncDecl(Id(main),[],Block([Call(Id(writeNumber),[CallExpr(Id(fibo),[NumLit(20.0)])])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,454))
    
    def test_455(self):
        input = """func perfectNum(number N) begin
            if ((N == 6) or (N == 28) or (N == 496) or (N == 8128) or (N == 33550336))
            begin
                return true
            end
            return false
        end
        """
        expect = """Program([\
FuncDecl(Id(perfectNum),[VarDecl(NumberType,Id(N))],\
Block([If(BinaryOp(or,\
BinaryOp(or,\
BinaryOp(or,\
BinaryOp(or,\
BinaryOp(==,Id(N),NumLit(6.0)),\
BinaryOp(==,Id(N),NumLit(28.0))),\
BinaryOp(==,Id(N),NumLit(496.0))),\
BinaryOp(==,Id(N),NumLit(8128.0))),\
BinaryOp(==,Id(N),NumLit(33550336.0))),\
Block([Return(BooleanLit(True))])),\
Return(BooleanLit(False))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,455))
    
    def test_456(self):
        input = """func foo(number a) begin
            a <- a + (-2018)
            return a
        end
        func main() begin
            number a <- 2018
            a <- a + foo(a)
            readNumber()
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a))],\
Block([AssignStmt(Id(a),BinaryOp(+,Id(a),UnaryOp(-,NumLit(2018.0)))),\
Return(Id(a))])),\
FuncDecl(Id(main),[],\
Block([VarDecl(NumberType,Id(a),NumLit(2018.0)),\
AssignStmt(Id(a),BinaryOp(+,Id(a),CallExpr(Id(foo),[Id(a)]))),\
Call(Id(readNumber),[])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,456))
    
    def test_457(self):
        input = """number a[4]
        func main() begin
            number i
            for i until i >= 4 by 1 begin
                a[i] <- readNumber()
                writeNumber(a[i])
            end
        end
        """
        expect = """Program([\
VarDecl(ArrayType([4],NumberType),Id(a)),\
FuncDecl(Id(main),[],Block([VarDecl(NumberType,Id(i)),\
For(Id(i),BinaryOp(>=,Id(i),NumLit(4.0)),NumLit(1.0),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),CallExpr(Id(readNumber),[])),\
Call(Id(writeNumber),[ArrayCell(Id(a),[Id(i)])])]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,457))
    
    def test_458(self):
        input = """number a[4]
        func main() begin
            number i
            for i until i >= 4 by 1 begin
                a[i] <- 3 * readNumber()
                writeNumber(a[i])
            end
        end
        """
        expect = """Program([\
VarDecl(ArrayType([4],NumberType),Id(a)),\
FuncDecl(Id(main),[],\
Block([VarDecl(NumberType,Id(i)),\
For(Id(i),BinaryOp(>=,Id(i),NumLit(4.0)),NumLit(1.0),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),\
BinaryOp(*,NumLit(3.0),CallExpr(Id(readNumber),[]))),\
Call(Id(writeNumber),[ArrayCell(Id(a),[Id(i)])])]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,458))
    
    def test_459(self):
        input = """func main() begin
            number a[100]
            number i <- 0
            for i until i >= 100 by 1 begin
                a[i] <- readNumber()
                if (a[i] % 2 == 0)
                begin
                    a[i] <- a[i] / 2
                end
                else
                begin
                    a[i] <- a[i] * 3 + 1
                end
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(main),[],\
Block([VarDecl(ArrayType([100],NumberType),Id(a)),\
VarDecl(NumberType,Id(i),NumLit(0.0)),\
For(Id(i),BinaryOp(>=,Id(i),NumLit(100.0)),NumLit(1.0),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),CallExpr(Id(readNumber),[])),\
If(BinaryOp(==,BinaryOp(%,ArrayCell(Id(a),[Id(i)]),NumLit(2.0)),NumLit(0.0)),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),BinaryOp(/,ArrayCell(Id(a),[Id(i)]),NumLit(2.0)))]),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),[Id(i)]),NumLit(3.0)),NumLit(1.0)))]))]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,459))
    
    def test_460(self):
        input = """func main() begin
            number a[100]
            number i <- 0
            number n
            for i until i >= n by 1 begin
                a[i] <- readNumber()
                if (a[i] % 2 == 0)
                begin
                    a[i] <- a[i] / 2
                end
                else
                begin
                    a[i] <- a[i] * 3 + 1
                end
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(main),[],\
Block([VarDecl(ArrayType([100],NumberType),Id(a)),\
VarDecl(NumberType,Id(i),NumLit(0.0)),\
VarDecl(NumberType,Id(n)),\
For(Id(i),BinaryOp(>=,Id(i),Id(n)),NumLit(1.0),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),CallExpr(Id(readNumber),[])),\
If(BinaryOp(==,BinaryOp(%,ArrayCell(Id(a),[Id(i)]),NumLit(2.0)),NumLit(0.0)),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),BinaryOp(/,ArrayCell(Id(a),[Id(i)]),NumLit(2.0)))]),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),[Id(i)]),NumLit(3.0)),NumLit(1.0)))]))]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,460))
    
    def test_461(self):
        input = """func foo(number a[10]) begin
            return a
        end
        number b <- 20
        func main() begin
        return
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(ArrayType([10],NumberType),Id(a))],\
Block([Return(Id(a))])),\
VarDecl(NumberType,Id(b),NumLit(20.0)),\
FuncDecl(Id(main),[],Block([Return()]))\
])"""
        self.assertTrue(TestAST.test(input,expect,461))
    
    def test_462(self):
        input = """func foo(number a) begin
            if (a > 220) begin
                if (a % 2 == 0)
                begin
                    return a
                end
                else
                begin
                    return a + 1
                end
            end
            else
            begin
                return a + 10
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a))],\
Block([If(BinaryOp(>,Id(a),NumLit(220.0)),\
Block([If(BinaryOp(==,BinaryOp(%,Id(a),NumLit(2.0)),NumLit(0.0)),\
Block([Return(Id(a))]),\
Block([Return(BinaryOp(+,Id(a),NumLit(1.0)))]))]),\
Block([Return(BinaryOp(+,Id(a),NumLit(10.0)))]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,462))
    
    def test_463(self):
        input = """func foo() begin
            if (a < b)
                if (c < d)
                    writeString("True")
                else
                    writeString("False")
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[],\
Block([If(BinaryOp(<,Id(a),Id(b)),\
If(BinaryOp(<,Id(c),Id(d)),\
Call(Id(writeString),[StringLit(True)]),\
Call(Id(writeString),[StringLit(False)])))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,463))
    
    def test_464(self):
        input = """number x <- 2018
        func fact(number n) begin
            if (n == 0) return 1
            else return n * fact(n - 1)
        end
        func decr(number n, number delta) begin
            n <- n - delta
        end
        func main() begin
            number delta <- fact(32)
            decr(x,delta)
            writeNumber(x)
        end
        """
        expect = """Program([\
VarDecl(NumberType,Id(x),NumLit(2018.0)),\
FuncDecl(Id(fact),[VarDecl(NumberType,Id(n))],\
Block([If(BinaryOp(==,Id(n),NumLit(0.0)),\
Return(NumLit(1.0)),\
Return(BinaryOp(*,Id(n),CallExpr(Id(fact),[BinaryOp(-,Id(n),NumLit(1.0))]))))])),\
FuncDecl(Id(decr),[VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(delta))],\
Block([AssignStmt(Id(n),BinaryOp(-,Id(n),Id(delta)))])),\
FuncDecl(Id(main),[],\
Block([VarDecl(NumberType,Id(delta),CallExpr(Id(fact),[NumLit(32.0)])),\
Call(Id(decr),[Id(x),Id(delta)]),\
Call(Id(writeNumber),[Id(x)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,464))
        
    def test_465(self):
        input = """number x <- 2018
        func fibo(number n) begin
            if (n <= 1) return 1
            else return fibo(n - 1) + fibo(n - 2)
    end
        func decr(number n, number delta) begin
            n <- n - delta
        end
        func main() begin
            number delta <- fact(100)
            decr(x,delta)
            writeNumber(x)
        end
        """
        expect = """Program([\
VarDecl(NumberType,Id(x),NumLit(2018.0)),\
FuncDecl(Id(fibo),[VarDecl(NumberType,Id(n))],\
Block([If(BinaryOp(<=,Id(n),NumLit(1.0)),\
Return(NumLit(1.0)),\
Return(BinaryOp(+,CallExpr(Id(fibo),[BinaryOp(-,Id(n),NumLit(1.0))]),CallExpr(Id(fibo),[BinaryOp(-,Id(n),NumLit(2.0))]))))])),\
FuncDecl(Id(decr),[VarDecl(NumberType,Id(n)),VarDecl(NumberType,Id(delta))],\
Block([AssignStmt(Id(n),BinaryOp(-,Id(n),Id(delta)))])),\
FuncDecl(Id(main),[],\
Block([VarDecl(NumberType,Id(delta),CallExpr(Id(fact),[NumLit(100.0)])),\
Call(Id(decr),[Id(x),Id(delta)]),\
Call(Id(writeNumber),[Id(x)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,465))
    
    def test_466(self):
        input = """var x <- 20
        dynamic y <- x * 0.25
        """
        expect = """Program([\
VarDecl(var,Id(x),NumLit(20.0)),\
VarDecl(dynamic,Id(y),BinaryOp(*,Id(x),NumLit(0.25)))\
])"""
        self.assertTrue(TestAST.test(input,expect,466))
    def test_467(self):
        input = """func foo(number a[3]) begin
            return a
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(ArrayType([3],NumberType),Id(a))],Block([Return(Id(a))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,467))
    def test_468(self):
        input = """func foo() begin
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[],Block([]))\
])"""
        self.assertTrue(TestAST.test(input,expect,468))
    def test_469(self):
        input = """var x <- 2
        var y <- false
        var z <- true
        var t <- "It's me '"Hello'" "
       """
        expect = """Program([\
VarDecl(var,Id(x),NumLit(2.0)),\
VarDecl(var,Id(y),BooleanLit(False)),\
VarDecl(var,Id(z),BooleanLit(True)),\
VarDecl(var,Id(t),StringLit(It's me '"Hello'" ))\
])"""
        self.assertTrue(TestAST.test(input,expect,469))
    def test_470(self): 
        input = """var x <- 2
        var y <- false
        var z <- true
        var t <- "It's me '"Hello'" "
        dynamic u <- -1.e23
        """
        expect = """Program([\
VarDecl(var,Id(x),NumLit(2.0)),\
VarDecl(var,Id(y),BooleanLit(False)),\
VarDecl(var,Id(z),BooleanLit(True)),\
VarDecl(var,Id(t),StringLit(It's me '"Hello'" )),\
VarDecl(dynamic,Id(u),UnaryOp(-,NumLit(1e+23)))\
])"""
        self.assertTrue(TestAST.test(input,expect,470))
    
    def test_471(self):
        input = """func foo(number a, number b, number c) begin
            writeNumber(a + 2 * b + 3 * c)
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b)),VarDecl(NumberType,Id(c))],\
Block([Call(Id(writeNumber),[BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(*,NumLit(2.0),Id(b))),BinaryOp(*,NumLit(3.0),Id(c)))])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,471))
    def test_472(self):
        input = """func foo(number a, number b, number c) begin
            writeNumber(a + 2 * b + 3 * c)
        end
        func main() begin
            foo(2,3,4)
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b)),VarDecl(NumberType,Id(c))],\
Block([Call(Id(writeNumber),[BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(*,NumLit(2.0),Id(b))),BinaryOp(*,NumLit(3.0),Id(c)))])])),\
FuncDecl(Id(main),[],Block([Call(Id(foo),[NumLit(2.0),NumLit(3.0),NumLit(4.0)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,472))
    
    def test_473(self):
        input = """func foo(number a, number b) begin
            number c <- 2018
            writeNumber(a + 2 * b + 3 * c)
        end
        func main() begin
            foo(2,3)
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b))],\
Block([VarDecl(NumberType,Id(c),NumLit(2018.0)),Call(Id(writeNumber),[BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(*,NumLit(2.0),Id(b))),BinaryOp(*,NumLit(3.0),Id(c)))])])),\
FuncDecl(Id(main),[],Block([Call(Id(foo),[NumLit(2.0),NumLit(3.0)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,473))
    def test_474(self):
        input = """func foo(number a, number b) begin
            writeNumber(a + b)
            return
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b))],\
Block([Call(Id(writeNumber),[BinaryOp(+,Id(a),Id(b))]),Return()]))\
])"""
        self.assertTrue(TestAST.test(input,expect,474))
    
    def test_475(self):
        input = """func foo(number a, number b) begin
            number i <- a
            for i until i > b by 1 begin
                number c <- a + i
                writeNumber(c)
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b))],\
Block([VarDecl(NumberType,Id(i),Id(a)),\
For(Id(i),BinaryOp(>,Id(i),Id(b)),NumLit(1.0),\
Block([VarDecl(NumberType,Id(c),BinaryOp(+,Id(a),Id(i))),\
Call(Id(writeNumber),[Id(c)])]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,475))

    def test_476(self):
        input = """func foo() begin
            if (true) begin
                if (not true) begin
                    
                end
                else return
            end
            return
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[],\
Block([If(BooleanLit(True),\
Block([If(UnaryOp(not,BooleanLit(True)),\
Block([]),\
Return())])),\
Return()]))\
])"""
        self.assertTrue(TestAST.test(input,expect,476))
        
    def test_477(self):
        input = """func foo() begin
            if (not true) begin
                if (true) begin
                    number a <- 10
                    a <- a + 1
                    return
                end
                else
                    return
            end
            else begin
                number a <- 1
                writeNumber(a)
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[],\
Block([If(UnaryOp(not,BooleanLit(True)),\
Block([If(BooleanLit(True),\
Block([VarDecl(NumberType,Id(a),NumLit(10.0)),\
AssignStmt(Id(a),BinaryOp(+,Id(a),NumLit(1.0))),Return()]),\
Return())]),\
Block([VarDecl(NumberType,Id(a),NumLit(1.0)),\
Call(Id(writeNumber),[Id(a)])]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,477))
    
    def test_478(self):
        input = """func foo(number a[10]) begin
            number i <- 0
            for i until i >= 10 by 1 begin
                a[i] <- a[i] * 2 + 1
            end
            return a
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(ArrayType([10],NumberType),Id(a))],\
Block([VarDecl(NumberType,Id(i),NumLit(0.0)),\
For(Id(i),BinaryOp(>=,Id(i),NumLit(10.0)),NumLit(1.0),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i)]),\
BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),[Id(i)]),NumLit(2.0)),NumLit(1.0)))])),\
Return(Id(a))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,478))
    def test_479(self):
        input = """func foo(number N, number i) begin
            number j <- 0
            for j until j >= i by 1 begin
                if (N % j == 0) begin
                    N <- N - j
                end
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(N)),VarDecl(NumberType,Id(i))],\
Block([VarDecl(NumberType,Id(j),NumLit(0.0)),\
For(Id(j),BinaryOp(>=,Id(j),Id(i)),NumLit(1.0),\
Block([If(BinaryOp(==,BinaryOp(%,Id(N),Id(j)),NumLit(0.0)),\
Block([AssignStmt(Id(N),BinaryOp(-,Id(N),Id(j)))]))]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,479))
    def test_480(self):
        input = """func foo1(number N, number i) begin
            N <- N * i
        end
        func main() begin
            number N <- 2018
            foo1(N,3)
            writeNumber(N)
        end
        """
        expect = """Program([\
FuncDecl(Id(foo1),[VarDecl(NumberType,Id(N)),VarDecl(NumberType,Id(i))],\
Block([AssignStmt(Id(N),BinaryOp(*,Id(N),Id(i)))])),\
FuncDecl(Id(main),[],\
Block([VarDecl(NumberType,Id(N),NumLit(2018.0)),\
Call(Id(foo1),[Id(N),NumLit(3.0)]),\
Call(Id(writeNumber),[Id(N)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,480))
    
    def test_481(self):
        input = """func foo1(string s, number N) begin
            number i <- 0
            for i until i >= N by 1 begin
                string temp <- s[N - i - 1]
                s[N - i - 1] <- s[i]
                s[i] <- temp
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(foo1),[VarDecl(StringType,Id(s)),VarDecl(NumberType,Id(N))],\
Block([VarDecl(NumberType,Id(i),NumLit(0.0)),\
For(Id(i),BinaryOp(>=,Id(i),Id(N)),NumLit(1.0),\
Block([VarDecl(StringType,Id(temp),ArrayCell(Id(s),[BinaryOp(-,BinaryOp(-,Id(N),Id(i)),NumLit(1.0))])),\
AssignStmt(ArrayCell(Id(s),[BinaryOp(-,BinaryOp(-,Id(N),Id(i)),NumLit(1.0))]),ArrayCell(Id(s),[Id(i)])),\
AssignStmt(ArrayCell(Id(s),[Id(i)]),Id(temp))]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,481))
    def test_482(self):
        input = """func foo1(string s, number N) begin
            number i <- 0
            for i until i >= N / 2 by 1 begin
                string temp <- s[N - i - 1]
                s[N - i - 1] <- s[i]
                s[i] <- temp
            end
            writeString(s)
        end
        func main() begin
            foo1(\"Hello,this is me\",17)
        end
        """
        expect = """Program([\
FuncDecl(Id(foo1),[VarDecl(StringType,Id(s)),VarDecl(NumberType,Id(N))],\
Block([VarDecl(NumberType,Id(i),NumLit(0.0)),\
For(Id(i),BinaryOp(>=,Id(i),BinaryOp(/,Id(N),NumLit(2.0))),NumLit(1.0),\
Block([VarDecl(StringType,Id(temp),ArrayCell(Id(s),[BinaryOp(-,BinaryOp(-,Id(N),Id(i)),NumLit(1.0))])),\
AssignStmt(ArrayCell(Id(s),[BinaryOp(-,BinaryOp(-,Id(N),Id(i)),NumLit(1.0))]),ArrayCell(Id(s),[Id(i)])),\
AssignStmt(ArrayCell(Id(s),[Id(i)]),Id(temp))])),\
Call(Id(writeString),[Id(s)])])),\
FuncDecl(Id(main),[],\
Block([Call(Id(foo1),[StringLit(Hello,this is me),NumLit(17.0)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,482))
    
    def test_483(self):
        input = """number a <- foo(2018) + goo(2018)
        """
        expect = """Program([\
VarDecl(NumberType,Id(a),\
BinaryOp(+,CallExpr(Id(foo),[NumLit(2018.0)]),CallExpr(Id(goo),[NumLit(2018.0)])))\
])"""
        self.assertTrue(TestAST.test(input,expect,483))
    def test_484(self): # redundant
        input = """func foo(number a, number b) begin
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b))],Block([]))\
])"""
        self.assertTrue(TestAST.test(input,expect,484))
    def test_485(self):
        input = """func foo(number a, number b) begin
            number i <- 0
            for i until i >= 5 by 1 begin
                number x <- 10
                number y <- 20
                number z <- 30
                return (x + a + y + b) > (y + a + z + b)
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b))],\
Block([VarDecl(NumberType,Id(i),NumLit(0.0)),\
For(Id(i),BinaryOp(>=,Id(i),NumLit(5.0)),NumLit(1.0),\
Block([VarDecl(NumberType,Id(x),NumLit(10.0)),\
VarDecl(NumberType,Id(y),NumLit(20.0)),\
VarDecl(NumberType,Id(z),NumLit(30.0)),\
Return(BinaryOp(>,\
BinaryOp(+,BinaryOp(+,\
BinaryOp(+,Id(x),Id(a)),Id(y)),Id(b)),\
BinaryOp(+,BinaryOp(+,\
BinaryOp(+,Id(y),Id(a)),Id(z)),Id(b))))]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,485))
    def test_486(self):
        input = """func foo1(number a, number b) begin
            number c <- a+b
            writeNumber(c)
        end
        """
        expect = """Program([\
FuncDecl(Id(foo1),[VarDecl(NumberType,Id(a)),VarDecl(NumberType,Id(b))],\
Block([VarDecl(NumberType,Id(c),BinaryOp(+,Id(a),Id(b))),\
Call(Id(writeNumber),[Id(c)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,486))
    
    def test_487(self):
        input = """func foo2(number a) begin
            writeString(\"Test\")
            a <- a + 1
            writeNumber(a)
        end
        func main() begin
            foo2(10)
        end
        """
        expect = """Program([\
FuncDecl(Id(foo2),[VarDecl(NumberType,Id(a))],\
Block([Call(Id(writeString),[StringLit(Test)]),\
AssignStmt(Id(a),BinaryOp(+,Id(a),NumLit(1.0))),\
Call(Id(writeNumber),[Id(a)])])),\
FuncDecl(Id(main),[],Block([Call(Id(foo2),[NumLit(10.0)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,487))
    def test_488(self):
        input = """bool a <- true
        bool b <- false
        bool c <- true
        """
        expect = """Program([\
VarDecl(BoolType,Id(a),BooleanLit(True)),\
VarDecl(BoolType,Id(b),BooleanLit(False)),\
VarDecl(BoolType,Id(c),BooleanLit(True))\
])"""
        self.assertTrue(TestAST.test(input,expect,488))
    def test_489(self): 
        input = """func foo() begin
            if (true)
            begin
                number a <- 10
                number b <- 20
                number c <- 30
                writeNumber(a + b + c)
            end
            else
            begin
                number x <- 2.3e2
                number y <- -2.3e2
                writeNumber(x + y)
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[],\
Block([If(BooleanLit(True),\
Block([VarDecl(NumberType,Id(a),NumLit(10.0)),\
VarDecl(NumberType,Id(b),NumLit(20.0)),\
VarDecl(NumberType,Id(c),NumLit(30.0)),\
Call(Id(writeNumber),[BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c))])]),\
Block([VarDecl(NumberType,Id(x),NumLit(230.0)),\
VarDecl(NumberType,Id(y),UnaryOp(-,NumLit(230.0))),\
Call(Id(writeNumber),[BinaryOp(+,Id(x),Id(y))])]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,489))
    def test_490(self):
        input = """bool a_20 <- (2 < 3) < 4
        """
        expect = """Program([\
VarDecl(BoolType,Id(a_20),BinaryOp(<,BinaryOp(<,NumLit(2.0),NumLit(3.0)),NumLit(4.0)))\
])"""
        self.assertTrue(TestAST.test(input,expect,490))
    def test_491(self):
        input = """func foo(string a, number b) begin
            return (a ... a[b])
        end
        """
        expect = """Program([\
FuncDecl(Id(foo),[VarDecl(StringType,Id(a)),VarDecl(NumberType,Id(b))],\
Block([Return(BinaryOp(...,Id(a),ArrayCell(Id(a),[Id(b)])))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,491))
    
    def test_492(self):
        input = """number x <- 65
        func y(number x) return x + 1
        
        number z <- 65.20
        func t(number z) return z * 2.0

        func main() begin
            number y <- y(x)
            number t <- t(z)
            writeNumber(y)
            writeNumber(t)
        end
        """
        expect = """Program([\
VarDecl(NumberType,Id(x),NumLit(65.0)),\
FuncDecl(Id(y),[VarDecl(NumberType,Id(x))],Return(BinaryOp(+,Id(x),NumLit(1.0)))),\
VarDecl(NumberType,Id(z),NumLit(65.2)),\
FuncDecl(Id(t),[VarDecl(NumberType,Id(z))],Return(BinaryOp(*,Id(z),NumLit(2.0)))),\
FuncDecl(Id(main),[],\
Block([VarDecl(NumberType,Id(y),CallExpr(Id(y),[Id(x)])),\
VarDecl(NumberType,Id(t),CallExpr(Id(t),[Id(z)])),\
Call(Id(writeNumber),[Id(y)]),\
Call(Id(writeNumber),[Id(t)])]))\
])"""
        self.assertTrue(TestAST.test(input,expect,492))
        
    def test_493(self):
        input = """func main() begin
            number a[2,2]
            number i <- 0
            number j <- 0
            for i until i >= 2 by 1 begin
                for j until j >= 2 by 1 begin
                    a[i,j] <- readNumber()
                end
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(main),[],\
Block([VarDecl(ArrayType([2,2],NumberType),Id(a)),\
VarDecl(NumberType,Id(i),NumLit(0.0)),\
VarDecl(NumberType,Id(j),NumLit(0.0)),\
For(Id(i),BinaryOp(>=,Id(i),NumLit(2.0)),NumLit(1.0),\
Block([For(Id(j),BinaryOp(>=,Id(j),NumLit(2.0)),NumLit(1.0),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i),Id(j)]),\
CallExpr(Id(readNumber),[]))]))]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,493))
    def test_494(self):
        input = """func main() begin
            number a[2,2]
            number i <- 0
            number j <- 0
            for i until i >= 2 by 1 begin
                for j until j >= 2 by 1 begin
                    a[i,j] <- readNumber()
                end
            end
            for i until i >= 2 by 1 begin
                for j until j >= 2 by 1 begin
                    writeNumber(a[i,j])
                end
            end
        end
        """
        expect = """Program([\
FuncDecl(Id(main),[],\
Block([VarDecl(ArrayType([2,2],NumberType),Id(a)),\
VarDecl(NumberType,Id(i),NumLit(0.0)),\
VarDecl(NumberType,Id(j),NumLit(0.0)),\
For(Id(i),BinaryOp(>=,Id(i),NumLit(2.0)),NumLit(1.0),\
Block([For(Id(j),BinaryOp(>=,Id(j),NumLit(2.0)),NumLit(1.0),\
Block([AssignStmt(ArrayCell(Id(a),[Id(i),Id(j)]),\
CallExpr(Id(readNumber),[]))]))])),\
For(Id(i),BinaryOp(>=,Id(i),NumLit(2.0)),NumLit(1.0),\
Block([For(Id(j),BinaryOp(>=,Id(j),NumLit(2.0)),NumLit(1.0),\
Block([Call(Id(writeNumber),\
[ArrayCell(Id(a),[Id(i),Id(j)])])]))]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,494))
        
    def test_495(self):
        input = """func test(number a, string c) 
                        begin
                        if (a > 2) a <- 3
                        elif (a > 3) a <- 4
                        end
        """
        expect = """Program([\
FuncDecl(Id(test),[VarDecl(NumberType,Id(a)),VarDecl(StringType,Id(c))],\
Block([If(BinaryOp(>,Id(a),NumLit(2.0)),\
AssignStmt(Id(a),NumLit(3.0)),\
BinaryOp(>,Id(a),NumLit(3.0)),\
AssignStmt(Id(a),NumLit(4.0)))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,495))
        
    def test_496(self):
        input = """func main()
begin
           if (a) do(a)
           elif (a=2) do(b)
end
        """
        expect = """Program([\
FuncDecl(Id(main),[],\
Block([If(Id(a),Call(Id(do),[Id(a)]),\
BinaryOp(=,Id(a),NumLit(2.0)),\
Call(Id(do),[Id(b)]))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,496))
        
    def test_497(self):
        input = """func test(number a, string c) 
                        begin
                        if (a > 2) a <- 3
                        elif (a > 3) a <- 4
                        else b <- 5
                        end
        """
        expect = """Program([\
FuncDecl(Id(test),[VarDecl(NumberType,Id(a)),VarDecl(StringType,Id(c))],\
Block([If(BinaryOp(>,Id(a),NumLit(2.0)),\
AssignStmt(Id(a),NumLit(3.0)),\
BinaryOp(>,Id(a),NumLit(3.0)),\
AssignStmt(Id(a),NumLit(4.0)),\
AssignStmt(Id(b),NumLit(5.0)))]))\
])"""
        self.assertTrue(TestAST.test(input,expect,497))
    
    
    

   