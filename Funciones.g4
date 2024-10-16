grammar Funciones;

program
    : statement+ EOF
    ;

statement
    : mapStatement
    | filterStatement
    ;

mapStatement
    : 'MAP' '(' expression ',' iterable ')'
    ;

filterStatement
    : 'FILTER' '(' conditionExpression ',' iterable ')'
    ;

expression
    : IDENTIFIER
    | NUMBER
    | STRING
    | '(' expression ')' // Permite anidar expresiones
    ;

conditionExpression
    : IDENTIFIER
    | comparison
    ;

iterable
    : lista
    | tupla
    ;

lista
    : '[' (expression (',' expression)*)? ']'
    ;

tupla
    : '(' (expression (',' expression)*)? ')'
    ;

comparison
    : IDENTIFIER comparisonOperator expression
    ;

comparisonOperator
    : '==' | '!=' | '<' | '<=' | '>' | '>='
    ;

IDENTIFIER
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

NUMBER
    : [0-9]+ ('.' [0-9]+)? // Soporta números decimales
    ;

STRING
    : '"' (~["\r\n] | '""')* '"'
    ;

WS
    : [ \t\r\n]+ -> skip
    ;
