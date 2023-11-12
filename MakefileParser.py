# Generated from Makefile.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,55,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,0,
        14,8,0,11,0,12,0,15,1,0,1,0,1,1,4,1,21,8,1,11,1,12,1,22,1,2,1,2,
        1,2,1,2,3,2,29,8,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,37,8,3,1,3,1,3,1,
        4,1,4,1,4,1,4,3,4,45,8,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,53,8,5,1,5,
        0,0,6,0,2,4,6,8,10,0,1,1,0,1,4,56,0,13,1,0,0,0,2,20,1,0,0,0,4,24,
        1,0,0,0,6,32,1,0,0,0,8,40,1,0,0,0,10,52,1,0,0,0,12,14,3,10,5,0,13,
        12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,
        0,17,18,5,0,0,1,18,1,1,0,0,0,19,21,8,0,0,0,20,19,1,0,0,0,21,22,1,
        0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,23,3,1,0,0,0,24,25,5,5,0,0,25,
        26,5,7,0,0,26,28,3,2,1,0,27,29,5,1,0,0,28,27,1,0,0,0,28,29,1,0,0,
        0,29,30,1,0,0,0,30,31,5,2,0,0,31,5,1,0,0,0,32,33,3,2,1,0,33,34,5,
        3,0,0,34,36,3,2,1,0,35,37,5,1,0,0,36,35,1,0,0,0,36,37,1,0,0,0,37,
        38,1,0,0,0,38,39,5,2,0,0,39,7,1,0,0,0,40,41,3,2,1,0,41,42,5,4,0,
        0,42,44,3,2,1,0,43,45,5,1,0,0,44,43,1,0,0,0,44,45,1,0,0,0,45,46,
        1,0,0,0,46,47,5,2,0,0,47,9,1,0,0,0,48,53,3,4,2,0,49,53,3,6,3,0,50,
        53,3,8,4,0,51,53,5,6,0,0,52,48,1,0,0,0,52,49,1,0,0,0,52,50,1,0,0,
        0,52,51,1,0,0,0,53,11,1,0,0,0,6,15,22,28,36,44,52
    ]

class MakefileParser ( Parser ):

    grammarFileName = "Makefile.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\r'", "'\\n'", "':'", "'='", "'ifeq'", 
                     "'endif'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "IFEQ", "ENDIF", "WS", "NL" ]

    RULE_makefile = 0
    RULE_identity = 1
    RULE_conditional = 2
    RULE_rule = 3
    RULE_assign = 4
    RULE_statement = 5

    ruleNames =  [ "makefile", "identity", "conditional", "rule", "assign", 
                   "statement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    IFEQ=5
    ENDIF=6
    WS=7
    NL=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MakefileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MakefileParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MakefileParser.StatementContext)
            else:
                return self.getTypedRuleContext(MakefileParser.StatementContext,i)


        def getRuleIndex(self):
            return MakefileParser.RULE_makefile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMakefile" ):
                listener.enterMakefile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMakefile" ):
                listener.exitMakefile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMakefile" ):
                return visitor.visitMakefile(self)
            else:
                return visitor.visitChildren(self)




    def makefile(self):

        localctx = MakefileParser.MakefileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_makefile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.statement()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                    break

            self.state = 17
            self.match(MakefileParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MakefileParser.RULE_identity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentity" ):
                listener.enterIdentity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentity" ):
                listener.exitIdentity(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentity" ):
                return visitor.visitIdentity(self)
            else:
                return visitor.visitChildren(self)




    def identity(self):

        localctx = MakefileParser.IdentityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_identity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                _la = self._input.LA(1)
                if _la <= 0 or (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 480) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IFEQ(self):
            return self.getToken(MakefileParser.IFEQ, 0)

        def WS(self):
            return self.getToken(MakefileParser.WS, 0)

        def identity(self):
            return self.getTypedRuleContext(MakefileParser.IdentityContext,0)


        def getRuleIndex(self):
            return MakefileParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional" ):
                return visitor.visitConditional(self)
            else:
                return visitor.visitChildren(self)




    def conditional(self):

        localctx = MakefileParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_conditional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(MakefileParser.IFEQ)
            self.state = 25
            self.match(MakefileParser.WS)
            self.state = 26
            self.identity()
            self.state = 28
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 27
                self.match(MakefileParser.T__0)


            self.state = 30
            self.match(MakefileParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MakefileParser.IdentityContext)
            else:
                return self.getTypedRuleContext(MakefileParser.IdentityContext,i)


        def getRuleIndex(self):
            return MakefileParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule" ):
                return visitor.visitRule(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = MakefileParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.identity()
            self.state = 33
            self.match(MakefileParser.T__2)
            self.state = 34
            self.identity()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 35
                self.match(MakefileParser.T__0)


            self.state = 38
            self.match(MakefileParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identity(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MakefileParser.IdentityContext)
            else:
                return self.getTypedRuleContext(MakefileParser.IdentityContext,i)


        def getRuleIndex(self):
            return MakefileParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = MakefileParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.identity()
            self.state = 41
            self.match(MakefileParser.T__3)
            self.state = 42
            self.identity()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 43
                self.match(MakefileParser.T__0)


            self.state = 46
            self.match(MakefileParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional(self):
            return self.getTypedRuleContext(MakefileParser.ConditionalContext,0)


        def rule_(self):
            return self.getTypedRuleContext(MakefileParser.RuleContext,0)


        def assign(self):
            return self.getTypedRuleContext(MakefileParser.AssignContext,0)


        def ENDIF(self):
            return self.getToken(MakefileParser.ENDIF, 0)

        def getRuleIndex(self):
            return MakefileParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MakefileParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.conditional()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.rule_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.assign()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.match(MakefileParser.ENDIF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





