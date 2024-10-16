# Generated from Funciones.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\2\3\2\3\3\3\3\5\3\"\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\69\n\6\3\7\3\7\5\7=\n\7\3\b\3\b\5\bA")
        buf.write("\n\b\3\t\3\t\3\t\3\t\7\tG\n\t\f\t\16\tJ\13\t\5\tL\n\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\7\nT\n\n\f\n\16\nW\13\n\5\nY")
        buf.write("\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\2\3\3\2\n\17\2b\2\31\3\2\2\2\4")
        buf.write("!\3\2\2\2\6#\3\2\2\2\b*\3\2\2\2\n8\3\2\2\2\f<\3\2\2\2")
        buf.write("\16@\3\2\2\2\20B\3\2\2\2\22O\3\2\2\2\24\\\3\2\2\2\26`")
        buf.write("\3\2\2\2\30\32\5\4\3\2\31\30\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\31\3\2\2\2\33\34\3\2\2\2\34\35\3\2\2\2\35\36\7\2\2\3")
        buf.write("\36\3\3\2\2\2\37\"\5\6\4\2 \"\5\b\5\2!\37\3\2\2\2! \3")
        buf.write("\2\2\2\"\5\3\2\2\2#$\7\3\2\2$%\7\4\2\2%&\5\n\6\2&\'\7")
        buf.write("\5\2\2\'(\5\16\b\2()\7\6\2\2)\7\3\2\2\2*+\7\7\2\2+,\7")
        buf.write("\4\2\2,-\5\f\7\2-.\7\5\2\2./\5\16\b\2/\60\7\6\2\2\60\t")
        buf.write("\3\2\2\2\619\7\20\2\2\629\7\21\2\2\639\7\22\2\2\64\65")
        buf.write("\7\4\2\2\65\66\5\n\6\2\66\67\7\6\2\2\679\3\2\2\28\61\3")
        buf.write("\2\2\28\62\3\2\2\28\63\3\2\2\28\64\3\2\2\29\13\3\2\2\2")
        buf.write(":=\7\20\2\2;=\5\24\13\2<:\3\2\2\2<;\3\2\2\2=\r\3\2\2\2")
        buf.write(">A\5\20\t\2?A\5\22\n\2@>\3\2\2\2@?\3\2\2\2A\17\3\2\2\2")
        buf.write("BK\7\b\2\2CH\5\n\6\2DE\7\5\2\2EG\5\n\6\2FD\3\2\2\2GJ\3")
        buf.write("\2\2\2HF\3\2\2\2HI\3\2\2\2IL\3\2\2\2JH\3\2\2\2KC\3\2\2")
        buf.write("\2KL\3\2\2\2LM\3\2\2\2MN\7\t\2\2N\21\3\2\2\2OX\7\4\2\2")
        buf.write("PU\5\n\6\2QR\7\5\2\2RT\5\n\6\2SQ\3\2\2\2TW\3\2\2\2US\3")
        buf.write("\2\2\2UV\3\2\2\2VY\3\2\2\2WU\3\2\2\2XP\3\2\2\2XY\3\2\2")
        buf.write("\2YZ\3\2\2\2Z[\7\6\2\2[\23\3\2\2\2\\]\7\20\2\2]^\5\26")
        buf.write("\f\2^_\5\n\6\2_\25\3\2\2\2`a\t\2\2\2a\27\3\2\2\2\13\33")
        buf.write("!8<@HKUX")
        return buf.getvalue()


class FuncionesParser ( Parser ):

    grammarFileName = "Funciones.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'('", "','", "')'", "'FILTER'", 
                     "'['", "']'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER", "NUMBER", 
                      "STRING", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_mapStatement = 2
    RULE_filterStatement = 3
    RULE_expression = 4
    RULE_conditionExpression = 5
    RULE_iterable = 6
    RULE_lista = 7
    RULE_tupla = 8
    RULE_comparison = 9
    RULE_comparisonOperator = 10

    ruleNames =  [ "program", "statement", "mapStatement", "filterStatement", 
                   "expression", "conditionExpression", "iterable", "lista", 
                   "tupla", "comparison", "comparisonOperator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    IDENTIFIER=14
    NUMBER=15
    STRING=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FuncionesParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncionesParser.StatementContext)
            else:
                return self.getTypedRuleContext(FuncionesParser.StatementContext,i)


        def getRuleIndex(self):
            return FuncionesParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = FuncionesParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FuncionesParser.T__0 or _la==FuncionesParser.T__4):
                    break

            self.state = 27
            self.match(FuncionesParser.EOF)
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

        def mapStatement(self):
            return self.getTypedRuleContext(FuncionesParser.MapStatementContext,0)


        def filterStatement(self):
            return self.getTypedRuleContext(FuncionesParser.FilterStatementContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = FuncionesParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FuncionesParser.T__0]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.mapStatement()
                pass
            elif token in [FuncionesParser.T__4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.filterStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MapStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(FuncionesParser.ExpressionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(FuncionesParser.IterableContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_mapStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapStatement" ):
                listener.enterMapStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapStatement" ):
                listener.exitMapStatement(self)




    def mapStatement(self):

        localctx = FuncionesParser.MapStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mapStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(FuncionesParser.T__0)
            self.state = 34
            self.match(FuncionesParser.T__1)
            self.state = 35
            self.expression()
            self.state = 36
            self.match(FuncionesParser.T__2)
            self.state = 37
            self.iterable()
            self.state = 38
            self.match(FuncionesParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FilterStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionExpression(self):
            return self.getTypedRuleContext(FuncionesParser.ConditionExpressionContext,0)


        def iterable(self):
            return self.getTypedRuleContext(FuncionesParser.IterableContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_filterStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStatement" ):
                listener.enterFilterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStatement" ):
                listener.exitFilterStatement(self)




    def filterStatement(self):

        localctx = FuncionesParser.FilterStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(FuncionesParser.T__4)
            self.state = 41
            self.match(FuncionesParser.T__1)
            self.state = 42
            self.conditionExpression()
            self.state = 43
            self.match(FuncionesParser.T__2)
            self.state = 44
            self.iterable()
            self.state = 45
            self.match(FuncionesParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FuncionesParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(FuncionesParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(FuncionesParser.STRING, 0)

        def expression(self):
            return self.getTypedRuleContext(FuncionesParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = FuncionesParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FuncionesParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.match(FuncionesParser.IDENTIFIER)
                pass
            elif token in [FuncionesParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.match(FuncionesParser.NUMBER)
                pass
            elif token in [FuncionesParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
                self.match(FuncionesParser.STRING)
                pass
            elif token in [FuncionesParser.T__1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 50
                self.match(FuncionesParser.T__1)
                self.state = 51
                self.expression()
                self.state = 52
                self.match(FuncionesParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FuncionesParser.IDENTIFIER, 0)

        def comparison(self):
            return self.getTypedRuleContext(FuncionesParser.ComparisonContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_conditionExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionExpression" ):
                listener.enterConditionExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionExpression" ):
                listener.exitConditionExpression(self)




    def conditionExpression(self):

        localctx = FuncionesParser.ConditionExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditionExpression)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(FuncionesParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista(self):
            return self.getTypedRuleContext(FuncionesParser.ListaContext,0)


        def tupla(self):
            return self.getTypedRuleContext(FuncionesParser.TuplaContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_iterable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterable" ):
                listener.enterIterable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterable" ):
                listener.exitIterable(self)




    def iterable(self):

        localctx = FuncionesParser.IterableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_iterable)
        try:
            self.state = 62
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [FuncionesParser.T__5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.lista()
                pass
            elif token in [FuncionesParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.tupla()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncionesParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FuncionesParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FuncionesParser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)




    def lista(self):

        localctx = FuncionesParser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(FuncionesParser.T__5)
            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FuncionesParser.T__1) | (1 << FuncionesParser.IDENTIFIER) | (1 << FuncionesParser.NUMBER) | (1 << FuncionesParser.STRING))) != 0):
                self.state = 65
                self.expression()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==FuncionesParser.T__2:
                    self.state = 66
                    self.match(FuncionesParser.T__2)
                    self.state = 67
                    self.expression()
                    self.state = 72
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 75
            self.match(FuncionesParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TuplaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FuncionesParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(FuncionesParser.ExpressionContext,i)


        def getRuleIndex(self):
            return FuncionesParser.RULE_tupla

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTupla" ):
                listener.enterTupla(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTupla" ):
                listener.exitTupla(self)




    def tupla(self):

        localctx = FuncionesParser.TuplaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tupla)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(FuncionesParser.T__1)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FuncionesParser.T__1) | (1 << FuncionesParser.IDENTIFIER) | (1 << FuncionesParser.NUMBER) | (1 << FuncionesParser.STRING))) != 0):
                self.state = 78
                self.expression()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==FuncionesParser.T__2:
                    self.state = 79
                    self.match(FuncionesParser.T__2)
                    self.state = 80
                    self.expression()
                    self.state = 85
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 88
            self.match(FuncionesParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(FuncionesParser.IDENTIFIER, 0)

        def comparisonOperator(self):
            return self.getTypedRuleContext(FuncionesParser.ComparisonOperatorContext,0)


        def expression(self):
            return self.getTypedRuleContext(FuncionesParser.ExpressionContext,0)


        def getRuleIndex(self):
            return FuncionesParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)




    def comparison(self):

        localctx = FuncionesParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(FuncionesParser.IDENTIFIER)
            self.state = 91
            self.comparisonOperator()
            self.state = 92
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return FuncionesParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)




    def comparisonOperator(self):

        localctx = FuncionesParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << FuncionesParser.T__7) | (1 << FuncionesParser.T__8) | (1 << FuncionesParser.T__9) | (1 << FuncionesParser.T__10) | (1 << FuncionesParser.T__11) | (1 << FuncionesParser.T__12))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





