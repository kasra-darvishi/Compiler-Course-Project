import ply.lex as lex


class Lexer:
    tokens = ['Const', 'reserved', 'Num', 'Letter', 'Opening_Bracket', 'Closing_Bracket', 'Semicolon', 'Boolean',
              'Character', 'Integer', 'char', 'bool', 'int', 'void', 'If', 'Other', 'Till',
              'ComeBack', 'GiveBack', 'Continue', 'PP', 'MM', 'Opening_Parentheses', 'Static',
              'Closing_Parentheses', 'Opening_Brace', 'Closing_Brace', 'Equal', 'PlusEqual',
              'MinusEqual', 'TimesEqual', 'DivideEqual', 'Then', 'Else', 'LEqual', 'GEqual',
              'EEqual', 'GreaterOP', 'LessOP', 'NonEqualOP', 'Plus', 'Minus', 'Times',
              'Divide', 'ModeOP', 'QMark', 'True', 'False', 'DoubleAnd', 'DoubleOr',
              'Tilda', 'And', 'Or']


    t_ignore = ' \t'
    t_Const = r'CONST'

    t_Num = r'[0-9]'
    t_Letter = r'[a-zA-Z]'
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
    t_And = r'\&'
    t_Or = r'\|'

    reserved = {
        'Boolean': 't_Boolean',
        'character': 't_Character',
        'integer': 't_Integer',
        'char': 't_char',
        'bool': 't_bool',
        'int': 't_int',
        'void': 't_void',
        'if': 't_If',
        'other': 't_Other',
        'till': 't_Till',
        'comeback': 't_ComeBack',
        'giveback': 't_GiveBack',
        'continue': 't_Continue',
        'static': 't_Static',
        'then': 't_Then',
        'else': 't_Else',
        'CONST': 't_Const',
        'true': 't_True',
        'false': 't_False'
    }

    # def t_reserved(self, t):
    #     t.type = self.reserved.get(t.value)  # Check for reserved words
    #     return t


    def t_error(self, t):
        print("Invalid character: ", t.value[0])
        t.lexer.skip(1)


    def build(self, **kwargs):
        '''
        build the lexer
        '''
        self.lexer = lex.lex(module=self, **kwargs)

        return self.lexer