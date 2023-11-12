# Generated from Makefile.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MakefileParser import MakefileParser
else:
    from MakefileParser import MakefileParser

# This class defines a complete generic visitor for a parse tree produced by MakefileParser.

class MakefileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MakefileParser#makefile.
    def visitMakefile(self, ctx:MakefileParser.MakefileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MakefileParser#identity.
    def visitIdentity(self, ctx:MakefileParser.IdentityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MakefileParser#conditional.
    def visitConditional(self, ctx:MakefileParser.ConditionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MakefileParser#rule.
    def visitRule(self, ctx:MakefileParser.RuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MakefileParser#assign.
    def visitAssign(self, ctx:MakefileParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MakefileParser#statement.
    def visitStatement(self, ctx:MakefileParser.StatementContext):
        return self.visitChildren(ctx)



del MakefileParser