# Generated from BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKITParser#decllist.
    def enterDecllist(self, ctx:BKITParser.DecllistContext):
        pass

    # Exit a parse tree produced by BKITParser#decllist.
    def exitDecllist(self, ctx:BKITParser.DecllistContext):
        pass


    # Enter a parse tree produced by BKITParser#decl.
    def enterDecl(self, ctx:BKITParser.DeclContext):
        pass

    # Exit a parse tree produced by BKITParser#decl.
    def exitDecl(self, ctx:BKITParser.DeclContext):
        pass


    # Enter a parse tree produced by BKITParser#vardecl.
    def enterVardecl(self, ctx:BKITParser.VardeclContext):
        pass

    # Exit a parse tree produced by BKITParser#vardecl.
    def exitVardecl(self, ctx:BKITParser.VardeclContext):
        pass


    # Enter a parse tree produced by BKITParser#vardecl_full.
    def enterVardecl_full(self, ctx:BKITParser.Vardecl_fullContext):
        pass

    # Exit a parse tree produced by BKITParser#vardecl_full.
    def exitVardecl_full(self, ctx:BKITParser.Vardecl_fullContext):
        pass


    # Enter a parse tree produced by BKITParser#vardecl_not_full.
    def enterVardecl_not_full(self, ctx:BKITParser.Vardecl_not_fullContext):
        pass

    # Exit a parse tree produced by BKITParser#vardecl_not_full.
    def exitVardecl_not_full(self, ctx:BKITParser.Vardecl_not_fullContext):
        pass


    # Enter a parse tree produced by BKITParser#vardecl_array.
    def enterVardecl_array(self, ctx:BKITParser.Vardecl_arrayContext):
        pass

    # Exit a parse tree produced by BKITParser#vardecl_array.
    def exitVardecl_array(self, ctx:BKITParser.Vardecl_arrayContext):
        pass


    # Enter a parse tree produced by BKITParser#funcdecl.
    def enterFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by BKITParser#funcdecl.
    def exitFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by BKITParser#func_prototype.
    def enterFunc_prototype(self, ctx:BKITParser.Func_prototypeContext):
        pass

    # Exit a parse tree produced by BKITParser#func_prototype.
    def exitFunc_prototype(self, ctx:BKITParser.Func_prototypeContext):
        pass


    # Enter a parse tree produced by BKITParser#func_body.
    def enterFunc_body(self, ctx:BKITParser.Func_bodyContext):
        pass

    # Exit a parse tree produced by BKITParser#func_body.
    def exitFunc_body(self, ctx:BKITParser.Func_bodyContext):
        pass


    # Enter a parse tree produced by BKITParser#paramdecl.
    def enterParamdecl(self, ctx:BKITParser.ParamdeclContext):
        pass

    # Exit a parse tree produced by BKITParser#paramdecl.
    def exitParamdecl(self, ctx:BKITParser.ParamdeclContext):
        pass


    # Enter a parse tree produced by BKITParser#param_list.
    def enterParam_list(self, ctx:BKITParser.Param_listContext):
        pass

    # Exit a parse tree produced by BKITParser#param_list.
    def exitParam_list(self, ctx:BKITParser.Param_listContext):
        pass


    # Enter a parse tree produced by BKITParser#param_prime.
    def enterParam_prime(self, ctx:BKITParser.Param_primeContext):
        pass

    # Exit a parse tree produced by BKITParser#param_prime.
    def exitParam_prime(self, ctx:BKITParser.Param_primeContext):
        pass


    # Enter a parse tree produced by BKITParser#stmt.
    def enterStmt(self, ctx:BKITParser.StmtContext):
        pass

    # Exit a parse tree produced by BKITParser#stmt.
    def exitStmt(self, ctx:BKITParser.StmtContext):
        pass


    # Enter a parse tree produced by BKITParser#assign_stmt.
    def enterAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#assign_stmt.
    def exitAssign_stmt(self, ctx:BKITParser.Assign_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#if_stmt.
    def enterIf_stmt(self, ctx:BKITParser.If_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#if_stmt.
    def exitIf_stmt(self, ctx:BKITParser.If_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#for_stmt.
    def enterFor_stmt(self, ctx:BKITParser.For_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#for_stmt.
    def exitFor_stmt(self, ctx:BKITParser.For_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#break_stmt.
    def enterBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#break_stmt.
    def exitBreak_stmt(self, ctx:BKITParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#continue_stmt.
    def enterContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#continue_stmt.
    def exitContinue_stmt(self, ctx:BKITParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#return_stmt.
    def enterReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#return_stmt.
    def exitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#call_stmt.
    def enterCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#call_stmt.
    def exitCall_stmt(self, ctx:BKITParser.Call_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#block_stmt.
    def enterBlock_stmt(self, ctx:BKITParser.Block_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#block_stmt.
    def exitBlock_stmt(self, ctx:BKITParser.Block_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#blocked_list.
    def enterBlocked_list(self, ctx:BKITParser.Blocked_listContext):
        pass

    # Exit a parse tree produced by BKITParser#blocked_list.
    def exitBlocked_list(self, ctx:BKITParser.Blocked_listContext):
        pass


    # Enter a parse tree produced by BKITParser#stmt_plus_vardecl.
    def enterStmt_plus_vardecl(self, ctx:BKITParser.Stmt_plus_vardeclContext):
        pass

    # Exit a parse tree produced by BKITParser#stmt_plus_vardecl.
    def exitStmt_plus_vardecl(self, ctx:BKITParser.Stmt_plus_vardeclContext):
        pass


    # Enter a parse tree produced by BKITParser#lhs.
    def enterLhs(self, ctx:BKITParser.LhsContext):
        pass

    # Exit a parse tree produced by BKITParser#lhs.
    def exitLhs(self, ctx:BKITParser.LhsContext):
        pass


    # Enter a parse tree produced by BKITParser#exp.
    def enterExp(self, ctx:BKITParser.ExpContext):
        pass

    # Exit a parse tree produced by BKITParser#exp.
    def exitExp(self, ctx:BKITParser.ExpContext):
        pass


    # Enter a parse tree produced by BKITParser#expr_list.
    def enterExpr_list(self, ctx:BKITParser.Expr_listContext):
        pass

    # Exit a parse tree produced by BKITParser#expr_list.
    def exitExpr_list(self, ctx:BKITParser.Expr_listContext):
        pass


    # Enter a parse tree produced by BKITParser#exprprime.
    def enterExprprime(self, ctx:BKITParser.ExprprimeContext):
        pass

    # Exit a parse tree produced by BKITParser#exprprime.
    def exitExprprime(self, ctx:BKITParser.ExprprimeContext):
        pass


    # Enter a parse tree produced by BKITParser#exp0.
    def enterExp0(self, ctx:BKITParser.Exp0Context):
        pass

    # Exit a parse tree produced by BKITParser#exp0.
    def exitExp0(self, ctx:BKITParser.Exp0Context):
        pass


    # Enter a parse tree produced by BKITParser#exp1.
    def enterExp1(self, ctx:BKITParser.Exp1Context):
        pass

    # Exit a parse tree produced by BKITParser#exp1.
    def exitExp1(self, ctx:BKITParser.Exp1Context):
        pass


    # Enter a parse tree produced by BKITParser#exp2.
    def enterExp2(self, ctx:BKITParser.Exp2Context):
        pass

    # Exit a parse tree produced by BKITParser#exp2.
    def exitExp2(self, ctx:BKITParser.Exp2Context):
        pass


    # Enter a parse tree produced by BKITParser#exp3.
    def enterExp3(self, ctx:BKITParser.Exp3Context):
        pass

    # Exit a parse tree produced by BKITParser#exp3.
    def exitExp3(self, ctx:BKITParser.Exp3Context):
        pass


    # Enter a parse tree produced by BKITParser#exp4.
    def enterExp4(self, ctx:BKITParser.Exp4Context):
        pass

    # Exit a parse tree produced by BKITParser#exp4.
    def exitExp4(self, ctx:BKITParser.Exp4Context):
        pass


    # Enter a parse tree produced by BKITParser#exp5.
    def enterExp5(self, ctx:BKITParser.Exp5Context):
        pass

    # Exit a parse tree produced by BKITParser#exp5.
    def exitExp5(self, ctx:BKITParser.Exp5Context):
        pass


    # Enter a parse tree produced by BKITParser#exp6.
    def enterExp6(self, ctx:BKITParser.Exp6Context):
        pass

    # Exit a parse tree produced by BKITParser#exp6.
    def exitExp6(self, ctx:BKITParser.Exp6Context):
        pass


    # Enter a parse tree produced by BKITParser#exp7.
    def enterExp7(self, ctx:BKITParser.Exp7Context):
        pass

    # Exit a parse tree produced by BKITParser#exp7.
    def exitExp7(self, ctx:BKITParser.Exp7Context):
        pass


    # Enter a parse tree produced by BKITParser#constant.
    def enterConstant(self, ctx:BKITParser.ConstantContext):
        pass

    # Exit a parse tree produced by BKITParser#constant.
    def exitConstant(self, ctx:BKITParser.ConstantContext):
        pass


    # Enter a parse tree produced by BKITParser#sub_exp.
    def enterSub_exp(self, ctx:BKITParser.Sub_expContext):
        pass

    # Exit a parse tree produced by BKITParser#sub_exp.
    def exitSub_exp(self, ctx:BKITParser.Sub_expContext):
        pass


    # Enter a parse tree produced by BKITParser#index_expr.
    def enterIndex_expr(self, ctx:BKITParser.Index_exprContext):
        pass

    # Exit a parse tree produced by BKITParser#index_expr.
    def exitIndex_expr(self, ctx:BKITParser.Index_exprContext):
        pass


    # Enter a parse tree produced by BKITParser#index_operator.
    def enterIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        pass

    # Exit a parse tree produced by BKITParser#index_operator.
    def exitIndex_operator(self, ctx:BKITParser.Index_operatorContext):
        pass


    # Enter a parse tree produced by BKITParser#func_call.
    def enterFunc_call(self, ctx:BKITParser.Func_callContext):
        pass

    # Exit a parse tree produced by BKITParser#func_call.
    def exitFunc_call(self, ctx:BKITParser.Func_callContext):
        pass


    # Enter a parse tree produced by BKITParser#array_lit.
    def enterArray_lit(self, ctx:BKITParser.Array_litContext):
        pass

    # Exit a parse tree produced by BKITParser#array_lit.
    def exitArray_lit(self, ctx:BKITParser.Array_litContext):
        pass


    # Enter a parse tree produced by BKITParser#array_type.
    def enterArray_type(self, ctx:BKITParser.Array_typeContext):
        pass

    # Exit a parse tree produced by BKITParser#array_type.
    def exitArray_type(self, ctx:BKITParser.Array_typeContext):
        pass


    # Enter a parse tree produced by BKITParser#dimensions.
    def enterDimensions(self, ctx:BKITParser.DimensionsContext):
        pass

    # Exit a parse tree produced by BKITParser#dimensions.
    def exitDimensions(self, ctx:BKITParser.DimensionsContext):
        pass


    # Enter a parse tree produced by BKITParser#number_lits.
    def enterNumber_lits(self, ctx:BKITParser.Number_litsContext):
        pass

    # Exit a parse tree produced by BKITParser#number_lits.
    def exitNumber_lits(self, ctx:BKITParser.Number_litsContext):
        pass


    # Enter a parse tree produced by BKITParser#atomic_types.
    def enterAtomic_types(self, ctx:BKITParser.Atomic_typesContext):
        pass

    # Exit a parse tree produced by BKITParser#atomic_types.
    def exitAtomic_types(self, ctx:BKITParser.Atomic_typesContext):
        pass


    # Enter a parse tree produced by BKITParser#number_lit.
    def enterNumber_lit(self, ctx:BKITParser.Number_litContext):
        pass

    # Exit a parse tree produced by BKITParser#number_lit.
    def exitNumber_lit(self, ctx:BKITParser.Number_litContext):
        pass



del BKITParser