# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bool_typ.
    def visitBool_typ(self, ctx:MT22Parser.Bool_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_typ.
    def visitInt_typ(self, ctx:MT22Parser.Int_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#float_typ.
    def visitFloat_typ(self, ctx:MT22Parser.Float_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_typ.
    def visitString_typ(self, ctx:MT22Parser.String_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#void_typ.
    def visitVoid_typ(self, ctx:MT22Parser.Void_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#auto_typ.
    def visitAuto_typ(self, ctx:MT22Parser.Auto_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_typ.
    def visitArray_typ(self, ctx:MT22Parser.Array_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_lit.
    def visitInt_lit(self, ctx:MT22Parser.Int_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ_of_array.
    def visitTyp_of_array(self, ctx:MT22Parser.Typ_of_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declare_var.
    def visitDeclare_var(self, ctx:MT22Parser.Declare_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_var.
    def visitInit_var(self, ctx:MT22Parser.Init_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#recursive_var.
    def visitRecursive_var(self, ctx:MT22Parser.Recursive_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlit.
    def visitIdlit(self, ctx:MT22Parser.IdlitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ_var.
    def visitTyp_var(self, ctx:MT22Parser.Typ_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declare_para.
    def visitDeclare_para(self, ctx:MT22Parser.Declare_paraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inherit.
    def visitInherit(self, ctx:MT22Parser.InheritContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#out.
    def visitOut(self, ctx:MT22Parser.OutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#declare_func.
    def visitDeclare_func(self, ctx:MT22Parser.Declare_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paralit.
    def visitParalit(self, ctx:MT22Parser.ParalitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paraPrime.
    def visitParaPrime(self, ctx:MT22Parser.ParaPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#body.
    def visitBody(self, ctx:MT22Parser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stm.
    def visitBlock_stm(self, ctx:MT22Parser.Block_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_lit.
    def visitBlock_lit(self, ctx:MT22Parser.Block_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp.
    def visitExp(self, ctx:MT22Parser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp1.
    def visitExp1(self, ctx:MT22Parser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp2.
    def visitExp2(self, ctx:MT22Parser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp3.
    def visitExp3(self, ctx:MT22Parser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp4.
    def visitExp4(self, ctx:MT22Parser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp5.
    def visitExp5(self, ctx:MT22Parser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp6.
    def visitExp6(self, ctx:MT22Parser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp7.
    def visitExp7(self, ctx:MT22Parser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp8.
    def visitExp8(self, ctx:MT22Parser.Exp8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#list_exp.
    def visitList_exp(self, ctx:MT22Parser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fun_call.
    def visitFun_call(self, ctx:MT22Parser.Fun_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_fun.
    def visitPara_fun(self, ctx:MT22Parser.Para_funContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#para_fun_Prime.
    def visitPara_fun_Prime(self, ctx:MT22Parser.Para_fun_PrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ass_stm.
    def visitAss_stm(self, ctx:MT22Parser.Ass_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stm.
    def visitIf_stm(self, ctx:MT22Parser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stm.
    def visitFor_stm(self, ctx:MT22Parser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_exp.
    def visitInit_exp(self, ctx:MT22Parser.Init_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stm.
    def visitWhile_stm(self, ctx:MT22Parser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_wh_stm.
    def visitDo_wh_stm(self, ctx:MT22Parser.Do_wh_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stm.
    def visitBreak_stm(self, ctx:MT22Parser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stm.
    def visitContinue_stm(self, ctx:MT22Parser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stm.
    def visitReturn_stm(self, ctx:MT22Parser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stm.
    def visitCall_stm(self, ctx:MT22Parser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#special_function.
    def visitSpecial_function(self, ctx:MT22Parser.Special_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readInteger.
    def visitReadInteger(self, ctx:MT22Parser.ReadIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printInteger.
    def visitPrintInteger(self, ctx:MT22Parser.PrintIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readFloat.
    def visitReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#writeFloat.
    def visitWriteFloat(self, ctx:MT22Parser.WriteFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readBoolean.
    def visitReadBoolean(self, ctx:MT22Parser.ReadBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printBoolean.
    def visitPrintBoolean(self, ctx:MT22Parser.PrintBooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#readString.
    def visitReadString(self, ctx:MT22Parser.ReadStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#printString.
    def visitPrintString(self, ctx:MT22Parser.PrintStringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#suPer.
    def visitSuPer(self, ctx:MT22Parser.SuPerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#preventDefault.
    def visitPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array.
    def visitArray(self, ctx:MT22Parser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element_array.
    def visitElement_array(self, ctx:MT22Parser.Element_arrayContext):
        return self.visitChildren(ctx)



del MT22Parser