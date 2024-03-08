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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u025c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\7!\u0186")
        buf.write("\n!\f!\16!\u0189\13!\3!\3!\3\"\3\"\3\"\3\"\7\"\u0191\n")
        buf.write("\"\f\"\16\"\u0194\13\"\3\"\3\"\3\"\3\"\3\"\3#\3#\6#\u019d")
        buf.write("\n#\r#\16#\u019e\3#\5#\u01a2\n#\3#\6#\u01a5\n#\r#\16#")
        buf.write("\u01a6\7#\u01a9\n#\f#\16#\u01ac\13#\5#\u01ae\n#\3#\3#")
        buf.write("\3$\3$\3$\5$\u01b5\n$\3$\5$\u01b8\n$\3$\3$\3$\5$\u01bd")
        buf.write("\n$\3$\3$\3%\3%\6%\u01c3\n%\r%\16%\u01c4\3%\5%\u01c8\n")
        buf.write("%\3%\6%\u01cb\n%\r%\16%\u01cc\7%\u01cf\n%\f%\16%\u01d2")
        buf.write("\13%\5%\u01d4\n%\3&\3&\7&\u01d8\n&\f&\16&\u01db\13&\3")
        buf.write("\'\3\'\5\'\u01df\n\'\3\'\6\'\u01e2\n\'\r\'\16\'\u01e3")
        buf.write("\3(\3(\5(\u01e8\n(\3)\3)\3)\7)\u01ed\n)\f)\16)\u01f0\13")
        buf.write(")\3)\3)\3)\3*\3*\3*\3+\3+\7+\u01fa\n+\f+\16+\u01fd\13")
        buf.write("+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\3\67\38\38\39\39\39\3:\3:\3:\3;\3;\3<")
        buf.write("\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3")
        buf.write("E\3E\3F\6F\u023b\nF\rF\16F\u023c\3F\3F\3G\3G\3G\7G\u0244")
        buf.write("\nG\fG\16G\u0247\13G\3G\5G\u024a\nG\3G\3G\3H\3H\3H\7H")
        buf.write("\u0251\nH\fH\16H\u0254\13H\3H\3H\3H\3H\3I\3I\3I\3\u0192")
        buf.write("\2J\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I\2K")
        buf.write("\2M\2O&Q\'S\2U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65")
        buf.write("q\66s\67u8w9y:{;}<\177=\u0081>\u0083?\u0085@\u0087A\u0089")
        buf.write("B\u008bC\u008dD\u008fE\u0091F\3\2\16\4\2\f\f\17\17\3\2")
        buf.write("\63;\3\2\62;\4\2GGgg\4\2--//\5\2\f\f$$^^\n\2$$))^^ddh")
        buf.write("hppttvv\5\2C\\aac|\6\2\62;C\\aac|\5\2\n\f\16\17\"\"\6")
        buf.write("\2\f\f$$))^^\3\3\f\f\2\u0272\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2")
        buf.write("\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\3\u0093")
        buf.write("\3\2\2\2\5\u009b\3\2\2\2\7\u00a3\3\2\2\2\t\u00a9\3\2\2")
        buf.write("\2\13\u00b0\3\2\2\2\r\u00b5\3\2\2\2\17\u00ba\3\2\2\2\21")
        buf.write("\u00c2\3\2\2\2\23\u00c6\3\2\2\2\25\u00cf\3\2\2\2\27\u00d3")
        buf.write("\3\2\2\2\31\u00d9\3\2\2\2\33\u00dc\3\2\2\2\35\u00e3\3")
        buf.write("\2\2\2\37\u00ec\3\2\2\2!\u00f2\3\2\2\2#\u00f5\3\2\2\2")
        buf.write("%\u00fa\3\2\2\2\'\u00ff\3\2\2\2)\u0105\3\2\2\2+\u010b")
        buf.write("\3\2\2\2-\u010e\3\2\2\2/\u011a\3\2\2\2\61\u0127\3\2\2")
        buf.write("\2\63\u0131\3\2\2\2\65\u013c\3\2\2\2\67\u0148\3\2\2\2")
        buf.write("9\u0155\3\2\2\2;\u0160\3\2\2\2=\u016c\3\2\2\2?\u0172\3")
        buf.write("\2\2\2A\u0181\3\2\2\2C\u018c\3\2\2\2E\u01ad\3\2\2\2G\u01bc")
        buf.write("\3\2\2\2I\u01d3\3\2\2\2K\u01d5\3\2\2\2M\u01dc\3\2\2\2")
        buf.write("O\u01e7\3\2\2\2Q\u01e9\3\2\2\2S\u01f4\3\2\2\2U\u01f7\3")
        buf.write("\2\2\2W\u01fe\3\2\2\2Y\u0200\3\2\2\2[\u0202\3\2\2\2]\u0204")
        buf.write("\3\2\2\2_\u0206\3\2\2\2a\u0208\3\2\2\2c\u020a\3\2\2\2")
        buf.write("e\u020d\3\2\2\2g\u0210\3\2\2\2i\u0213\3\2\2\2k\u0216\3")
        buf.write("\2\2\2m\u0218\3\2\2\2o\u021b\3\2\2\2q\u021d\3\2\2\2s\u0220")
        buf.write("\3\2\2\2u\u0223\3\2\2\2w\u0225\3\2\2\2y\u0227\3\2\2\2")
        buf.write("{\u0229\3\2\2\2}\u022b\3\2\2\2\177\u022d\3\2\2\2\u0081")
        buf.write("\u022f\3\2\2\2\u0083\u0231\3\2\2\2\u0085\u0233\3\2\2\2")
        buf.write("\u0087\u0235\3\2\2\2\u0089\u0237\3\2\2\2\u008b\u023a\3")
        buf.write("\2\2\2\u008d\u0240\3\2\2\2\u008f\u024d\3\2\2\2\u0091\u0259")
        buf.write("\3\2\2\2\u0093\u0094\7d\2\2\u0094\u0095\7q\2\2\u0095\u0096")
        buf.write("\7q\2\2\u0096\u0097\7n\2\2\u0097\u0098\7g\2\2\u0098\u0099")
        buf.write("\7c\2\2\u0099\u009a\7p\2\2\u009a\4\3\2\2\2\u009b\u009c")
        buf.write("\7k\2\2\u009c\u009d\7p\2\2\u009d\u009e\7v\2\2\u009e\u009f")
        buf.write("\7g\2\2\u009f\u00a0\7i\2\2\u00a0\u00a1\7g\2\2\u00a1\u00a2")
        buf.write("\7t\2\2\u00a2\6\3\2\2\2\u00a3\u00a4\7h\2\2\u00a4\u00a5")
        buf.write("\7n\2\2\u00a5\u00a6\7q\2\2\u00a6\u00a7\7c\2\2\u00a7\u00a8")
        buf.write("\7v\2\2\u00a8\b\3\2\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab")
        buf.write("\7v\2\2\u00ab\u00ac\7t\2\2\u00ac\u00ad\7k\2\2\u00ad\u00ae")
        buf.write("\7p\2\2\u00ae\u00af\7i\2\2\u00af\n\3\2\2\2\u00b0\u00b1")
        buf.write("\7x\2\2\u00b1\u00b2\7q\2\2\u00b2\u00b3\7k\2\2\u00b3\u00b4")
        buf.write("\7f\2\2\u00b4\f\3\2\2\2\u00b5\u00b6\7c\2\2\u00b6\u00b7")
        buf.write("\7w\2\2\u00b7\u00b8\7v\2\2\u00b8\u00b9\7q\2\2\u00b9\16")
        buf.write("\3\2\2\2\u00ba\u00bb\7k\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd")
        buf.write("\7j\2\2\u00bd\u00be\7g\2\2\u00be\u00bf\7t\2\2\u00bf\u00c0")
        buf.write("\7k\2\2\u00c0\u00c1\7v\2\2\u00c1\20\3\2\2\2\u00c2\u00c3")
        buf.write("\7q\2\2\u00c3\u00c4\7w\2\2\u00c4\u00c5\7v\2\2\u00c5\22")
        buf.write("\3\2\2\2\u00c6\u00c7\7h\2\2\u00c7\u00c8\7w\2\2\u00c8\u00c9")
        buf.write("\7p\2\2\u00c9\u00ca\7e\2\2\u00ca\u00cb\7v\2\2\u00cb\u00cc")
        buf.write("\7k\2\2\u00cc\u00cd\7q\2\2\u00cd\u00ce\7p\2\2\u00ce\24")
        buf.write("\3\2\2\2\u00cf\u00d0\7h\2\2\u00d0\u00d1\7q\2\2\u00d1\u00d2")
        buf.write("\7t\2\2\u00d2\26\3\2\2\2\u00d3\u00d4\7y\2\2\u00d4\u00d5")
        buf.write("\7j\2\2\u00d5\u00d6\7k\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\30\3\2\2\2\u00d9\u00da\7f\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\32\3\2\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7g\2\2\u00de\u00df\7v\2\2\u00df\u00e0\7w\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7p\2\2\u00e2\34\3\2\2\2\u00e3\u00e4")
        buf.write("\7e\2\2\u00e4\u00e5\7q\2\2\u00e5\u00e6\7p\2\2\u00e6\u00e7")
        buf.write("\7v\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea")
        buf.write("\7w\2\2\u00ea\u00eb\7g\2\2\u00eb\36\3\2\2\2\u00ec\u00ed")
        buf.write("\7d\2\2\u00ed\u00ee\7t\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0")
        buf.write("\7c\2\2\u00f0\u00f1\7m\2\2\u00f1 \3\2\2\2\u00f2\u00f3")
        buf.write("\7k\2\2\u00f3\u00f4\7h\2\2\u00f4\"\3\2\2\2\u00f5\u00f6")
        buf.write("\7g\2\2\u00f6\u00f7\7n\2\2\u00f7\u00f8\7u\2\2\u00f8\u00f9")
        buf.write("\7g\2\2\u00f9$\3\2\2\2\u00fa\u00fb\7v\2\2\u00fb\u00fc")
        buf.write("\7t\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7g\2\2\u00fe&\3")
        buf.write("\2\2\2\u00ff\u0100\7h\2\2\u0100\u0101\7c\2\2\u0101\u0102")
        buf.write("\7n\2\2\u0102\u0103\7u\2\2\u0103\u0104\7g\2\2\u0104(\3")
        buf.write("\2\2\2\u0105\u0106\7c\2\2\u0106\u0107\7t\2\2\u0107\u0108")
        buf.write("\7t\2\2\u0108\u0109\7c\2\2\u0109\u010a\7{\2\2\u010a*\3")
        buf.write("\2\2\2\u010b\u010c\7q\2\2\u010c\u010d\7h\2\2\u010d,\3")
        buf.write("\2\2\2\u010e\u010f\7t\2\2\u010f\u0110\7g\2\2\u0110\u0111")
        buf.write("\7c\2\2\u0111\u0112\7f\2\2\u0112\u0113\7K\2\2\u0113\u0114")
        buf.write("\7p\2\2\u0114\u0115\7v\2\2\u0115\u0116\7g\2\2\u0116\u0117")
        buf.write("\7i\2\2\u0117\u0118\7g\2\2\u0118\u0119\7t\2\2\u0119.\3")
        buf.write("\2\2\2\u011a\u011b\7r\2\2\u011b\u011c\7t\2\2\u011c\u011d")
        buf.write("\7k\2\2\u011d\u011e\7p\2\2\u011e\u011f\7v\2\2\u011f\u0120")
        buf.write("\7K\2\2\u0120\u0121\7p\2\2\u0121\u0122\7v\2\2\u0122\u0123")
        buf.write("\7g\2\2\u0123\u0124\7i\2\2\u0124\u0125\7g\2\2\u0125\u0126")
        buf.write("\7t\2\2\u0126\60\3\2\2\2\u0127\u0128\7t\2\2\u0128\u0129")
        buf.write("\7g\2\2\u0129\u012a\7c\2\2\u012a\u012b\7f\2\2\u012b\u012c")
        buf.write("\7H\2\2\u012c\u012d\7n\2\2\u012d\u012e\7q\2\2\u012e\u012f")
        buf.write("\7c\2\2\u012f\u0130\7v\2\2\u0130\62\3\2\2\2\u0131\u0132")
        buf.write("\7r\2\2\u0132\u0133\7t\2\2\u0133\u0134\7k\2\2\u0134\u0135")
        buf.write("\7p\2\2\u0135\u0136\7v\2\2\u0136\u0137\7H\2\2\u0137\u0138")
        buf.write("\7n\2\2\u0138\u0139\7q\2\2\u0139\u013a\7c\2\2\u013a\u013b")
        buf.write("\7v\2\2\u013b\64\3\2\2\2\u013c\u013d\7t\2\2\u013d\u013e")
        buf.write("\7g\2\2\u013e\u013f\7c\2\2\u013f\u0140\7f\2\2\u0140\u0141")
        buf.write("\7D\2\2\u0141\u0142\7q\2\2\u0142\u0143\7q\2\2\u0143\u0144")
        buf.write("\7n\2\2\u0144\u0145\7g\2\2\u0145\u0146\7c\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\66\3\2\2\2\u0148\u0149\7r\2\2\u0149\u014a")
        buf.write("\7t\2\2\u014a\u014b\7k\2\2\u014b\u014c\7p\2\2\u014c\u014d")
        buf.write("\7v\2\2\u014d\u014e\7D\2\2\u014e\u014f\7q\2\2\u014f\u0150")
        buf.write("\7q\2\2\u0150\u0151\7n\2\2\u0151\u0152\7g\2\2\u0152\u0153")
        buf.write("\7c\2\2\u0153\u0154\7p\2\2\u01548\3\2\2\2\u0155\u0156")
        buf.write("\7t\2\2\u0156\u0157\7g\2\2\u0157\u0158\7c\2\2\u0158\u0159")
        buf.write("\7f\2\2\u0159\u015a\7U\2\2\u015a\u015b\7v\2\2\u015b\u015c")
        buf.write("\7t\2\2\u015c\u015d\7k\2\2\u015d\u015e\7p\2\2\u015e\u015f")
        buf.write("\7i\2\2\u015f:\3\2\2\2\u0160\u0161\7r\2\2\u0161\u0162")
        buf.write("\7t\2\2\u0162\u0163\7k\2\2\u0163\u0164\7p\2\2\u0164\u0165")
        buf.write("\7v\2\2\u0165\u0166\7U\2\2\u0166\u0167\7v\2\2\u0167\u0168")
        buf.write("\7t\2\2\u0168\u0169\7k\2\2\u0169\u016a\7p\2\2\u016a\u016b")
        buf.write("\7i\2\2\u016b<\3\2\2\2\u016c\u016d\7u\2\2\u016d\u016e")
        buf.write("\7w\2\2\u016e\u016f\7r\2\2\u016f\u0170\7g\2\2\u0170\u0171")
        buf.write("\7t\2\2\u0171>\3\2\2\2\u0172\u0173\7r\2\2\u0173\u0174")
        buf.write("\7t\2\2\u0174\u0175\7g\2\2\u0175\u0176\7x\2\2\u0176\u0177")
        buf.write("\7g\2\2\u0177\u0178\7p\2\2\u0178\u0179\7v\2\2\u0179\u017a")
        buf.write("\7F\2\2\u017a\u017b\7g\2\2\u017b\u017c\7h\2\2\u017c\u017d")
        buf.write("\7c\2\2\u017d\u017e\7w\2\2\u017e\u017f\7n\2\2\u017f\u0180")
        buf.write("\7v\2\2\u0180@\3\2\2\2\u0181\u0182\7\61\2\2\u0182\u0183")
        buf.write("\7\61\2\2\u0183\u0187\3\2\2\2\u0184\u0186\n\2\2\2\u0185")
        buf.write("\u0184\3\2\2\2\u0186\u0189\3\2\2\2\u0187\u0185\3\2\2\2")
        buf.write("\u0187\u0188\3\2\2\2\u0188\u018a\3\2\2\2\u0189\u0187\3")
        buf.write("\2\2\2\u018a\u018b\b!\2\2\u018bB\3\2\2\2\u018c\u018d\7")
        buf.write("\61\2\2\u018d\u018e\7,\2\2\u018e\u0192\3\2\2\2\u018f\u0191")
        buf.write("\13\2\2\2\u0190\u018f\3\2\2\2\u0191\u0194\3\2\2\2\u0192")
        buf.write("\u0193\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u0195\3\2\2\2")
        buf.write("\u0194\u0192\3\2\2\2\u0195\u0196\7,\2\2\u0196\u0197\7")
        buf.write("\61\2\2\u0197\u0198\3\2\2\2\u0198\u0199\b\"\2\2\u0199")
        buf.write("D\3\2\2\2\u019a\u01ae\7\62\2\2\u019b\u019d\t\3\2\2\u019c")
        buf.write("\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u019c\3\2\2\2")
        buf.write("\u019e\u019f\3\2\2\2\u019f\u01aa\3\2\2\2\u01a0\u01a2\7")
        buf.write("a\2\2\u01a1\u01a0\3\2\2\2\u01a1\u01a2\3\2\2\2\u01a2\u01a4")
        buf.write("\3\2\2\2\u01a3\u01a5\t\4\2\2\u01a4\u01a3\3\2\2\2\u01a5")
        buf.write("\u01a6\3\2\2\2\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2")
        buf.write("\u01a7\u01a9\3\2\2\2\u01a8\u01a1\3\2\2\2\u01a9\u01ac\3")
        buf.write("\2\2\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ae")
        buf.write("\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u019a\3\2\2\2\u01ad")
        buf.write("\u019c\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\b#\3\2")
        buf.write("\u01b0F\3\2\2\2\u01b1\u01b7\5I%\2\u01b2\u01b4\5K&\2\u01b3")
        buf.write("\u01b5\5M\'\2\u01b4\u01b3\3\2\2\2\u01b4\u01b5\3\2\2\2")
        buf.write("\u01b5\u01b8\3\2\2\2\u01b6\u01b8\5M\'\2\u01b7\u01b2\3")
        buf.write("\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01bd\3\2\2\2\u01b9\u01ba")
        buf.write("\5K&\2\u01ba\u01bb\5M\'\2\u01bb\u01bd\3\2\2\2\u01bc\u01b1")
        buf.write("\3\2\2\2\u01bc\u01b9\3\2\2\2\u01bd\u01be\3\2\2\2\u01be")
        buf.write("\u01bf\b$\4\2\u01bfH\3\2\2\2\u01c0\u01d4\7\62\2\2\u01c1")
        buf.write("\u01c3\t\3\2\2\u01c2\u01c1\3\2\2\2\u01c3\u01c4\3\2\2\2")
        buf.write("\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01d0\3")
        buf.write("\2\2\2\u01c6\u01c8\7a\2\2\u01c7\u01c6\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01ca\3\2\2\2\u01c9\u01cb\t\4\2\2\u01ca")
        buf.write("\u01c9\3\2\2\2\u01cb\u01cc\3\2\2\2\u01cc\u01ca\3\2\2\2")
        buf.write("\u01cc\u01cd\3\2\2\2\u01cd\u01cf\3\2\2\2\u01ce\u01c7\3")
        buf.write("\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d0\u01d1")
        buf.write("\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d3")
        buf.write("\u01c0\3\2\2\2\u01d3\u01c2\3\2\2\2\u01d4J\3\2\2\2\u01d5")
        buf.write("\u01d9\7\60\2\2\u01d6\u01d8\t\4\2\2\u01d7\u01d6\3\2\2")
        buf.write("\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da")
        buf.write("\3\2\2\2\u01daL\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01de")
        buf.write("\t\5\2\2\u01dd\u01df\t\6\2\2\u01de\u01dd\3\2\2\2\u01de")
        buf.write("\u01df\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01e2\t\4\2\2")
        buf.write("\u01e1\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e1\3")
        buf.write("\2\2\2\u01e3\u01e4\3\2\2\2\u01e4N\3\2\2\2\u01e5\u01e8")
        buf.write("\5%\23\2\u01e6\u01e8\5\'\24\2\u01e7\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e8P\3\2\2\2\u01e9\u01ee\7$\2\2\u01ea")
        buf.write("\u01ed\n\7\2\2\u01eb\u01ed\5S*\2\u01ec\u01ea\3\2\2\2\u01ec")
        buf.write("\u01eb\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2")
        buf.write("\u01ee\u01ef\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01ee\3")
        buf.write("\2\2\2\u01f1\u01f2\7$\2\2\u01f2\u01f3\b)\5\2\u01f3R\3")
        buf.write("\2\2\2\u01f4\u01f5\7^\2\2\u01f5\u01f6\t\b\2\2\u01f6T\3")
        buf.write("\2\2\2\u01f7\u01fb\t\t\2\2\u01f8\u01fa\t\n\2\2\u01f9\u01f8")
        buf.write("\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb")
        buf.write("\u01fc\3\2\2\2\u01fcV\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe")
        buf.write("\u01ff\7-\2\2\u01ffX\3\2\2\2\u0200\u0201\7/\2\2\u0201")
        buf.write("Z\3\2\2\2\u0202\u0203\7,\2\2\u0203\\\3\2\2\2\u0204\u0205")
        buf.write("\7\61\2\2\u0205^\3\2\2\2\u0206\u0207\7\'\2\2\u0207`\3")
        buf.write("\2\2\2\u0208\u0209\7#\2\2\u0209b\3\2\2\2\u020a\u020b\7")
        buf.write("(\2\2\u020b\u020c\7(\2\2\u020cd\3\2\2\2\u020d\u020e\7")
        buf.write("~\2\2\u020e\u020f\7~\2\2\u020ff\3\2\2\2\u0210\u0211\7")
        buf.write("?\2\2\u0211\u0212\7?\2\2\u0212h\3\2\2\2\u0213\u0214\7")
        buf.write("#\2\2\u0214\u0215\7?\2\2\u0215j\3\2\2\2\u0216\u0217\7")
        buf.write(">\2\2\u0217l\3\2\2\2\u0218\u0219\7>\2\2\u0219\u021a\7")
        buf.write("?\2\2\u021an\3\2\2\2\u021b\u021c\7@\2\2\u021cp\3\2\2\2")
        buf.write("\u021d\u021e\7@\2\2\u021e\u021f\7?\2\2\u021fr\3\2\2\2")
        buf.write("\u0220\u0221\7<\2\2\u0221\u0222\7<\2\2\u0222t\3\2\2\2")
        buf.write("\u0223\u0224\7.\2\2\u0224v\3\2\2\2\u0225\u0226\7=\2\2")
        buf.write("\u0226x\3\2\2\2\u0227\u0228\7<\2\2\u0228z\3\2\2\2\u0229")
        buf.write("\u022a\7?\2\2\u022a|\3\2\2\2\u022b\u022c\7\60\2\2\u022c")
        buf.write("~\3\2\2\2\u022d\u022e\7*\2\2\u022e\u0080\3\2\2\2\u022f")
        buf.write("\u0230\7+\2\2\u0230\u0082\3\2\2\2\u0231\u0232\7}\2\2\u0232")
        buf.write("\u0084\3\2\2\2\u0233\u0234\7\177\2\2\u0234\u0086\3\2\2")
        buf.write("\2\u0235\u0236\7]\2\2\u0236\u0088\3\2\2\2\u0237\u0238")
        buf.write("\7_\2\2\u0238\u008a\3\2\2\2\u0239\u023b\t\13\2\2\u023a")
        buf.write("\u0239\3\2\2\2\u023b\u023c\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023c\u023d\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f\b")
        buf.write("F\2\2\u023f\u008c\3\2\2\2\u0240\u0245\7$\2\2\u0241\u0244")
        buf.write("\n\f\2\2\u0242\u0244\5S*\2\u0243\u0241\3\2\2\2\u0243\u0242")
        buf.write("\3\2\2\2\u0244\u0247\3\2\2\2\u0245\u0243\3\2\2\2\u0245")
        buf.write("\u0246\3\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245\3\2\2\2")
        buf.write("\u0248\u024a\t\r\2\2\u0249\u0248\3\2\2\2\u024a\u024b\3")
        buf.write("\2\2\2\u024b\u024c\bG\6\2\u024c\u008e\3\2\2\2\u024d\u0252")
        buf.write("\7$\2\2\u024e\u0251\n\7\2\2\u024f\u0251\5S*\2\u0250\u024e")
        buf.write("\3\2\2\2\u0250\u024f\3\2\2\2\u0251\u0254\3\2\2\2\u0252")
        buf.write("\u0250\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0255\3\2\2\2")
        buf.write("\u0254\u0252\3\2\2\2\u0255\u0256\7^\2\2\u0256\u0257\n")
        buf.write("\b\2\2\u0257\u0258\bH\7\2\u0258\u0090\3\2\2\2\u0259\u025a")
        buf.write("\13\2\2\2\u025a\u025b\bI\b\2\u025b\u0092\3\2\2\2\37\2")
        buf.write("\u0187\u0192\u019e\u01a1\u01a6\u01aa\u01ad\u01b4\u01b7")
        buf.write("\u01bc\u01c4\u01c7\u01cc\u01d0\u01d3\u01d9\u01de\u01e3")
        buf.write("\u01e7\u01ec\u01ee\u01fb\u023c\u0243\u0245\u0249\u0250")
        buf.write("\u0252\t\b\2\2\3#\2\3$\3\3)\4\3G\5\3H\6\3I\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BOOL = 1
    INT = 2
    FLOAT = 3
    STRING = 4
    VOID = 5
    AUTO = 6
    INHERIT = 7
    OUT = 8
    FUNCTION = 9
    FOR = 10
    WHILE = 11
    DO = 12
    RETURN = 13
    CONTINUE = 14
    BREAK = 15
    IF = 16
    ELSE = 17
    TRUE = 18
    FALSE = 19
    ARRAY = 20
    OF = 21
    READ_INTEGER = 22
    PRINT_INTEGER = 23
    READ_FLOAT = 24
    PRINT_FLOAT = 25
    READ_BOOLEAN = 26
    PRINT_BOOLEAN = 27
    READ_STRING = 28
    PRINT_STRING = 29
    SUPER = 30
    PREVENT_DEFAULT = 31
    LINE_COMMENT = 32
    BLOCK_COMMENT = 33
    DECIMAL = 34
    REAL = 35
    BOOLEAN = 36
    STRINGLIT = 37
    IDENTIFIERS = 38
    ADD = 39
    SUB = 40
    MUL = 41
    DIV = 42
    MOD = 43
    NOT = 44
    AND = 45
    OR = 46
    EQ = 47
    NEQ = 48
    LT = 49
    LTE = 50
    GT = 51
    GTE = 52
    SCOPE = 53
    COMMA = 54
    SEMI = 55
    COLON = 56
    ASSIGN = 57
    DOT = 58
    LP = 59
    RP = 60
    LB = 61
    RB = 62
    LBK = 63
    RBK = 64
    WS = 65
    UNCLOSE_STRING = 66
    ILLEGAL_ESCAPE = 67
    ERROR_CHAR = 68

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'boolean'", "'integer'", "'float'", "'string'", "'void'", "'auto'", 
            "'inherit'", "'out'", "'function'", "'for'", "'while'", "'do'", 
            "'return'", "'continue'", "'break'", "'if'", "'else'", "'true'", 
            "'false'", "'array'", "'of'", "'readInteger'", "'printInteger'", 
            "'readFloat'", "'printFloat'", "'readBoolean'", "'printBoolean'", 
            "'readString'", "'printString'", "'super'", "'preventDefault'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'::'", "','", "';'", 
            "':'", "'='", "'.'", "'('", "')'", "'{'", "'}'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "BOOL", "INT", "FLOAT", "STRING", "VOID", "AUTO", "INHERIT", 
            "OUT", "FUNCTION", "FOR", "WHILE", "DO", "RETURN", "CONTINUE", 
            "BREAK", "IF", "ELSE", "TRUE", "FALSE", "ARRAY", "OF", "READ_INTEGER", 
            "PRINT_INTEGER", "READ_FLOAT", "PRINT_FLOAT", "READ_BOOLEAN", 
            "PRINT_BOOLEAN", "READ_STRING", "PRINT_STRING", "SUPER", "PREVENT_DEFAULT", 
            "LINE_COMMENT", "BLOCK_COMMENT", "DECIMAL", "REAL", "BOOLEAN", 
            "STRINGLIT", "IDENTIFIERS", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "NOT", "AND", "OR", "EQ", "NEQ", "LT", "LTE", "GT", "GTE", "SCOPE", 
            "COMMA", "SEMI", "COLON", "ASSIGN", "DOT", "LP", "RP", "LB", 
            "RB", "LBK", "RBK", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "BOOL", "INT", "FLOAT", "STRING", "VOID", "AUTO", "INHERIT", 
                  "OUT", "FUNCTION", "FOR", "WHILE", "DO", "RETURN", "CONTINUE", 
                  "BREAK", "IF", "ELSE", "TRUE", "FALSE", "ARRAY", "OF", 
                  "READ_INTEGER", "PRINT_INTEGER", "READ_FLOAT", "PRINT_FLOAT", 
                  "READ_BOOLEAN", "PRINT_BOOLEAN", "READ_STRING", "PRINT_STRING", 
                  "SUPER", "PREVENT_DEFAULT", "LINE_COMMENT", "BLOCK_COMMENT", 
                  "DECIMAL", "REAL", "INTPART", "FRACPART", "EXPPART", "BOOLEAN", 
                  "STRINGLIT", "ESQ", "IDENTIFIERS", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "NOT", "AND", "OR", "EQ", "NEQ", "LT", "LTE", 
                  "GT", "GTE", "SCOPE", "COMMA", "SEMI", "COLON", "ASSIGN", 
                  "DOT", "LP", "RP", "LB", "RB", "LBK", "RBK", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
            actions[33] = self.DECIMAL_action 
            actions[34] = self.REAL_action 
            actions[39] = self.STRINGLIT_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[71] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def DECIMAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

    def REAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text =str(self.text[1:-1])
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	uncloseStr= str(self.text)
            	impossible='\n'
            	if uncloseStr[-1] in impossible:
            		raise UncloseString(uncloseStr[1:-1])
            	else:
            		raise UncloseString(uncloseStr[1:])


     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	raise IllegalEscape(str(self.text[1:]))

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


