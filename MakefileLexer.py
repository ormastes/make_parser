# Generated from Makefile.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,48,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,4,6,38,8,6,11,6,12,6,39,1,6,1,6,1,
        7,3,7,45,8,7,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,
        0,1,2,0,9,9,32,32,49,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,
        0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,1,17,1,0,
        0,0,3,19,1,0,0,0,5,21,1,0,0,0,7,23,1,0,0,0,9,25,1,0,0,0,11,30,1,
        0,0,0,13,37,1,0,0,0,15,44,1,0,0,0,17,18,5,13,0,0,18,2,1,0,0,0,19,
        20,5,10,0,0,20,4,1,0,0,0,21,22,5,58,0,0,22,6,1,0,0,0,23,24,5,61,
        0,0,24,8,1,0,0,0,25,26,5,105,0,0,26,27,5,102,0,0,27,28,5,101,0,0,
        28,29,5,113,0,0,29,10,1,0,0,0,30,31,5,101,0,0,31,32,5,110,0,0,32,
        33,5,100,0,0,33,34,5,105,0,0,34,35,5,102,0,0,35,12,1,0,0,0,36,38,
        7,0,0,0,37,36,1,0,0,0,38,39,1,0,0,0,39,37,1,0,0,0,39,40,1,0,0,0,
        40,41,1,0,0,0,41,42,6,6,0,0,42,14,1,0,0,0,43,45,5,13,0,0,44,43,1,
        0,0,0,44,45,1,0,0,0,45,46,1,0,0,0,46,47,5,10,0,0,47,16,1,0,0,0,3,
        0,39,44,1,6,0,0
    ]

class MakefileLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    IFEQ = 5
    ENDIF = 6
    WS = 7
    NL = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\\r'", "'\\n'", "':'", "'='", "'ifeq'", "'endif'" ]

    symbolicNames = [ "<INVALID>",
            "IFEQ", "ENDIF", "WS", "NL" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "IFEQ", "ENDIF", "WS", 
                  "NL" ]

    grammarFileName = "Makefile.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


