import ply.lex as lex


class Lexer:
    sTable = []

    tokens = ['Const_KW', 'reserved', 'Num', 'VarName', 'MethName', 'Opening_Bracket', 'Closing_Bracket', 'Semicolon', 'Boolean_KW',
              'Character_KW', 'Integer_KW', 'char_KW', 'bool_KW', 'int_KW', 'void_KW', 'If_KW', 'Other_KW', 'Till_KW',
              'ComeBack_KW', 'GiveBack_KW', 'Continue_KW', 'PP', 'MM', 'Opening_Parentheses', 'Static_KW',
              'Closing_Parentheses', 'Opening_Brace', 'Closing_Brace', 'Equal', 'PlusEqual',
              'MinusEqual', 'TimesEqual', 'DivideEqual', 'Then_KW', 'Else_KW', 'LEqual', 'GEqual',
              'EEqual', 'GreaterOP', 'LessOP', 'NonEqualOP', 'Plus', 'Minus', 'Times',
              'Divide', 'ModeOP', 'QMark', 'True_KW', 'False_KW', 'DoubleAnd', 'DoubleOr',
              'Tilda', 'And', 'Or', 'Comment', 'Comma', 'Colon', 'Dot']


    t_ignore = ' \t'
    t_Dot = '\.'
    t_Colon = '\:'
    t_Comma = r'\,'
    t_Opening_Bracket = r'\['
    t_Closing_Bracket = r']'
    t_Semicolon = r';'
    t_PP = r'\+\+'
    t_MM = r'--'
    t_Opening_Parentheses = r'\('
    t_Closing_Parentheses = r'\)'
    t_Opening_Brace = r'\{'
    t_Closing_Brace = r'}'
    t_Equal = r'='
    t_PlusEqual = r'\+='
    t_MinusEqual = r'-='
    t_TimesEqual = r'\*='
    t_DivideEqual = r'/='
    t_LEqual = r'<='
    t_GEqual = r'>='
    t_EEqual = r'=='
    t_GreaterOP = r'>'
    t_LessOP = r'<'
    t_NonEqualOP = r'!='
    t_Plus = r'\+'
    t_Minus = r'-'
    t_Times = r'\*'
    t_Divide = r'/'
    t_ModeOP = r'%'
    t_QMark = r'\?'
    t_DoubleAnd = r'\&\&'
    t_DoubleOr = r'\|\|'
    t_Tilda = r'\~'

    reserved = {
        'Boolean': 'Boolean_KW',
        'character': 'Character_KW',
        'integer': 'Integer_KW',
        'char': 'char_KW',
        'bool': 'bool_KW',
        'int': 'int_KW',
        'void': 'void_KW',
        'if': 'If_KW',
        'other': 'Other_KW',
        'till': 'Till_KW',
        'comeback': 'ComeBack_KW',
        'giveback': 'GiveBack_KW',
        'continue': 'Continue_KW',
        'static': 'Static_KW',
        'then': 'Then_KW',
        'else': 'Else_KW',
        'CONST': 'Const_KW',
        'and': 'And',
        'or': 'Or',
        'true': 'True_KW',
        'false': 'False_KW'
    }

    def t_reserved(self, t):
        r"""[a-zA-Z0-9_]+"""
        isANum = True
        for char in t.value:
            if char != '0' and char != '1' and char != '2' and char != '3' and char != '4' and char != '5' and char != '6' and char != '7' and char != '8' and char != '9':
                isANum = False

        if isANum:
            t.type = 'Num'
            t.value = int(t.value)
        else:
            t.type = self.reserved.get(t.value, 'non')  # Check for reserved words
            if t.type == 'non':
                if t.value not in self.sTable:
                    self.sTable.append(t.value)
                if t.value[0] == '0' or t.value[0] == '1' or t.value[0] == '2' or t.value[0] == '3' or t.value[0] == '4' or t.value[0] == '5' or t.value[0] == '6' or t.value[0] == '7' or t.value[0] == '8' or t.value[0] == '9':
                    t.type = 'MethName'
                else:
                    t.type = 'VarName'
        return t

    # def t_MethName(self, t):
    #     r"""[a-zA-Z0-9_]+"""
    #     if t.value not in self.sTable:
    #         self.sTable.append(t.value)
    #     return t
    #
    # def t_reserved(self, t):
    #     r"""[a-zA-Z_][a-zA-Z0-9_]*"""
    #     t.type = self.reserved.get(t.value, 'VarName')  # Check for reserved words
    #     if t.type == 'VarName':
    #         if t.value not in self.sTable:
    #             self.sTable.append(t.value)
    #     return t

    def t_error(self, t):
        # print("Invalid character: ", t.value[0])
        t.lexer.skip(1)

    def t_COMMENT(self, t):
        r"""//.*"""
        pass

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

        return self.lexer