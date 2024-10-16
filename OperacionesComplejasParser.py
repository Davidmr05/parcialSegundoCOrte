# Generated from OperacionesComplejas.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("&\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\2\2\b\2")
        buf.write("\4\6\b\n\f\2\4\3\2\6\t\3\2\6\7\2 \2\17\3\2\2\2\4\23\3")
        buf.write("\2\2\2\6\26\3\2\2\2\b\32\3\2\2\2\n \3\2\2\2\f\"\3\2\2")
        buf.write("\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21\3\2\2\2\21\17\3\2")
        buf.write("\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\24\5\6\4\2\24\25\7")
        buf.write("\13\2\2\25\5\3\2\2\2\26\27\5\b\5\2\27\30\t\2\2\2\30\31")
        buf.write("\5\b\5\2\31\7\3\2\2\2\32\33\7\3\2\2\33\34\5\n\6\2\34\35")
        buf.write("\t\3\2\2\35\36\5\f\7\2\36\37\7\4\2\2\37\t\3\2\2\2 !\7")
        buf.write("\n\2\2!\13\3\2\2\2\"#\7\n\2\2#$\7\5\2\2$\r\3\2\2\2\3\21")
        return buf.getvalue()


class OperacionesComplejasParser ( Parser ):

    grammarFileName = "OperacionesComplejas.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'i'", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ADD", "SUB", "MUL", "DIV", "NUMBER", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_start = 1
    RULE_operation = 2
    RULE_complexNumber = 3
    RULE_realPart = 4
    RULE_imaginaryPart = 5

    ruleNames =  [ "prog", "start", "operation", "complexNumber", "realPart", 
                   "imaginaryPart" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ADD=4
    SUB=5
    MUL=6
    DIV=7
    NUMBER=8
    NEWLINE=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def start(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OperacionesComplejasParser.StartContext)
            else:
                return self.getTypedRuleContext(OperacionesComplejasParser.StartContext,i)


        def getRuleIndex(self):
            return OperacionesComplejasParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = OperacionesComplejasParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.start()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==OperacionesComplejasParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OperacionesComplejasParser.RULE_start

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PrintContext(StartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OperacionesComplejasParser.StartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operation(self):
            return self.getTypedRuleContext(OperacionesComplejasParser.OperationContext,0)

        def NEWLINE(self):
            return self.getToken(OperacionesComplejasParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint" ):
                listener.enterPrint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint" ):
                listener.exitPrint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint" ):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)



    def start(self):

        localctx = OperacionesComplejasParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_start)
        try:
            localctx = OperacionesComplejasParser.PrintContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.operation()
            self.state = 18
            self.match(OperacionesComplejasParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OperacionesComplejasParser.RULE_operation

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OperarContext(OperationContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OperacionesComplejasParser.OperationContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def complexNumber(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(OperacionesComplejasParser.ComplexNumberContext)
            else:
                return self.getTypedRuleContext(OperacionesComplejasParser.ComplexNumberContext,i)

        def ADD(self):
            return self.getToken(OperacionesComplejasParser.ADD, 0)
        def SUB(self):
            return self.getToken(OperacionesComplejasParser.SUB, 0)
        def MUL(self):
            return self.getToken(OperacionesComplejasParser.MUL, 0)
        def DIV(self):
            return self.getToken(OperacionesComplejasParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperar" ):
                listener.enterOperar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperar" ):
                listener.exitOperar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperar" ):
                return visitor.visitOperar(self)
            else:
                return visitor.visitChildren(self)



    def operation(self):

        localctx = OperacionesComplejasParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_operation)
        self._la = 0 # Token type
        try:
            localctx = OperacionesComplejasParser.OperarContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.complexNumber()
            self.state = 21
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << OperacionesComplejasParser.ADD) | (1 << OperacionesComplejasParser.SUB) | (1 << OperacionesComplejasParser.MUL) | (1 << OperacionesComplejasParser.DIV))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 22
            self.complexNumber()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComplexNumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OperacionesComplejasParser.RULE_complexNumber

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefComplexContext(ComplexNumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OperacionesComplejasParser.ComplexNumberContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def realPart(self):
            return self.getTypedRuleContext(OperacionesComplejasParser.RealPartContext,0)

        def imaginaryPart(self):
            return self.getTypedRuleContext(OperacionesComplejasParser.ImaginaryPartContext,0)

        def ADD(self):
            return self.getToken(OperacionesComplejasParser.ADD, 0)
        def SUB(self):
            return self.getToken(OperacionesComplejasParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefComplex" ):
                listener.enterDefComplex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefComplex" ):
                listener.exitDefComplex(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefComplex" ):
                return visitor.visitDefComplex(self)
            else:
                return visitor.visitChildren(self)



    def complexNumber(self):

        localctx = OperacionesComplejasParser.ComplexNumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_complexNumber)
        self._la = 0 # Token type
        try:
            localctx = OperacionesComplejasParser.DefComplexContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(OperacionesComplejasParser.T__0)
            self.state = 25
            self.realPart()
            self.state = 26
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==OperacionesComplejasParser.ADD or _la==OperacionesComplejasParser.SUB):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 27
            self.imaginaryPart()
            self.state = 28
            self.match(OperacionesComplejasParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RealPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OperacionesComplejasParser.RULE_realPart

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class RealContext(RealPartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OperacionesComplejasParser.RealPartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(OperacionesComplejasParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal" ):
                listener.enterReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal" ):
                listener.exitReal(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReal" ):
                return visitor.visitReal(self)
            else:
                return visitor.visitChildren(self)



    def realPart(self):

        localctx = OperacionesComplejasParser.RealPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_realPart)
        try:
            localctx = OperacionesComplejasParser.RealContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(OperacionesComplejasParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ImaginaryPartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return OperacionesComplejasParser.RULE_imaginaryPart

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ImgContext(ImaginaryPartContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a OperacionesComplejasParser.ImaginaryPartContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(OperacionesComplejasParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImg" ):
                listener.enterImg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImg" ):
                listener.exitImg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImg" ):
                return visitor.visitImg(self)
            else:
                return visitor.visitChildren(self)



    def imaginaryPart(self):

        localctx = OperacionesComplejasParser.ImaginaryPartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_imaginaryPart)
        try:
            localctx = OperacionesComplejasParser.ImgContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(OperacionesComplejasParser.NUMBER)
            self.state = 33
            self.match(OperacionesComplejasParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





