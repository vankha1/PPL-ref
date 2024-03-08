import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):

    
    def test_case_101(self):

        input = """ func test(number a, bool b)
        return a + b"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 101))

    def test_case_102(self):

        input = """func test(number a, bool b) return a + b"""
        expect = "Error on line 1 col 28: return"
        self.assertTrue(TestParser.test(input, expect, 102))

    def test_case_103(self):

        input = """bool a_b"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 103))

    def test_case_104(self):

        input = """number x_Y_z"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 104))

    # def test_case_105(self):

    #     input = """_Aa: auto;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 105))

    def test_case_106(self):

        input = """number a[1,2]"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 106))

    def test_case_107(self):

        input = """bool array[2,3,10,5,10,10]"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 107))

    def test_case_108(self):

        input = """number a <- 2, b <- 3"""
        expect = "Error on line 1 col 13: ,"
        self.assertTrue(TestParser.test(input, expect, 108))

    def test_case_109(self):

        input = """number vvk <- 12 + 2"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 109))

    def test_case_110(self):

        input = """string chatgpt <- "uaalo" """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 110))

    def test_case_111(self):

        input = """number array[1,1] <- [[1,2,3]]
                    string x <- "hello"
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 111))

    # def test_case_112(self):

    #     input = """dynamic a <- 2"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 112))

    # def test_case_113(self):

    #     input = """x <- bool"""
    #     expect = "Error on line 1 col 0: x"
    #     self.assertTrue(TestParser.test(input, expect, 113))

    # def test_case_114(self):

    #     input = """number Aee123 <- 1 + 1
    #             number _aDC <- 2 * 1
    #             number A_bc <- -1
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 114))

    # def test_case_115(self):

    #     input = """bool x <- true
    #             bool y <- false
    #             number x <- 123.
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 115))

    # def test_case_116(self):

    #     input = """number1 arg1 <- 1 - 1
    #                 number arg2 <- 1 + a
    #     """
    #     expect = "Error on line 1 col 0: number1"
    #     self.assertTrue(TestParser.test(input, expect, 116))

    # def test_case_117(self):

    #     input = """
    #         number a[]
    #     """
    #     expect = "Error on line 2 col 21: ]"
    #     self.assertTrue(TestParser.test(input, expect, 117))

    # def test_case_118(self):

    #     input = """
    #         func name(number x, number y)
    #         begin
    #             number a <- 2
    #             a <- a + 1
    #             aPI <- 3.14
                
    #             l[3] <- value * aPi
    #             a[3 + foo(2)] <- a[b[2, 3]] + 4
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 118))

    # def test_case_119(self):

    #     input = """
    #         func foo(number a[5], string b)
    #         begin
    #             var i <- 0
    #             for i until i >= 5 by 1
    #             begin
    #             a[i] <- i * i + 5
    #             end
    #             return -1
    #         end 
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 119))

    # def test_case_120(self):

    #     input = """string str <- "a"..."b" """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 120))

    # def test_case_121(self):

    #     input = """
    #         func name()
    #         begin
    #             a[3 + foo(2)] <- a[b[2, 3]] + 4
    #     """
    #     expect = "Error on line 5 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 121))

    # def test_case_122(self):

    #     input = """number java <- not a and b - "love" / "you" """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 122))

    # def test_case_123(self):

    #     input = """string love <- "I" ... "LOVE" ... "YOU" """
    #     expect = "Error on line 1 col 30: ..."
    #     self.assertTrue(TestParser.test(input, expect, 123))

    # def test_case_124(self):

    #     input = """number array[3] <- [31, 12, 2002]"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 124))

    # def test_case_125(self):

    #     input = """bool array[t]"""
    #     expect = "Error on line 1 col 11: t"
    #     self.assertTrue(TestParser.test(input, expect, 125))

    # def test_case_126(self):

    #     input = """number array[] <- a, -1 + 2"""
    #     expect = "Error on line 1 col 13: ]"
    #     self.assertTrue(TestParser.test(input, expect, 126))

    # def test_case_127(self):

    #     input = """number a <- str[1]"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 127))

    # def test_case_128(self):

    #     input = """string siuuuuuuuuuuuuuuuu <- "Ronaldo" """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 128))

    # def test_case_129(self):

    #     input = """string messi <- "Linel Messi" """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 129))

    # def test_case_130(self):

    #     input = """number a <- a[1]
    #             number b <- b[5]
    #             number c <- c[2]
    #             number d <- d[3]
    #             number e <- e[4]
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 130))

    # def test_case_131(self):

    #     input = """func number ()"""
    #     expect = "Error on line 1 col 5: number"
    #     self.assertTrue(TestParser.test(input, expect, 131))

    # def test_case_132(self):

    #     input = """func boolean ()
    #     """
    #     expect = "Error on line 2 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 132))

    # def test_case_133(self):

    #     input = """
    #         func array[10, 10] ()
    #         begin
    #         end
    #     """
    #     expect = "Error on line 2 col 22: ["
    #     self.assertTrue(TestParser.test(input, expect, 133))

    # def test_case_134(self):

    #     input = """
    #         func void (number x)
    #         begin
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 134))

    # def test_case_135(self):

    #     input = """func Func_1 (number t, string z) begin end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 135))

    # def test_case_136(self):

    #     input = """
    #         func Siuuuuuuuuu_A7 ()
    #             begin
    #             begin
    #             end
    #             end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 136))

    # def test_case_137(self):

    #     input = """func Messssssssssssssssssssi (number a[1]) 
    #                 begin
    #                 end
    #             """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 137))

    # def test_case_138(self):
    #     input = """
    #         func Cavani (number a, string b, bool c) 
    #             begin
    #             begin
    #             end
    #             end
    #         """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 138))

    # def test_case_139(self):

    #     input = """func number ()
    #         begin
    #         end
    #     """
    #     expect = "Error on line 1 col 5: number"
    #     self.assertTrue(TestParser.test(input, expect, 139))

    # def test_case_140(self):

    #     input = """func /a_a () 
    #         begin
    #         end
    #     """
    #     expect = "Error on line 1 col 5: /"
    #     self.assertTrue(TestParser.test(input, expect, 140))

    # def test_case_141(self):

    #     input = """funccxyz Raphinha () 
    #             begin
    #             begin
    #             end
    #             end
    #     """
    #     expect = "Error on line 1 col 0: funccxyz"
    #     self.assertTrue(TestParser.test(input, expect, 141))

    # def test_case_142(self):

    #     input = """func _Casemiro () 
    #             begin
    #             begin
    #             begin
    #             end
    #             end
    #         """
    #     expect = "Error on line 7 col 12: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 142))

    # def test_case_143(self):

    #     input = """func decl ()
    #         a <- 1
    #         b <- 2
    #     """
    #     expect = "Error on line 2 col 12: a"
    #     self.assertTrue(TestParser.test(input, expect, 143))

    # def test_case_144(self):
    #     input = """func void ()
    #         begin
    #             if (n == 1) return 1
    #             else break   
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 144))

    # def test_case_145(self):

    #     input = """
    #         func integer ()
    #         begin
    #             a[1] <- true and false and not a > 1
    #         end
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 145))

    # def test_case_146(self):

    #     input = """func boolean () 
    #     begin
    #         continue
    #         break
    #         writeNumber(1)
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 146))

    # def test_case_147(self):

    #     input = """
    #     func vankha () 
    #     begin
    #         begin
    #         end
    #         return 1
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 147))

    # def test_case_148(self):

    #     input = """
    #     func void () 
    #     begin
    #         if (n == 1) a <- true
    #         continue
    #         for i until i < 1 by -1 
    #             a <- b and true
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 148))

    # def test_case_149(self):

    #     input = """
    #     func vankha () 
    #     begin
    #         for i until i < 1 by -1 
    #             break
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 149))

    # def test_case_150(self):

    #     input = """
    #     func void () 
    #     begin
    #         foo()
    #         return not a
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 150))

    # def test_case_151(self):

    #     input = """
    #     func function () 
    #     begin
    #         if ( i <= 1) 
    #         return i <- i + 2
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 151))

    # def test_case_152(self):

    #     input = """
    #     func function () 
    #     begin
    #         begin
    #             for i until v < 10 by 1
    #                 return a <- a + 1
    #         end
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 152))

    # def test_case_153(self):

    #     input = """func integer () 
    #     begin
    #         if (a + 1 and true)
    #             if (a + 1 and true)
    #                 if (a + 1 and true)
    #                     if (a + 1 and true)
    #                         if (a + 1 and true)
    #                             continue
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 153))

    # def test_case_154(self):

    #     input = """
    #     func integer () 
    #     begin
    #         if (i==1)
    #             a <- a + 1
    #         elif (i == 2) a <- a + 2
    #         else a <- a + 3
    #     end            
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 154))

    # def test_case_155(self):

    #     input = """func integer () 
    #     begin
    #         break
    #         if (true) a <- 1 + 1
    #         else b <- b
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 155))

    # def test_case_156(self):

    #     input = """
    #     func boolean () 
    #     begin
    #         if (a[10] >= 100 )
    #             if (a[1,1] == 10)  printInteger(1)
    #             else if (a[-1, 10]  or false) b[-1] <- 10
                   
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 156))

    # def test_case_157(self):
    #     ## Lack of statement after if-condition
    #     input = """
    #     func boolean () 
    #     begin
    #         if (a[10] >= 100 )
    #         elif (a[1,1] == 10)  printInteger(1)
    #         elif (a[-1, 10]  or false) b[-1] <- 10
    #     end"""
    #     expect = "Error on line 5 col 12: elif"
    #     self.assertTrue(TestParser.test(input, expect, 157))

    # def test_case_158(self):
    #     ## Special not implemented, so it log errors at the second elif
    #     input = """
    #     func boolean () 
    #     begin
    #         if (a[10] >= 100 ) a <- a + 1
    #         elif (a[1,1] == 10)  printInteger(1)
    #         elif (a[-1, 10]  or false) b[-1] <- 10
    #         else return foo(2 + 2)
    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 158))

    # def test_case_159(self):

    #     input = """
    #     ## khai bao ham func
    #     func integer () 
    #         begin
    #         begin
    #             if (a[10] >= 100 )
    #             if (a[1,1] == 10)  printInteger(1)
    #             else if (a[-1, 10]  or false) b[-1] <- 10
    #         end
    #         end
    #     end"""
    #     expect = "Error on line 5 col 8: end"
    #     self.assertTrue(TestParser.test(input, expect, 159))

    # def test_case_160(self):

    #     input = """
    #     ## alo
    #     func void () 
    #     begin

    #     end"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 160))

    # def test_case_161(self):

    #     input = """
    #     /* heelo */
    #     func: function integer () {
            
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 161))

    # def test_case_162(self):

    #     input = """
        
    #     func: function integer () {
    #         /* error
    #     }"""
    #     expect = "Error on line 4 col 12: /"
    #     self.assertTrue(TestParser.test(input, expect, 162))

    # def test_case_163(self):

    #     input = """func: function boolean () {
    #         break;
    #         /* error */
    #          do {
    #     while (i % 10 == 0) {
    #          x = 20;
    #     }
    #     if (n == 2) {
    #         return 0;
    #     } 
    # } while (i > 100);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 163))

    # def test_case_164(self):

    #     input = """func: function integer () {
    #         continue;
    #         do {
    #     while (i + 1 == 2) {
    #          x = 10;
    #     }
    #     if (n == 1) {
    #         return 0;
    #     } else {
    #         break;
    #     }
    # } while (i - 100);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 164))

    # def test_case_165(self):

    #     input = """func: function integer () {
    #         while (a < 10) {
    #     for ( i = 0, i < 5, i - 100) {
    #         while (i > 2) {
    #             a = a[i];
    #         }
    #     }
    # }
    # return a;
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 165))

    # def test_case_166(self):

    #     input = """func: function integer () {
    #        do {
    #     while (b % 2 == 0) {
    #         b = b / 2;
    #     }
    #     for ( i = 0, i < 3, i - a) {
    #         if (i == b) {
    #             continue;
    #         } else {
    #             b = 1;
    #         }
    #     }
    # } while (b > 0);
    # return b;
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 166))

    # def test_case_167(self):

    #     input = """func: function integer () {
    #         /* sinh code moi */
    #         preventDefault();
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 167))

    # def test_case_168(self):

    #     input = """func: function float (out a: integer, b: float) {
    #        a = a[1];
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 168))

    # def test_case_169(self):

    #     input = """func: function float () {
    #         readInteger();
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 169))

    # def test_case_170(self):

    #     input = """func: function integer () {
    #         printFloat("1+1");
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 170))

    # def test_case_171(self):

    #     input = """func: function array[] of float () {
          
    #            printFloat(12.1e45);
    #     }"""
    #     expect = "Error on line 1 col 21: ]"
    #     self.assertTrue(TestParser.test(input, expect, 171))

    # def test_case_172(self):

    #     input = """func: function integer () {
    #        readFloat(1e10);
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 172))

    # def test_case_173(self):

    #     input = """func: function boolean () {
    #         readBoolean();
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 173))

    # def test_case_174(self):

    #     input = """func: function boolean (a: boolean, b: float) {
    #         printBoolean(a);    
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 174))

    # def test_case_175(self):

    #     input = """func: function integer (inherit out a: integer, b: string) {
    #         readString();
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 175))

    # def test_case_176(self):

    #     input = """func: function integer () {
    #     break;
    #     {
        
    #     }
    #         preventDefault();    
    #     }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 176))

    # def test_case_177(self):

    #     input = """
    #     a = 10;
    #     func: function integer () {
    #        if (true) 10;
    #     }"""
    #     expect = "Error on line 2 col 10: ="
    #     self.assertTrue(TestParser.test(input, expect, 177))

    # def test_case_178(self):

    #     input = """
    #     a: integer = func(10);
    #     for(i = 3, i <= 10, i + 1) {
    #         sum = sum + i;
    #     }
    #     print("I Love you");
    #     """
    #     expect = "Error on line 3 col 8: for"
    #     self.assertTrue(TestParser.test(input, expect, 178))

    # def test_case_179(self):

    #     input = """
    #         integers: array [5] of integer = {1, 2, 3, "a"};
    #         a = 10;
    #     """
    #     expect = "Error on line 3 col 14: ="
    #     self.assertTrue(TestParser.test(input, expect, 179))

    # def test_case_180(self):

    #     input = """
    #     str func();
    #     if (true == a) return 0;"""
    #     expect = "Error on line 2 col 12: func"
    #     self.assertTrue(TestParser.test(input, expect, 180))

    # def test_case_181(self):

    #     input = """
    #     func: function void ()
    #     {
    #     arr = {10.5, 20.3, 15.6, 18.9, 25.4};
    #     integer n = sizeof(arr) / sizeof(arr[0]);
    #      average = calculateAverage(arr, n);
    #     }
    #     """
    #     expect = "Error on line 5 col 8: integer"
    #     self.assertTrue(TestParser.test(input, expect, 181))

    # def test_case_182(self):

    #     input = """func: function reverseString(str: string) {
    #         n = strlen(str);
    #         for (i = 0, i < n / 2, i + 1) {
    #             swap(str[i], str[n - i - 1]);
    #         }
    #     """
    #     expect = "Error on line 1 col 15: reverseString"
    #     self.assertTrue(TestParser.test(input, expect, 182))

    # def test_case_183(self):

    #     input = """
    #             calculateExpApproximation(int n) {
    #         double result = 1.0;
    #         double term = 1.0;
    #         for (int i = 1; i <= n; i++) {
    #             term *= (1.0 / n);
    #             result += term;
    #         }
    #         return result;"""
    #     expect = "Error on line 2 col 41: ("
    #     self.assertTrue(TestParser.test(input, expect, 183))

    # def test_case_184(self):

    #     input = """func: function float () {
    #         func();
    #         return expr;
    #     }

    #     c = expr;"""
    #     expect = "Error on line 6 col 10: ="
    #     self.assertTrue(TestParser.test(input, expect, 184))

    # def test_case_185(self):

    #     input = """/* 
    #     double calculateExpression(int n) {
    #         double result = 0.0;
    #         for (int i = 1; i <= n; i++) {
    #             result += (double) i / (i + 1);
    #         }
    #         return result;*/
    #     """
    #     expect = "Error on line 8 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 185))

    # def test_case_186(self):

    #     input = """
    #     func: function integer () {
    #         e: int;
           
    #         c = true * d / 20 ;
         
    #     }"""
    #     expect = "Error on line 3 col 15: int"
    #     self.assertTrue(TestParser.test(input, expect, 186))

    # def test_case_187(self):

    #     input = """/* 
       
    #                 int sumNumbers(int n) {
    #                     int sum = 0;
    #                     int i = 1;
    #                     do {
    #                         sum += i;
    #                         i++;
    #                     } while (i <= n);
    #                     return sum;
    #                 }*/"""
    #     expect = "Error on line 11 col 23: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 187))

    # def test_case_188(self):

    #     input = """// khai bao bien
    #     printNumbers: function integer (n: integer) {
    #     for (i = 1, i <= n, i + 10) {
    #       break;
    #     }
       
    #     """
    #     expect = "Error on line 7 col 8: <EOF>"
    #     self.assertTrue(TestParser.test(input, expect, 188))

    # def test_case_189(self):

    #     input = """a: boolean = true;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 189))

    # def test_case_90(self):

    #     input = """a = 65;
    #     fact: function integer (n: integer) {
    #         if (n == 0) return 1;
    #         else return n * fact(n - 1);
    #     }
    #     inc: function void(out n: integer, delta: integer) {
    #         n = n + delta;
    #     }
    #    """
    #     expect = "Error on line 1 col 2: ="
    #     self.assertTrue(TestParser.test(input, expect, 190))

    # def test_case_191(self):
    #     input =	"""a: integer;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 191))
    # def test_case_192(self):
    #     input =	"""a: integer = 1;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 192))
    # def test_case_193(self):
    #     input =	"""a: integer = 10.0;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 193))
    # def test_case_194(self):
    #     input =	"""a: integer = "str";"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 194))
    # def test_case_195(self):
    #     input =	"""a: integer = b;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 195))
    # def test_case_196(self):
    #     input =	"""a: boolean = foo(1);"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 196))
    # def test_case_197(self):
    #     input =	"""a: boolean = true;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 197))
    # def test_case_198(self):
    #     input =	"""a, b: boolean = 1, 2;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 198))
    # def test_case_199(self):
    #     input =	"""a: boolean = x + 1;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.test(input, expect, 199))
    # def test_case_200(self):
    #     input =	"""a: array[100] of void = x + 1;"""
    #     expect = "Error on line 1 col 17: void"
    #     self.assertTrue(TestParser.test(input, expect, 200))