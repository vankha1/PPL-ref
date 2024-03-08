grammar BKOOL;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
// Use ANTLR to write regular expressions describing 
// Pascal strings are made up of a sequence of characters between single quotes: 'string'. 
// The single quote itself can appear as two single quotes back to back in a string: 'isn''t'.


program:  EOF;

IDENTIFIER: [a-z][a-z0-9]*;

REAL : INTPART DECPART | INTPART DECPART? EXPPART;
fragment INTPART : ([0-9]+);
fragment DECPART : ('.' [0-9]+);
fragment EXPPART : ([eE] [+\-]? [0-9]+);

// STRINGLIT : Sing0 (~['] | Sing0 Sing0)* Sing0;
// fragment Sing0 : ['];

/* Partial correct */
// BKNetID: NAME '.' NAME CUSTOM_STRING;

// fragment NAME : [a-z]+;
// fragment CUSTOM_STRING : [a-z0-9_.] [a-z0-9_.]? [a-z0-9_.]? [a-z0-9_.]? [a-z0-9_.]? [^.];

// IPv4 : (STRING) '.' (STRING) '.' (STRING) '.' (STRING);

// fragment STRING : '0' | [1-9] [0-9]? [0-9]?;

// PHP : ZERO | NON_ZERO_DIGIT DIGIT * ;

// fragment  DIGIT : [0-9] | [0-9] '_'? DIGIT;

// fragment  ZERO : '0';

// fragment  NON_ZERO_DIGIT : [1-9];

// program : decllist EOF ;

// decllist : decl decllist | decl;
// decl : vardecl | funcdecl;

// vardecl: 'vardecl' ;
// funcdecl: 'funcdecl' ;

// vardecl: typ idlist SEMI;
// funcdecl : typ ID paradecl body;
// paradecl : LB paralist RB;
// paralist : paraprime | ;
// paraprime : param SEMI paraprime | param;
// param : typ idlist;
// body : LR (stmtlist) RR;
// stmtlist : (vardecl | stmt) stmtlist | ;
// stmt : ( assignstmt | callstmt | returnstmt) SEMI;
// assignstmt : ID EQUAL expr ;
// callstmt : ID LB exprlist RB ;
// exprlist : exprprime | ;
// exprprime : expr COMMA exprprime | expr;
// returnstmt : RETURN expr ;

// typ : INT | FLOAT ;
// idlist: ID COMMA idlist | ID;

// expr : expr1 ADD expr | expr1 ;
// expr1 : expr2 SUB expr2 | expr2;
// expr2 : expr2 (MUL | DIV) expr3 | expr3; 
// expr3 : INTLIT | FLOATLIT | ID | callexpr | subexpr ;
// callexpr : ID LB exprlist RB ;
// subexpr : LB expr RB ;

// ADD : '+'; SUB : '-'; MUL : '*'; DIV : '/';
// EQUAL : '=';
// RETURN : 'return';
// LB : '('; RB : ')';
// LR : '{'; RR : '}';
// COMMA: ',';
// INT : 'int';
// FLOAT : 'float';
// SEMI: ';' ;

// FLOATLIT : INTLIT ('.') INTLIT ;
// INTLIT : [0-9]+;
// ID : [a-zA-Z]+;

// exercise 5 MiniPHP
// program : decllist EOF ;
// decllist : decl decllist | decl;
// decl : array | vardecl ;

// vardecl : 

// assignstmt : VARNAME EQ expr SEMI ;
// expr : operands operator ;
// operator : VARNAME (INTLIT | FLOATLIT | STRINGLIT | array);
// array : ARRAY ( indexarr | associativearr );
// indexarr : LP exprlist RP ;
// exprlist: exprprime | ;
// exprprime : expr COMMA exprprime | expr;
// associativearr : LP associativepairlist RP ;
// associativepairlist: associativepairprime | ;
// associativepairprime: associativepair COMMA associativepairprime | associativepair ;
// associativepair: PAIRNAME ARROW expr ;


// ARROW : '=>';
// COMMA : ',';
// LP : '('; 
// RP : ')';
// EQ : '=';
// SEMI : ';';
// ARRAY : 'array';
// STRINGLIT : '"' .*? '"';
// DSTAR : '**';
// DOT : '.';
// MUL : '*';
// DIV : '/';
// MOD : '%';
// ADD : '+';
// SUB : '-';
// DQUES: '??';


// PAIRNAME: [a-zA-Z_][a-zA-Z0-9_]*; 
// FLOATLIT : INTLIT ('.') INTLIT ;
// INTLIT : [0-9]+ ;
// VARNAME : [a-zA-Z_][a-zA-Z0-9_]*;


WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;