import sys
from antlr4 import *
from MakefileLexer import MakefileLexer
from MakefileParser import MakefileParser
from MakefileVisitor import MakefileVisitor


class MyVisitor(MakefileVisitor):

    # Visit a parse tree produced by makefileParser#makefile.
    def visitMakefile(self, ctx:MakefileParser.MakefileContext):
        text = ctx.getText()
        return self.visitChildren(ctx)



    # Visit a parse tree produced by makefileParser#statement.
    def visitStatement(self, ctx:MakefileParser.StatementContext):
        text = ctx.getText()
        print('statement: ', text)
        return self.visitChildren(ctx)
        # Visit a parse tree produced by MakefileParser#conditional.
    def visitConditional(self, ctx:MakefileParser.ConditionalContext):
        text = ctx.getText()
        print('condition: ', text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MakefileParser#rule.
    def visitRule(self, ctx:MakefileParser.RuleContext):
        text = ctx.getText()
        print('rule: ', text)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MakefileParser#assign.
    def visitAssign(self, ctx:MakefileParser.AssignContext):
        text = ctx.getText()
        print('assign: ', text)
        return self.visitChildren(ctx)
    
def main(argv):
    input_stream = FileStream('sample.mk')
    lexer = MakefileLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MakefileParser(stream)
    tree = parser.makefile()
     # evaluator
    visitor = MyVisitor()
    output = visitor.visit(tree)
    print(output)


if __name__ == '__main__':
    main(sys.argv)