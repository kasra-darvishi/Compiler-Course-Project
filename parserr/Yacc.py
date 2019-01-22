from ply import yacc
from lexer import Lexer


class Yacc:
    tokens = Lexer.Lexer.tokens

    quadruple = []
    tempNumber = 0

    precedence = (
        ('left', 'Or', 'DoubleOr'),
        ('left', 'And', 'DoubleAnd'),
        # ('left', 'LEqual', 'GEqual', 'EEqual', 'NonEqualOP', 'GreaterOP', 'LessOP'),
        ('left', 'Plus', 'Minus'),
        ('left', 'Times', 'Divide'),
        ('left', 'ModeOP'),
        ('right', 'Tilda', 'PP', 'MM'),
        ('left', 'Else_KW', 'Then_KW'),
        ('nonassoc', 'Other_KW')
    )

    def p_program(self, p):
        """program : list"""
        print("[Operator , arg1 , arg2 , Result]\n")
        for p in self.quadruple:
            print(p[0], " ", p[1], " ", p[2], " ", p[3])

    # def p_numOrLetter(self, p):
    #     """numOrLetter : Num
    #     | Letter
    #     | numOrLetter
    #     | """

    def p_list(self, p):
        """list : list declaration
        | declaration"""
        if len(p) == 2:
            p[0] = ('list', p[1])
        else:
            p[0] = ('list', p[1], p[2])

    def p_declaration(self, p):
        """declaration : function
        | varDeclaration"""
        p[0] = ('declaration', p[1])

    def p_varDeclaration(self, p):
        """varDeclaration : type  variableList Semicolon"""

    def p_ScopedVariableDec(self, p):
        """ScopedVariableDec : scopedSpecifier variableList Semicolon"""

    def p_variableList(self, p):
        """variableList : variableList Comma varInitialization
        | varInitialization"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = p[3]

    def p_varInitialization(self, p):
        """varInitialization : varForm
        | varForm Colon Opening_Parentheses eachExpression Closing_Parentheses"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            self.quadruple.append(['=', p[4], '_None_', p[1]])
            p[0] = p[1]

    def p_varForm(self, p):
        """varForm : VarName Opening_Bracket Num Closing_Bracket
        | VarName """
        if len(p) == 2:
            p[0] = p[1]
        else:
            # p[0] = ('varForm', p[1], p[2], p[3], p[4])
            p[0] = p[1]

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
        p[0] = ('type', p[1])

    def p_nameOfMethod(self, p):
        """nameOfMethod : MethName
                        | VarName"""

    def p_function(self, p):
        """function : void_KW nameOfMethod Opening_Parentheses parameter Closing_Parentheses Opening_Brace statement Closing_Brace
                    | type VarName Opening_Parentheses parameter Closing_Parentheses statement"""

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
        """paramId : VarName
        | VarName Opening_Bracket Closing_Bracket"""

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
        | GiveBack_KW allExpression Semicolon"""

    def p_continue(self, p):
        """continue : Continue_KW Semicolon"""

    def p_allExpression(self, p):
        """allExpression : alterable mathOp allExpression
        | alterable PP
        | alterable MM
        | eachExpression"""
        if len(p) == 3:
            result_temp = "_t" + str(self.tempNumber)
            if p[2] == '++':
                self.quadruple.append(['+', p[1], '1', result_temp])
            elif p[2] == '--':
                self.quadruple.append(['-', p[1], '1', result_temp])
            self.tempNumber += 1
            self.quadruple.append(['=', result_temp, '_None_', p[1]])
            p[0] = p[1]
        elif len(p) == 2:
            p[0] = p[1]

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
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            result_temp = "_t" + str(self.tempNumber)
            self.quadruple.append([p[1], p[2], '_None_', result_temp])
            self.tempNumber += 1
            p[0] = result_temp
        elif len(p) == 4:
            result_temp = "_t" + str(self.tempNumber)
            self.quadruple.append([p[2], p[1], p[3], result_temp])
            self.tempNumber += 1
            p[0] = result_temp

    def p_relExpression(self, p):
        """relExpression : mathEXP compareType mathEXP
        | mathEXP"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            result_temp = "_t" + str(self.tempNumber)
            self.quadruple.append([p[2], p[1], p[3], result_temp])
            self.tempNumber += 1
            p[0] = result_temp

    def p_compareType(self, p):
        """compareType : equal
        | nonEqual"""
        p[0] = p[1]

    def p_equal(self, p):
        """equal : LEqual
        | GEqual
        | EEqual"""
        p[0] = p[1]


    def p_nonEqual(self, p):
        """nonEqual : GreaterOP
        | LessOP
        | NonEqualOP"""
        p[0] = p[1]


    def p_mathEXP(self, p):
        """mathEXP : mathEXP Plus mathEXP
        | mathEXP Minus mathEXP
        | mathEXP Times mathEXP
        | mathEXP Divide mathEXP
        | mathEXP ModeOP mathEXP
        | unaryExpression"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            result_temp = "_t" + str(self.tempNumber)
            self.quadruple.append([p[2], p[1], p[3], result_temp])
            self.tempNumber += 1
            p[0] = result_temp

    # def p_op(self, p):
    #     """op : Plus
    #     | Minus
    #     | Times
    #     | Divide
    #     | ModeOP"""

    def p_unaryExpression(self, p):
        """unaryExpression : unaryop unaryExpression
        | factor"""
        if len(p) == 2:
            p[0] = p[1]
        else:
            result_temp = "_t"+str(self.tempNumber)
            self.quadruple.append([p[1], p[2], '_None_', result_temp])
            self.tempNumber += 1
            p[0] = result_temp

    def p_unaryop(self, p):
        """unaryop : Minus
        | Times
        | QMark """
        p[0] = p[1]

    def p_factor(self, p):
        """factor : inalterable
        | alterable"""
        p[0] = p[1]

    def p_alterable(self, p):
        """alterable : VarName
        | alterable Opening_Bracket allExpression Closing_Bracket
        | alterable Dot VarName"""
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 4:
            # p[0] = ('alterable', p[1], p[2], p[3])
            # TODO: get the index using symbol table
            p[0] = p[1]
        else:
            # p[0] = ('alterable', p[1], p[2], p[3], p[4])
            # TODO: get the index using symbol table
            p[0] = p[1]

    def p_inalterable(self, p):
        """inalterable : Opening_Parentheses allExpression Closing_Parentheses
        | constant
        | VarName Opening_Parentheses args Closing_Parentheses"""
        if len(p) == 4:
            p[0] = p[2]
        elif len(p) == 2:
            p[0] = p[1]

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
