# Generated from d:/Learning_Documents_of_Third_Year/Principles of Programming Languages/Assignment 222/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,6,71,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,1,1,
        1,1,1,1,1,1,1,3,1,32,8,1,1,1,1,1,3,1,36,8,1,1,2,4,2,39,8,2,11,2,
        12,2,40,1,3,1,3,4,3,45,8,3,11,3,12,3,46,1,4,1,4,3,4,51,8,4,1,4,4,
        4,54,8,4,11,4,12,4,55,1,5,4,5,59,8,5,11,5,12,5,60,1,5,1,5,1,6,1,
        6,1,6,1,7,1,7,1,8,1,8,0,0,9,1,1,3,2,5,0,7,0,9,0,11,3,13,4,15,5,17,
        6,1,0,6,1,0,97,122,2,0,48,57,97,122,1,0,48,57,2,0,69,69,101,101,
        2,0,43,43,45,45,3,0,9,10,13,13,32,32,75,0,1,1,0,0,0,0,3,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,
        3,35,1,0,0,0,5,38,1,0,0,0,7,42,1,0,0,0,9,48,1,0,0,0,11,58,1,0,0,
        0,13,64,1,0,0,0,15,67,1,0,0,0,17,69,1,0,0,0,19,23,7,0,0,0,20,22,
        7,1,0,0,21,20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,
        24,2,1,0,0,0,25,23,1,0,0,0,26,27,3,5,2,0,27,28,3,7,3,0,28,36,1,0,
        0,0,29,31,3,5,2,0,30,32,3,7,3,0,31,30,1,0,0,0,31,32,1,0,0,0,32,33,
        1,0,0,0,33,34,3,9,4,0,34,36,1,0,0,0,35,26,1,0,0,0,35,29,1,0,0,0,
        36,4,1,0,0,0,37,39,7,2,0,0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,
        0,0,40,41,1,0,0,0,41,6,1,0,0,0,42,44,5,46,0,0,43,45,7,2,0,0,44,43,
        1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,46,47,1,0,0,0,47,8,1,0,0,0,48,
        50,7,3,0,0,49,51,7,4,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,53,1,0,0,
        0,52,54,7,2,0,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,
        1,0,0,0,56,10,1,0,0,0,57,59,7,5,0,0,58,57,1,0,0,0,59,60,1,0,0,0,
        60,58,1,0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,63,6,5,0,0,63,12,1,
        0,0,0,64,65,9,0,0,0,65,66,6,6,1,0,66,14,1,0,0,0,67,68,9,0,0,0,68,
        16,1,0,0,0,69,70,9,0,0,0,70,18,1,0,0,0,9,0,23,31,35,40,46,50,55,
        60,2,6,0,0,1,6,0
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    REAL = 2
    WS = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "REAL", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IDENTIFIER", "REAL", "INTPART", "DECPART", "EXPPART", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


