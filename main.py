from Lexer.Lexer import Lexer

lexer = Lexer().build()
lexer.input("a x = 3 CONST else wtf ] &&")
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
