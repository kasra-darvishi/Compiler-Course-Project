from lexer.Lexer import Lexer

lexer = Lexer().build()
lexer.input("a x = 333 CONST else wtf ] ee33 && Boolean true //gg ggg$%^$%^cc\n%")
fo = open("foo.txt", "w")

fo.write("RegEx    Token    AttVal\n")
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    index = "-"
    if tok.type == 'ID':
        index = Lexer.sTable.index(tok.value)
    if tok.type == 'Num':
        index = tok.value
    fo.write(str(tok.value) + "    " + str(tok.type) + "    " +  str(index) + "\n")
    print(tok)

fo.close()
