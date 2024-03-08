# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01ca\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\5\2")
        buf.write("\u0086\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u0096\n\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5")
        buf.write("\5\5\u009f\n\5\3\6\3\6\5\6\u00a3\n\6\3\6\3\6\3\7\3\7\7")
        buf.write("\7\u00a9\n\7\f\7\16\7\u00ac\13\7\3\b\3\b\3\b\7\b\u00b1")
        buf.write("\n\b\f\b\16\b\u00b4\13\b\3\b\3\b\6\b\u00b8\n\b\r\b\16")
        buf.write("\b\u00b9\7\b\u00bc\n\b\f\b\16\b\u00bf\13\b\5\b\u00c1\n")
        buf.write("\b\3\t\3\t\7\t\u00c5\n\t\f\t\16\t\u00c8\13\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\5\n\u00cf\n\n\3\13\3\13\3\13\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\7\"\u0156\n\"\f\"\16\"\u0159\13\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\7#\u0161\n#\f#\16#\u0164\13#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\39\3:\3:\3:\3;\3;\3;\3<\3<\3=\3=\7=")
        buf.write("\u01a6\n=\f=\16=\u01a9\13=\3>\6>\u01ac\n>\r>\16>\u01ad")
        buf.write("\3>\3>\3?\3?\7?\u01b4\n?\f?\16?\u01b7\13?\3?\5?\u01ba")
        buf.write("\n?\3?\3?\3@\3@\7@\u01c0\n@\f@\16@\u01c3\13@\3@\3@\3@")
        buf.write("\3A\3A\3A\3\u0162\2B\3\3\5\4\7\5\t\2\13\2\r\2\17\2\21")
        buf.write("\6\23\2\25\2\27\2\31\7\33\b\35\t\37\n!\13#\f%\r\'\16)")
        buf.write("\17+\20-\21/\22\61\23\63\24\65\25\67\269\27;\30=\31?\32")
        buf.write("A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e-g.i")
        buf.write("/k\60m\61o\62q\63s\64u\65w\66y\67{8}9\177:\u0081;\3\2")
        buf.write("\16\4\2GGgg\4\2--//\3\2\62;\3\2\63;\3\2$$\6\2\f\f$$))")
        buf.write("^^\n\2$$))^^ddhhppttvv\4\2\f\f\17\17\5\2C\\aac|\6\2\62")
        buf.write(";C\\aac|\5\2\n\f\16\17\"\"\4\3\f\f\17\17\2\u01d5\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\21\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\3\u0085\3\2\2\2\5\u0095\3\2\2\2\7\u0099\3\2\2")
        buf.write("\2\t\u009c\3\2\2\2\13\u00a0\3\2\2\2\r\u00a6\3\2\2\2\17")
        buf.write("\u00c0\3\2\2\2\21\u00c2\3\2\2\2\23\u00ce\3\2\2\2\25\u00d0")
        buf.write("\3\2\2\2\27\u00d3\3\2\2\2\31\u00d6\3\2\2\2\33\u00de\3")
        buf.write("\2\2\2\35\u00e4\3\2\2\2\37\u00eb\3\2\2\2!\u00f0\3\2\2")
        buf.write("\2#\u00f6\3\2\2\2%\u00fc\3\2\2\2\'\u0101\3\2\2\2)\u0107")
        buf.write("\3\2\2\2+\u010b\3\2\2\2-\u0113\3\2\2\2/\u0117\3\2\2\2")
        buf.write("\61\u011e\3\2\2\2\63\u0127\3\2\2\2\65\u012a\3\2\2\2\67")
        buf.write("\u0133\3\2\2\29\u0138\3\2\2\2;\u013b\3\2\2\2=\u0143\3")
        buf.write("\2\2\2?\u0148\3\2\2\2A\u014b\3\2\2\2C\u0151\3\2\2\2E\u015c")
        buf.write("\3\2\2\2G\u016a\3\2\2\2I\u016c\3\2\2\2K\u016e\3\2\2\2")
        buf.write("M\u0170\3\2\2\2O\u0172\3\2\2\2Q\u0174\3\2\2\2S\u0176\3")
        buf.write("\2\2\2U\u0178\3\2\2\2W\u017a\3\2\2\2Y\u017c\3\2\2\2[\u017e")
        buf.write("\3\2\2\2]\u0180\3\2\2\2_\u0182\3\2\2\2a\u0184\3\2\2\2")
        buf.write("c\u0186\3\2\2\2e\u0188\3\2\2\2g\u018b\3\2\2\2i\u018e\3")
        buf.write("\2\2\2k\u0191\3\2\2\2m\u0194\3\2\2\2o\u0196\3\2\2\2q\u0198")
        buf.write("\3\2\2\2s\u019b\3\2\2\2u\u019e\3\2\2\2w\u01a1\3\2\2\2")
        buf.write("y\u01a3\3\2\2\2{\u01ab\3\2\2\2}\u01b1\3\2\2\2\177\u01bd")
        buf.write("\3\2\2\2\u0081\u01c7\3\2\2\2\u0083\u0086\5\67\34\2\u0084")
        buf.write("\u0086\5#\22\2\u0085\u0083\3\2\2\2\u0085\u0084\3\2\2\2")
        buf.write("\u0086\4\3\2\2\2\u0087\u0088\5\17\b\2\u0088\u0089\5\t")
        buf.write("\5\2\u0089\u0096\3\2\2\2\u008a\u008b\5\17\b\2\u008b\u008c")
        buf.write("\5\13\6\2\u008c\u0096\3\2\2\2\u008d\u008e\7\60\2\2\u008e")
        buf.write("\u008f\5\r\7\2\u008f\u0090\5\13\6\2\u0090\u0096\3\2\2")
        buf.write("\2\u0091\u0092\5\17\b\2\u0092\u0093\5\t\5\2\u0093\u0094")
        buf.write("\5\13\6\2\u0094\u0096\3\2\2\2\u0095\u0087\3\2\2\2\u0095")
        buf.write("\u008a\3\2\2\2\u0095\u008d\3\2\2\2\u0095\u0091\3\2\2\2")
        buf.write("\u0096\u0097\3\2\2\2\u0097\u0098\b\3\2\2\u0098\6\3\2\2")
        buf.write("\2\u0099\u009a\5\17\b\2\u009a\u009b\b\4\3\2\u009b\b\3")
        buf.write("\2\2\2\u009c\u009e\7\60\2\2\u009d\u009f\5\r\7\2\u009e")
        buf.write("\u009d\3\2\2\2\u009e\u009f\3\2\2\2\u009f\n\3\2\2\2\u00a0")
        buf.write("\u00a2\t\2\2\2\u00a1\u00a3\t\3\2\2\u00a2\u00a1\3\2\2\2")
        buf.write("\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a5\5")
        buf.write("\r\7\2\u00a5\f\3\2\2\2\u00a6\u00aa\t\4\2\2\u00a7\u00a9")
        buf.write("\t\4\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00ac\3\2\2\2\u00aa")
        buf.write("\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\16\3\2\2\2\u00ac")
        buf.write("\u00aa\3\2\2\2\u00ad\u00c1\7\62\2\2\u00ae\u00b2\t\5\2")
        buf.write("\2\u00af\u00b1\t\4\2\2\u00b0\u00af\3\2\2\2\u00b1\u00b4")
        buf.write("\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3")
        buf.write("\u00bd\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b5\u00b7\7a\2\2")
        buf.write("\u00b6\u00b8\t\4\2\2\u00b7\u00b6\3\2\2\2\u00b8\u00b9\3")
        buf.write("\2\2\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00bc")
        buf.write("\3\2\2\2\u00bb\u00b5\3\2\2\2\u00bc\u00bf\3\2\2\2\u00bd")
        buf.write("\u00bb\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00c1\3\2\2\2")
        buf.write("\u00bf\u00bd\3\2\2\2\u00c0\u00ad\3\2\2\2\u00c0\u00ae\3")
        buf.write("\2\2\2\u00c1\20\3\2\2\2\u00c2\u00c6\t\6\2\2\u00c3\u00c5")
        buf.write("\5\23\n\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2")
        buf.write("\u00c8\u00c6\3\2\2\2\u00c9\u00ca\t\6\2\2\u00ca\u00cb\b")
        buf.write("\t\4\2\u00cb\22\3\2\2\2\u00cc\u00cf\n\7\2\2\u00cd\u00cf")
        buf.write("\5\25\13\2\u00ce\u00cc\3\2\2\2\u00ce\u00cd\3\2\2\2\u00cf")
        buf.write("\24\3\2\2\2\u00d0\u00d1\7^\2\2\u00d1\u00d2\t\b\2\2\u00d2")
        buf.write("\26\3\2\2\2\u00d3\u00d4\7^\2\2\u00d4\u00d5\n\b\2\2\u00d5")
        buf.write("\30\3\2\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8\7p\2\2\u00d8")
        buf.write("\u00d9\7v\2\2\u00d9\u00da\7g\2\2\u00da\u00db\7i\2\2\u00db")
        buf.write("\u00dc\7g\2\2\u00dc\u00dd\7t\2\2\u00dd\32\3\2\2\2\u00de")
        buf.write("\u00df\7h\2\2\u00df\u00e0\7n\2\2\u00e0\u00e1\7q\2\2\u00e1")
        buf.write("\u00e2\7c\2\2\u00e2\u00e3\7v\2\2\u00e3\34\3\2\2\2\u00e4")
        buf.write("\u00e5\7t\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7\7v\2\2\u00e7")
        buf.write("\u00e8\7w\2\2\u00e8\u00e9\7t\2\2\u00e9\u00ea\7p\2\2\u00ea")
        buf.write("\36\3\2\2\2\u00eb\u00ec\7c\2\2\u00ec\u00ed\7w\2\2\u00ed")
        buf.write("\u00ee\7v\2\2\u00ee\u00ef\7q\2\2\u00ef \3\2\2\2\u00f0")
        buf.write("\u00f1\7d\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7g\2\2\u00f3")
        buf.write("\u00f4\7c\2\2\u00f4\u00f5\7m\2\2\u00f5\"\3\2\2\2\u00f6")
        buf.write("\u00f7\7h\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7n\2\2\u00f9")
        buf.write("\u00fa\7u\2\2\u00fa\u00fb\7g\2\2\u00fb$\3\2\2\2\u00fc")
        buf.write("\u00fd\7x\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7k\2\2\u00ff")
        buf.write("\u0100\7f\2\2\u0100&\3\2\2\2\u0101\u0102\7c\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103\u0104\7t\2\2\u0104\u0105\7c\2\2\u0105")
        buf.write("\u0106\7{\2\2\u0106(\3\2\2\2\u0107\u0108\7q\2\2\u0108")
        buf.write("\u0109\7w\2\2\u0109\u010a\7v\2\2\u010a*\3\2\2\2\u010b")
        buf.write("\u010c\7d\2\2\u010c\u010d\7q\2\2\u010d\u010e\7q\2\2\u010e")
        buf.write("\u010f\7n\2\2\u010f\u0110\7g\2\2\u0110\u0111\7c\2\2\u0111")
        buf.write("\u0112\7p\2\2\u0112,\3\2\2\2\u0113\u0114\7h\2\2\u0114")
        buf.write("\u0115\7q\2\2\u0115\u0116\7t\2\2\u0116.\3\2\2\2\u0117")
        buf.write("\u0118\7u\2\2\u0118\u0119\7v\2\2\u0119\u011a\7t\2\2\u011a")
        buf.write("\u011b\7k\2\2\u011b\u011c\7p\2\2\u011c\u011d\7i\2\2\u011d")
        buf.write("\60\3\2\2\2\u011e\u011f\7e\2\2\u011f\u0120\7q\2\2\u0120")
        buf.write("\u0121\7p\2\2\u0121\u0122\7v\2\2\u0122\u0123\7k\2\2\u0123")
        buf.write("\u0124\7p\2\2\u0124\u0125\7w\2\2\u0125\u0126\7g\2\2\u0126")
        buf.write("\62\3\2\2\2\u0127\u0128\7f\2\2\u0128\u0129\7q\2\2\u0129")
        buf.write("\64\3\2\2\2\u012a\u012b\7h\2\2\u012b\u012c\7w\2\2\u012c")
        buf.write("\u012d\7p\2\2\u012d\u012e\7e\2\2\u012e\u012f\7v\2\2\u012f")
        buf.write("\u0130\7k\2\2\u0130\u0131\7q\2\2\u0131\u0132\7p\2\2\u0132")
        buf.write("\66\3\2\2\2\u0133\u0134\7v\2\2\u0134\u0135\7t\2\2\u0135")
        buf.write("\u0136\7w\2\2\u0136\u0137\7g\2\2\u01378\3\2\2\2\u0138")
        buf.write("\u0139\7q\2\2\u0139\u013a\7h\2\2\u013a:\3\2\2\2\u013b")
        buf.write("\u013c\7k\2\2\u013c\u013d\7p\2\2\u013d\u013e\7j\2\2\u013e")
        buf.write("\u013f\7g\2\2\u013f\u0140\7t\2\2\u0140\u0141\7k\2\2\u0141")
        buf.write("\u0142\7v\2\2\u0142<\3\2\2\2\u0143\u0144\7g\2\2\u0144")
        buf.write("\u0145\7n\2\2\u0145\u0146\7u\2\2\u0146\u0147\7g\2\2\u0147")
        buf.write(">\3\2\2\2\u0148\u0149\7k\2\2\u0149\u014a\7h\2\2\u014a")
        buf.write("@\3\2\2\2\u014b\u014c\7y\2\2\u014c\u014d\7j\2\2\u014d")
        buf.write("\u014e\7k\2\2\u014e\u014f\7n\2\2\u014f\u0150\7g\2\2\u0150")
        buf.write("B\3\2\2\2\u0151\u0152\7\61\2\2\u0152\u0153\7\61\2\2\u0153")
        buf.write("\u0157\3\2\2\2\u0154\u0156\n\t\2\2\u0155\u0154\3\2\2\2")
        buf.write("\u0156\u0159\3\2\2\2\u0157\u0155\3\2\2\2\u0157\u0158\3")
        buf.write("\2\2\2\u0158\u015a\3\2\2\2\u0159\u0157\3\2\2\2\u015a\u015b")
        buf.write("\b\"\5\2\u015bD\3\2\2\2\u015c\u015d\7\61\2\2\u015d\u015e")
        buf.write("\7,\2\2\u015e\u0162\3\2\2\2\u015f\u0161\13\2\2\2\u0160")
        buf.write("\u015f\3\2\2\2\u0161\u0164\3\2\2\2\u0162\u0163\3\2\2\2")
        buf.write("\u0162\u0160\3\2\2\2\u0163\u0165\3\2\2\2\u0164\u0162\3")
        buf.write("\2\2\2\u0165\u0166\7,\2\2\u0166\u0167\7\61\2\2\u0167\u0168")
        buf.write("\3\2\2\2\u0168\u0169\b#\5\2\u0169F\3\2\2\2\u016a\u016b")
        buf.write("\7=\2\2\u016bH\3\2\2\2\u016c\u016d\7.\2\2\u016dJ\3\2\2")
        buf.write("\2\u016e\u016f\7<\2\2\u016fL\3\2\2\2\u0170\u0171\7*\2")
        buf.write("\2\u0171N\3\2\2\2\u0172\u0173\7+\2\2\u0173P\3\2\2\2\u0174")
        buf.write("\u0175\7}\2\2\u0175R\3\2\2\2\u0176\u0177\7\177\2\2\u0177")
        buf.write("T\3\2\2\2\u0178\u0179\7]\2\2\u0179V\3\2\2\2\u017a\u017b")
        buf.write("\7_\2\2\u017bX\3\2\2\2\u017c\u017d\7?\2\2\u017dZ\3\2\2")
        buf.write("\2\u017e\u017f\7,\2\2\u017f\\\3\2\2\2\u0180\u0181\7\61")
        buf.write("\2\2\u0181^\3\2\2\2\u0182\u0183\7-\2\2\u0183`\3\2\2\2")
        buf.write("\u0184\u0185\7/\2\2\u0185b\3\2\2\2\u0186\u0187\7#\2\2")
        buf.write("\u0187d\3\2\2\2\u0188\u0189\7>\2\2\u0189\u018a\7?\2\2")
        buf.write("\u018af\3\2\2\2\u018b\u018c\7@\2\2\u018c\u018d\7?\2\2")
        buf.write("\u018dh\3\2\2\2\u018e\u018f\7#\2\2\u018f\u0190\7?\2\2")
        buf.write("\u0190j\3\2\2\2\u0191\u0192\7?\2\2\u0192\u0193\7?\2\2")
        buf.write("\u0193l\3\2\2\2\u0194\u0195\7>\2\2\u0195n\3\2\2\2\u0196")
        buf.write("\u0197\7@\2\2\u0197p\3\2\2\2\u0198\u0199\7<\2\2\u0199")
        buf.write("\u019a\7<\2\2\u019ar\3\2\2\2\u019b\u019c\7(\2\2\u019c")
        buf.write("\u019d\7(\2\2\u019dt\3\2\2\2\u019e\u019f\7~\2\2\u019f")
        buf.write("\u01a0\7~\2\2\u01a0v\3\2\2\2\u01a1\u01a2\7\'\2\2\u01a2")
        buf.write("x\3\2\2\2\u01a3\u01a7\t\n\2\2\u01a4\u01a6\t\13\2\2\u01a5")
        buf.write("\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8z\3\2\2\2\u01a9\u01a7\3\2\2")
        buf.write("\2\u01aa\u01ac\t\f\2\2\u01ab\u01aa\3\2\2\2\u01ac\u01ad")
        buf.write("\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b0\b>\5\2\u01b0|\3\2\2\2\u01b1")
        buf.write("\u01b5\7$\2\2\u01b2\u01b4\5\23\n\2\u01b3\u01b2\3\2\2\2")
        buf.write("\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3")
        buf.write("\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01ba")
        buf.write("\t\r\2\2\u01b9\u01b8\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u01bc\b?\6\2\u01bc~\3\2\2\2\u01bd\u01c1\t\6\2\2\u01be")
        buf.write("\u01c0\5\23\n\2\u01bf\u01be\3\2\2\2\u01c0\u01c3\3\2\2")
        buf.write("\2\u01c1\u01bf\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4\u01c5\5\27\f\2\u01c5")
        buf.write("\u01c6\b@\7\2\u01c6\u0080\3\2\2\2\u01c7\u01c8\13\2\2\2")
        buf.write("\u01c8\u01c9\bA\b\2\u01c9\u0082\3\2\2\2\25\2\u0085\u0095")
        buf.write("\u009e\u00a2\u00aa\u00b2\u00b9\u00bd\u00c0\u00c6\u00ce")
        buf.write("\u0157\u0162\u01a7\u01ad\u01b5\u01b9\u01c1\t\3\3\2\3\4")
        buf.write("\3\3\t\4\b\2\2\3?\5\3@\6\3A\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOLEANLIT = 1
    FLOATLIT = 2
    INTLIT = 3
    STRINGLIT = 4
    INTEGER = 5
    FLOAT = 6
    RETURN = 7
    AUTO = 8
    BREAK = 9
    FALSE = 10
    VOID = 11
    ARRAY = 12
    OUT = 13
    BOOLEAN = 14
    FOR = 15
    STRING = 16
    CONTINUE = 17
    DO = 18
    FUNCTION = 19
    TRUE = 20
    OF = 21
    INHERIT = 22
    ELSE = 23
    IF = 24
    WHILE = 25
    CPP_STYLE_CMT = 26
    C_STYLE_CMT = 27
    SEMI = 28
    COMMA = 29
    COLON = 30
    LR = 31
    RR = 32
    LC = 33
    RC = 34
    LS = 35
    RS = 36
    ASS = 37
    MUL = 38
    DIV = 39
    ADD = 40
    MINUS = 41
    NOT = 42
    LTE = 43
    GTE = 44
    NEQ = 45
    EQ = 46
    LT = 47
    GT = 48
    STR_OPR = 49
    AND = 50
    OR = 51
    MOD = 52
    ID = 53
    WS = 54
    UNCLOSE_STRING = 55
    ILLEGAL_ESCAPE = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'integer'", "'float'", "'return'", "'auto'", "'break'", "'false'", 
            "'void'", "'array'", "'out'", "'boolean'", "'for'", "'string'", 
            "'continue'", "'do'", "'function'", "'true'", "'of'", "'inherit'", 
            "'else'", "'if'", "'while'", "';'", "','", "':'", "'('", "')'", 
            "'{'", "'}'", "'['", "']'", "'='", "'*'", "'/'", "'+'", "'-'", 
            "'!'", "'<='", "'>='", "'!='", "'=='", "'<'", "'>'", "'::'", 
            "'&&'", "'||'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLEANLIT", "FLOATLIT", "INTLIT", "STRINGLIT", "INTEGER", 
            "FLOAT", "RETURN", "AUTO", "BREAK", "FALSE", "VOID", "ARRAY", 
            "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
            "TRUE", "OF", "INHERIT", "ELSE", "IF", "WHILE", "CPP_STYLE_CMT", 
            "C_STYLE_CMT", "SEMI", "COMMA", "COLON", "LR", "RR", "LC", "RC", 
            "LS", "RS", "ASS", "MUL", "DIV", "ADD", "MINUS", "NOT", "LTE", 
            "GTE", "NEQ", "EQ", "LT", "GT", "STR_OPR", "AND", "OR", "MOD", 
            "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "BOOLEANLIT", "FLOATLIT", "INTLIT", "DECPART", "EXPPART", 
                  "DIGIT_SEQ", "INTPART", "STRINGLIT", "STRINGABLE_CHARACTER", 
                  "STRINGABLE_ESCAPE", "ILLEGAL_ESCAPE_CHARACTER", "INTEGER", 
                  "FLOAT", "RETURN", "AUTO", "BREAK", "FALSE", "VOID", "ARRAY", 
                  "OUT", "BOOLEAN", "FOR", "STRING", "CONTINUE", "DO", "FUNCTION", 
                  "TRUE", "OF", "INHERIT", "ELSE", "IF", "WHILE", "CPP_STYLE_CMT", 
                  "C_STYLE_CMT", "SEMI", "COMMA", "COLON", "LR", "RR", "LC", 
                  "RC", "LS", "RS", "ASS", "MUL", "DIV", "ADD", "MINUS", 
                  "NOT", "LTE", "GTE", "NEQ", "EQ", "LT", "GT", "STR_OPR", 
                  "AND", "OR", "MOD", "ID", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.FLOATLIT_action 
            actions[2] = self.INTLIT_action 
            actions[7] = self.STRINGLIT_action 
            actions[61] = self.UNCLOSE_STRING_action 
            actions[62] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_', '')
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text[1:-1]
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    raise UncloseString(self.text[1:].replace('\n','').replace('\r',''))

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		raise IllegalEscape(self.text[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		raise ErrorToken(self.text)

     


