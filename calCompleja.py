# calCompleja.py

from antlr4 import *
from OperacionesComplejasLexer import OperacionesComplejasLexer
from OperacionesComplejasParser import OperacionesComplejasParser
from myVisitor import myVisitor  # Asegúrate de que la clase sea myVisitor y esté definida correctamente

def main():
    # Cargar el archivo de entrada
    input_stream = FileStream('input.txt')
    
    # Crear el lexer
    lexer = OperacionesComplejasLexer(input_stream)
    
    # Crear el flujo de tokens
    stream = CommonTokenStream(lexer)
    
    # Crear el parser
    parser = OperacionesComplejasParser(stream)
    
    # Parsear la entrada y obtener el árbol de análisis
    tree = parser.expr()  # Asegúrate de que 'expr' sea la regla principal en tu gramática
    
    # Crear el visitante
    visitor = myVisitor()  # Asegúrate de que el nombre de la clase coincida
    
    # Visitar el árbol de análisis y obtener el resultado
    result = visitor.visit(tree)
    
    # Imprimir el resultado
    print(f'Resultado: {result}')

if __name__ == '__main__':
    main()
