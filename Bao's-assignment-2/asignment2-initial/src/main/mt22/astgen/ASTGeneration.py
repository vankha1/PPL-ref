# MSSV: 2012670
# Nguyễn Lê Minh Bảo


from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from functools import reduce
from AST import *



# flatten
def flatten(lst):
    return reduce(lambda prev, curr: prev + (flatten(curr) if type(curr) is list else [curr]), lst, [])



class ASTGeneration(MT22Visitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return Program(self.visit(ctx.decllist()))


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        if ctx.decllist():
            return self.visit(ctx.decl())+ self.visit(ctx.decllist())
        else:
            return self.visit(ctx.decl())


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bool_typ.
    def visitBool_typ(self, ctx:MT22Parser.Bool_typContext):
        return BooleanType()


    # Visit a parse tree produced by MT22Parser#int_typ.
    def visitInt_typ(self, ctx:MT22Parser.Int_typContext):
        return IntegerType()


    # Visit a parse tree produced by MT22Parser#float_typ.
    def visitFloat_typ(self, ctx:MT22Parser.Float_typContext):
        return FloatType()


    # Visit a parse tree produced by MT22Parser#string_typ.
    def visitString_typ(self, ctx:MT22Parser.String_typContext):
        return StringType()


    # Visit a parse tree produced by MT22Parser#void_typ.
    def visitVoid_typ(self, ctx:MT22Parser.Void_typContext):
        return VoidType()


    # Visit a parse tree produced by MT22Parser#auto_typ.
    def visitAuto_typ(self, ctx:MT22Parser.Auto_typContext):
        return AutoType()


    # Visit a parse tree produced by MT22Parser#array_typ.
    def visitArray_typ(self, ctx:MT22Parser.Array_typContext):
        dimensions = self.visit(ctx.int_lit())
        typ = self.visit(ctx.typ_of_array())
        return ArrayType(dimensions, typ)


    # Visit a parse tree produced by MT22Parser#int_lit.
    def visitInt_lit(self, ctx:MT22Parser.Int_litContext):

        if ctx.COMMA():
            return [int(ctx.DECIMAL().getText())] + self.visit(ctx.int_lit())
        else:
            return [int(ctx.DECIMAL().getText())]


    # Visit a parse tree produced by MT22Parser#typ_of_array.
    def visitTyp_of_array(self, ctx:MT22Parser.Typ_of_arrayContext):
        if ctx.bool_typ():
            return self.visit(ctx.bool_typ())
        elif ctx.int_typ():
            return self.visit(ctx.int_typ())
        elif ctx.float_typ():
            return self.visit(ctx.float_typ())
        elif ctx.string_typ():
            return self.visit(ctx.string_typ())


    # Visit a parse tree produced by MT22Parser#declare_var.
    def visitDeclare_var(self, ctx:MT22Parser.Declare_varContext):
       
        if ctx.idlit():
            ids= self.visit(ctx.idlit())
            if ctx.typ_var():
                typ=self.visit(ctx.typ_var())
                return [VarDecl(x, typ) for x in ids]
            elif ctx.array_typ():
                typ=self.visit(ctx.array_typ())
                return [VarDecl(x, typ) for x in ids]
        elif ctx.init_var():
            arr= self.visit(ctx.init_var())
            typ= arr[-1]

            ids=[]
            vals=[]
            for i in arr[:-1]:
                ids.append(i[0])
                vals.append(i[1])
            vals.reverse()
            
            result=[]
            for i in range(len(ids)):
                result.append(VarDecl(ids[i], typ,vals[i]))
            return result

        else:
            name = ctx.IDENTIFIERS().getText()
            expr = self.visit(ctx.exp())
            if ctx.typ_var():
                typ=self.visit(ctx.typ_var())
                return [VarDecl(name, typ,expr)]
            elif ctx.array_typ():
                typ=self.visit(ctx.array_typ())
                return [VarDecl(name, typ,expr)]
       
       
   


    # Visit a parse tree produced by MT22Parser#init_var.
    def visitInit_var(self, ctx:MT22Parser.Init_varContext):
        return [(ctx.IDENTIFIERS().getText(), self.visit(ctx.exp()))] + self.visit(ctx.recursive_var())


    # Visit a parse tree produced by MT22Parser#recursive_var.
    def visitRecursive_var(self, ctx:MT22Parser.Recursive_varContext):
        
        if ctx.COMMA():
            return [(ctx.IDENTIFIERS().getText(), self.visit(ctx.exp()))] + self.visit(ctx.recursive_var())
        elif ctx.typ_var(): 
            return [(ctx.IDENTIFIERS().getText(), self.visit(ctx.exp())), self.visit(ctx.typ_var())]
        elif ctx.array_typ():
            return [(ctx.IDENTIFIERS().getText(), self.visit(ctx.exp())), self.visit(ctx.array_typ())]


    # Visit a parse tree produced by MT22Parser#idlit.
    def visitIdlit(self, ctx:MT22Parser.IdlitContext):
        if ctx.COMMA():
            return [ctx.IDENTIFIERS().getText()] + self.visit(ctx.idlit())
            
        else:
            return [ctx.IDENTIFIERS().getText()]
           
            


    # Visit a parse tree produced by MT22Parser#typ_var.
    def visitTyp_var(self, ctx:MT22Parser.Typ_varContext):
        
        if ctx.int_typ():
            return self.visit(ctx.int_typ())
        elif ctx.auto_typ():
            return self.visit(ctx.auto_typ())       
        elif ctx.bool_typ():
            return self.visit(ctx.bool_typ())
        elif ctx.float_typ():
            return self.visit(ctx.float_typ())
        elif ctx.string_typ():
            return self.visit(ctx.string_typ())
       
    



    # Visit a parse tree produced by MT22Parser#declare_para.
    def visitDeclare_para(self, ctx:MT22Parser.Declare_paraContext):
        name = ctx.IDENTIFIERS().getText()
        inherit= False
        out = False
        if ctx.inherit(): inherit = True
        if ctx.out(): out = True

        if ctx.typ_var():
            typ = self.visit(ctx.typ_var())
            return ParamDecl(name, typ, out, inherit)
        elif ctx.array_typ():
            typ = self.visit(ctx.array_typ())
            return ParamDecl(name, typ, out, inherit)



    # Visit a parse tree produced by MT22Parser#inherit.
    def visitInherit(self, ctx:MT22Parser.InheritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#out.
    def visitOut(self, ctx:MT22Parser.OutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declare_func.
    def visitDeclare_func(self, ctx:MT22Parser.Declare_funcContext):
        name    = ctx.IDENTIFIERS(0).getText()
        params  = self.visit(ctx.paralit())
        inherit =  ctx.IDENTIFIERS(1).getText() if ctx.inherit() else None
        body    = self.visit(ctx.body()) 

        if ctx.typ():
            return_type = self.visit(ctx.typ())
            return [FuncDecl(name, return_type, params, inherit, body)]
        elif ctx.array_typ():
            return_type = self.visit(ctx.array_typ())
            return [FuncDecl(name, return_type, params, inherit, body)]



    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):

        if ctx.int_typ():
            return self.visit(ctx.int_typ())
        elif ctx.auto_typ():
            return self.visit(ctx.auto_typ())
        elif ctx.bool_typ():
            return self.visit(ctx.bool_typ())
        elif ctx.void_typ():
            return self.visit(ctx.void_typ())
        elif ctx.float_typ():
            return self.visit(ctx.float_typ())
        elif ctx.string_typ():
            return self.visit(ctx.string_typ())
       

    # Visit a parse tree produced by MT22Parser#paralit.
    def visitParalit(self, ctx:MT22Parser.ParalitContext):
        if ctx.paraPrime():
            return self.visit(ctx.paraPrime())
        else:
            return []


    # Visit a parse tree produced by MT22Parser#paraPrime.
    def visitParaPrime(self, ctx:MT22Parser.ParaPrimeContext):
        if ctx.COMMA():
            return [self.visit(ctx.declare_para())] + self.visit(ctx.paraPrime())
        else:
            return [self.visit(ctx.declare_para())]


    # Visit a parse tree produced by MT22Parser#body.
    def visitBody(self, ctx:MT22Parser.BodyContext): # ????
        return self.visitChildren(ctx)


       
    # Visit a parse tree produced by MT22Parser#block_stm.
    def visitBlock_stm(self, ctx:MT22Parser.Block_stmContext):
        return BlockStmt(flatten(self.visit(ctx.block_lit())))


    # Visit a parse tree produced by MT22Parser#block_lit.
    def visitBlock_lit(self, ctx:MT22Parser.Block_litContext):
        if ctx.stmt():
            return [self.visit(ctx.stmt())] + self.visit(ctx.block_lit())
        elif ctx.declare_var():
            return self.visit(ctx.declare_var()) + self.visit(ctx.block_lit())
        else : 
            return []


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        if ctx.LB() and ctx.RB():
            return ctx.LB().getText() + ctx.RB().getText()
        return self.visitChildren(ctx)       
       

    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):

        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp1(0))
        else:  
            left = self.visit(ctx.exp1(0))
            right = self.visit(ctx.exp1(1))
            op = ctx.SCOPE().getText()
            return BinExpr(op, left, right)



    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        
        if ctx.getChildCount() == 1 :
            return self.visit(ctx.exp2(0))
        else:
            left = self.visit(ctx.exp2(0))
            right = self.visit(ctx.exp2(1))
            if ctx.EQ(): 
                op = ctx.EQ().getText()
                return BinExpr(op, left, right)
            elif ctx.NEQ():
                op = ctx.NEQ().getText()
                return BinExpr(op, left, right)
            elif ctx.LT():
                op = ctx.LT().getText()
                return BinExpr(op, left, right)
            elif ctx.GT():
                op = ctx.GT().getText()
                return BinExpr(op, left, right)
            elif ctx.LTE():
                op = ctx.LTE().getText()
                return BinExpr(op, left, right)
            elif ctx.GTE():
                op = ctx.GTE().getText()
                return BinExpr(op, left, right)



    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        
        if ctx.getChildCount()  ==1:
            return self.visit(ctx.exp3())
        else:
            left = self.visit(ctx.exp2())
            right = self.visit(ctx.exp3())
            if ctx.AND(): 
                op = ctx.AND().getText()
                return BinExpr(op, left, right)
            elif ctx.OR():
                op = ctx.OR().getText()
            return BinExpr(op, left, right)
    

    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        
        if ctx.getChildCount() ==1:
            return self.visit(ctx.exp4())
        else:
            left = self.visit(ctx.exp3())
            right = self.visit(ctx.exp4())
            if ctx.ADD(): 
                op = ctx.ADD().getText()
                return BinExpr(op, left, right)
            elif ctx.SUB():
                op = ctx.SUB().getText()
                return BinExpr(op, left, right)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):

        if ctx.getChildCount() ==1:
            return self.visit(ctx.exp5())
        else:
            left = self.visit(ctx.exp4())
            right = self.visit(ctx.exp5())
            if ctx.MUL(): 
                op = ctx.MUL().getText()
                return BinExpr(op, left, right)
            elif ctx.DIV():
                op = ctx.DIV().getText()
                return BinExpr(op, left, right)
            elif ctx.MOD():
                op = ctx.MOD().getText()
                return BinExpr(op, left, right)
  

    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        if ctx.NOT():
            op = ctx.NOT().getText()
            val = self.visit(ctx.exp5())
            return UnExpr(op, val)
        else:
            return self.visit(ctx.exp6())


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        if ctx.SUB():
            op = ctx.SUB().getText()
            val = self.visit(ctx.exp6())
            return UnExpr(op, val)
        else:
            return self.visit(ctx.exp7())


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        if ctx.LBK() and ctx.LBK():
            name = ctx.exp7().getText()
            cell = self.visit(ctx.list_exp())
            return ArrayCell(name, cell)
        else:
            return self.visit(ctx.exp8())


    # Visit a parse tree produced by MT22Parser#exp8.
    def visitExp8(self, ctx:MT22Parser.Exp8Context):
        if ctx.IDENTIFIERS():
            return Id(ctx.IDENTIFIERS().getText())
        elif ctx.DECIMAL():
            return IntegerLit(int(ctx.DECIMAL().getText()))
        elif ctx.REAL():
            if ctx.REAL().getText()[0] == '.' and (ctx.REAL().getText()[1] == 'e' or ctx.REAL().getText()[1] == 'E') :
                return FloatLit(0.0)
            return FloatLit(float(ctx.REAL().getText()))
        elif ctx.STRINGLIT():
            return StringLit(str(ctx.STRINGLIT().getText()))
        elif ctx.FALSE():
            return BooleanLit(False)
        elif ctx.TRUE():
            return BooleanLit(True)
      
        elif ctx.fun_call():
            return self.visit(ctx.fun_call())
        elif ctx.array():
            return self.visit(ctx.array())
        else:
            return self.visit(ctx.exp())


    # Visit a parse tree produced by MT22Parser#list_exp.
    def visitList_exp(self, ctx:MT22Parser.List_expContext):
        if ctx.COMMA():
            return [self.visit(ctx.exp())] + self.visit(ctx.list_exp())
        else:
            return [self.visit(ctx.exp())]


    # Visit a parse tree produced by MT22Parser#fun_call.
    def visitFun_call(self, ctx:MT22Parser.Fun_callContext):
        if ctx.LP() and ctx.LP() :
            name = ctx.IDENTIFIERS().getText()
            args = self.visit(ctx.para_fun())

            return FuncCall(name, args)
        else:
            return self.visit(ctx.special_function())


    # Visit a parse tree produced by MT22Parser#para_fun.
    def visitPara_fun(self, ctx:MT22Parser.Para_funContext):
        if ctx.getChildCount()  == 0:
            return []
        else:
            return self.visit(ctx.para_fun_Prime())



    # Visit a parse tree produced by MT22Parser#para_fun_Prime.
    def visitPara_fun_Prime(self, ctx:MT22Parser.Para_fun_PrimeContext):
        if ctx.getChildCount()  == 1:
            return [self.visit(ctx.exp())]
        else :
            return [self.visit(ctx.exp())] + self.visit(ctx.para_fun_Prime())
       
        

    # Visit a parse tree produced by MT22Parser#ass_stm.
    def visitAss_stm(self, ctx:MT22Parser.Ass_stmContext):
        return  AssignStmt(self.visit(ctx.exp(0)),self.visit(ctx.exp(1)))


    # Visit a parse tree produced by MT22Parser#if_stm.
    def visitIf_stm(self, ctx:MT22Parser.If_stmContext):
        if ctx.ELSE():
            return IfStmt(self.visit(ctx.exp()), self.visit(ctx.body(0)), self.visit(ctx.body(1))) 
        else:
            return IfStmt(self.visit(ctx.exp()), self.visit(ctx.body(0)))


    # Visit a parse tree produced by MT22Parser#for_stm.
    def visitFor_stm(self, ctx:MT22Parser.For_stmContext):
        
        return ForStmt( self.visit(ctx.init_exp()), self.visit(ctx.exp(0)), self.visit(ctx.exp(1)),
                       self.visit(ctx.body()))


    # Visit a parse tree produced by MT22Parser#init_exp.
    def visitInit_exp(self, ctx:MT22Parser.Init_expContext):

        return AssignStmt(Id(ctx.IDENTIFIERS().getText()),self.visit(ctx.exp()))

    # Visit a parse tree produced by MT22Parser#while_stm.
    def visitWhile_stm(self, ctx:MT22Parser.While_stmContext):
        return WhileStmt(self.visit(ctx.exp()), self.visit(ctx.body()))


    # Visit a parse tree produced by MT22Parser#do_wh_stm.
    def visitDo_wh_stm(self, ctx:MT22Parser.Do_wh_stmContext):
        return DoWhileStmt(self.visit(ctx.exp()), self.visit(ctx.body()))


    # Visit a parse tree produced by MT22Parser#break_stm.
    def visitBreak_stm(self, ctx:MT22Parser.Break_stmContext):
        return BreakStmt()


    # Visit a parse tree produced by MT22Parser#continue_stm.
    def visitContinue_stm(self, ctx:MT22Parser.Continue_stmContext):
        return ContinueStmt()


    # Visit a parse tree produced by MT22Parser#return_stm.
    def visitReturn_stm(self, ctx:MT22Parser.Return_stmContext):
        
        if ctx.exp():  
            expr = self.visit(ctx.exp())
            return ReturnStmt(expr)
        else:
            return ReturnStmt(None)
        


    # Visit a parse tree produced by MT22Parser#call_stm.
    def visitCall_stm(self, ctx:MT22Parser.Call_stmContext):
        fun_call = self.visit(ctx.fun_call())
        name = fun_call.name
        args= fun_call.args
        return CallStmt(name, args)

    # Visit a parse tree produced by MT22Parser#seprcial_function.
    def visitSpecial_function(self, ctx:MT22Parser.Special_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readInteger.
    def visitReadInteger(self, ctx:MT22Parser.ReadIntegerContext):
        name = "readInteger"
        args= []
        return FuncCall(name,args)


    # Visit a parse tree produced by MT22Parser#printInteger.
    def visitPrintInteger(self, ctx:MT22Parser.PrintIntegerContext):
        name = "printInteger"
        args=  [self.visit(ctx.exp())]
        return FuncCall(name,args)

    # Visit a parse tree produced by MT22Parser#readFloat.
    def visitReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        name = "readFloat"
        args= []
        return FuncCall(name,args)


    # Visit a parse tree produced by MT22Parser#printFloat.
    def visitWriteFloat(self, ctx:MT22Parser.WriteFloatContext):
        name = "writeFloat"
        args=  [self.visit(ctx.exp())]
        return FuncCall(name,args)


    # Visit a parse tree produced by MT22Parser#readBoolean.
    def visitReadBoolean(self, ctx:MT22Parser.ReadBooleanContext):
        name = "readBoolean"
        args= []
        return FuncCall(name,args)


    # Visit a parse tree produced by MT22Parser#printBoolean.
    def visitPrintBoolean(self, ctx:MT22Parser.PrintBooleanContext):
        name = "printBoolean"
        args=  [self.visit(ctx.exp())]
        return FuncCall(name,args)


    # Visit a parse tree produced by MT22Parser#readString.
    def visitReadString(self, ctx:MT22Parser.ReadStringContext):
        name = "readString"
        args= []
        return FuncCall(name,args)


    # Visit a parse tree produced by MT22Parser#printString.
    def visitPrintString(self, ctx:MT22Parser.PrintStringContext):
        name = "printString"
        args=  [self.visit(ctx.exp())]
        return FuncCall(name,args)


    # Visit a parse tree produced by MT22Parser#suPer.
    def visitSuPer(self, ctx:MT22Parser.SuPerContext):
        name = "super"
        if ctx.list_exp():
            args=  self.visit(ctx.list_exp())
            return FuncCall(name,args)
        else:
            args=[]
            return FuncCall(name,args)


    # Visit a parse tree produced by MT22Parser#preventDefault.
    def visitPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        name= "preventDefault"
        args=[]
        return FuncCall(name,args)


    # Visit a parse tree produced by MT22Parser#array.
    def visitArray(self, ctx:MT22Parser.ArrayContext):
        
        if ctx.getChildCount() == 2:
            return ArrayLit([])
        return ArrayLit(self.visit(ctx.element_array()))


    # Visit a parse tree produced by MT22Parser#element_array.
    def visitElement_array(self, ctx:MT22Parser.Element_arrayContext):

        if ctx.COMMA():
            return [self.visit(ctx.exp())] + self.visit(ctx.element_array())
        return [self.visit(ctx.exp())]