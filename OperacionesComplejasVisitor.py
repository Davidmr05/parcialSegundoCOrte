# Generated from OperacionesComplejas.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .OperacionesComplejasParser import OperacionesComplejasParser
else:
    from OperacionesComplejasParser import OperacionesComplejasParser

# This class defines a complete generic visitor for a parse tree produced by OperacionesComplejasParser.

class OperacionesComplejasVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OperacionesComplejasParser#prog.
    def visitProg(self, ctx:OperacionesComplejasParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperacionesComplejasParser#Print.
    def visitPrint(self, ctx:OperacionesComplejasParser.PrintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperacionesComplejasParser#Operar.
    def visitOperar(self, ctx:OperacionesComplejasParser.OperarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperacionesComplejasParser#DefComplex.
    def visitDefComplex(self, ctx:OperacionesComplejasParser.DefComplexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperacionesComplejasParser#real.
    def visitReal(self, ctx:OperacionesComplejasParser.RealContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperacionesComplejasParser#img.
    def visitImg(self, ctx:OperacionesComplejasParser.ImgContext):
        return self.visitChildren(ctx)



del OperacionesComplejasParser