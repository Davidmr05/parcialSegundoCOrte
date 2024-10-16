from FuncionesParser import FuncionesParser
from antlr4 import ParseTreeVisitor

class MyVisitor(ParseTreeVisitor):
    def visitMapStatement(self, ctx: FuncionesParser.MapStatementContext):
        function = ctx.expression().getText()
        iterable = ctx.iterable().getText()
        return f"map({function}, {iterable})"

    def visitFilterStatement(self, ctx: FuncionesParser.FilterStatementContext):
        condition = ctx.conditionExpression().getText()
        iterable = ctx.iterable().getText()
        return f"filter({condition}, {iterable})"
