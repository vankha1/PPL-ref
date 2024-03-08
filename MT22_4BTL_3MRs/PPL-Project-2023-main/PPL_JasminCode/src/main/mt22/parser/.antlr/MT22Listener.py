# Generated from d:/Learning_Documents_of_Third_Year/Principles of Programming Languages/MT22_4BTL_3MRs/PPL-Project-2023-main/PPL_JasminCode/src/main/mt22/parser/MT22.g4 by ANTLR 4.13.1
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


    # Enter a parse tree produced by MT22Parser#decl_list.
    def enterDecl_list(self, ctx:MT22Parser.Decl_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#decl_list.
    def exitDecl_list(self, ctx:MT22Parser.Decl_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#decl.
    def enterDecl(self, ctx:MT22Parser.DeclContext):
        pass

    # Exit a parse tree produced by MT22Parser#decl.
    def exitDecl(self, ctx:MT22Parser.DeclContext):
        pass


    # Enter a parse tree produced by MT22Parser#var_decl.
    def enterVar_decl(self, ctx:MT22Parser.Var_declContext):
        pass

    # Exit a parse tree produced by MT22Parser#var_decl.
    def exitVar_decl(self, ctx:MT22Parser.Var_declContext):
        pass


    # Enter a parse tree produced by MT22Parser#full_var_decl.
    def enterFull_var_decl(self, ctx:MT22Parser.Full_var_declContext):
        pass

    # Exit a parse tree produced by MT22Parser#full_var_decl.
    def exitFull_var_decl(self, ctx:MT22Parser.Full_var_declContext):
        pass


    # Enter a parse tree produced by MT22Parser#func_decl.
    def enterFunc_decl(self, ctx:MT22Parser.Func_declContext):
        pass

    # Exit a parse tree produced by MT22Parser#func_decl.
    def exitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        pass


    # Enter a parse tree produced by MT22Parser#param_decl.
    def enterParam_decl(self, ctx:MT22Parser.Param_declContext):
        pass

    # Exit a parse tree produced by MT22Parser#param_decl.
    def exitParam_decl(self, ctx:MT22Parser.Param_declContext):
        pass


    # Enter a parse tree produced by MT22Parser#id_list.
    def enterId_list(self, ctx:MT22Parser.Id_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#id_list.
    def exitId_list(self, ctx:MT22Parser.Id_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#param_list.
    def enterParam_list(self, ctx:MT22Parser.Param_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#param_list.
    def exitParam_list(self, ctx:MT22Parser.Param_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#param_list_body.
    def enterParam_list_body(self, ctx:MT22Parser.Param_list_bodyContext):
        pass

    # Exit a parse tree produced by MT22Parser#param_list_body.
    def exitParam_list_body(self, ctx:MT22Parser.Param_list_bodyContext):
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


    # Enter a parse tree produced by MT22Parser#match_stmt.
    def enterMatch_stmt(self, ctx:MT22Parser.Match_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#match_stmt.
    def exitMatch_stmt(self, ctx:MT22Parser.Match_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#unmatch_stmt.
    def enterUnmatch_stmt(self, ctx:MT22Parser.Unmatch_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#unmatch_stmt.
    def exitUnmatch_stmt(self, ctx:MT22Parser.Unmatch_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#stov.
    def enterStov(self, ctx:MT22Parser.StovContext):
        pass

    # Exit a parse tree produced by MT22Parser#stov.
    def exitStov(self, ctx:MT22Parser.StovContext):
        pass


    # Enter a parse tree produced by MT22Parser#stov_list.
    def enterStov_list(self, ctx:MT22Parser.Stov_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#stov_list.
    def exitStov_list(self, ctx:MT22Parser.Stov_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#assign_stmt.
    def enterAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#assign_stmt.
    def exitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
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


    # Enter a parse tree produced by MT22Parser#block_stmt.
    def enterBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#block_stmt.
    def exitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        pass


    # Enter a parse tree produced by MT22Parser#call_stmt.
    def enterCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        pass

    # Exit a parse tree produced by MT22Parser#call_stmt.
    def exitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
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


    # Enter a parse tree produced by MT22Parser#expr.
    def enterExpr(self, ctx:MT22Parser.ExprContext):
        pass

    # Exit a parse tree produced by MT22Parser#expr.
    def exitExpr(self, ctx:MT22Parser.ExprContext):
        pass


    # Enter a parse tree produced by MT22Parser#expr_list.
    def enterExpr_list(self, ctx:MT22Parser.Expr_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#expr_list.
    def exitExpr_list(self, ctx:MT22Parser.Expr_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#exprprime.
    def enterExprprime(self, ctx:MT22Parser.ExprprimeContext):
        pass

    # Exit a parse tree produced by MT22Parser#exprprime.
    def exitExprprime(self, ctx:MT22Parser.ExprprimeContext):
        pass


    # Enter a parse tree produced by MT22Parser#expr0.
    def enterExpr0(self, ctx:MT22Parser.Expr0Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr0.
    def exitExpr0(self, ctx:MT22Parser.Expr0Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr1.
    def enterExpr1(self, ctx:MT22Parser.Expr1Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr1.
    def exitExpr1(self, ctx:MT22Parser.Expr1Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr2.
    def enterExpr2(self, ctx:MT22Parser.Expr2Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr2.
    def exitExpr2(self, ctx:MT22Parser.Expr2Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr3.
    def enterExpr3(self, ctx:MT22Parser.Expr3Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr3.
    def exitExpr3(self, ctx:MT22Parser.Expr3Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr4.
    def enterExpr4(self, ctx:MT22Parser.Expr4Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr4.
    def exitExpr4(self, ctx:MT22Parser.Expr4Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr5.
    def enterExpr5(self, ctx:MT22Parser.Expr5Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr5.
    def exitExpr5(self, ctx:MT22Parser.Expr5Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr6.
    def enterExpr6(self, ctx:MT22Parser.Expr6Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr6.
    def exitExpr6(self, ctx:MT22Parser.Expr6Context):
        pass


    # Enter a parse tree produced by MT22Parser#expr7.
    def enterExpr7(self, ctx:MT22Parser.Expr7Context):
        pass

    # Exit a parse tree produced by MT22Parser#expr7.
    def exitExpr7(self, ctx:MT22Parser.Expr7Context):
        pass


    # Enter a parse tree produced by MT22Parser#func_call_expr.
    def enterFunc_call_expr(self, ctx:MT22Parser.Func_call_exprContext):
        pass

    # Exit a parse tree produced by MT22Parser#func_call_expr.
    def exitFunc_call_expr(self, ctx:MT22Parser.Func_call_exprContext):
        pass


    # Enter a parse tree produced by MT22Parser#constant.
    def enterConstant(self, ctx:MT22Parser.ConstantContext):
        pass

    # Exit a parse tree produced by MT22Parser#constant.
    def exitConstant(self, ctx:MT22Parser.ConstantContext):
        pass


    # Enter a parse tree produced by MT22Parser#sub_expr.
    def enterSub_expr(self, ctx:MT22Parser.Sub_exprContext):
        pass

    # Exit a parse tree produced by MT22Parser#sub_expr.
    def exitSub_expr(self, ctx:MT22Parser.Sub_exprContext):
        pass


    # Enter a parse tree produced by MT22Parser#index_operator.
    def enterIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        pass

    # Exit a parse tree produced by MT22Parser#index_operator.
    def exitIndex_operator(self, ctx:MT22Parser.Index_operatorContext):
        pass


    # Enter a parse tree produced by MT22Parser#array_lit.
    def enterArray_lit(self, ctx:MT22Parser.Array_litContext):
        pass

    # Exit a parse tree produced by MT22Parser#array_lit.
    def exitArray_lit(self, ctx:MT22Parser.Array_litContext):
        pass


    # Enter a parse tree produced by MT22Parser#var_type.
    def enterVar_type(self, ctx:MT22Parser.Var_typeContext):
        pass

    # Exit a parse tree produced by MT22Parser#var_type.
    def exitVar_type(self, ctx:MT22Parser.Var_typeContext):
        pass


    # Enter a parse tree produced by MT22Parser#func_ret_type.
    def enterFunc_ret_type(self, ctx:MT22Parser.Func_ret_typeContext):
        pass

    # Exit a parse tree produced by MT22Parser#func_ret_type.
    def exitFunc_ret_type(self, ctx:MT22Parser.Func_ret_typeContext):
        pass


    # Enter a parse tree produced by MT22Parser#para_type.
    def enterPara_type(self, ctx:MT22Parser.Para_typeContext):
        pass

    # Exit a parse tree produced by MT22Parser#para_type.
    def exitPara_type(self, ctx:MT22Parser.Para_typeContext):
        pass


    # Enter a parse tree produced by MT22Parser#atomic_type.
    def enterAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        pass

    # Exit a parse tree produced by MT22Parser#atomic_type.
    def exitAtomic_type(self, ctx:MT22Parser.Atomic_typeContext):
        pass


    # Enter a parse tree produced by MT22Parser#array_type.
    def enterArray_type(self, ctx:MT22Parser.Array_typeContext):
        pass

    # Exit a parse tree produced by MT22Parser#array_type.
    def exitArray_type(self, ctx:MT22Parser.Array_typeContext):
        pass


    # Enter a parse tree produced by MT22Parser#dimension.
    def enterDimension(self, ctx:MT22Parser.DimensionContext):
        pass

    # Exit a parse tree produced by MT22Parser#dimension.
    def exitDimension(self, ctx:MT22Parser.DimensionContext):
        pass


    # Enter a parse tree produced by MT22Parser#void_type.
    def enterVoid_type(self, ctx:MT22Parser.Void_typeContext):
        pass

    # Exit a parse tree produced by MT22Parser#void_type.
    def exitVoid_type(self, ctx:MT22Parser.Void_typeContext):
        pass


    # Enter a parse tree produced by MT22Parser#auto_type.
    def enterAuto_type(self, ctx:MT22Parser.Auto_typeContext):
        pass

    # Exit a parse tree produced by MT22Parser#auto_type.
    def exitAuto_type(self, ctx:MT22Parser.Auto_typeContext):
        pass


    # Enter a parse tree produced by MT22Parser#intlit_list.
    def enterIntlit_list(self, ctx:MT22Parser.Intlit_listContext):
        pass

    # Exit a parse tree produced by MT22Parser#intlit_list.
    def exitIntlit_list(self, ctx:MT22Parser.Intlit_listContext):
        pass


    # Enter a parse tree produced by MT22Parser#lhs.
    def enterLhs(self, ctx:MT22Parser.LhsContext):
        pass

    # Exit a parse tree produced by MT22Parser#lhs.
    def exitLhs(self, ctx:MT22Parser.LhsContext):
        pass


    # Enter a parse tree produced by MT22Parser#index_expr.
    def enterIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        pass

    # Exit a parse tree produced by MT22Parser#index_expr.
    def exitIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        pass



del MT22Parser