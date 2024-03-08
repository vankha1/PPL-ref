from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import *

from main.mt22.utils.AST import BooleanType, FloatType, IntegerType, StringType, VoidType


class Utils:
    def infer(env, name, typ,funcName=None,isParam=False):
        if isParam:
            for ele in env[-1]:
                if ele.name == funcName:
                    for eleParam in ele.param:
                        if eleParam.name == name:
                            eleParam.typ =typ
                            return eleParam
        else:
            for symbolList in env:
                for symbol in symbolList:
                    if symbol.name == name and (symbol.kind=="FUNCDECL" or symbol.kind=="PARAM" or symbol.kind=="VARDECL"):
                        symbol.type = typ
                        return symbol.type

class SymbolVar:
    def __init__(self, name,type,ast,kind):
        self.name = name
        self.type = type
        self.ast = ast # giữ nguyên cây của hàm
        self.kind = kind

class SymbolFunc:
    def __init__(self,name,type,param,parent,env,ast,kind):
        self.name = name
        self.type = type
        self.param = param
        self.parent = parent
        self.env = env
        self.ast = ast # giữ nguyên cây của hàm
        self.kind = kind

class SymbolStmt:
    def __init__(self,name,kind,inherit=None):
        self.kind = kind
        self.name = name
        self.inherit = inherit

class GetEnv(Visitor):

    def __init__(self, ast):
        self.ast = ast
    
    def check(self):
        return self.visitProgram(self.ast,[])
    
    def global_env():
        global_env= [
            SymbolFunc("readInteger",IntegerType(),None,"",None,None,"SPECICALFUNC"),
            SymbolFunc("printInteger",VoidType(),None,"",None,None,"SPECICALFUNC"),
            SymbolFunc("readFloat",FloatType(),None,"",None,None,"SPECICALFUNC"),
            SymbolFunc("printFloat",VoidType(),None,"",None,None,"SPECICALFUNC"),
            SymbolFunc("readBoolean",BooleanType(),None,"",None,None,"SPECICALFUNC"),
            SymbolFunc("printBoolean",VoidType(),None,"",None,None,"SPECICALFUNC"),
            SymbolFunc("readString",StringType(),None,"",None,None,"SPECICALFUNC"),
            SymbolFunc("printString",VoidType(),None,"",None,None,"SPECICALFUNC"),
            SymbolFunc("super",VoidType(),None,"",None,None,"SPECICALFUNC"),
            SymbolFunc("preventDefault",VoidType(),None,"",None,None,"SPECICALFUNC"),
        ]
        return global_env
    
   
    # VarDecl: name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast, param):
               
        param[0] += [SymbolVar(ast.name,ast.typ,ast,'VARDECL')] # 1: name , 2: type, 3: kind 
        return param
    

    # ParamDecl: name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, param):         
        return SymbolVar(ast.name, ast.typ,None,'PARAM')
        

    # FuncDecl: name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, param): 
    
        env= [[]] + param

        for decl in ast.params:
            env[0]+= [self.visit(decl,env)]
        block = ast.body
        for decl in block.body:
            string = str(decl)
            if string[0:7] == "VarDecl":
                env = self.visit(decl,env)
                        
        param[0] += [SymbolFunc(ast.name,ast.return_type,ast.params,ast.inherit,[env[0]],ast,"FUNCDECL")]
      
        return param

    # Program: decls:List[Decl] (decl: varDecl or funcDecl)  
    def visitProgram(self, ast, param):
        
        param=[GetEnv.global_env()] # param dau la thong tin cuc bo, param cuoi thong tin so bo
        
        for decl in ast.decls:
            param = self.visit(decl,param)  
        
        return param

########################################################################################################      

class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        self.InLoop=[]
        self.func=None
      
    
    def check(self):
        return self.visitProgram(self.ast,[])

    def checkNoneSuper(self,param):
        # check inherit super
        

        funcInherit= param[0][0].inherit        
        if len(param[0])==1 and funcInherit is not None: # có hàm cha
            for func in param[-1]:
                if func.name == funcInherit and func.kind == "FUNCDECL":
                    if len(func.param) >0: # TH: không có super nên super được gọi ngầm định
                        raise InvalidStatementInFunction(self.func.name) # khúc này có thể có stmt kh ???

    def checkExitVar(ast,env):
        
        flag=True
        count = 0
        lst=[]
        for ele in env:
            lst+=[ele]
            if ele.ast is ast: 
                flag=False
                break
        for ele in lst:
            if ele.name == ast.name: 
                count+=1
                if count == 2: break


        if flag: 
            raise Undeclared(Identifier(),ast.name)
        elif len(lst)==2 and lst[0]=="VARDECL" and lst[1]=="FUNCDECL":
            raise Redeclared("Function",ast.name)
        elif count > 1: raise Redeclared("Variable",ast.name)
        elif count == 1: return

    
    def checkExitPara(name,env):
        count=0
        for ele in env:
            if ele.name == name : count+=1
        
        if count > 1: raise Redeclared("Parameter",name)
        elif count == 1: return  

    def checkExitFunc(ast,env):
        flag=True
        count = 0
        lst=[]
        for ele in env:
            lst+=[ele]
            if ele.ast is ast: 
                flag=False
                break
        for ele in lst:
            if ele.name == ast.name: 
                count+=1
                if count == 2: break


        if flag: 
            raise Undeclared(Function(),ast.name)
        elif len(lst)==2 and lst[0]=="VARDECL" and lst[1]=="FUNCDECL":
            raise Redeclared("Variable",ast.name)
        elif count > 1: raise Redeclared("Function",ast.name)
        elif count == 1: return

    def checkExitFuncInherit(name,env):
        flag = True
        for ele in env:
            if ele.name == name : 
                return

        if flag: 
            raise Undeclared(Function(),name)
    def checkSpecicalFunc(self,ast,func,param):

        if ast.name =="printInteger":
            typeArg = self.visit(ast.args[0],param)
            if type(typeArg) is not IntegerType:
                raise TypeMismatchInStatement(ast)
        elif ast.name =="printFloat":
            typeArg = self.visit(ast.args[0],param)
            if type(typeArg) not in [FloatType, IntegerType]:
                raise TypeMismatchInStatement(ast)
        elif ast.name =="printBoolean":
            typeArg = self.visit(ast.args[0],param)
            if type(typeArg) is not BooleanType:
                raise TypeMismatchInStatement(ast)
        elif ast.name =="printString":
            typeArg = self.visit(ast.args[0],param)
            if type(typeArg) is not StringType:
                raise TypeMismatchInStatement(ast)
        return func.type
    
    def inferParam(ID,inferType,param):
        if "Id" in str(ID):
            for idList in param:
                for id in idList:
                    if id.name == ID.name and id.kind =="PARAM":
                        Utils.infer(param,ID.name,inferType,param[0][0].name,True)


    def visitIntegerType(self, ast, param): 
        pass
    def visitFloatType(self, ast, param): 
        pass
    def visitBooleanType(self, ast, param): 
        pass
    def visitStringType(self, ast, param): 
        pass
    def visitArrayType(self, ast, param): 
        pass
    def visitAutoType(self, ast, param): 
        pass
    def visitVoidType(self, ast, param): 
        pass

    # BinExpr: op: str, left: Expr, right: Expr
    def visitBinExpr(self, ast, param): 
        left = self.visit(ast.left, param)
        right = self.visit(ast.right, param)

        if ast.op == '%' :
            if type(left) is IntegerType and type(right) is IntegerType:
                return IntegerType()
            if type(left) is AutoType:
                StaticChecker.inferParam(ast.left,right,param)
                return Utils.infer(param,ast.left.name,right)
            if type(right) is AutoType:
                StaticChecker.inferParam(ast.right,left,param)
                return Utils.infer(param,ast.right.name,left)
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['+', '-', '*','/']:
            if type(left) is IntegerType and type(right) is IntegerType:
                return IntegerType()
            if  type(left) in [FloatType, IntegerType] and type(right) in [FloatType, IntegerType]:
                return FloatType()
            if type(left) is AutoType:
                StaticChecker.inferParam(ast.left,right,param)
                return Utils.infer(param,ast.left.name,right)
            if type(right) is AutoType:
                StaticChecker.inferParam(ast.right,left,param)
                return Utils.infer(param,ast.right.name,left)
            raise TypeMismatchInExpression(ast)
          

        if ast.op in ['&&', '||']:
            if type(left) is BooleanType and type(right) is BooleanType:
                return  BooleanType()
            if type(left) is AutoType:
                StaticChecker.inferParam(ast.left,right,param)
                return Utils.infer(param,ast.left.name,right)
            if type(right) is AutoType:
                StaticChecker.inferParam(ast.right,left,param)
                return Utils.infer(param,ast.right.name,left)
            raise TypeMismatchInExpression(ast)
        
        if ast.op == '::':
            if type(left) is StringType and type(right) is StringType:
                return  StringType()
            if type(left) is AutoType:
                StaticChecker.inferParam(ast.left,right,param)
                return Utils.infer(param,ast.left.name,right)
            if type(right) is AutoType:
                StaticChecker.inferParam(ast.right,left,param)
                return Utils.infer(param,ast.right.name,left)
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['==', '!=']:
            if type(left) in [IntegerType, BooleanType] and type(right) in [IntegerType, BooleanType] :
                return BooleanType()
            if type(left) is AutoType:
                StaticChecker.inferParam(ast.left,right,param)
                Utils.infer(param,ast.left.name,right)
                return BooleanType()    
            if type(right) is AutoType:
                StaticChecker.inferParam(ast.right,left,param)
                Utils.infer(param,ast.right.name,left)
                return BooleanType()  
            
            raise TypeMismatchInExpression(ast)
        
        if ast.op in ['>', '<', '>=', '<=']:
           
            
            if  type(left) in [FloatType, IntegerType] and type(right) in [FloatType, IntegerType]:
                return BooleanType()
            if type(left) is AutoType:
                StaticChecker.inferParam(ast.left,right,param)
                Utils.infer(param,ast.left.name,right)
                return BooleanType()
            if type(right) is AutoType:
                StaticChecker.inferParam(ast.right,left,param)
                Utils.infer(param,ast.right.name,left)
                return BooleanType()
            raise TypeMismatchInExpression(ast)
        

    # UnExpr: op: str, val: Expr
    def visitUnExpr(self, ast, param): 
        valType = self.visit(ast.val, param)

        if ast.op == '-':
            if type(valType) is IntegerType:
                return IntegerType()
            if type(valType) is FloatType:
                return FloatType()
            raise TypeMismatchInExpression(ast)
        
        if ast.op == '!' and type(valType) is BooleanType:
            return BooleanType()
        else: 
            raise TypeMismatchInExpression(ast)
        

    # Id: name: str
    def visitId(self, ast, param): 
        for idList in param:
            for id in idList:
                if id.name == ast.name:
                    return id.type
        
        

        raise Undeclared(Identifier(), ast.name)
    
        #raise  Undeclared(Function(), <function-name>) 


    # ArrayCell: name: str, cell: List[Expr]
    def visitArrayCell(self, ast, param):
        
        for ele1 in param:
            for ele2 in ele1:
                if ele2.name == ast.name:
                    nameType = ele2.type
                   
                    if type(nameType) is not ArrayType:
                        raise TypeMismatchInExpression(ast)
                    
                    if len(nameType.dimensions) < len(ast.cell):
                        raise TypeMismatchInExpression(ast) 
                    
                    for mem in ast.cell:
                        memType = self.visit(mem, param)
                        if type(memType) is not IntegerType:    
                            raise TypeMismatchInExpression(ast)
                    
                    if len(nameType.dimensions) == len(ast.cell):
                        return nameType.typ
                    elif len(nameType.dimensions) > len(ast.cell):
                        return nameType
        
        raise Undeclared(Identifier(), ast.name) #???

    # IntegerLit: val:int
    def visitIntegerLit(self, ast, param): 
        return IntegerType()
    # FloatLit:  val: float
    def visitFloatLit(self, ast, param): 
        return FloatType()
    # StringLit: val: str
    def visitStringLit(self, ast, param): 
        return StringType()
    # BooleanLit: val: bool
    def visitBooleanLit(self, ast, param): 
        return BooleanType()
    

    # ArrayLit: explist: List[Expr]
    def visitArrayLit(self,ast,param):
        firstType = self.visit(ast.explist[0],param)
        
        if type(firstType) not in [IntegerType, BooleanType, StringType, FloatType,ArrayType]:
            #raise IllegalArrayLiteral(ast)
            return -1
        
        for mem in ast.explist:
         
            memType = self.visit(mem,param)
           
            if type(memType) is ArrayType and type(firstType) is ArrayType:
                if type(memType.typ) is not type(firstType.typ) or memType.dimensions != firstType.dimensions:
                    #raise IllegalArrayLiteral(ast)
                    return -1
            if type(memType) is not type(firstType):
                #raise IllegalArrayLiteral(ast)
                return -1
        if type(firstType) is ArrayType:
            dimension = [len(ast.explist)] + firstType.dimensions
            return  ArrayType(dimension,firstType.typ)
        return ArrayType([len(ast.explist)],firstType)

    # FuncCall: name: str, args: List[Expr]
    def visitFuncCall(self, ast, param):
       
        for func in param[-1]:
            if  func.name == ast.name and func.kind == "SPECICALFUNC":
                return  self.checkSpecicalFunc(ast,func, param)
            elif func.name == ast.name and func.kind == "FUNCDECL":

                if type(func.type) is VoidType:
                    raise TypeMismatchInExpression(ast)
                
                funcParam = func.param
                length1 = len(funcParam) 
                length2 = len(ast.args)

                if length1 != length2:
                    raise  TypeMismatchInExpression(ast) #???
                
               
                for i  in range(0,length1):
                    eleParam=funcParam[i].typ
                    eleArg= self.visit(ast.args[i],param)
                    if type(eleParam) is FloatType and type(eleArg) is IntegerType:
                        continue
                    if type(eleParam) is AutoType:
                        Utils.infer(param,funcParam[i].name,eleArg,ast.name,True)
                    elif type(eleParam) is not type (eleArg):
                        raise TypeMismatchInExpression(ast)
                
                return func.type
        raise Undeclared(Function(),ast.name)

    # AssignStmt: lhs: LHS, rhs: Expr
    def visitAssignStmt(self, ast, param):
        self.checkNoneSuper(param)
        
        
        nameFunc= param[0][0].name

        for ele in param[-1]:
            if ele.name == nameFunc:
                lstParams = ele.param
                n = len(lstParams)
                for i in range(0,n):
                    if type(param[-2][i].type) is AutoType:
                        param[-2][i].type = lstParams[i].typ 

        right = self.visit(ast.rhs,param)
        left = self.visit(ast.lhs,param)
       
        if type(right) is AutoType:
            right = self.visit(ast.rhs,param)
            if type(right) is AutoType:
              
                Utils.infer(param,ast.rhs.name,left)
                param[0] +=[SymbolStmt(None,'ASSIGNSMTMT')]
                return   

        if type(left) is AutoType:
            left = self.visit(ast.lhs,param)
            if type(left) is AutoType:
               
                Utils.infer(param,ast.lhs.name,right)
                param[0] +=[SymbolStmt(None,'ASSIGNSMTMT')]
                return
      


        if type(left) in [VoidType, ArrayType]:
            raise TypeMismatchInStatement(ast)
        if type(left) is FloatType and type(right) is IntegerType:
            param[0] +=[SymbolStmt(None,'ASSIGNSMTMT')]
            return
        if type(right) != type(left):
            raise TypeMismatchInStatement(ast)

        param[0] +=[SymbolStmt(None,'ASSIGNSMTMT')]
            
        

    # BlockStmt: body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast, param): 

        n= len(param[0])


        local=[] # biến local trong blockstmt
        for stmt in ast.body:
            string = str(stmt)
            if string[0:7] == "VarDecl":
                local += [SymbolVar(stmt.name,stmt.typ,stmt,'VARDECL')]

       
        param.insert(1,local) # cộng thêm block


        for stmt in ast.body:
            self.visit(stmt,param)
   

        param[0]=param[0][0:n]
                
        param.pop(1) # xóa đi block
        
        
        
        
       

    # IfStmt: cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast, param):
        self.checkNoneSuper(param)
        
        
        condition = self.visit(ast.cond, param)
        if type(condition) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.tstmt, param)

        if ast.fstmt is not None:
            self.visit(ast.fstmt, param)

        param[0] +=[SymbolStmt(None,'IFSMTMT')]
    # ForStmt: init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast, param):
        self.checkNoneSuper(param)
        

        self.InLoop.append(True) # check break...


        if type(self.visit(ast.init.lhs,param)) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.init,param)
        
        condition = self.visit(ast.cond, param)
        if type(condition) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        
        update = self.visit(ast.upd, param)
        if type(update) is not IntegerType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.stmt,param)
        
        

        param[0] +=[SymbolStmt(None,'FORSMTMT')]




        self.InLoop.pop() # check break...

    # WhileStmt: cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast, param):
        self.checkNoneSuper(param)
        

        self.InLoop.append(True) # check break...

        condition = self.visit(ast.cond, param)
        if type(condition) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        self.visit(ast.stmt, param)

        param[0] +=[SymbolStmt(None,'WHILESMTMT')]

        self.InLoop.pop() # check break...
        
    # DoWhileStmt: cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast, param):
        self.checkNoneSuper(param)
        

        self.InLoop.append(True) # check break...

        condition = self.visit(ast.cond, param)
        if type(condition) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        
        self.visit(ast.stmt, param)
        param[0] +=[SymbolStmt(None,'DOWHILESMTMT')]

        self.InLoop.pop() # check break...

    # BreakStmt: 
    def visitBreakStmt(self, ast, param):
        self.checkNoneSuper(param)
        

        if len(self.InLoop)==0: 
            raise MustInLoop(ast)
    # ContinueStmt: 
    def visitContinueStmt(self, ast, param):
        self.checkNoneSuper(param)
        


        if len(self.InLoop)==0: 
            raise MustInLoop(ast)
    # ReturnStmt: expr: Expr or None = None
    def visitReturnStmt(self, ast, param):
        self.checkNoneSuper(param)
        


        nameFunc = param[0][0].name
        for ele1 in param:
            for ele2 in ele1:
                if ele2.kind == "FUNCDECL" and ele2.name == nameFunc:
                    if ast.expr is not None:
                        returnType =self.visit(ast.expr,param)
                        if type(ele2.type) is AutoType:
                            Utils.infer(param,ele2.name,returnType)
                            param[0] +=[SymbolStmt(None,'RETURNSTMT')]
                            return returnType
                        if type(returnType) is AutoType:
                            Utils.infer(param,ast.expr.name,ele2.type)
                            param[0] +=[SymbolStmt(None,'RETURNSTMT')]
                            return returnType
                        if type(ele2.type) is FloatType and  type(returnType) is IntegerType:
                            param[0] +=[SymbolStmt(None,'RETURNSTMT')]
                            return FloatType()
                        if type(ele2.type) is not type(returnType):
                            raise TypeMismatchInStatement(ast)
                        param[0] +=[SymbolStmt(None,'RETURNSTMT')]
                        return returnType
                    else:
              
                        param[0] +=[SymbolStmt(None,'RETURNSTMT')]
                       
                        return 
                    
                    
                        
   
               
    # CallStmt: name: str, args: List[Expr]
    def visitCallStmt(self, ast, param): 
        

        
        # check inherit super
        funcInherit= param[0][0].inherit
        if (ast.name == 'super' or ast.name =="preventDefault") and len(param[0])==1 and funcInherit is None: # gọi super() nhưng kh có hàm cha
            raise InvalidStatementInFunction(param[0][0].name)
        

        if len(param[0])==1 and funcInherit is not None: # có hàm cha
           
            for func in param[-1]:
                if func.name == funcInherit and func.kind == "FUNCDECL":
                    if ast.name == 'super': # TH: gọi super
                        
                        funcParam = func.param
                        length1 = len(funcParam) 
                        length2 = len(ast.args)

                        if length2 > length1:
                            raise  TypeMismatchInExpression(ast.args[length1])
                        elif length2 < length1:
                            raise  TypeMismatchInExpression("")

                        
                    
                        for i  in range(0,length1):
                            eleParam=funcParam[i].typ
                            eleArg= self.visit(ast.args[i],param)
                        
                            if type(eleParam) is AutoType:
                               Utils.infer(param,funcParam[i].name,eleArg,ast.name,True)
                            if type(eleParam) is FloatType and type(eleArg) is IntegerType:
                                continue
                            if type(eleParam) is not type (eleArg):
                                raise TypeMismatchInExpression(ast.args[i])
                        
                        param[0]+=[SymbolStmt(None,"CALLSTMT")]
                        return
                    else: # TH: không có super nên super được gọi ngầm định nhưng callStmt hiện tại kh là preventDefault
    
                        if ast.name != "preventDefault" and len(func.param) >0:
                            raise TypeMismatchInExpression(ast) # khúc này có thể có stmt kh
                             
        
       

        # check call stmt bình thường
        for func in param[-1]:
            if  func.name == ast.name and func.kind == "SPECICALFUNC": # check call stmt special function
                param[0]+=[SymbolStmt(None,"CALLSTMT")]
                return  self.checkSpecicalFunc(ast,func, param)
            elif func.name == ast.name and func.kind == "FUNCDECL": #or func.kind == "SPECICALFUNC":
                
                if type(func.type) is AutoType:
                    Utils.infer(param,ast.name,VoidType())
      
                funcParam = func.param
               
                length1 = len(funcParam)  #if funcParam is not None else 0 
                length2 = len(ast.args) #if ast.args is not None else 0

                if length1 != length2:
                    raise  TypeMismatchInExpression(ast) #???
                
               
                for i  in range(0,length1):
                    eleParam=funcParam[i].typ
                    eleArg= self.visit(ast.args[i],param)
                   
                    if type(eleParam) is AutoType:
                        Utils.infer(param,funcParam[i].name,eleArg,ast.name,True)
                    elif type(eleParam) is FloatType and type(eleArg) is IntegerType:
                        continue
                    elif type(eleParam) is not type (eleArg):
                        raise TypeMismatchInStatement(ast)
                
                param[0]+=[SymbolStmt(None,"CALLSTMT")]
                return
                         
        raise Undeclared(Function(),ast.name)

    # VarDecl: name: str, typ: Type, init: Expr or None = None
    def visitVarDecl(self, ast, param):
        # param[1] chứa biến cục bộ của thân hàm
        # param[0] chứa biến toàn cục

          
        env = param[1] if len(param)>1 else param[0] 

        

        StaticChecker.checkExitVar(ast,env)  
        

        if type(ast.typ) is AutoType: 
            if ast.init is not None:
                initType = self.visit(ast.init,param)
                Utils.infer(param,ast.name,initType)
            else: 
                raise Invalid(Variable(), ast.name)
        elif type(ast.typ) is ArrayType: 
            if ast.init is not None:
                initType = self.visit(ast.init,param)
               
                if type(initType) is int: 
                    raise IllegalArrayLiteral(ast.init)
             
                if type(initType) is not ArrayType:
                    raise TypeMismatchInVarDecl(ast)
              
                string = str(ast.init)
                if string[0:8] == "ArrayLit" and (type(ast.typ.typ) is not type(initType.typ)or ast.typ.dimensions != initType.dimensions):
                    raise TypeMismatchInVarDecl(ast)
                elif type(ast.typ.typ) is not type(initType.typ): 
                    raise TypeMismatchInVarDecl(ast)
        else:
         
            if ast.init is not None:
                initType = self.visit(ast.init,param)
                if type(initType) is AutoType and "FuncCall" in str(ast.init):
                    Utils.infer(param,ast.init.name,ast.typ)
                    return
                elif type(initType) is AutoType :

                    Utils.infer(param,ast.init.name,ast.typ)
                    return
                if type(ast.typ) is FloatType and type(initType) is IntegerType:  
                    param[0] += [SymbolVar(ast.name,ast.typ,ast,'VARDECL')] # 1: name , 2: type, 3: kind       
                    return 
    
                elif  type(initType) != type(ast.typ):
                
                    raise TypeMismatchInVarDecl(ast) 

    # ParamDecl: name: str, typ: Type, out: bool = False, inherit: bool = False
    def visitParamDecl(self, ast, param): 
        StaticChecker.checkExitPara(ast.name,param)
        

    # FuncDecl: name: str, return_type: Type, params: List[ParamDecl], inherit: str or None, body: BlockStmt
    def visitFuncDecl(self, ast, param): # khó ở chỗ xử lý môi trường cục bộ tham số, môi trường cụ bộ inherit
        self.func =ast
        # check error redeclared function
        StaticChecker.checkExitFunc(ast,param[0])


        # xử lý để lấy biến môi trường inherit từ hàm cha
        envInherit=[]
        stop = ast.body.body
        # kiểm tra nếu là hàm preventDefault 
        # 1. Không có preventDefault lấy tham số inherit từ hàm cha
        if (len(stop)>0 and "preventDefault" not in str(stop[0])) and  ast.inherit is not None:
            flag=True
            for decl in param[0]:
                if decl.name == ast.inherit:
                    flag = False

                    for eleParam in decl.param: # check error tham số hàm cha
                        self.visit(eleParam,decl.env[0][0:len(decl.param)])

                    for eleParam in decl.param:
                        if eleParam.inherit:
                            envInherit+= [SymbolVar(eleParam.name,eleParam.typ,None,"PARAMINHERIT")]

                    break
        
            if flag: raise Undeclared(Function(),ast.inherit)
            env =[[SymbolStmt(ast.name,None,ast.inherit)]]

        elif  len(stop)==0  and  ast.inherit is not None:
          
            StaticChecker.checkExitFuncInherit(ast.inherit,param[0])
            for decl in param[0]:
                if decl.name == ast.inherit and decl.kind =="FUNCDECL":
                    for eleParam in decl.param: # check error tham số hàm cha
                        self.visit(eleParam,decl.env[0][0:len(decl.param)])

            env =[[SymbolStmt(ast.name,None,ast.inherit)]]
        # 2. Có preventDefault không lấy tham số inherit từ hàm cha  
        elif (len(stop)>0 and "preventDefault" in str(stop[0]) and ast.inherit is not None ): 
            env =[[SymbolStmt(ast.name,None,ast.inherit)]]
        # 3. Không kế thừa từ hàm cha
        else : env =[[SymbolStmt(ast.name,None)]]

        
        # lấy biến môi trường của hàm hiện tại và xử lý lỗi inherit
        for ele in param[0]:
            if ele.kind == "FUNCDECL" and ele.name == ast.name:
                #check error các tham số của hàm
                for eleParam in ast.params:
                    self.visit(eleParam,ele.env[0][0:len(ast.params)])

                nameInherits = [i.name for i in envInherit]
                # check error từ các tham số inherit
                for eleParam in ele.env[0]:
                    if eleParam.kind == "PARAM" and eleParam.name in nameInherits: 
                        raise Invalid(Parameter(), eleParam.name)
                    if eleParam.kind == "VARDECL" and eleParam.name in nameInherits: 
                        raise Redeclared("Variable",eleParam.name)
                                    

                envLocal = envInherit + ele.env[0]
                env += [envLocal] # cộng môi trường cục bộ của hàm
               
        env += param # cộng thêm môi trường toàn cục 

        block = ast.body

        if ast.inherit is not None and len(block.body) ==0:
            self.checkNoneSuper(env)
        for decl in block.body:
            self.visit(decl,env)

    # Program: decls:List[Decl] (decl: varDecl or funcDecl)  
    def visitProgram(self, ast, param): 
        
        param= GetEnv(ast).visit(ast,param) # param dau la thong tin cuc bo, param cuoi thong tin so bo 
        
        for decl in ast.decls:
            self.visit(decl,param)

        flag = True
 
        for ele1 in param:
            for ele2 in ele1:
                if ele2.kind =="FUNCDECL":
                    if ele2.name == "main" and type(ele2.type) is VoidType and len(ele2.param) == 0 :
                        flag= False
                        break
        
        if flag: raise NoEntryPoint()   
        return ""

# param[0] : chứa tên hàm, và các list stmt
# param[1]: chứa các tham số inherit, tham số của hàm , biến cục bộ
# param[2]: chứa tên các hàm đặc biêt, các khai báo biến và các khai báo hàm
                    
        

       
        
       

       

