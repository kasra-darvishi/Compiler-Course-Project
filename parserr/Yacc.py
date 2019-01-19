from ply import yacc
from lexer import Lexer


class Yacc:
    tokens = Lexer.Lexer.tokens
    precedence = (
        ('left', 'Or', 'DoubleOr'),
        ('left', 'And', 'DoubleAnd'),
        # ('left', 'LEqual', 'GEqual', 'EEqual', 'NonEqualOP', 'GreaterOP', 'LessOP'),
        ('left', 'Plus', 'Minus'),
        ('left', 'Times', 'Divide'),
        ('left', 'ModeOP'),
        ('right', 'Tilda', 'PP', 'MM'),
        ('nonassoc', 'Else_KW', 'Then_KW'),
    )

    def p_program(self, p):
        """program : list"""

    # def p_numOrLetter(self, p):
    #     """numOrLetter : Num
    #     | Letter
    #     | numOrLetter
    #     | """

    def p_numOrLetter(self, p):
        """numOrLetter : Num
        | Letter
        | """

    def p_list(self, p):
        """list : list declaration
        | declaration"""

    def p_declaration(self, p):
        """declaration : function
        | varDeclaration"""

    def p_varDeclaration(self, p):
        """varDeclaration : type  variableList Semicolon"""

    def p_ScopedVariableDec(self, p):
        """ScopedVariableDec : scopedSpecifier variableList Semicolon"""

    def p_variableList(self, p):
        """variableList : variableList Comma varInitialization
        | varInitialization"""

    def p_varInitialization(self, p):
        """varInitialization : varForm
        | varForm Colon Opening_Parentheses eachExpression Closing_Parentheses"""

    def p_varForm(self, p):
        """varForm : Letter numOrLetter Opening_Bracket Num Closing_Bracket
        | Letter  numOrLetter """

    def p_scopedSpecifier(self, p):
        """scopedSpecifier : Static_KW type
        | type"""

    def p_type(self, p):
        """type : Boolean_KW
        | Character_KW
        | Integer_KW
        | char_KW
        | bool_KW
        | int_KW"""

    def p_function(self, p):
        """function : void_KW numOrLetter Opening_Parentheses parameter Closing_Parentheses Opening_Brace statement Closing_Brace
                    | type Letter numOrLetter Opening_Parentheses parameter Closing_Parentheses statement"""

    def p_parameter(self, p):
        """parameter : listOfParameters
        | """

    def p_listOfParameters(self, p):
        """listOfParameters : listOfParameters Semicolon paramTypeList
        | paramTypeList"""

    def p_paramTypeList(self, p):
        """paramTypeList : type paramList"""

    def p_paramList(self, p):
        """paramList :  paramList Comma paramId
        | paramId"""

    def p_localDeclarations(self, p):
        """localDeclarations : localDeclarations ScopedVariableDec
        | """

    def p_paramId(self, p):
        """paramId : Letter numOrLetter
        | Letter numOrLetter Opening_Bracket Closing_Bracket"""

    def p_statement(self, p):
        """statement : phrase
        | compoundPhrase
        | selectPhrase
        | iterationPhrase
        | returnPhrase
        | continue"""

    def p_compoundPhrase(self, p):
        """compoundPhrase : Opening_Brace localDeclarations  statementList Closing_Brace"""

    def p_statementList(self, p):
        """statementList : statementList statement
        | """

    def p_phrase(self, p):
        """phrase : allExpression Semicolon
        | Semicolon"""

    def p_selectPhrase(self, p):
        """selectPhrase : If_KW Opening_Parentheses eachExpression Closing_Parentheses ifBody
                        | If_KW Opening_Parentheses eachExpression Closing_Parentheses Opening_Brace ifBody ifBody Closing_Brace"""

    def p_ifBody(self, p):
        """ifBody : statement
        | statement Other_KW statement"""

    def p_iterationPhrase(self, p):
        """iterationPhrase : Till_KW Opening_Parentheses eachExpression Closing_Parentheses statement"""

    def p_returnPhrase(self, p):
        """returnPhrase : ComeBack_KW Semicolon
        | GiveBack_KW allExpression Semicolon
        | GiveBack_KW numOrLetter Semicolon"""

    def p_continue(self, p):
        """continue : Continue_KW Semicolon"""

    def p_allExpression(self, p):
        """allExpression : alterable mathOp allExpression
        | alterable PP
        | alterable MM
        | eachExpression
        | alterable mathOp alterable"""

    def p_mathOp(self, p):
        """mathOp : Equal
        | PlusEqual
        | MinusEqual
        | TimesEqual
        | DivideEqual"""

    def p_eachExpression(self, p):
        """eachExpression : eachExpression DoubleAnd eachExpression
        | eachExpression DoubleOr eachExpression
        | eachExpression Tilda eachExpression
        | eachExpression And eachExpression
        | eachExpression Or eachExpression
        | eachExpression DoubleAnd Then_KW eachExpression
        | eachExpression DoubleOr Then_KW eachExpression
        | eachExpression Tilda Then_KW eachExpression
        | eachExpression And Then_KW eachExpression
        | eachExpression Or Then_KW eachExpression
        | DoubleAnd eachExpression
        | DoubleOr eachExpression
        | Tilda eachExpression
        | And eachExpression
        | Or eachExpression
        | relExpression
        | eachExpression Or Else_KW eachExpression
        | eachExpression And Else_KW eachExpression
        | eachExpression Tilda Else_KW eachExpression
        | eachExpression DoubleOr Else_KW eachExpression
        | eachExpression DoubleAnd Else_KW eachExpression"""

    def p_relExpression(self, p):
        """relExpression : mathEXP compareType mathEXP
        | mathEXP"""

    def p_compareType(self, p):
        """compareType : equal
        | nonEqual"""

    def p_equal(self, p):
        """equal : LEqual
        | GEqual
        | EEqual"""

    def p_nonEqual(self, p):
        """nonEqual : GreaterOP
        | LessOP
        | NonEqualOP"""

    def p_mathEXP(self, p):
        """mathEXP : mathEXP Plus mathEXP
        | mathEXP Minus mathEXP
        | mathEXP Times mathEXP
        | mathEXP Divide mathEXP
        | mathEXP ModeOP mathEXP
        | unaryExpression"""

    # def p_op(self, p):
    #     """op : Plus
    #     | Minus
    #     | Times
    #     | Divide
    #     | ModeOP"""

    def p_unaryExpression(self, p):
        """unaryExpression : unaryop unaryExpression
        | factor"""

    def p_unaryop(self, p):
        """unaryop : Minus
        | Times
        | QMark """

    def p_factor(self, p):
        """factor : inalterable
        | alterable"""

    def p_alterable(self, p):
        """alterable : Letter numOrLetter
        | alterable Opening_Bracket allExpression Closing_Bracket
        | alterable Letter numOrLetter"""

    def p_inalterable(self, p):
        """inalterable : Opening_Parentheses allExpression Closing_Parentheses
        | constant
        | Letter numOrLetter Opening_Parentheses args Closing_Parentheses"""

    def p_args(self, p):
        """args : arguments
        | """

    def p_arguments(self, p):
        """arguments : arguments Comma allExpression
        | allExpression"""

    def p_constant(self, p):
        """constant : Const_KW
        | True_KW
        | False_KW"""

    # def p_logicOp(self, p):
    #     """logicOp : DoubleAnd
    #     | DoubleOr
    #     | Tilda
    #     | And
    #     | Or"""

    def p_error(self, p):
        print('syntax error')
        exit(5)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser