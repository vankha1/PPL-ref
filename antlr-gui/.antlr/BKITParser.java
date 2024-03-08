// Generated from d:/Learning_Documents_of_Third_Year/Principles of Programming Languages/antlr-gui/BKIT.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class BKITParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, INTTYPE=3, FLOATTYPE=4, ID=5, WS=6;
	public static final int
		RULE_program = 0, RULE_vardecls = 1, RULE_vardecltail = 2, RULE_vardecl = 3, 
		RULE_mptype = 4, RULE_ids = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "vardecls", "vardecltail", "vardecl", "mptype", "ids"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "','", "'int'", "'float'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "INTTYPE", "FLOATTYPE", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "BKIT.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public BKITParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public VardeclsContext vardecls() {
			return getRuleContext(VardeclsContext.class,0);
		}
		public TerminalNode EOF() { return getToken(BKITParser.EOF, 0); }
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitProgram(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			vardecls();
			setState(13);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VardeclsContext extends ParserRuleContext {
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public VardecltailContext vardecltail() {
			return getRuleContext(VardecltailContext.class,0);
		}
		public VardeclsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecls; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVardecls(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVardecls(this);
		}
	}

	public final VardeclsContext vardecls() throws RecognitionException {
		VardeclsContext _localctx = new VardeclsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_vardecls);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(15);
			vardecl();
			setState(16);
			vardecltail();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VardecltailContext extends ParserRuleContext {
		public VardeclContext vardecl() {
			return getRuleContext(VardeclContext.class,0);
		}
		public VardecltailContext vardecltail() {
			return getRuleContext(VardecltailContext.class,0);
		}
		public VardecltailContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecltail; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVardecltail(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVardecltail(this);
		}
	}

	public final VardecltailContext vardecltail() throws RecognitionException {
		VardecltailContext _localctx = new VardecltailContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_vardecltail);
		try {
			setState(22);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INTTYPE:
			case FLOATTYPE:
				enterOuterAlt(_localctx, 1);
				{
				setState(18);
				vardecl();
				setState(19);
				vardecltail();
				}
				break;
			case EOF:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VardeclContext extends ParserRuleContext {
		public MptypeContext mptype() {
			return getRuleContext(MptypeContext.class,0);
		}
		public IdsContext ids() {
			return getRuleContext(IdsContext.class,0);
		}
		public VardeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_vardecl; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterVardecl(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitVardecl(this);
		}
	}

	public final VardeclContext vardecl() throws RecognitionException {
		VardeclContext _localctx = new VardeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_vardecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(24);
			mptype();
			setState(25);
			ids();
			setState(26);
			match(T__0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MptypeContext extends ParserRuleContext {
		public TerminalNode INTTYPE() { return getToken(BKITParser.INTTYPE, 0); }
		public TerminalNode FLOATTYPE() { return getToken(BKITParser.FLOATTYPE, 0); }
		public MptypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mptype; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterMptype(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitMptype(this);
		}
	}

	public final MptypeContext mptype() throws RecognitionException {
		MptypeContext _localctx = new MptypeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_mptype);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			_la = _input.LA(1);
			if ( !(_la==INTTYPE || _la==FLOATTYPE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(BKITParser.ID, 0); }
		public IdsContext ids() {
			return getRuleContext(IdsContext.class,0);
		}
		public IdsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ids; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).enterIds(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof BKITListener ) ((BKITListener)listener).exitIds(this);
		}
	}

	public final IdsContext ids() throws RecognitionException {
		IdsContext _localctx = new IdsContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_ids);
		try {
			setState(34);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(30);
				match(ID);
				setState(31);
				match(T__1);
				setState(32);
				ids();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(33);
				match(ID);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0006%\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003"+
		"\u0002\u0017\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005#\b\u0005\u0001\u0005\u0000\u0000\u0006\u0000\u0002\u0004\u0006"+
		"\b\n\u0000\u0001\u0001\u0000\u0003\u0004 \u0000\f\u0001\u0000\u0000\u0000"+
		"\u0002\u000f\u0001\u0000\u0000\u0000\u0004\u0016\u0001\u0000\u0000\u0000"+
		"\u0006\u0018\u0001\u0000\u0000\u0000\b\u001c\u0001\u0000\u0000\u0000\n"+
		"\"\u0001\u0000\u0000\u0000\f\r\u0003\u0002\u0001\u0000\r\u000e\u0005\u0000"+
		"\u0000\u0001\u000e\u0001\u0001\u0000\u0000\u0000\u000f\u0010\u0003\u0006"+
		"\u0003\u0000\u0010\u0011\u0003\u0004\u0002\u0000\u0011\u0003\u0001\u0000"+
		"\u0000\u0000\u0012\u0013\u0003\u0006\u0003\u0000\u0013\u0014\u0003\u0004"+
		"\u0002\u0000\u0014\u0017\u0001\u0000\u0000\u0000\u0015\u0017\u0001\u0000"+
		"\u0000\u0000\u0016\u0012\u0001\u0000\u0000\u0000\u0016\u0015\u0001\u0000"+
		"\u0000\u0000\u0017\u0005\u0001\u0000\u0000\u0000\u0018\u0019\u0003\b\u0004"+
		"\u0000\u0019\u001a\u0003\n\u0005\u0000\u001a\u001b\u0005\u0001\u0000\u0000"+
		"\u001b\u0007\u0001\u0000\u0000\u0000\u001c\u001d\u0007\u0000\u0000\u0000"+
		"\u001d\t\u0001\u0000\u0000\u0000\u001e\u001f\u0005\u0005\u0000\u0000\u001f"+
		" \u0005\u0002\u0000\u0000 #\u0003\n\u0005\u0000!#\u0005\u0005\u0000\u0000"+
		"\"\u001e\u0001\u0000\u0000\u0000\"!\u0001\u0000\u0000\u0000#\u000b\u0001"+
		"\u0000\u0000\u0000\u0002\u0016\"";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}