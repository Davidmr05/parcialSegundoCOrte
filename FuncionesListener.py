# Generated from Funciones.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FuncionesParser import FuncionesParser
else:
    from FuncionesParser import FuncionesParser

# This class defines a complete listener for a parse tree produced by FuncionesParser.
class FuncionesListener(ParseTreeListener):

    # Enter a parse tree produced by FuncionesParser#program.
    def enterProgram(self, ctx:FuncionesParser.ProgramContext):
        pass

    # Exit a parse tree produced by FuncionesParser#program.
    def exitProgram(self, ctx:FuncionesParser.ProgramContext):
        pass


    # Enter a parse tree produced by FuncionesParser#statement.
    def enterStatement(self, ctx:FuncionesParser.StatementContext):
        pass

    # Exit a parse tree produced by FuncionesParser#statement.
    def exitStatement(self, ctx:FuncionesParser.StatementContext):
        pass


    # Enter a parse tree produced by FuncionesParser#mapStatement.
    def enterMapStatement(self, ctx:FuncionesParser.MapStatementContext):
        pass

    # Exit a parse tree produced by FuncionesParser#mapStatement.
    def exitMapStatement(self, ctx:FuncionesParser.MapStatementContext):
        pass


    # Enter a parse tree produced by FuncionesParser#filterStatement.
    def enterFilterStatement(self, ctx:FuncionesParser.FilterStatementContext):
        pass

    # Exit a parse tree produced by FuncionesParser#filterStatement.
    def exitFilterStatement(self, ctx:FuncionesParser.FilterStatementContext):
        pass


    # Enter a parse tree produced by FuncionesParser#expression.
    def enterExpression(self, ctx:FuncionesParser.ExpressionContext):
        pass

    # Exit a parse tree produced by FuncionesParser#expression.
    def exitExpression(self, ctx:FuncionesParser.ExpressionContext):
        pass


    # Enter a parse tree produced by FuncionesParser#conditionExpression.
    def enterConditionExpression(self, ctx:FuncionesParser.ConditionExpressionContext):
        pass

    # Exit a parse tree produced by FuncionesParser#conditionExpression.
    def exitConditionExpression(self, ctx:FuncionesParser.ConditionExpressionContext):
        pass


    # Enter a parse tree produced by FuncionesParser#iterable.
    def enterIterable(self, ctx:FuncionesParser.IterableContext):
        pass

    # Exit a parse tree produced by FuncionesParser#iterable.
    def exitIterable(self, ctx:FuncionesParser.IterableContext):
        pass


    # Enter a parse tree produced by FuncionesParser#lista.
    def enterLista(self, ctx:FuncionesParser.ListaContext):
        pass

    # Exit a parse tree produced by FuncionesParser#lista.
    def exitLista(self, ctx:FuncionesParser.ListaContext):
        pass


    # Enter a parse tree produced by FuncionesParser#tupla.
    def enterTupla(self, ctx:FuncionesParser.TuplaContext):
        pass

    # Exit a parse tree produced by FuncionesParser#tupla.
    def exitTupla(self, ctx:FuncionesParser.TuplaContext):
        pass


    # Enter a parse tree produced by FuncionesParser#comparison.
    def enterComparison(self, ctx:FuncionesParser.ComparisonContext):
        pass

    # Exit a parse tree produced by FuncionesParser#comparison.
    def exitComparison(self, ctx:FuncionesParser.ComparisonContext):
        pass


    # Enter a parse tree produced by FuncionesParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:FuncionesParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by FuncionesParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:FuncionesParser.ComparisonOperatorContext):
        pass



del FuncionesParser