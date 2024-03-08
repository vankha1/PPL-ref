# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("p\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\3\3\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3")
        buf.write("\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\21\6\21Z\n\21\r\21\16\21[\3\22\6\22_\n\22\r\22\16\22")
        buf.write("`\3\23\6\23d\n\23\r\23\16\23e\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\2\2\27\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27\3\2\5\3\2\62;\4\2C\\c|\5\2\13\f\17\17")
        buf.write("\"\"\2r\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write("\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3")
        buf.write("\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3")
        buf.write("-\3\2\2\2\5/\3\2\2\2\7\61\3\2\2\2\t\63\3\2\2\2\13\65\3")
        buf.write("\2\2\2\r\67\3\2\2\2\17>\3\2\2\2\21@\3\2\2\2\23B\3\2\2")
        buf.write("\2\25D\3\2\2\2\27F\3\2\2\2\31H\3\2\2\2\33L\3\2\2\2\35")
        buf.write("R\3\2\2\2\37T\3\2\2\2!Y\3\2\2\2#^\3\2\2\2%c\3\2\2\2\'")
        buf.write("i\3\2\2\2)l\3\2\2\2+n\3\2\2\2-.\7-\2\2.\4\3\2\2\2/\60")
        buf.write("\7/\2\2\60\6\3\2\2\2\61\62\7,\2\2\62\b\3\2\2\2\63\64\7")
        buf.write("\61\2\2\64\n\3\2\2\2\65\66\7?\2\2\66\f\3\2\2\2\678\7t")
        buf.write("\2\289\7g\2\29:\7v\2\2:;\7w\2\2;<\7t\2\2<=\7p\2\2=\16")
        buf.write("\3\2\2\2>?\7*\2\2?\20\3\2\2\2@A\7+\2\2A\22\3\2\2\2BC\7")
        buf.write("}\2\2C\24\3\2\2\2DE\7\177\2\2E\26\3\2\2\2FG\7.\2\2G\30")
        buf.write("\3\2\2\2HI\7k\2\2IJ\7p\2\2JK\7v\2\2K\32\3\2\2\2LM\7h\2")
        buf.write("\2MN\7n\2\2NO\7q\2\2OP\7c\2\2PQ\7v\2\2Q\34\3\2\2\2RS\7")
        buf.write("=\2\2S\36\3\2\2\2TU\5!\21\2UV\7\60\2\2VW\5!\21\2W \3\2")
        buf.write("\2\2XZ\t\2\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\\3\2\2")
        buf.write("\2\\\"\3\2\2\2]_\t\3\2\2^]\3\2\2\2_`\3\2\2\2`^\3\2\2\2")
        buf.write("`a\3\2\2\2a$\3\2\2\2bd\t\4\2\2cb\3\2\2\2de\3\2\2\2ec\3")
        buf.write("\2\2\2ef\3\2\2\2fg\3\2\2\2gh\b\23\2\2h&\3\2\2\2ij\13\2")
        buf.write("\2\2jk\b\24\3\2k(\3\2\2\2lm\13\2\2\2m*\3\2\2\2no\13\2")
        buf.write("\2\2o,\3\2\2\2\6\2[`e\4\b\2\2\3\24\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    EQUAL = 5
    RETURN = 6
    LB = 7
    RB = 8
    LR = 9
    RR = 10
    COMMA = 11
    INT = 12
    FLOAT = 13
    SEMI = 14
    FLOATLIT = 15
    INTLIT = 16
    ID = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'='", "'return'", "'('", "')'", 
            "'{'", "'}'", "','", "'int'", "'float'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "EQUAL", "RETURN", "LB", "RB", "LR", 
            "RR", "COMMA", "INT", "FLOAT", "SEMI", "FLOATLIT", "INTLIT", 
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ADD", "SUB", "MUL", "DIV", "EQUAL", "RETURN", "LB", "RB", 
                  "LR", "RR", "COMMA", "INT", "FLOAT", "SEMI", "FLOATLIT", 
                  "INTLIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


