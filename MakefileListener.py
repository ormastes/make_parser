# Generated from Makefile.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MakefileParser import MakefileParser
else:
    from MakefileParser import MakefileParser

# This class defines a complete listener for a parse tree produced by MakefileParser.
class MakefileListener(ParseTreeListener):

    # Enter a parse tree produced by MakefileParser#makefile.
    def enterMakefile(self, ctx:MakefileParser.MakefileContext):
        pass

    # Exit a parse tree produced by MakefileParser#makefile.
    def exitMakefile(self, ctx:MakefileParser.MakefileContext):
        pass


    # Enter a parse tree produced by MakefileParser#identity.
    def enterIdentity(self, ctx:MakefileParser.IdentityContext):
        pass

    # Exit a parse tree produced by MakefileParser#identity.
    def exitIdentity(self, ctx:MakefileParser.IdentityContext):
        pass


    # Enter a parse tree produced by MakefileParser#conditional.
    def enterConditional(self, ctx:MakefileParser.ConditionalContext):
        pass

    # Exit a parse tree produced by MakefileParser#conditional.
    def exitConditional(self, ctx:MakefileParser.ConditionalContext):
        pass


    # Enter a parse tree produced by MakefileParser#rule.
    def enterRule(self, ctx:MakefileParser.RuleContext):
        pass

    # Exit a parse tree produced by MakefileParser#rule.
    def exitRule(self, ctx:MakefileParser.RuleContext):
        pass


    # Enter a parse tree produced by MakefileParser#assign.
    def enterAssign(self, ctx:MakefileParser.AssignContext):
        pass

    # Exit a parse tree produced by MakefileParser#assign.
    def exitAssign(self, ctx:MakefileParser.AssignContext):
        pass


    # Enter a parse tree produced by MakefileParser#statement.
    def enterStatement(self, ctx:MakefileParser.StatementContext):
        pass

    # Exit a parse tree produced by MakefileParser#statement.
    def exitStatement(self, ctx:MakefileParser.StatementContext):
        pass



del MakefileParser