from AST import *
from Visitor import Visitor
from StaticError import *
from Visitor import *


''' 
    o = [local,Scope(N-1),Scope(0),global]
    Scope(i) = [Symbol1,Symbol2,...,SymbolN]
    Symbol:
        name: str
        typ: Type
        modifier: None
        param: [Symbol]: Name
'''

class Symbol:
    def __init__(self, name, type, modifier = None, param = None, is_body_having = False):
        self.name = name
        self.type = type
        self.modifier = modifier
        self.param = param
        self.is_body_having = is_body_having
        
    def __str__(self):
        return "Symbol" + "(" + str(self.name) + ", " + str(self.type) + (", " + str(self.modifier) if self.modifier != None else "") + (", " + str(self.param) if self.param != None else "") + ")"    
        
class Utils:
    def infer(env, name, type):
        for symbol_list in env:
            for symbol in symbol_list:
                name_str = name.name if name.name else name
                # print("Check here....", type)
                if symbol.name == name_str:
                    symbol.type = type
                    return type
                
    def isFunc(symbol):
        return symbol.param != None

class GetEnv(Visitor):
    def __init__(self, ast):
        self.ast = ast
        
    def visitProgram(self, ast, o):
        print("Round 1: program")
        global_scope = [[Symbol("readNumber",NumberType(), None, [], True),
                        Symbol("readBool",BoolType(), None, [], True),
                        Symbol("readString",StringType(), None, [], True),
                        Symbol("writeNumber",VoidType(), None,[Symbol("<Param>",NumberType())], True),
                        Symbol("writeString",VoidType(), None,[Symbol("<Param>",StringType())], True),
                        Symbol("writeBool",VoidType(), None,[Symbol("<Param>",BoolType())], True)
                        ]]
        for decl in ast.decl:
            self.visit(decl, global_scope)
        return global_scope     
    
    def visitVarDecl(self, ast, o):
        print("Round 1: vardecl")
        # o here is o1 of visitFuncDecl in GetEnv
        # just only for case of parameters:
        print(ast.name, ast.varType)
        if Utils.isFunc(o[0][0]):
            o[0] += [Symbol(ast.name, ast.varType, ast.modifier, ast.varInit)]
            
    
    def visitFuncDecl(self, ast, o):
        print("Round 1: funcdecl")
        # Goal: o1 = [[Symbol(ast.name, None, None, []), param_symbol, param_symbol,...]] + o
        o1 = [[Symbol(ast.name, None, None, [])]] + o # o1 = [[local]] + [[scope], [scope]] = [[local], [scope], [scope]]
        # for symbol in o1[0]:
        #     print("Check here ........", symbol.name)
        for param in ast.param:
            self.visit(param, o1) # go to visitVarDecl in GetEnv
            
        list_params = []
        for i in range(1, len(ast.param) + 1):
            # o1[0][i] is the symbol which is added to the list (line 62)
            list_params += [Symbol(o1[0][i].name, o1[0][i].type, None, None)]

        o[0] += [Symbol(ast.name, None, None, list_params)]

class StaticChecker(Visitor):
    def __init__(self,ast):
        self.ast = ast
    
    def check(self):
        return self.visit(self.ast, None)
    
    def visitId(self, ast, o):
        print("This is from visitId")
        for symbol_list in o:
            for symbol in symbol_list:
                # symbol.name here is Id() or str -> want to get name of Id() -> symbol.name.name
                # print(type(symbol.name))
                name_symbol = symbol.name.name if type(symbol.name) is Id else symbol.name
                if ast.name == name_symbol and not Utils.isFunc(symbol):
                    return symbol.type
        raise Undeclared(Identifier(),ast.name)

    def visitNumberType(self, ast, o):
        print("This is from visitNumberType")
        return NumberType()
    
    def visitFloatType(self, ast, o):
        return BoolType()
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitVoidType(self, ast, o):
        return VoidType()
    
    def visitArrayType(self, ast, o): # number a[6]
        return ArrayType(ast.size, ast.eleType)
    
    def visitBinaryOp(self, ast, o):
        op = ast.op
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)
        lefttype = type(left)
        righttype = type(right)
        
        if (op in ['+','-','*','/', '%']):
            print(lefttype, righttype)
            if lefttype == NumberType and righttype == NumberType:
                return NumberType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['and','or']:
            if lefttype is BoolType and righttype is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['...']:
            if lefttype is StringType and righttype is StringType:
                return StringType()
            raise TypeMismatchInExpression(ast)
        
        if op in ['<', '>', '<=', '>=', '!=']:
            if not (lefttype is NumberType) and not (righttype is NumberType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
        if op in ['==']:
            if not (lefttype is StringType) and not (righttype is StringType):
                raise TypeMismatchInExpression(ast)
            return BoolType()
        
    def visitUnaryOp(self, ast, o):
        op = ast.op
        val = self.visit(ast.val, o)
        valtype = type(val)
        
        if op in ['-']:
            if not (valtype is NumberType):
                raise TypeMismatchInExpression(ast)
            return NumberType()
        
        if op in ['not']:
            if valtype is BoolType:
                return BoolType()
            raise TypeMismatchInExpression(ast)
    
    def visitArrayCell(self, ast, o): # a[1, 2, 3]
        for symbol_list in o:
            for symbol in symbol_list:
                if ast.arr == symbol.name:
                    name_type = symbol.type
                    # The name should be in ArrayType
                    if type(name_type) is not ArrayType:
                        raise TypeMismatchInExpression(ast)
                     # All cell vals must be of NumberType
                    for item in ast.idx:
                        item_type = self.visit(item, o)
                        if type(item_type) is not NumberType:
                            raise TypeMismatchInExpression(item)
                        elif type(item_type) is None: 
                            Utils.infer(o, item.name, NumberType())
                    # Check dimensions and cell in ArrayType and ArrayCell with name_type is ArrayType
                    if len(name_type.size) == len(ast.idx):
                        return name_type.eleType
                    elif len(name_type.size) < len(ast.idx):
                        raise TypeMismatchInExpression(ast)
                    else:
                        return ArrayType(name_type.size[len(ast.idx):], name_type.eleType)
        raise Undeclared(Identifier(), ast.arr)
    
    def visitNumberLiteral(self, ast, o):
        return NumberType()
    
    def visitBooleanLiteral(self, ast, o):
        return BoolType()
    
    def visitStringLiteral(self, ast, o):
        return StringType()
    
    def visitArrayLiteral(self, ast, o): # [1,2,3,4]
        print("This is from array literal")
        exprlist = ast.value
        arr_type_check = None
        
        for expr in exprlist:
            expr_type = self.visit(expr, o)
            # first time
            if arr_type_check is None:
                arr_type_check = expr_type
            else:
                if type(expr_type) is ArrayType or type(arr_type_check) is ArrayType:
                    if not hasattr(expr_type, "size") or not hasattr(arr_type_check, "size") or expr_type.size != arr_type_check.size:
                        # print("Check here.....")    
                        raise TypeMismatchInExpression(ast)
                elif type(arr_type_check) != type(expr_type):
                    raise TypeMismatchInExpression(ast) ## need to fix because it must return at Vardecl.
                
        arr_dim = [len(ast.value)] + arr_type_check.size if type(arr_type_check) is ArrayType else [len(ast.value)]
        arr_type = arr_type_check.eleType if type(arr_type_check) is ArrayType else arr_type_check
        return ArrayType(arr_dim, arr_type)
    
    def visitCallExpr(self, ast, o):
        flag = False
        
        for symbol in o[-1]:
            if ast.name == symbol.name and Utils.isFunc(symbol):
                flag = True
                # print("Call expression", symbol.is_body_having)
                # if type(symbol.type) is VoidType:
                #     raise TypeCannotBeInferred(ast)
                break
        
        if not flag: Undeclared(Function(), ast.name)
        # for symbollist in o:
        #     for symbol in symbollist:
        #         print("Check here .........", symbol)
        #     print('.///', len(o))
        if flag:
            # o[0] is block containing this callstmt, o[1] is non-local (it means the function which contains this callstmt)        
            for symbol in o[1]: #TypeCannotBeInfered error for calling again this function itself  
                # print("check here", symbol)
                if symbol.name == ast.name and Utils.isFunc(symbol):
                    raise TypeCannotBeInferred(ast)
            for symbol in o[-1]:
                if symbol.name == ast.name and Utils.isFunc(symbol):
                    if symbol.is_body_having == False:
                        raise NoDefinition(symbol.name)
                    break
        
        for symbol in o[-1]:
            if symbol.name == ast.name and Utils.isFunc(symbol):
                list_param = symbol.param
                args = ast.args
                
                if len(list_param) > len(args):
                    raise TypeMismatchInExpression(ast)
                elif len(args) < len(list_param):
                    raise TypeMismatchInExpression(ast)
                else:
                    for i in range(0, len(list_param)):
                        param_type = list_param[i].type # param element here is symbol
                        args_type = self.visit(ast.args[i], o)
                        
                        # May be wrong because of passing by value
                        # atomic_types = [NumberType, BoolType, StringType]                        
                        # if not (type(args_type) in atomic_types):
                        #     args_type = param_type
                        
                        # Passing by reference
                        if type(param_type) is ArrayType:
                            args_type = param_type
                            continue
                        # TYPE MISMATCH
                        if type(args_type) is not type(param_type):
                            return TypeMismatchInExpression(ast) ## for the case: y <- a + foo(x) of TypeCannotBeInferred in spec
                return symbol.type
    
    def visitAssign(self, ast, o):
        print("This is from visitAssign")
        lhs_type = self.visit(ast.lhs, o)
        exp_type = self.visit(ast.exp, o)
        print("Check assign", lhs_type, exp_type)
        
        if type(lhs_type) is VoidType or type(lhs_type) is ArrayType:
            raise TypeMismatchInStatement(ast)
        
        if lhs_type is None and exp_type is None:
            raise TypeCannotBeInferred(ast)
        
        if type(lhs_type) is None:
            lhs_type = Utils.infer(o, ast.lhs, exp_type)
            return
        
        if type(exp_type) is None:
            exp_type = Utils.infer(o, ast.exp, lhs_type)
            return
                    
        if type(lhs_type) is type(exp_type):
            return exp_type
        
        if type(lhs_type) is not type(exp_type):
            raise TypeCannotBeInferred(ast)
        
    def visitIf(self, ast, o):
        condition_type = self.visit(ast.expr, o)
        if type(condition_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        # Go to new scope -> need new o
        o1 = [[]] + o
        if ast.thenStmt:
            self.visit(ast.thenStmt, o1)
        o2 = [[]] + o
        if ast.elifStmt:
            self.visit(ast.elifStmt, o2)
        o3 = [[]] + o
        if ast.elseStmt:
            self.visit(ast.elifStmt, o3)

    def visitFor(self, ast, o):
        init_type = self.visit(ast.name, o)
        condition_type = self.visit(ast.condExpr, o)
        update_type = self.visit(ast.updpExpr, o)
        if type(init_type) is not NumberType or type(condition_type) is not BoolType or type(update_type) is not NumberType:
            raise TypeMismatchInStatement(ast)
        # new scope
        o1 = [[Symbol("<Loop>", VoidType)]] + o
        self.visit(ast.body, o1)
        
    def visitBreak(self, ast, o):
        flag = False
        for symbol_list in o: # visit all outer blocks
            for symbol in symbol_list:
                if symbol.name == "<Loop>":
                    flag = True
                    return
        if not flag: raise MustInLoop(ast)
        
    def visitContinue(self, ast, o):
        flag = False
        for symbol_list in o: # visit all outer blocks
            for symbol in symbol_list:
                if symbol.name == "<Loop>":
                    flag = True
                    return
        if not flag: raise MustInLoop(ast)
        
    def visitReturn(self, ast, o):
        print("Return")
        # 'Cause the function does not have return type, we don't need to check type here. What we just need to do is that assign return_expr type to function type
        right_type = self.visit(ast.expr, o) if ast.expr else VoidType() # RHS
        for i in range(1, len(o)):
            if len(o[i]) > 0 and Utils.isFunc(o[i][0]):
                o[i][0].type = right_type
                # print("CHECK HERE", len(o), o[i][0])
                break
        
    def visitCallStmt(self, ast, o):
        flag = False
        
        for symbol in o[-1]:
            if ast.name == symbol.name and Utils.isFunc(symbol):
                flag = True
                break
        
        if not flag: Undeclared(Function(), ast.name)
        # for symbollist in o:
        #     for symbol in symbollist:
        #         print("Check here .........", symbol)
        #     print('.///', len(o))
        if flag:
            # o[0] is block containing this callstmt, o[1] is non-local (it means the function which contains this callstmt)        
            for symbol in o[1]: #TypeCannotBeInfered error for calling again this function itself  
                print("check here", symbol)
                if symbol.name == ast.name and Utils.isFunc(symbol):
                    raise TypeCannotBeInferred(ast)
            for symbol in o[-1]:
                if symbol.name == ast.name and Utils.isFunc(symbol):
                    if symbol.is_body_having == False:
                        raise NoDefinition(symbol.name)
                    break
        
        for symbol in o[-1]:
            if symbol.name == ast.name and Utils.isFunc(symbol):
                list_param = symbol.param
                args = ast.args
                
                if len(list_param) > len(args):
                    raise TypeMismatchInExpression(ast)
                elif len(args) < len(list_param):
                    raise TypeMismatchInExpression(ast)
                else:
                    for i in range(0, len(list_param)):
                        param_type = list_param[i].type # param element here is symbol
                        args_type = self.visit(ast.args[i], o)
                        
                        # May be wrong because of passing by value
                        # atomic_types = [NumberType, BoolType, StringType]                        
                        # if not (type(args_type) in atomic_types):
                        #     args_type = param_type
                        
                        # Passing by reference
                        if type(param_type) is ArrayType: # args_type is None because ast.args[i] is declared 'dynamic' -> ast.args[i] is Id
                            ast.args[i].varType = param_type
                            continue
                        # TYPE MISMATCH
                        if type(args_type) is not type(param_type):
                            raise TypeMismatchInExpression(ast)
                return symbol.type
                 
    def visitBlock(self, ast, o):
        print("From block >.............")
        o1 = [[]] + o
        # check if this block belongs to a function or not
        check_func = False
        for symbol in o1[1]:
            if Utils.isFunc(symbol):
                check_func = True
                
        if not check_func: # just a block (not a block of function), so visit stmt and decl in this block
            for stmt_decl in ast.stmt:
                self.visit(stmt_decl, o1)
        else:
            # o1: [[block],[func_name,func_param1,...],...]
            function_scope = o1[1]
            check_return_stmt = False
            # first_stmt = True
            
            for stmt_decl in ast.stmt:
                if hasattr(stmt_decl, "name"): # Vardecl
                    # print("11111")  
                    for func_component in function_scope[1:]: # FuncDecl is of outer scope, check if parameters are declared same as variables out of this function
                        if stmt_decl.name == func_component.name: 
                            raise Redeclared(Variable(),stmt_decl.name)
                # Check if encountering return statement or not
                if check_return_stmt is True and type(stmt_decl) is Return: continue
                self.visit(stmt_decl,o1)
                if type(stmt_decl) is Return:
                    check_return_stmt = True
                if type(stmt_decl) is CallStmt:
                    print("Check here!!! >>>>>>>", o1[1][0])
                    # Write TypeCannotBeInfered error for calling again this function itself 
                    if stmt_decl.name == o1[1][0].name:
                        raise TypeCannotBeInferred(stmt_decl)
                    
                # first_stmt = False
            if not check_return_stmt: # there are no return statements, func type is VoidType
                o1[1][0].type = VoidType
                
    def visitVarDecl(self, ast, o):
        print("This is from visitVarDecl")
        flag = False
        # check redeclare
        for symbol in o[0]: # vì ở dưới hàm visitProgram chúng ta khai báo biến env = [[]] + global_scope nên mỗi biến được tạo ra sẽ được thêm vào env[0] (tức là o[0])
            if symbol.name == ast.name:
                raise Redeclared(Variable(), ast.name)
          
        # check duplicate with special function
        for symbol in o[-1][:6]:
            if symbol.name == ast.name and Utils.isFunc(symbol):
                raise Redeclared(Variable(), ast.name)
        
        if not ast.varInit: 
            # print("Check here >>>>>>>>", ast.name, ast.varType)
            o[0] += [Symbol(ast.name, ast.varType, ast.modifier, ast.varInit)]
            
        else:
            init = self.visit(ast.varInit, o)
            if ast.modifier == 'var' or ast.modifier == 'dynamic':
                o[0] += [Symbol(ast.name, init, ast.modifier, None)]
                # Utils.infer(o, ast.name, init)
            elif type(ast.varType) is ArrayType and type(init) is ArrayType:
                ast.varType.size = list(map(lambda x: int(x), ast.varType.size))       
                init.size = list(map(lambda x: int(x), init.size))   
                if ast.varType.size != init.size:
                    # print(11111)
                    raise TypeMismatchInExpression(ast)
                
                if type(ast.varType.eleType) is not type(init.eleType):
                    # print(3333)
                    raise TypeMismatchInExpression(ast)
                
                if hasattr(ast.varInit, 'value'): # ArrayLiteral -> init là: [1,2,3]
                    # print(2222)
                    for expr in ast.varInit.value:
                        expr_type = self.visit(expr, o) # if expr_type has modifier, need to define at visitExpr -> it means adding Symbol(name, None, 'var' / 'dynamic', None) at visitExpr
                        # print("Check here>>>>", type(expr_type))
                        if type(expr_type) is None: # biến này đã được khai báo trước đó
                            Utils.infer(o, expr_type.name, ast.varType.eleType)
                        elif type(expr_type) is not type(ast.varType.eleType):
                            raise TypeMismatchInExpression(ast)
                o[0] += [Symbol(ast.name, ast.varType, ast.modifier, None)]
            elif type(ast.varType) is ArrayType and (init.modifier == 'var' or init.modifier == 'dynamic'): 
                Utils.infer(o, init.name, ast.varType)
                o[0] += [Symbol(ast.name, ast.varType, init.modifier, None)]
            else:
                o[0] += [Symbol(ast.name, ast.varType, ast.modifier, None)]
            
    def visitFuncDecl(self, ast, o):
        print("This is from visitFuncDecl")
        found = False
        
        for symbol in o[-1] + o[-1][:6]: # Function declaration
            # print("This is from function", symbol)
            if symbol.name == ast.name:
                if not found: found = True # ignore round 1
                else:
                    raise Redeclared(Function(),ast.name)
        
        for symbol in o[0]: # Variable declaration
            # print("This is from function", symbol)
            if symbol.name == ast.name:
                raise Redeclared(Function(),ast.name)
        
        o1 = [[Symbol(ast.name, None, None, [])]] + o
        for param in ast.param:
            self.visit(param, o1)
        check_having_body = False
        if ast.body:
            check_having_body = True
            self.visit(ast.body, o1) # after visiting body, we try to assign type of return stmt to o1[0][0].type (which is type of function)
        # for symbollist in o1:
        #     for symbol in symbollist:
        #         print("Checking symbol", symbol)
        #     print(".......")
        list_params = []
        for i in range(1, len(ast.param) + 1):
            list_params += [Symbol(o1[0][i].name, o1[0][i].type, o1[0][i].modifier, None )]
        
        o[0] += [Symbol(ast.name, o1[0][0].type, None, list_params, check_having_body)]
        # Assign func type again because in first round, we assign func type to None
        for symbol in o[-1]:
            if symbol.name == ast.name:
                symbol.type = o1[0][0].type
                symbol.is_body_having = check_having_body
                break
    
    def visitProgram(self, ast, o):
        global_scope = GetEnv(ast).visit(ast, o)
        
        # Round 2 - Visit inside body
        env = [[]] + global_scope
        for decl in ast.decl:
            self.visit(decl, env)
        
        # for func in env[0] + env[1]:
        #     print(func)    
        
        check_main_func = False
        for func in env[0]:
            # print(func.name.name == "main", func.type is VoidType, len(func.param)==0)
            if func.name.name == "main" and func.type is VoidType is VoidType and len(func.param)==0:
                check_main_func = True
                break
        
        if not check_main_func:
            raise NoEntryPoint()
        