import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    
    """
    TESTCASE STRATEGY:
        100-109: Single Cases
        110-119: ID
        120-129: Keyword, Operators, Separators
        130-139: Int, Comment
        140-149: Float
        150-159: String
        160-199: Mixed Cases
    """
    #Single Cases
    def test_case_1(self):
        input = """## comment block"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 1))

    def test_case_2(self):
        input = """##comment block"""
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 2))

    def test_case_3(self):
        input = """## al o #alo """
        output = """<EOF>"""
        self.assertTrue(TestLexer.test(input, output, 3))
    
    def test_case_4(self): 
        input ="""Counter_1"""
        expect ="""Counter_1,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 4))
        
    def test_case_5(self): 
        input ="""invalid-identifier"""
        expect ="""invalid,-,identifier,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 5))
        
    def test_case_6(self): 
        input ="""0"""
        expect ="""0,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 6))
        
    def test_case_7(self): 
        input ="""123"""
        expect ="""123,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 7))
    def test_case_8(self): 
        input ="""1.234"""
        expect ="""1.234,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 8))
    def test_case_11(self): 
        input ="""0123"""
        expect ="""0,123,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 11))
    # def test_case_12(self):
    #     """testcase 12""" 
    #     input ="""1_234_567"""
    #     expect ="""1234567,<EOF>"""
    #     self.assertTrue(TestLexer.test(input,expect, 12))
    def test_case_13(self):
        """testcase 13""" 
        input ="""0.123"""
        expect ="""0.123,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 13))
    def test_case_15(self):
        """testcase 15""" 
        input ="""3.14159265359"""
        expect ="""3.14159265359,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 15))
    def test_case_16(self):
        """testcase 16""" 
        input ="""1e2"""
        expect ="""1e2,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 16))
    def test_case_17(self):
        """testcase 17""" 
        input ="""2.5e-1"""
        expect ="""2.5e-1,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 17))
    # def test_case_18(self):
    #     """testcase 18""" 
    #     input ="""1_000e+10"""
    #     expect ="""1000e+10,<EOF>"""
    #     self.assertTrue(TestLexer.test(input,expect, 18))
    def test_case_19(self):
        """testcase 19""" 
        input ="""12."""
        expect ="""12.,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 19))
    def test_case_20(self):
        """testcase 20""" 
        input ="""5.7e-01"""
        expect ="""5.7e-01,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 20))
    def test_case_21(self):
        """testcase 21""" 
        input =""".1e"""
        expect ="""Error Token ."""
        self.assertTrue(TestLexer.test(input,expect, 21))
    def test_case_22(self):
        """testcase 22""" 
        input =""" "hjhasdfasdk\n" """
        expect ="""Unclosed String: hjhasdfasdk"""
        self.assertTrue(TestLexer.test(input,expect, 22))
    def test_case_23(self): 
        """testcase 23""" 
        input ="abc\"" 
        expect ="""abc,Unclosed String: """
        self.assertTrue(TestLexer.test(input,expect, 23))  
    def test_case_24(self): 
        """testcase 24""" 
        input =	""" "hello world" """
        expect ="hello world,<EOF>"
        self.assertTrue(TestLexer.test(input,expect, 24))
    def test_case_25(self): 
        """testcase 25""" 
        input =	""" "It's a beautiful day" """
        expect ="""It's a beautiful day,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 25))
    def test_case_26(self): 
        """testcase 26""" 
        input =	""" "I am a \'"chatbot\'"" """
        expect ="""I am a '"chatbot'",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 26))
    def test_case_27(self): 
        """testcase 27"""   
        input =	""" "\\n\\t\\r" """
        expect ="""\\n\\t\\r,<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 27))
    def test_case_28(self): 
        """testcase 28"""     
        input = """ "mixed escape \" sequences: " """
        expect ="mixed escape ,sequences,Error Token :"
        self.assertTrue(TestLexer.test(input,expect, 28))
    # def test_case_29(self):
    #     input = "1_000_000.12345"
    #     expect = """1000000.12345,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 29))

    # def test_case_30(self):
    #     input = "100_000_000.00001e-6"
    #     expect = """100000000.00001e-6,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 30))

    def test_case_31(self):
        input ="0.00000123E-10"
        expect = """0.00000123E-10,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 31))

    def test_case_35(self):
        input = """11."""
        expect = """11.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 35))

    # def test_case_36(self):
    #     input = """3_000.1_23e-4"""
    #     expect = """3000.1,_23e,-,4,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 36))

    # def test_case_37(self):
    #     input = """123456.7890E-123_4"""
    #     expect = """123456.7890E-123,_4,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 37))

    # def test_case_38(self):
    #     input = """1_0_0_0_0.1_2_3_4E-1_0"""
    #     expect = """10000.1,_2_3_4E,-,10,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 38))

    def test_case_39(self):
        input = """123."""
        expect = """123.,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 39))

    # def test_case_40(self):
    #     input = """1_2.3e4_5"""
    #     expect = """12.3e4,_5,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 40))

    def test_case_41(self):
        input = r""" "Double quote '"" """
        expect = r"""Double quote '",<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 41))

    def test_case_42(self):
        input = """ "Single quote: '''"  """
        expect ="""Single quote: ''',<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 42))

    def test_case_43(self):
        input = """ "Line 1\nLine 2" """
        expect = """Unclosed String: Line 1"""
        self.assertTrue(TestLexer.test(input, expect, 43))

    def test_case_44(self):
        input = """ "Tab:\tTab\t" """
        expect = """Tab:\tTab\t,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 44))

    def test_case_45(self):
        input = """ "Bell: \a" """
        expect = """Bell: \a,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 45))

    def test_case_46(self):
        input = """ "Form feed: \f" """
        expect = """Form feed: \f,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 46))

    def test_case_47(self):
        input = """ "Carriage return:Return" """
        expect = """Carriage return:Return,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 47))

    def test_case_48(self):
        input = """ "Backspace:\bSpace" """
        expect = """Backspace:\bSpace,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 48))

    def test_case_49(self):
        input = """ "Unicode: \\u2764" """
        expect = """Illegal Escape In String: Unicode: \\u"""
        self.assertTrue(TestLexer.test(input, expect, 49))

    def test_case_50(self):
        input = """ "Unicode: \\u0939\" """
        expect = """Illegal Escape In String: Unicode: \\u"""
        self.assertTrue(TestLexer.test(input, expect, 50))

    def test_case_51(self):
        input = """ "Escaped backslash: \\" """
        expect = """Unclosed String: Escaped backslash: \\" """
        self.assertTrue(TestLexer.test(input, expect, 51))

    # def test_case_52(self):
    #     input = """ "Escaped single quote: '\''" """
    #     expect ="""Error Token \""""
    #     self.assertTrue(TestLexer.test(input, expect, 52))

    def test_case_53(self):
        input = """ "Multiple escape characters: \t\n\r" """
        expect = """Unclosed String: Multiple escape characters: 	"""
        self.assertTrue(TestLexer.test(input, expect, 53))

    def test_case_54(self):
        input = """ "Multiple lines:\nLine 1\nLine 2\nLine 3" """
        expect = """Unclosed String: Multiple lines:"""
        self.assertTrue(TestLexer.test(input, expect, 54))

    def test_case_55(self):
        input = """ "Hexadecimal escape: \\t x" """
        expect = """Hexadecimal escape: \\t x,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 55))

    def test_case_56(self):
        input = """ "Mixed Unicode and escape: \c" """
        expect = """Illegal Escape In String: Mixed Unicode and escape: \c"""
        self.assertTrue(TestLexer.test(input, expect, 56))

    def test_case_57(self):
        input = """ "Multi-line and escapes: \n\t\"Hello, 'world'!\"\\nGoodbye." """
        expect = """Unclosed String: Multi-line and escapes: """
        self.assertTrue(TestLexer.test(input, expect, 57))

    def test_case_58(self):
        input = """ "Octal escape: \064" """
        expect = """Octal escape: 4,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 58))
        
    def test_case_60(self):
        input = """ "Unicode plane 2: " """
        expect = """Unicode plane 2: ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 60))

    def test_case_61(self):
        input = """ "" """
        expect = """,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 61))

    def test_case_63(self):
        input = """ func a() """
        expect = """func,a,(,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 63))

    def test_case_64(self):
        input = """ integer """
        expect = """integer,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 64))

    def test_case_65(self):
        input = """func test (number a, bool b) return a+b"""
        expect = """func,test,(,number,a,,,bool,b,),return,a,+,b,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 65))

    def test_case_66(self):
        input = """number a <- 1"""
        expect = """number,a,<-,1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 66))

    # def test_case_67(self):
    #     input = """ a: float = 1; """
    #     expect = """a,:,float,=,1,;,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 67))

    def test_case_68(self):
        input = """ bool a <- 1 """
        expect = """bool,a,<-,1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 68))

    def test_case_69(self):
        input = """printf("I LOVE YOU")"""
        expect = """printf,(,I LOVE YOU,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 69))

    # def test_case_70(self):
    #     input = """ "THAY CHO EM 10 DIEM" """
    #     expect = """THAY CHO EM 10 DIEM,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 70))

    # def test_case_71(self):
    #     input = """ "THAY CHO EM 10 DIEM integer" """
    #     expect = """THAY CHO EM 10 DIEM integer,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 71))

    def test_case_72(self):
        input = """ if(n == 0 ) return 1 """
        expect = """if,(,n,==,0,),return,1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 72))
    # def test_case_73(self):
    #     input = """// THAY CHO EM 10 DIEM"""
    #     expect = """<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 73))

    def test_case_74(self):
        input = """number matrix[4, 4] = [[1, 2, 3, 4]]"""
        expect = """number,matrix,[,4,,,4,],=,[,[,1,,,2,,,3,,,4,],],<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 74))

    def test_case_75(self):
        input = """printf("bool: %s\n", bool ? "true" : "false")   printf("string: %s\n", string)"""
        expect = """printf,(,Unclosed String: bool: %s"""
        self.assertTrue(TestLexer.test(input, expect, 75))

    def test_case_76(self):
        input = """* + > / %"""
        expect = """*,+,>,/,%,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 76))
  

    def test_case_77(self):
        input = """not and or ?"""
        expect = """not,and,or,Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 77))

    def test_case_78(self):
        input = """== != < > <= >="""
        expect = """==,!=,<,>,<=,>=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 78))


    def test_case_79(self):
        input = """..."""
        expect = """...,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 79))


    def test_case_80(self):
        input = """( [] )"""
        expect = """(,[,],),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 80))

    # def test_case_81(self):
    #     input = """[ ]"""
    #     expect = """[,],<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 81))

    # def test_case_82(self):
    #     input = """( {} )"""
    #     expect = """(,{,},),<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 82))

    # def test_case_83(self):
    #     input = ""","""
    #     expect = """,,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 83))

    # def test_case_84(self):
    #     input = """;"""
    #     expect = """;,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 84))

    # def test_case_85(self):
    #     input = """."""
    #     expect = """Error Token ."""
    #     self.assertTrue(TestLexer.test(input, expect, 85))

    # def test_case_86(self):
    #     input = """:"""
    #     expect = """:,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 86))


    def test_case_87(self):
        input = """ "XIN $&@^!\{\}[]#%CHAO" """
        expect = """Illegal Escape In String: XIN $&@^!\{"""
        self.assertTrue(TestLexer.test(input, expect, 87))

    def test_case_88(self):
        input = """ (3 + 4)"""
        expect = """(,3,+,4,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 88))

    def test_case_89(self):
        input = """a and b or c - 1"""
        expect = """a,and,b,or,c,-,1,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 89))

    def test_case_90(self):
        input = """ z > w >="""
        expect = """z,>,w,>=,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 90))

    def test_case_91(self):
        input = """(a and b) ? (c - d)"""
        expect = """(,a,and,b,),Error Token ?"""
        self.assertTrue(TestLexer.test(input, expect, 91))

    def test_case_92(self):
        input = """if x == y then x = x * y else x ++"""
        expect = """if,x,==,y,then,x,=,x,*,y,else,x,+,+,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 92))

    def test_case_93(self):
        input = """for i until i >= 10 by 1 print(i)"""
        expect = """for,i,until,i,>=,10,by,1,print,(,i,),<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 93))

    # def test_case_94(self):
    #     input = """A = 100 // This is a comment"""
    #     expect = """A,=,100,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 94))

    # def test_case_95(self):
    #     input = """/* THAY CHO\nEM 10 \n*/ DIEM"""
    #     expect = """DIEM,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 95))

    # def test_case_96(self):
    #     input = """"/* THAY CHO /* EM */ 10 DIEM */"""
    #     expect = """Unclosed String: /* THAY CHO /* EM */ 10 DIEM */"""
    #     self.assertTrue(TestLexer.test(input, expect, 96))

    # def test_case_97(self):
    #     input = """ ""THAY CHO EM 10 DIEM """
    #     expect = """,THAY,CHO,EM,10,DIEM,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 97))

    # def test_case_98(self):
    #     input = """{}"""
    #     expect = """{,},<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 98))

    # def test_case_99(self):
    #     input = """ /* This is a multiline comment // int z = 20; */  """
    #     expect = """<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 99))

    # def test_case_100(self):
    #     input = """ /* This is a comment that should be ignored */ """
    #     expect = """<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 100))
    def test_case_200(self):
        input = """ This is a "string with \t escape sequences" """
        expect = """This,is,a,string with 	 escape sequences,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 200))
        
    def test_LS201(self):
        self.assertTrue(TestLexer.test("ewrw<wq.QWE>eqw", "ewrw,<,wq,Error Token .", 201))
    
    def test_case_202(self): 
        input =	""" "He asked me: \'"Where is John\'"" """
        expect ="""He asked me: '"Where is John'",<EOF>"""
        self.assertTrue(TestLexer.test(input,expect, 202))
        
    def test_case_203(self):
        input = """ \"dsfg\\e def\" """
        expect = """Illegal Escape In String: dsfg\\e"""
        self.assertTrue(TestLexer.test(input, expect, 203))
    ## -------------------------------------------------------------------
        
    # Single Cases
    def test100_normal_int(self):
        input = """123 0 1234.567 \b 102250 """
        expect = "123,0,1234.567,102250,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 100))

    def test101_normal_float(self):
        input = r"""0.1 0.0001 101.2021 1e10 2E-5 2.5e6 0.004E-2 1.234 1234.567 123.2e+10 0.0 0.00e00 0.00 55."""
        expect = "0.1,0.0001,101.2021,1e10,2E-5,2.5e6,0.004E-2,1.234,1234.567,123.2e+10,0.0,0.00e00,0.00,55.,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 101))

    def test102_normal_boolean(self):
        input = """true \r\n false """
        expect = "true,false,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 102))

    def test103_normal_string(self):
        input = r"""
            "Hello world" "1S0S2" "1234"
        """
        expect = """

,Hello world,1S0S2,1234,

,<EOF>""" 
        self.assertTrue(TestLexer.test(input, expect, 103))

    def test104_keywords(self):
        input = r"""var break bool do elif false number for func if dynamic return string true continue and not or begin end until"""
        expect = "var,break,bool,do,elif,false,number,for,func,if,dynamic,return,string,true,continue,and,not,or,begin,end,until,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 104))

    def test105_operators(self):
        input = r"""+ - * / % == != < <= > >= ..."""
        expect = "+,-,*,/,%,==,!=,<,<=,>,>=,...,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 105))

    def test106_separators(self):
        input = r"""( ) [ ] , =
        """
        expect = """(,),[,],,,=,
        
        ,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 106))

    def test107_normal_line_comments(self):
        input = """
            ## This is a line comment
        """
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 107))

    def test108_normal_block_comments(self):
        input = r"""
            
            abc <- a ## This is a block comment
            
        """
        expect = "abc,<-,a,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 108))

    def test109_normal_array(self):
        input = "[1,2,3,4]"
        expect = "[,1,,,2,,,3,,,4,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 109))

    # # ID
    def test110_lowercase_ID(self):
        input = "abc,2.E1_00"
        expect = "abc,,,2.E1,_00,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 110))

    def test111_uppercase_ID(self):
        input = "ABC"
        expect = "ABC,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 111))

    def test112_alphabet_ID(self):
        input = "aAbBcC AaBbCc"
        expect = "aAbBcC,AaBbCc,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 112))

    def test113_alphanumeric_ID(self):
        input = "aA0bB1cC2 A0aB1bC2c"
        expect = "aA0bB1cC2,A0aB1bC2c,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 113))

    def test114_underscore_ID(self):
        input = "aA0_bB1_cC2 _123"
        expect = "aA0_bB1_cC2,_123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 114))

    def test115_wrong_ID(self):
        input = "1abc )abcd (aka ==hello ...I am crying"
        expect = "1,abc,),abcd,(,aka,==,hello,...,I,am,crying,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 115))

    def test116_weird_char(self):
        input = "SOS#"
        expect = "SOS,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 116))

    def test117_esc_ID(self):
        input = "SOS\\n"
        expect = "SOS,Error Token \\"
        self.assertTrue(TestLexer.test(input, expect, 117))

    def test118_start_with_num_ID(self):
        input = "1_MT"
        expect = "1,_MT,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 118))

    def test119_case_sensitive_ID(self):
        input = "false False fAlSe"
        expect = "false,False,fAlSe,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 119))

    # Keyword, Operators, Separators
    def test120_boolean_operators(self):
        input = "not and or"
        expect = "not,and,or,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 120))

    def test121_arithmetic_operators(self):
        input = "+ - * / %"
        expect = "+,-,*,/,%,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 121))

    def test122_string_index_operators(self):
        input = "... a[5]"
        expect = "...,a,[,5,],<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 122))

    def test123_relational_operators(self):
        input = "== != < > <= >="
        expect = "==,!=,<,>,<=,>=,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 123))

    def test124_mixed_operands_operators(self):
        input = "s1...s2 a<-a+3.5 5*7 a%b 5<=7 c/d"
        expect = "s1,...,s2,a,<-,a,+,3.5,5,*,7,a,%,b,5,<=,7,c,/,d,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 124))

    def test125_invalid_keywords(self):
        input = "ConTiNue BrEAK If"
        expect = "ConTiNue,BrEAK,If,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 125))

    def test126_forloop_keywords(self):
        input = r"""
            for i until i < 10 by 1 
                writeInt(i)
        """
        expect = "for,i,until,i,<,10,by,1,writeInt,(,i,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 126))

    def test127_call_keywords(self):
        input = r"""
            foo(2 + x, 4.0 / y)
            goo()
        """
        expect = "foo,(,2,+,x,,,4.0,/,y,),goo,(,),<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 127))

    def test128_comments_in_keywords(self):
        input = "br##commenteak"
        expect = "br,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 128))

    def test129_comments_in_expr(self):
        input = "1+2##2"
        expect = "1,+,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 129))

    # NUMBER, COMMENT
    def test130_wrong_int(self):
        input = "123a123 0 687 99aa9aaa"
        expect = "123,a123,0,687,99,aa9aaa,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 130))

    def test131_underscore_int(self):
        input = "1234. 123456.0 2.e4567 1.00000000123"
        expect = "1234.,123456.0,2.e4567,1.00000000123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 131))

    def test132_zero_int(self):
        input = "0 09"
        expect = "0,0,9,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 132))

    def test133_nongreedy_cmt(self):
        input = r"""
            ###
                Inside ##
                Block Comment ? ## @@@@@ ^^^^^^ ||||||
             ##   Have # # # # # # # # # # \t \n \r
                */
            ###
        """
        expect = "Inside,Block,Comment,Error Token ?"
        self.assertTrue(TestLexer.test(input, expect, 133))

    def test134_block_cmt(self):
        input = r"""
            
            ##    Hello it's me
            printhere
            ## It's me again */
            ## and again
            ##
        """
        expect = "printhere,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 134))

    def test135_cmt_with_escape(self):
        input = "##Hello. This is comment has \\t \\n \\f \\b \\r \\\\"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 135))

    def test136_nested_cmt_1(self):
        input = "##Outer/*Inner Comment*/Comment*/"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 136))

    def test137_nested_cmt_2(self):
        input = """#Outer#Inner 
                    ##Comment/*Comment*/##
                """
        expect = "Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 137))

    def test138_seq_line_cmt(self):
        input = "##Outer/##Inner"
        expect = "<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 138))

    def test139_mixed_cmt(self):
        input = r"""
            ## Line /* and also block */
            printhere
            ##
            #    Block //and also line
             #   notprinthere
            ##
        """
        expect = "printhere,Error Token #"
        self.assertTrue(TestLexer.test(input, expect, 139))

    # FLOAT
    def test140_without_int_float(self):
        input = ".023 .1e23 .1e-32 .014E+10"
        expect = "Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 140))

    def test141_multipleE_float(self):
        input = "1ee2 1EE2 1eE2 1eE-2"
        expect = "1,ee2,1,EE2,1,eE2,1,eE,-,2,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 141))

    def test142_only_exp_float(self):
        input = "e1 e+1 e-1"
        expect = "e1,e,+,1,e,-,1,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 142))

    def test143_invalid_int_float(self):
        input = "001.001 0_123.001"
        expect = "0,0,1.001,0,_123,Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 143))

    def test144_invalid_underscore(self):
        input = "1.2_345 1e5_123"
        expect = "1.2,_345,1e5,_123,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 144))

    def test145_invalid_decimal(self):
        input = "1.234 1..2 1."
        expect = "1.234,1.,Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 145))

    def test146_empty_decimal(self):
        input = "1. 1.."
        expect = "1.,1.,Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 146))

    def test147_zero_exp(self):
        input = "1e0 1e+0 1e-01 1e"
        expect = "1e0,1e+0,1e-01,1,e,<EOF>"
        self.assertTrue(TestLexer.test(input, expect, 147))

    def test148_invalid_floats(self):
        input = "1e3e1 1e0.1"
        expect = "1e3,e1,1e0,Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 148))

    def test149_valid_floats(self):
        input = "1e-3 1234567e123 12.012 .6e-1"
        expect = "1e-3,1234567e123,12.012,Error Token ."
        self.assertTrue(TestLexer.test(input, expect, 149))

    # STRING
    def test150_unclose_str(self):
        self.assertTrue(
            TestLexer.test('"Hello world', "Unclosed String: Hello world", 150)
        )

    def test151_valid_esc_str(self):
        input = r""""Hello World \t \f \b \\ \'" """
        expect = r"""Hello World \t \f \b \\ \',<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 151))

    def test152_double_quote_str(self):
        self.assertTrue(
            TestLexer.test(
                '"Hello world: \'"Hi\'""', '''Hello world: '"Hi'",<EOF>''', 152
            )
        )

    def test153_ill_esc_str(self):
        self.assertTrue(
            TestLexer.test(
                '"Hello\n"', "Unclosed String: Hello", 153
            )
        )

    def test154_multiple_unclosed_string(self):
        input = """ "Sangvo" "nguyenthien" "ledo"""
        expect = "Sangvo,nguyenthien,Unclosed String: ledo"
        self.assertTrue(TestLexer.test(input, expect, 154))

    def test155_complex_string(self):
        input = (
            """ "This is a complex string with \\"quote\\" and has comment /*abcd*/" """
        )
        expect = """This is a complex string with \\"quote\\" and has comment /*abcd*/,<EOF>"""
        self.assertTrue(TestLexer.test(input, expect, 155))

    # def test156_unclosed_with_escape_seq(self):
    #     input = r"""
    #         "this is valid string \' \" \t \b \f"
    #     """
    #     expect = r"""this is valid string \' \" \t \b \f,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 156))

    # def test157_block_comment_string(self):
    #     input = r"""
    #         ##"This     should not be printed"*/
    #         "##This     should be printed"
    #     """
    #     expect = "/*This     should be printed*/,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 157))

    # def test158_line_comment_string(self):
    #     input = r""" "//Hello" """
    #     expect = "//Hello,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 158))

    # def test159_unclose_string_with_tab(self):
    #     input = """ "abcd\\t """
    #     expect = """Unclosed String: abcd\\t """
    #     self.assertTrue(TestLexer.test(input, expect, 159))

    # # MIXED
    # def test160_unexpected_token_1(self):
    #     input = "abc _ sang@"
    #     expect = "abc,_,sang,Error Token @"
    #     self.assertTrue(TestLexer.test(input, expect, 160))

    # def test161_unexpected_token_2(self):
    #     input = ",sang_?"
    #     expect = ",,sang_,Error Token ?"
    #     self.assertTrue(TestLexer.test(input, expect, 161))

    # def test162_escape_comment(self):
    #     input = "//hello//n"
    #     expect = "<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 162))

    # def test163_unclosed_string_with_illegal_escape(self):
    #     input = """ "Hello163 \t " """
    #     expect = "Hello163 	 ,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 163))

    # def test164_weird_unclose_1(self):
    #     input = r""" "abcd\" """
    #     expect = r"""Unclosed String: abcd\" """
    #     self.assertTrue(TestLexer.test(input, expect, 164))

    # def test165_weird_unclose_2(self):
    #     input = r""" "xyz\" """
    #     expect = """Unclosed String: xyz\\" """
    #     self.assertTrue(TestLexer.test(input, expect, 165))

    # def test166_weird_single_double_quotes(self):
    #     input = r"""
    #         "Sang" "Sang \"SangKha\" \"KhaSang\" KhaSangNguyen" "KhaSang" "" "\"Sang\""
    #     """
    #     expect = r"""Sang,Sang \"SangKha\" \"KhaSang\" KhaSangNguyen,KhaSang,,\"Sang\",<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 166))

    # def test167_string_concat(self):
    #     input = r"""
    #         a: string = "Kha";
    #         b: string = "Sang";
    #         c: string = a::b;
    #     """
    #     expect = (
    #         r"""a,:,string,=,Kha,;,b,:,string,=,Sang,;,c,:,string,=,a,::,b,;,<EOF>"""
    #     )
    #     self.assertTrue(TestLexer.test(input, expect, 167))

    # def test168_string_emojis(self):
    #     input = """
    #         ":)))" ":(((" ":v"
    #         ":o" "c"
    #     """
    #     expect = """:))),:(((,:v,:o,c,<EOF>"""
    #     self.assertTrue(TestLexer.test(input, expect, 168))

    # def test169_string_externel_quotes(self):
    #     input = r"""
    #         str1 = "Can you give me some testcases"
    #         str2 = "No!"
    #         \"Invalid\"
    #     """
    #     expect = """str1,=,Can you give me some testcases,str2,=,No!,Error Token \\"""
    #     self.assertTrue(TestLexer.test(input, expect, 169))

    # def test170_normal_loop(self):
    #     input = """
    #     main: function void (){
    #         for(i=get_started(),i<=5,i+2){
    #             printInteger("Yoooo!");
    #         }
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,for,(,i,=,get_started,(,),,,i,<=,5,,,i,+,2,),{,printInteger,(,Yoooo!,),;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 170))

    # def test171_nested_forloop(self):
    #     input = """
    #     main: function void (){
    #         for(i=get_started(), i<5*2, i+2){
    #             for(j=get_started(), j<5*2, j+1){
    #                 printInteger(i+j);
    #             }
    #         }
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,for,(,i,=,get_started,(,),,,i,<,5,*,2,,,i,+,2,),{,for,(,j,=,get_started,(,),,,j,<,5,*,2,,,j,+,1,),{,printInteger,(,i,+,j,),;,},},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 171))

    # def test172_normal_while(self):
    #     input = """
    #     main: function void (){
    #         while(a<5){
    #             printInteger(a);
    #             a = a+1;
    #         }
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,while,(,a,<,5,),{,printInteger,(,a,),;,a,=,a,+,1,;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 172))

    # def test173_nested_while(self):
    #     input = """
    #     main: function void (){
    #         a: integer = 0;
    #         while(match(a)<10){
    #             printInteger(a);
    #             while(match(a)*match(a)<69)
    #                 printInteger(10-a);
    #         }
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,a,:,integer,=,0,;,while,(,match,(,a,),<,10,),{,printInteger,(,a,),;,while,(,match,(,a,),*,match,(,a,),<,69,),printInteger,(,10,-,a,),;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 173))

    # def test174_normal_dowhile(self):
    #     input = """
    #     main: function void (){
    #         do {
    #             a = a+1;
    #             b = b-1;
    #         }
    #         while(a!=b);
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,do,{,a,=,a,+,1,;,b,=,b,-,1,;,},while,(,a,!=,b,),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 174))

    # def test175_nonblock_dowhile(self):
    #     input = """
    #     main: function void (){
    #         do 
    #             a = a+1;
    #         while(a<10);
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,do,a,=,a,+,1,;,while,(,a,<,10,),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 175))

    # def test176_nested_dowhile(self):
    #     input = """
    #     main: function void (){
    #         do{ 
    #             a = a+1;
    #             i: integer = 0;
    #             do{
    #                 printInteger(i);
    #                 i = i+1;
    #             }
    #             while(i<a);
    #         }
    #         while(a<10);
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,do,{,a,=,a,+,1,;,i,:,integer,=,0,;,do,{,printInteger,(,i,),;,i,=,i,+,1,;,},while,(,i,<,a,),;,},while,(,a,<,10,),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 176))

    # def test177_break_continue_loop(self):
    #     input = """
    #     main: function void (){
    #         for(i=1,i<getMax(),i+1){
    #             if(i==threshold)
    #                 break;
    #             if(i<0)
    #                 continue;
    #             else printInteger(i);
    #         }
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,for,(,i,=,1,,,i,<,getMax,(,),,,i,+,1,),{,if,(,i,==,threshold,),break,;,if,(,i,<,0,),continue,;,else,printInteger,(,i,),;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 177))

    # def test178_mixed_loop(self):
    #     input = """
    #     main: function void (){
    #         for(i=1,i<getMax(),i+1){
    #             while(true){
    #                 print("kaka");
    #                 do{
    #                     print("kuku");
    #                 }
    #                 while(false);
    #             }
    #         }
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,for,(,i,=,1,,,i,<,getMax,(,),,,i,+,1,),{,while,(,true,),{,print,(,kaka,),;,do,{,print,(,kuku,),;,},while,(,false,),;,},},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 178))

    # def test179_oneline_loop(self):
    #     input = """
    #     main: function void (){
    #         k: integer = 5;
    #         for(i=1,i<getMax(),i+1)
    #             printInteger(i);
    #         while((k<200) && (k>0))
    #             k = k + 5;
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,k,:,integer,=,5,;,for,(,i,=,1,,,i,<,getMax,(,),,,i,+,1,),printInteger,(,i,),;,while,(,(,k,<,200,),&&,(,k,>,0,),),k,=,k,+,5,;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 179))

    # def test180_normal_call(self):
    #     input = """
    #     main: function void (){
    #         hello();
    #         hello("Sang");
    #         hello("Sang","Kha");
    #         hello(hello("Sang"),"Kha");
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,hello,(,),;,hello,(,Sang,),;,hello,(,Sang,,,Kha,),;,hello,(,hello,(,Sang,),,,Kha,),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 180))

    # def test181_nested_call(self):
    #     input = """
    #     main: function void (){
    #         f(f());
    #         f(f(f(f(f()))));
    #         f(f(f(f(f(f())))),f(f(f(f(f())))));
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,f,(,f,(,),),;,f,(,f,(,f,(,f,(,f,(,),),),),),;,f,(,f,(,f,(,f,(,f,(,f,(,),),),),),,,f,(,f,(,f,(,f,(,f,(,),),),),),),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 181))

    # def test182_expr_call(self):
    #     input = """
    #     main: function void (){   
    #         f(1*x,_123,"sss"::"aaa",dsa("dsa"),x%5);
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,f,(,1,*,x,,,_123,,,sss,::,aaa,,,dsa,(,dsa,),,,x,%,5,),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 182))

    # def test183_normal_block(self):
    #     input = """
    #     main: function void (){
    #         {}
    #         {
    #             hello();
    #         }
    #         {
    #             a:integer = 1;
    #         }
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,{,},{,hello,(,),;,},{,a,:,integer,=,1,;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 183))

    # def test184_unclose_block(self):
    #     input = """
    #     main: function void(){
    #         {
    #             hello();
    #             a:integer = 1;
    #         {
    #             hello();
    #             a:integer = 1;
    #         }
    #     }
    #     """
    #     expect = "main,:,function,void,(,),{,{,hello,(,),;,a,:,integer,=,1,;,{,hello,(,),;,a,:,integer,=,1,;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 184))

    # def test185_normal_return(self):
    #     input = """
    #         hello: function void(){
    #             printString("hello");
    #         }
    #         one: function integer(x:integer){
    #             return 1;
    #         }
    #     """
    #     expect = "hello,:,function,void,(,),{,printString,(,hello,),;,},one,:,function,integer,(,x,:,integer,),{,return,1,;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 185))

    # def test186_complex_return(self):
    #     input = """
    #         isOdd: function boolean(x:integer){
    #             return x!=0;
    #         }
    #         getArr: function array [3] of integer (x:integer){
    #             return {x,x*2,x*3};
    #         }
    #     """
    #     expect = "isOdd,:,function,boolean,(,x,:,integer,),{,return,x,!=,0,;,},getArr,:,function,array,[,3,],of,integer,(,x,:,integer,),{,return,{,x,,,x,*,2,,,x,*,3,},;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 186))

    # def test187_invalid_return(self):
    #     input = """
    #         mismatchRet: function void(){
    #             return return;
    #         }
    #     """
    #     expect = "mismatchRet,:,function,void,(,),{,return,return,;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 187))

    # def test188_return_not_in_func(self):  # problem: can not solve this with lexer
    #     input = """
    #         missingRet: function void(){
    #             print("hello");
    #         }
    #         return 1;
    #     """
    #     expect = "missingRet,:,function,void,(,),{,print,(,hello,),;,},return,1,;,<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 188))

    # def test189_empty_program(self):
    #     input = """
        
    #     """
    #     expect = "<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 189))

    # def test190_binary_search(self):
    #     input = """
    #         binarySearch: function integer (arr:integer, x:integer, low:integer, high:integer){
    #             if (low>high) return -1;
    #             else{
    #                 mid: integer = (low+high)/2;
    #                 if (x == arr[mid]) return mid;
    #                 else if (x > arr[mid]) return binarySearch(arr,x,mid+1,high);
    #                 else return binarySearch(arr,x,low,mid-1);
    #             }
    #         }
    #     """
    #     expect = "binarySearch,:,function,integer,(,arr,:,integer,,,x,:,integer,,,low,:,integer,,,high,:,integer,),{,if,(,low,>,high,),return,-,1,;,else,{,mid,:,integer,=,(,low,+,high,),/,2,;,if,(,x,==,arr,[,mid,],),return,mid,;,else,if,(,x,>,arr,[,mid,],),return,binarySearch,(,arr,,,x,,,mid,+,1,,,high,),;,else,return,binarySearch,(,arr,,,x,,,low,,,mid,-,1,),;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 190))

    # def test191_interpolation_search(self):
    #     input = """
    #         interpolationSearch: function boolean (arr:array [100] of integer, x:integer, n:integer){
    #             low: integer = 0;
    #             high: integer = n-1;
    #             while((low<=high) && (target>=arr[low]) && (target <=arr[high])){
    #                 pos:integer = low + (((target - arr[low]) * (high - low)) / (arr[high] - arr[low]));
 
    #                 // Check if the target element is at the calculated position
    #                 if( arr[pos] == target){
    #                     return pos;
    #                 }
            
    #                 // If the target element is less than the element at the calculated position, search the left half of the list
    #                 if(arr[pos] > target){
    #                     high = pos - 1;
    #                 }
    #                 else{
    #                     // If the target element is greater than the element at the calculated position, search the right half of the list
    #                     low = pos + 1;
    #                 }
    #             }
    #             return -1;
    #         }
    #     """
    #     expect = "interpolationSearch,:,function,boolean,(,arr,:,array,[,100,],of,integer,,,x,:,integer,,,n,:,integer,),{,low,:,integer,=,0,;,high,:,integer,=,n,-,1,;,while,(,(,low,<=,high,),&&,(,target,>=,arr,[,low,],),&&,(,target,<=,arr,[,high,],),),{,pos,:,integer,=,low,+,(,(,(,target,-,arr,[,low,],),*,(,high,-,low,),),/,(,arr,[,high,],-,arr,[,low,],),),;,if,(,arr,[,pos,],==,target,),{,return,pos,;,},if,(,arr,[,pos,],>,target,),{,high,=,pos,-,1,;,},else,{,low,=,pos,+,1,;,},},return,-,1,;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 191))

    # def test192_selection_sort(self):
    #     input = """
    #         selectionSort: function void (out arr:array [100] of integer, n:integer){
    #             i, j, min_idx: integer;
    #             // One by one move boundary of
    #             // unsorted subarray
    #             for (i = 0, i < n-1, i+1)
    #             {
    #                 // Find the minimum element in
    #                 // unsorted array
    #                 min_idx = i;
    #                 for (j = i+1, j < n, j+1)
    #                 {
    #                 if (arr[j] < arr[min_idx])
    #                     min_idx = j;
    #                 }
    #                 // Swap the found minimum element
    #                 // with the first element
    #                 if (min_idx!=i)
    #                     swap(arr[min_idx], arr[i]);
    #             }
    #         }
    #     """
    #     expect = "selectionSort,:,function,void,(,out,arr,:,array,[,100,],of,integer,,,n,:,integer,),{,i,,,j,,,min_idx,:,integer,;,for,(,i,=,0,,,i,<,n,-,1,,,i,+,1,),{,min_idx,=,i,;,for,(,j,=,i,+,1,,,j,<,n,,,j,+,1,),{,if,(,arr,[,j,],<,arr,[,min_idx,],),min_idx,=,j,;,},if,(,min_idx,!=,i,),swap,(,arr,[,min_idx,],,,arr,[,i,],),;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 192))

    # def test193_merge_sort(self):
    #     input = """
    #         mergeSort: function void (out arr: array [100] of integer, begin:integer, end:integer){
    #             if (begin >= end)
    #                 return; // Returns recursively
            
    #             mid: auto = begin + (end - begin) / 2;
    #             mergeSort(arr, begin, mid);
    #             mergeSort(arr, mid + 1, end);
    #             merge(arr, begin, mid, end);
    #         }
    #     """
    #     expect = "mergeSort,:,function,void,(,out,arr,:,array,[,100,],of,integer,,,begin,:,integer,,,end,:,integer,),{,if,(,begin,>=,end,),return,;,mid,:,auto,=,begin,+,(,end,-,begin,),/,2,;,mergeSort,(,arr,,,begin,,,mid,),;,mergeSort,(,arr,,,mid,+,1,,,end,),;,merge,(,arr,,,begin,,,mid,,,end,),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 193))

    # def test194_quick_sort(self):
    #     input = """
    #         quickSort: function void (out arr:array [100] of integer, low:integer, high:integer){
    #             if (low < high) {
    #                 /* pi is partitioning index, arr[p] is now
    #                 at right place */
    #                 pi:integer = partition(arr, low, high);
            
    #                 // Separately sort elements before
    #                 // partition and after partition
    #                 quickSort(arr, low, pi - 1);
    #                 quickSort(arr, pi + 1, high);
    #             }
    #         }
    #     """
    #     expect = "quickSort,:,function,void,(,out,arr,:,array,[,100,],of,integer,,,low,:,integer,,,high,:,integer,),{,if,(,low,<,high,),{,pi,:,integer,=,partition,(,arr,,,low,,,high,),;,quickSort,(,arr,,,low,,,pi,-,1,),;,quickSort,(,arr,,,pi,+,1,,,high,),;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 194))

    # def test195_heap_sort(self):
    #     input = """
    #         heapSort: function void (out arr:array [100] of integer, n:integer){
    #             // Build heap (rearrange array)
    #             for (i = N / 2 - 1, i >= 0, i-1)
    #                 heapify(arr, N, i);
            
    #             // One by one extract an element
    #             // from heap
    #             for (i = N - 1, i > 0, i-1) {
            
    #                 // Move current root to end
    #                 swap(arr[0], arr[i]);
            
    #                 // call max heapify on the reduced heap
    #                 heapify(arr, i, 0);
    #             }
    #         }
    #     """
    #     expect = "heapSort,:,function,void,(,out,arr,:,array,[,100,],of,integer,,,n,:,integer,),{,for,(,i,=,N,/,2,-,1,,,i,>=,0,,,i,-,1,),heapify,(,arr,,,N,,,i,),;,for,(,i,=,N,-,1,,,i,>,0,,,i,-,1,),{,swap,(,arr,[,0,],,,arr,[,i,],),;,heapify,(,arr,,,i,,,0,),;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 195))

    # def test196_insertion_sort(self):
    #     input = """
    #         insertionSort: function void (out arr:array [100] of integer, n:integer){
    #             i, key, j: integer;
    #             for (i = 1, i < n, i+1)
    #             {
    #                 key = arr[i];
    #                 j = i - 1;
            
    #                 // Move elements of arr[0..i-1], 
    #                 // that are greater than key, to one
    #                 // position ahead of their
    #                 // current position
    #                 while ((j >= 0) && (arr[j] > key))
    #                 {
    #                     arr[j + 1] = arr[j];
    #                     j = j - 1;
    #                 }
    #                 arr[j + 1] = key;
    #             }
    #         }
    #     """
    #     expect = "insertionSort,:,function,void,(,out,arr,:,array,[,100,],of,integer,,,n,:,integer,),{,i,,,key,,,j,:,integer,;,for,(,i,=,1,,,i,<,n,,,i,+,1,),{,key,=,arr,[,i,],;,j,=,i,-,1,;,while,(,(,j,>=,0,),&&,(,arr,[,j,],>,key,),),{,arr,[,j,+,1,],=,arr,[,j,],;,j,=,j,-,1,;,},arr,[,j,+,1,],=,key,;,},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 196))

    # def test197_find_depth_tree(self):
    #     input = """
    #         findDepthRec: function integer (out arr:array [100] of integer, n:integer, out index:integer){
    #             if ((index >= n) || (tree[index] == "l"))
    #                 return 0;
            
    #             // calc height of left subtree (In preorder
    #             // left subtree is processed before right)
    #             index=index+1;
    #             left: integer = findDepthRec(tree, n, index);
            
    #             // calc height of right subtree
    #             index=index+1;
    #             right: integer = findDepthRec(tree, n, index);
            
    #             return max(left, right) + 1;
    #         }
    #         findDepth: function void (out arr:array [100] of integer, n:integer){
    #             index: integer = 0;
    #             return findDepthRec(tree, n, index);
    #         }
    #     """
    #     expect = "findDepthRec,:,function,integer,(,out,arr,:,array,[,100,],of,integer,,,n,:,integer,,,out,index,:,integer,),{,if,(,(,index,>=,n,),||,(,tree,[,index,],==,l,),),return,0,;,index,=,index,+,1,;,left,:,integer,=,findDepthRec,(,tree,,,n,,,index,),;,index,=,index,+,1,;,right,:,integer,=,findDepthRec,(,tree,,,n,,,index,),;,return,max,(,left,,,right,),+,1,;,},findDepth,:,function,void,(,out,arr,:,array,[,100,],of,integer,,,n,:,integer,),{,index,:,integer,=,0,;,return,findDepthRec,(,tree,,,n,,,index,),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 197))

    # def test198_lcs(self):
    #     input = """
    #         lcs: function int (out X:array [100] of integer, out Y:array [100] of integer, n:integer, m:integer){
    #             if (m == 0 || n == 0)
    #                 return 0;
    #             if (X[m-1] == Y[n-1])
    #                 return 1 + lcs(X, Y, m-1, n-1);
    #             else
    #                 return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestLexer.test(input, expect, 198))

    # def test198_lcs(self):
    #     input = """
    #         lcs: function integer (out X:array [100] of integer, out Y:array [100] of integer, n:integer, m:integer){
    #             if ((m == 0) || (n == 0))
    #                 return 0;
    #             if (X[m-1] == Y[n-1])
    #                 return 1 + lcs(X, Y, m-1, n-1);
    #             else
    #                 return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));
    #         }
    #     """
    #     expect = "lcs,:,function,integer,(,out,X,:,array,[,100,],of,integer,,,out,Y,:,array,[,100,],of,integer,,,n,:,integer,,,m,:,integer,),{,if,(,(,m,==,0,),||,(,n,==,0,),),return,0,;,if,(,X,[,m,-,1,],==,Y,[,n,-,1,],),return,1,+,lcs,(,X,,,Y,,,m,-,1,,,n,-,1,),;,else,return,max,(,lcs,(,X,,,Y,,,m,,,n,-,1,),,,lcs,(,X,,,Y,,,m,-,1,,,n,),),;,},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 198))

    # def test199_spiral_matrix(self):
    #     input = """
    #         spiralPrint: function void (out X:array [100,100] of integer, n:integer, m:integer){
    #             i,k,l:integer = -1,0,0;
    #             /* k - starting row index
    #                 m - ending row index
    #                 l - starting column index
    #                 n - ending column index
    #                 i - iterator
    #             */
            
    #             while ((k < m) && (l < n)) {
    #                 /* Print the first row from
    #                     the remaining rows */
    #                 for (i = l, i < n, i+1) {
    #                     printString(a[k,i]);
    #                 }
    #                 k=k+1;
            
    #                 /* Print the last column
    #                 from the remaining columns */
    #                 for (i = k, i < m, i+1) {
    #                     printString(a[i,n-1]);
    #                 }
    #                 n=n-1;
            
    #                 /* Print the last row from
    #                         the remaining rows */
    #                 if (k < m) {
    #                     for (i = n - 1, i >= l, i-1) {
    #                         printString(a[m-1,i]);
    #                     }
    #                     m=m-1;
    #                 }
            
    #                 /* Print the first column from
    #                         the remaining columns */
    #                 if (l < n) {
    #                     for (i = m - 1, i >= k, i-1) {
    #                         printString(a[i,l]);
    #                     }
    #                     l=l+1;
    #                 }
    #             }
    #         }
    #     """
    #     expect = "spiralPrint,:,function,void,(,out,X,:,array,[,100,,,100,],of,integer,,,n,:,integer,,,m,:,integer,),{,i,,,k,,,l,:,integer,=,-,1,,,0,,,0,;,while,(,(,k,<,m,),&&,(,l,<,n,),),{,for,(,i,=,l,,,i,<,n,,,i,+,1,),{,printString,(,a,[,k,,,i,],),;,},k,=,k,+,1,;,for,(,i,=,k,,,i,<,m,,,i,+,1,),{,printString,(,a,[,i,,,n,-,1,],),;,},n,=,n,-,1,;,if,(,k,<,m,),{,for,(,i,=,n,-,1,,,i,>=,l,,,i,-,1,),{,printString,(,a,[,m,-,1,,,i,],),;,},m,=,m,-,1,;,},if,(,l,<,n,),{,for,(,i,=,m,-,1,,,i,>=,k,,,i,-,1,),{,printString,(,a,[,i,,,l,],),;,},l,=,l,+,1,;,},},},<EOF>"
    #     self.assertTrue(TestLexer.test(input, expect, 199))