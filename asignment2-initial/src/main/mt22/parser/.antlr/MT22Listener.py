# Generated from d:/Learning_Documents_of_Third_Year/Principles of Programming Languages/asignment2-initial/src/main/mt22/parser/MT22.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by MT22Parser#vardecl.
    def enterVardecl(self, ctx:MT22Parser.VardeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#vardecl.
    def exitVardecl(self, ctx:MT22Parser.VardeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#vardecl_full.
    def enterVardecl_full(self, ctx:MT22Parser.Vardecl_fullContext):
        pass

    # Exit a parse tree produced by MT22Parser#vardecl_full.
    def exitVardecl_full(self, ctx:MT22Parser.Vardecl_fullContext):
        pass


    # Enter a parse tree produced by MT22Parser#vardecl_not_full.
    def enterVardecl_not_full(self, ctx:MT22Parser.Vardecl_not_fullContext):
        pass

    # Exit a parse tree produced by MT22Parser#vardecl_not_full.
    def exitVardecl_not_full(self, ctx:MT22Parser.Vardecl_not_fullContext):
        pass


    # Enter a parse tree produced by MT22Parser#id_list.
    def enterId_list(self, ctx:MT22Parser.Id_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#id_list.
    def exitId_list(self, ctx:MT22Parser.Id_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#funcdecl.
    def enterFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#funcdecl.
    def exitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#inherit_part.
    def enterInherit_part(self, ctx:MT22Parser.Inherit_partContext):
        pass

    # Exit a parse tree produced by MT22Parser#inherit_part.
    def exitInherit_part(self, ctx:MT22Parser.Inherit_partContext):
        pass


    # Enter a parse tree produced by MT22Parser#paramdecl.
    def enterParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#paramdecl.
    def exitParamdecl(self, ctx:MT22Parser.ParamdeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#param_list.
    def enterParam_list(self, ctx:MT22Parser.Param_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#param_list.
    def exitParam_list(self, ctx:MT22Parser.Param_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#param_prime.
    def enterParam_prime(self, ctx:MT22Parser.Param_primeContext):
        pass

    # Exit a parse tree produced by MT22Parser#param_prime.
    def exitParam_prime(self, ctx:MT22Parser.Param_primeContext):
        pass


    # Enter a parse tree produced by MT22Parser#stmt.
    def enterStmt(self, ctx:MT22Parser.StmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#stmt.
    def exitStmt(self, ctx:MT22Parser.StmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#assign_stmt.
    def enterAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#assign_stmt.
    def exitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#if_stmt.
    def enterIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#if_stmt.
    def exitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#for_stmt.
    def enterFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#for_stmt.
    def exitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#while_stmt.
    def enterWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#while_stmt.
    def exitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#do_while_stmt.
    def enterDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#do_while_stmt.
    def exitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#break_stmt.
    def enterBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#break_stmt.
    def exitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#continue_stmt.
    def enterContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#continue_stmt.
    def exitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#return_stmt.
    def enterReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#return_stmt.
    def exitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#call_stmt.
    def enterCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#call_stmt.
    def exitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#block_stmt.
    def enterBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#block_stmt.
    def exitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#blocked_list.
    def enterBlocked_list(self, ctx:MT22Parser.Blocked_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#blocked_list.
    def exitBlocked_list(self, ctx:MT22Parser.Blocked_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#blocked_list_prime.
    def enterBlocked_list_prime(self, ctx:MT22Parser.Blocked_list_primeContext):
        pass

    # Exit a parse tree produced by MT22Parser#blocked_list_prime.
    def exitBlocked_list_prime(self, ctx:MT22Parser.Blocked_list_primeContext):
        pass


    # Enter a parse tree produced by MT22Parser#stmt_plus_vardecl.
    def enterStmt_plus_vardecl(self, ctx:MT22Parser.Stmt_plus_vardeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#stmt_plus_vardecl.
    def exitStmt_plus_vardecl(self, ctx:MT22Parser.Stmt_plus_vardeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#scalar_var.
    def enterScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        pass

    # Exit a parse tree produced by MT22Parser#scalar_var.
    def exitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        pass


    # Enter a parse tree produced by MT22Parser#exp_list.
    def enterExp_list(self, ctx:MT22Parser.Exp_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#exp_list.
    def exitExp_list(self, ctx:MT22Parser.Exp_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#exp_prime.
    def enterExp_prime(self, ctx:MT22Parser.Exp_primeContext):
        pass

    # Exit a parse tree produced by MT22Parser#exp_prime.
    def exitExp_prime(self, ctx:MT22Parser.Exp_primeContext):
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


    # Enter a parse tree produced by MT22Parser#constant.
    def enterConstant(self, ctx:MT22Parser.ConstantContext):
        pass

    # Exit a parse tree produced by MT22Parser#constant.
    def exitConstant(self, ctx:MT22Parser.ConstantContext):
        pass


    # Enter a parse tree produced by MT22Parser#sub_exp.
    def enterSub_exp(self, ctx:MT22Parser.Sub_expContext):
        pass

    # Exit a parse tree produced by MT22Parser#sub_exp.
    def exitSub_exp(self, ctx:MT22Parser.Sub_expContext):
        pass


    # Enter a parse tree produced by MT22Parser#index_op.
    def enterIndex_op(self, ctx:MT22Parser.Index_opContext):
        pass

    # Exit a parse tree produced by MT22Parser#index_op.
    def exitIndex_op(self, ctx:MT22Parser.Index_opContext):
        pass


    # Enter a parse tree produced by MT22Parser#func_call.
    def enterFunc_call(self, ctx:MT22Parser.Func_callContext):
        pass

    # Exit a parse tree produced by MT22Parser#func_call.
    def exitFunc_call(self, ctx:MT22Parser.Func_callContext):
        pass


    # Enter a parse tree produced by MT22Parser#array_lit.
    def enterArray_lit(self, ctx:MT22Parser.Array_litContext):
        pass

    # Exit a parse tree produced by MT22Parser#array_lit.
    def exitArray_lit(self, ctx:MT22Parser.Array_litContext):
        pass


    # Enter a parse tree produced by MT22Parser#array_types.
    def enterArray_types(self, ctx:MT22Parser.Array_typesContext):
        pass

    # Exit a parse tree produced by MT22Parser#array_types.
    def exitArray_types(self, ctx:MT22Parser.Array_typesContext):
        pass


    # Enter a parse tree produced by MT22Parser#dimensions.
    def enterDimensions(self, ctx:MT22Parser.DimensionsContext):
        pass

    # Exit a parse tree produced by MT22Parser#dimensions.
    def exitDimensions(self, ctx:MT22Parser.DimensionsContext):
        pass


    # Enter a parse tree produced by MT22Parser#int_list.
    def enterInt_list(self, ctx:MT22Parser.Int_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#int_list.
    def exitInt_list(self, ctx:MT22Parser.Int_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#atomic_types.
    def enterAtomic_types(self, ctx:MT22Parser.Atomic_typesContext):
        pass

    # Exit a parse tree produced by MT22Parser#atomic_types.
    def exitAtomic_types(self, ctx:MT22Parser.Atomic_typesContext):
        pass



del MT22Parser