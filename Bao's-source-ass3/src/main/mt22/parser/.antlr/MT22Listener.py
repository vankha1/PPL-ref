# Generated from d:/Learning_Documents_of_Third_Year/Principles of Programming Languages/Bao's-source-ass3/src/main/mt22/parser/MT22.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete listener for a parse tree produced by MT22Parser.
class MT22Listener(ParseTreeListener):

    # Enter a parse tree produced by MT22Parser#program.
    def enterProgram(self, ctx:MT22Parser.ProgramContext):
        pass

    # Exit a parse tree produced by MT22Parser#program.
    def exitProgram(self, ctx:MT22Parser.ProgramContext):
        pass


    # Enter a parse tree produced by MT22Parser#decllist.
    def enterDecllist(self, ctx:MT22Parser.DecllistContext):
        pass

    # Exit a parse tree produced by MT22Parser#decllist.
    def exitDecllist(self, ctx:MT22Parser.DecllistContext):
        pass


    # Enter a parse tree produced by MT22Parser#decl.
    def enterDecl(self, ctx:MT22Parser.DeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#decl.
    def exitDecl(self, ctx:MT22Parser.DeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#bool_typ.
    def enterBool_typ(self, ctx:MT22Parser.Bool_typContext):
        pass

    # Exit a parse tree produced by MT22Parser#bool_typ.
    def exitBool_typ(self, ctx:MT22Parser.Bool_typContext):
        pass


    # Enter a parse tree produced by MT22Parser#int_typ.
    def enterInt_typ(self, ctx:MT22Parser.Int_typContext):
        pass

    # Exit a parse tree produced by MT22Parser#int_typ.
    def exitInt_typ(self, ctx:MT22Parser.Int_typContext):
        pass


    # Enter a parse tree produced by MT22Parser#float_typ.
    def enterFloat_typ(self, ctx:MT22Parser.Float_typContext):
        pass

    # Exit a parse tree produced by MT22Parser#float_typ.
    def exitFloat_typ(self, ctx:MT22Parser.Float_typContext):
        pass


    # Enter a parse tree produced by MT22Parser#string_typ.
    def enterString_typ(self, ctx:MT22Parser.String_typContext):
        pass

    # Exit a parse tree produced by MT22Parser#string_typ.
    def exitString_typ(self, ctx:MT22Parser.String_typContext):
        pass


    # Enter a parse tree produced by MT22Parser#void_typ.
    def enterVoid_typ(self, ctx:MT22Parser.Void_typContext):
        pass

    # Exit a parse tree produced by MT22Parser#void_typ.
    def exitVoid_typ(self, ctx:MT22Parser.Void_typContext):
        pass


    # Enter a parse tree produced by MT22Parser#auto_typ.
    def enterAuto_typ(self, ctx:MT22Parser.Auto_typContext):
        pass

    # Exit a parse tree produced by MT22Parser#auto_typ.
    def exitAuto_typ(self, ctx:MT22Parser.Auto_typContext):
        pass


    # Enter a parse tree produced by MT22Parser#array_typ.
    def enterArray_typ(self, ctx:MT22Parser.Array_typContext):
        pass

    # Exit a parse tree produced by MT22Parser#array_typ.
    def exitArray_typ(self, ctx:MT22Parser.Array_typContext):
        pass


    # Enter a parse tree produced by MT22Parser#int_lit.
    def enterInt_lit(self, ctx:MT22Parser.Int_litContext):
        pass

    # Exit a parse tree produced by MT22Parser#int_lit.
    def exitInt_lit(self, ctx:MT22Parser.Int_litContext):
        pass


    # Enter a parse tree produced by MT22Parser#typ_of_array.
    def enterTyp_of_array(self, ctx:MT22Parser.Typ_of_arrayContext):
        pass

    # Exit a parse tree produced by MT22Parser#typ_of_array.
    def exitTyp_of_array(self, ctx:MT22Parser.Typ_of_arrayContext):
        pass


    # Enter a parse tree produced by MT22Parser#declare_var.
    def enterDeclare_var(self, ctx:MT22Parser.Declare_varContext):
        pass

    # Exit a parse tree produced by MT22Parser#declare_var.
    def exitDeclare_var(self, ctx:MT22Parser.Declare_varContext):
        pass


    # Enter a parse tree produced by MT22Parser#init_var.
    def enterInit_var(self, ctx:MT22Parser.Init_varContext):
        pass

    # Exit a parse tree produced by MT22Parser#init_var.
    def exitInit_var(self, ctx:MT22Parser.Init_varContext):
        pass


    # Enter a parse tree produced by MT22Parser#recursive_var.
    def enterRecursive_var(self, ctx:MT22Parser.Recursive_varContext):
        pass

    # Exit a parse tree produced by MT22Parser#recursive_var.
    def exitRecursive_var(self, ctx:MT22Parser.Recursive_varContext):
        pass


    # Enter a parse tree produced by MT22Parser#idlit.
    def enterIdlit(self, ctx:MT22Parser.IdlitContext):
        pass

    # Exit a parse tree produced by MT22Parser#idlit.
    def exitIdlit(self, ctx:MT22Parser.IdlitContext):
        pass


    # Enter a parse tree produced by MT22Parser#typ_var.
    def enterTyp_var(self, ctx:MT22Parser.Typ_varContext):
        pass

    # Exit a parse tree produced by MT22Parser#typ_var.
    def exitTyp_var(self, ctx:MT22Parser.Typ_varContext):
        pass


    # Enter a parse tree produced by MT22Parser#declare_para.
    def enterDeclare_para(self, ctx:MT22Parser.Declare_paraContext):
        pass

    # Exit a parse tree produced by MT22Parser#declare_para.
    def exitDeclare_para(self, ctx:MT22Parser.Declare_paraContext):
        pass


    # Enter a parse tree produced by MT22Parser#inherit.
    def enterInherit(self, ctx:MT22Parser.InheritContext):
        pass

    # Exit a parse tree produced by MT22Parser#inherit.
    def exitInherit(self, ctx:MT22Parser.InheritContext):
        pass


    # Enter a parse tree produced by MT22Parser#out.
    def enterOut(self, ctx:MT22Parser.OutContext):
        pass

    # Exit a parse tree produced by MT22Parser#out.
    def exitOut(self, ctx:MT22Parser.OutContext):
        pass


    # Enter a parse tree produced by MT22Parser#declare_func.
    def enterDeclare_func(self, ctx:MT22Parser.Declare_funcContext):
        pass

    # Exit a parse tree produced by MT22Parser#declare_func.
    def exitDeclare_func(self, ctx:MT22Parser.Declare_funcContext):
        pass


    # Enter a parse tree produced by MT22Parser#typ.
    def enterTyp(self, ctx:MT22Parser.TypContext):
        pass

    # Exit a parse tree produced by MT22Parser#typ.
    def exitTyp(self, ctx:MT22Parser.TypContext):
        pass


    # Enter a parse tree produced by MT22Parser#paralit.
    def enterParalit(self, ctx:MT22Parser.ParalitContext):
        pass

    # Exit a parse tree produced by MT22Parser#paralit.
    def exitParalit(self, ctx:MT22Parser.ParalitContext):
        pass


    # Enter a parse tree produced by MT22Parser#paraPrime.
    def enterParaPrime(self, ctx:MT22Parser.ParaPrimeContext):
        pass

    # Exit a parse tree produced by MT22Parser#paraPrime.
    def exitParaPrime(self, ctx:MT22Parser.ParaPrimeContext):
        pass


    # Enter a parse tree produced by MT22Parser#body.
    def enterBody(self, ctx:MT22Parser.BodyContext):
        pass

    # Exit a parse tree produced by MT22Parser#body.
    def exitBody(self, ctx:MT22Parser.BodyContext):
        pass


    # Enter a parse tree produced by MT22Parser#block_stm.
    def enterBlock_stm(self, ctx:MT22Parser.Block_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#block_stm.
    def exitBlock_stm(self, ctx:MT22Parser.Block_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#block_lit.
    def enterBlock_lit(self, ctx:MT22Parser.Block_litContext):
        pass

    # Exit a parse tree produced by MT22Parser#block_lit.
    def exitBlock_lit(self, ctx:MT22Parser.Block_litContext):
        pass


    # Enter a parse tree produced by MT22Parser#stmt.
    def enterStmt(self, ctx:MT22Parser.StmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#stmt.
    def exitStmt(self, ctx:MT22Parser.StmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#exp.
    def enterExp(self, ctx:MT22Parser.ExpContext):
        pass

    # Exit a parse tree produced by MT22Parser#exp.
    def exitExp(self, ctx:MT22Parser.ExpContext):
        pass


    # Enter a parse tree produced by MT22Parser#exp1.
    def enterExp1(self, ctx:MT22Parser.Exp1Context):
        pass

    # Exit a parse tree produced by MT22Parser#exp1.
    def exitExp1(self, ctx:MT22Parser.Exp1Context):
        pass


    # Enter a parse tree produced by MT22Parser#exp2.
    def enterExp2(self, ctx:MT22Parser.Exp2Context):
        pass

    # Exit a parse tree produced by MT22Parser#exp2.
    def exitExp2(self, ctx:MT22Parser.Exp2Context):
        pass


    # Enter a parse tree produced by MT22Parser#exp3.
    def enterExp3(self, ctx:MT22Parser.Exp3Context):
        pass

    # Exit a parse tree produced by MT22Parser#exp3.
    def exitExp3(self, ctx:MT22Parser.Exp3Context):
        pass


    # Enter a parse tree produced by MT22Parser#exp4.
    def enterExp4(self, ctx:MT22Parser.Exp4Context):
        pass

    # Exit a parse tree produced by MT22Parser#exp4.
    def exitExp4(self, ctx:MT22Parser.Exp4Context):
        pass


    # Enter a parse tree produced by MT22Parser#exp5.
    def enterExp5(self, ctx:MT22Parser.Exp5Context):
        pass

    # Exit a parse tree produced by MT22Parser#exp5.
    def exitExp5(self, ctx:MT22Parser.Exp5Context):
        pass


    # Enter a parse tree produced by MT22Parser#exp6.
    def enterExp6(self, ctx:MT22Parser.Exp6Context):
        pass

    # Exit a parse tree produced by MT22Parser#exp6.
    def exitExp6(self, ctx:MT22Parser.Exp6Context):
        pass


    # Enter a parse tree produced by MT22Parser#exp7.
    def enterExp7(self, ctx:MT22Parser.Exp7Context):
        pass

    # Exit a parse tree produced by MT22Parser#exp7.
    def exitExp7(self, ctx:MT22Parser.Exp7Context):
        pass


    # Enter a parse tree produced by MT22Parser#exp8.
    def enterExp8(self, ctx:MT22Parser.Exp8Context):
        pass

    # Exit a parse tree produced by MT22Parser#exp8.
    def exitExp8(self, ctx:MT22Parser.Exp8Context):
        pass


    # Enter a parse tree produced by MT22Parser#list_exp.
    def enterList_exp(self, ctx:MT22Parser.List_expContext):
        pass

    # Exit a parse tree produced by MT22Parser#list_exp.
    def exitList_exp(self, ctx:MT22Parser.List_expContext):
        pass


    # Enter a parse tree produced by MT22Parser#fun_call.
    def enterFun_call(self, ctx:MT22Parser.Fun_callContext):
        pass

    # Exit a parse tree produced by MT22Parser#fun_call.
    def exitFun_call(self, ctx:MT22Parser.Fun_callContext):
        pass


    # Enter a parse tree produced by MT22Parser#para_fun.
    def enterPara_fun(self, ctx:MT22Parser.Para_funContext):
        pass

    # Exit a parse tree produced by MT22Parser#para_fun.
    def exitPara_fun(self, ctx:MT22Parser.Para_funContext):
        pass


    # Enter a parse tree produced by MT22Parser#para_fun_Prime.
    def enterPara_fun_Prime(self, ctx:MT22Parser.Para_fun_PrimeContext):
        pass

    # Exit a parse tree produced by MT22Parser#para_fun_Prime.
    def exitPara_fun_Prime(self, ctx:MT22Parser.Para_fun_PrimeContext):
        pass


    # Enter a parse tree produced by MT22Parser#ass_stm.
    def enterAss_stm(self, ctx:MT22Parser.Ass_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#ass_stm.
    def exitAss_stm(self, ctx:MT22Parser.Ass_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#if_stm.
    def enterIf_stm(self, ctx:MT22Parser.If_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#if_stm.
    def exitIf_stm(self, ctx:MT22Parser.If_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#for_stm.
    def enterFor_stm(self, ctx:MT22Parser.For_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#for_stm.
    def exitFor_stm(self, ctx:MT22Parser.For_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#init_exp.
    def enterInit_exp(self, ctx:MT22Parser.Init_expContext):
        pass

    # Exit a parse tree produced by MT22Parser#init_exp.
    def exitInit_exp(self, ctx:MT22Parser.Init_expContext):
        pass


    # Enter a parse tree produced by MT22Parser#while_stm.
    def enterWhile_stm(self, ctx:MT22Parser.While_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#while_stm.
    def exitWhile_stm(self, ctx:MT22Parser.While_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#do_wh_stm.
    def enterDo_wh_stm(self, ctx:MT22Parser.Do_wh_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#do_wh_stm.
    def exitDo_wh_stm(self, ctx:MT22Parser.Do_wh_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#break_stm.
    def enterBreak_stm(self, ctx:MT22Parser.Break_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#break_stm.
    def exitBreak_stm(self, ctx:MT22Parser.Break_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#continue_stm.
    def enterContinue_stm(self, ctx:MT22Parser.Continue_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#continue_stm.
    def exitContinue_stm(self, ctx:MT22Parser.Continue_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#return_stm.
    def enterReturn_stm(self, ctx:MT22Parser.Return_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#return_stm.
    def exitReturn_stm(self, ctx:MT22Parser.Return_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#call_stm.
    def enterCall_stm(self, ctx:MT22Parser.Call_stmContext):
        pass

    # Exit a parse tree produced by MT22Parser#call_stm.
    def exitCall_stm(self, ctx:MT22Parser.Call_stmContext):
        pass


    # Enter a parse tree produced by MT22Parser#special_function.
    def enterSpecial_function(self, ctx:MT22Parser.Special_functionContext):
        pass

    # Exit a parse tree produced by MT22Parser#special_function.
    def exitSpecial_function(self, ctx:MT22Parser.Special_functionContext):
        pass


    # Enter a parse tree produced by MT22Parser#readInteger.
    def enterReadInteger(self, ctx:MT22Parser.ReadIntegerContext):
        pass

    # Exit a parse tree produced by MT22Parser#readInteger.
    def exitReadInteger(self, ctx:MT22Parser.ReadIntegerContext):
        pass


    # Enter a parse tree produced by MT22Parser#printInteger.
    def enterPrintInteger(self, ctx:MT22Parser.PrintIntegerContext):
        pass

    # Exit a parse tree produced by MT22Parser#printInteger.
    def exitPrintInteger(self, ctx:MT22Parser.PrintIntegerContext):
        pass


    # Enter a parse tree produced by MT22Parser#readFloat.
    def enterReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        pass

    # Exit a parse tree produced by MT22Parser#readFloat.
    def exitReadFloat(self, ctx:MT22Parser.ReadFloatContext):
        pass


    # Enter a parse tree produced by MT22Parser#printFloat.
    def enterPrintFloat(self, ctx:MT22Parser.PrintFloatContext):
        pass

    # Exit a parse tree produced by MT22Parser#printFloat.
    def exitPrintFloat(self, ctx:MT22Parser.PrintFloatContext):
        pass


    # Enter a parse tree produced by MT22Parser#readBoolean.
    def enterReadBoolean(self, ctx:MT22Parser.ReadBooleanContext):
        pass

    # Exit a parse tree produced by MT22Parser#readBoolean.
    def exitReadBoolean(self, ctx:MT22Parser.ReadBooleanContext):
        pass


    # Enter a parse tree produced by MT22Parser#printBoolean.
    def enterPrintBoolean(self, ctx:MT22Parser.PrintBooleanContext):
        pass

    # Exit a parse tree produced by MT22Parser#printBoolean.
    def exitPrintBoolean(self, ctx:MT22Parser.PrintBooleanContext):
        pass


    # Enter a parse tree produced by MT22Parser#readString.
    def enterReadString(self, ctx:MT22Parser.ReadStringContext):
        pass

    # Exit a parse tree produced by MT22Parser#readString.
    def exitReadString(self, ctx:MT22Parser.ReadStringContext):
        pass


    # Enter a parse tree produced by MT22Parser#printString.
    def enterPrintString(self, ctx:MT22Parser.PrintStringContext):
        pass

    # Exit a parse tree produced by MT22Parser#printString.
    def exitPrintString(self, ctx:MT22Parser.PrintStringContext):
        pass


    # Enter a parse tree produced by MT22Parser#suPer.
    def enterSuPer(self, ctx:MT22Parser.SuPerContext):
        pass

    # Exit a parse tree produced by MT22Parser#suPer.
    def exitSuPer(self, ctx:MT22Parser.SuPerContext):
        pass


    # Enter a parse tree produced by MT22Parser#preventDefault.
    def enterPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        pass

    # Exit a parse tree produced by MT22Parser#preventDefault.
    def exitPreventDefault(self, ctx:MT22Parser.PreventDefaultContext):
        pass


    # Enter a parse tree produced by MT22Parser#array.
    def enterArray(self, ctx:MT22Parser.ArrayContext):
        pass

    # Exit a parse tree produced by MT22Parser#array.
    def exitArray(self, ctx:MT22Parser.ArrayContext):
        pass


    # Enter a parse tree produced by MT22Parser#element_array.
    def enterElement_array(self, ctx:MT22Parser.Element_arrayContext):
        pass

    # Exit a parse tree produced by MT22Parser#element_array.
    def exitElement_array(self, ctx:MT22Parser.Element_arrayContext):
        pass



del MT22Parser