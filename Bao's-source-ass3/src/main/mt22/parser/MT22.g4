grammar MT22;

// MSSV: 2012670
// Họ và tên : Nguyễn Lê Minh Bảo

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
@parser::members {

}



program: decllist EOF;

decllist: decl decllist | decl;
decl:( declare_var | declare_func ) ;


// 4 định nghĩa kiểu 


bool_typ: BOOL;
int_typ: INT;
float_typ: FLOAT;
string_typ: STRING;
void_typ: VOID;
auto_typ: AUTO;
array_typ: ARRAY LBK int_lit RBK OF typ_of_array;
int_lit:DECIMAL COMMA int_lit | DECIMAL;
typ_of_array: bool_typ | int_typ | float_typ | string_typ;




BOOL: 'boolean';
INT : 'integer';
FLOAT: 'float';
STRING: 'string'; 
VOID: 'void';
AUTO: 'auto';

INHERIT: 'inherit';
OUT: 'out';
FUNCTION: 'function';
FOR: 'for';
WHILE: 'while';
DO: 'do';
RETURN: 'return';
CONTINUE: 'continue';
BREAK: 'break';
IF: 'if';
ELSE: 'else';
TRUE: 'true';
FALSE: 'false';
ARRAY: 'array';
OF: 'of';
READ_INTEGER: 'readInteger';
PRINT_INTEGER: 'printInteger';
READ_FLOAT: 'readFloat';
PRINT_FLOAT: 'printFloat';
READ_BOOLEAN: 'readBoolean';
PRINT_BOOLEAN: 'printBoolean';
READ_STRING: 'readString';
PRINT_STRING: 'printString';
SUPER: 'super';
PREVENT_DEFAULT: 'preventDefault';



///////////////////////////////////////////////////////////////////////////////////


// 5.1.1 khai báo biến

declare_var: idlit COLON (typ_var | array_typ ) SEMI | IDENTIFIERS COLON (typ_var | array_typ ) ASSIGN exp SEMI | init_var;
init_var: IDENTIFIERS COMMA recursive_var COMMA exp SEMI;
recursive_var: IDENTIFIERS COMMA recursive_var COMMA exp   | IDENTIFIERS COLON (typ_var | array_typ ) ASSIGN exp;
idlit: (IDENTIFIERS COMMA)  idlit | IDENTIFIERS;


typ_var:   ( int_typ 
			| auto_typ 
			| bool_typ 
			| float_typ 
			| string_typ );


// 5.1.2 khai báo tham số

declare_para: inherit?  out?  IDENTIFIERS  COLON  (typ_var | array_typ ) ;

inherit: INHERIT;
out:  OUT ;

// 5.1.3 khai báo HÀM

declare_func: IDENTIFIERS COLON FUNCTION (typ | array_typ) LP paralit RP (inherit IDENTIFIERS)?  body  ; 
typ:  ( int_typ 
	  | auto_typ 
	  | bool_typ 
	  | void_typ 
	  | float_typ 
	  | string_typ) ;

paralit: paraPrime | ;
paraPrime: declare_para COMMA paraPrime | declare_para;

//  body : 7.2 -> 7.5

body: block_stm | stmt;

// 7.10 Block Statement
block_stm: LB block_lit RB; 
block_lit: (stmt | declare_var) block_lit | ;
stmt:  ( ass_stm 
		| if_stm 
		| for_stm 
		| do_wh_stm 
		| while_stm 
		| return_stm 
		| call_stm 
		| break_stm 
		| continue_stm 
		| block_stm
		| LB RB ) ;


///////////////////////////////////////////////////////////////////////////////////


// 6 Expressions

exp:  exp1 SCOPE exp1 | exp1;
exp1: exp2 (EQ | NEQ | LT | GT | LTE | GTE ) exp2 | exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB) exp4 | exp4;
exp4: exp4 (MUL | DIV | MOD) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: SUB exp6 | exp7;
exp7: exp7 LBK list_exp RBK | exp8;
exp8:  IDENTIFIERS | DECIMAL | REAL | STRINGLIT | TRUE | FALSE | fun_call | array | LP exp RP ;
list_exp: exp COMMA list_exp | exp;


// 6.6 Function call

fun_call: IDENTIFIERS LP para_fun RP | special_function;

para_fun: para_fun_Prime | ;
para_fun_Prime: exp COMMA para_fun_Prime | exp;



///////////////////////////////////////////////////////////////////////////////////


// 7 Statement
// 7.1 Assignment Statement

ass_stm: exp  ASSIGN  exp SEMI;




// 7.2 If Statement

if_stm: IF  LP? exp RP?   body  (ELSE  body)?; 

// 7.3 For Statement

for_stm: FOR  LP init_exp COMMA  exp COMMA  exp  RP  body  ; 
init_exp: IDENTIFIERS ASSIGN exp; 

// 7.4 While Statement

while_stm: WHILE  LP exp RP   body  ;

// 7.5 Do-While Statement

do_wh_stm: DO  body   WHILE  LP exp RP SEMI ; 

// 7.6 Break Statement
break_stm: BREAK SEMI;

// 7.7 Continue Statement
continue_stm: CONTINUE SEMI;

// 7.8 Return Statement
return_stm: RETURN  exp? SEMI;


// 7.9 Call Statement

call_stm: fun_call SEMI;


///////////////////////////////////////////////////////////////////////////////////



// 8 Special Functions

special_function: (  readInteger 
					| printInteger
					| readFloat
					| printFloat
					| readBoolean
					| printBoolean
					| readString
					| printString
					| suPer
					| preventDefault
				   );

readInteger: READ_INTEGER LP RP ;
printInteger: PRINT_INTEGER LP exp RP ;
readFloat: READ_FLOAT LP RP ;
printFloat: PRINT_FLOAT LP exp RP ;
readBoolean: READ_BOOLEAN LP RP ;
printBoolean: PRINT_BOOLEAN LP exp RP ;
readString: READ_STRING LP RP ;
printString: PRINT_STRING LP exp RP ;
suPer: SUPER LP list_exp? RP ;
preventDefault: PREVENT_DEFAULT LP RP ;


///////////////////////////////////////////////////////////////////////////////////



// 3.2 comment

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' ->skip;


// 3.7.1 định nghĩa số nguyên
DECIMAL: ('0' | [1-9]+ ('_'? [0-9]+)*) {self.text = self.text.replace("_", "")};

// 3.7.2 định nghĩa số thực
REAL: (INTPART (FRACPART EXPPART? | EXPPART) | FRACPART EXPPART) {self.text = self.text.replace("_", "")};

fragment INTPART: ('0' | [1-9]+ ('_'? [0-9]+)*); 
fragment FRACPART: '.' [0-9]*;
fragment EXPPART: ('e' | 'E') ('-' | '+')? [0-9]+;

// 3.7.3 định nghĩa bool

BOOLEAN: TRUE | FALSE;

// 3.7.4 định nghĩa chuỗi 

STRINGLIT: '"' (~[\\\n"] | ESQ)* '"' {self.text =str(self.text[1:-1])};
fragment ESQ: '\\' [btnfr\\'"];

// 3.3 định nghĩa tên biến (cần bổ sung thêm)
IDENTIFIERS:  [a-zA-Z_][a-zA-Z0-9_]*;


// 3.7.5 định nghĩa mảng 

array: LB element_array? RB ;
element_array: exp COMMA element_array | exp ;




///////////////////////////////////////////////////////////////////////////////////



// các kí hiệu


ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';
EQ: '==';
NEQ: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
SCOPE: '::';

COMMA: ',';
SEMI: ';';
COLON: ':';
ASSIGN: '=';
DOT: '.';
LP: '(';
RP: ')';
LB: '{';
RB: '}';
LBK: '[';
RBK: ']';



///////////////////////////////////////////////////////////////////////////////////



WS : [ \b\f\t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING: 
'"' (~[\\\n"'] | ESQ )* (EOF | '\n') {
	uncloseStr= str(self.text)
	impossible='\n'
	if uncloseStr[-1] in impossible:
		raise UncloseString(uncloseStr[1:-1])
	else:
		raise UncloseString(uncloseStr[1:])

};
ILLEGAL_ESCAPE: 
'"' (~[\\\n"] | ESQ )* '\\' ~[bntrf\\'"] {
	raise IllegalEscape(str(self.text[1:]))
};
ERROR_CHAR: . {raise ErrorToken(self.text)};

