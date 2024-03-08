grammar MT22;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: decllist EOF;
decllist: decl decllist | decl;
decl: vardecl | funcdecl;

// Variable ----------------
vardecl: (vardecl_not_full | vardecl_full | vardecl_array);
vardecl_full: (VAR | DYNAMIC) ID ASSIGN exp;
vardecl_not_full: atomic_types ID (ASSIGN exp)?;
vardecl_array: array_type (ASSIGN array_lit)?;
// exp_list: exp COMMA exp_list | exp; id_list: ID COMMA id_list | ID;

// Function -----------------
funcdecl: func_prototype | func_prototype func_body;
func_prototype: FUNC ID LP param_list RP NEW_LINE;
func_body: block_stmt | return_stmt;

paramdecl: ((atomic_types | VAR | DYNAMIC) ID) | (array_type);
param_list: param_prime |;
param_prime: paramdecl COMMA param_prime | paramdecl;

// Statements -----------------
stmt:
	(
		assign_stmt
		| if_stmt
		| for_stmt
		| block_stmt
		| break_stmt
		| continue_stmt
		| return_stmt
		| call_stmt
	) ;
assign_stmt: lhs ASSIGN exp;
if_stmt: IF sub_exp stmt (ELIF sub_exp stmt)? (ELSE stmt)?;
for_stmt: FOR lhs UNTIL exp BY exp stmt;

break_stmt: BREAK;
continue_stmt: CONTINUE;
return_stmt: RETURN (exp)?;
call_stmt: ID LP expr_list RP;
block_stmt: BEGIN blocked_list END;
blocked_list: stmt_plus_vardecl blocked_list |;
// blocked_list_prime: stmt_plus_vardecl blocked_list_prime | stmt_plus_vardecl;
stmt_plus_vardecl: (stmt | vardecl);

lhs: ID | index_expr;

// Expression -----------------
exp: exp0;
expr_list: exprprime |;
exprprime: exp COMMA exprprime | exp;

exp0: exp1 CONCAT exp1 | exp1;
exp1:
	exp2 (
		| EQUAL
		| NOT_SAME
		| SAME
		| LESS_THAN
		| LESS_THAN_EQUAL
		| GREATER_THAN
		| GREATER_THAN_EQUAL
	) exp2
	| exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: ID | constant | func_call | sub_exp | index_expr;

constant: number_lit | BOOL_LIT | STRING_LIT | array_lit;
sub_exp: LP exp RP;

index_expr: ID index_operator;
index_operator: LS exprprime RS;

func_call: ID LP expr_list RP;

// Array -------------------
array_lit: LS expr_list RS;
array_type: atomic_types ID dimensions;
dimensions: LS number_lits RS;
number_lits: number_lit COMMA number_lits | number_lit;
atomic_types: BOOL | NUMBER | STRING;

// Literal -----------------
BOOL_LIT: TRUE | FALSE;

FLOAT_LIT: ( INT_LIT DEC_PART? EXP_PART? | INT_LIT EXP_PART);

INT_LIT: '0' | [1-9]([0-9])*;

fragment DEC_PART: '.' ([0-9])*;
fragment EXP_PART: [eE] [+-]? ([0-9])+;

number_lit: FLOAT_LIT | INT_LIT;

STRING_LIT:
	'"' (ESC | ~[\\\n"] | '\'"')* '"' {self.text = self.text[1:-1]};

fragment ESC: '\\' [bfrnt"'\\];
fragment ILLEGAL_ESC: '\\' ~[bfrnt"'\\];

// fragment NL: [\r\n] ;

LP: '(';
RP: ')';
LS: '[';
RS: ']';
COMMA: ',';

// DOT: '.'; SEMI: ';'; COLON: ':'; LC: '{'; RC: '}';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '=';
ASSIGN: '<-';
NOT_SAME: '!=';
LESS_THAN: '<';
LESS_THAN_EQUAL: '<=';
GREATER_THAN_EQUAL: '>=';
GREATER_THAN: '>';
CONCAT: '...';
SAME: '==';

TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

// ARRAY: 'array'; AUTO: 'auto'; DO: 'do'; FLOAT: 'float'; INTEGER: 'integer'; VOID: 'void'; WHILE:
// 'while'; OUT: 'out'; OF: 'of'; INHERIT: 'inherit';

// COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '##' ~[\r\n]* -> skip; //

ID: [_a-zA-Z] ([a-zA-Z0-9_])*;

WS: [ \t\f\b]+ -> skip;

NEW_LINE: '\r'? '\n';

UNCLOSE_STRING:
	'"' (~[\\\n"'] | ESC)* (EOF | [\r\n]) {
	raise UncloseString(self.text[1:].replace('\n', '').replace('\r', ''))
};
ILLEGAL_ESCAPE:
	'"' (~[\\\n"] | ESC)* ILLEGAL_ESC {
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR:
	. {
		raise ErrorToken(self.text)
	};