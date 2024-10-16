import sys
from antlr4 import *
from FuncionesLexer import FuncionesLexer
from FuncionesParser import FuncionesParser
from myvisitor import MyVisitor

def main():
    input_stream = FileStream(sys.argv[1])
    lexer = FuncionesLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = FuncionesParser(stream)
    tree = parser.program()
    visitor = MyVisitor()
    result = visitor.visit(tree)
    print(result)

if __name__ == "__main__":
    main()
