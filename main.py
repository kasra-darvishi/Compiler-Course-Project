from lexer.Lexer import Lexer
from parserr.Yacc import Yacc

# lexer = Lexer().build()
f = open("samples/sample1.txt", "r")
# lexer.input(f.read())
# fo = open("foo.txt", "w")
#
# fo.write("RegEx    Token    AttVal\n")
# while True:
#     tok = lexer.token()
#     if not tok:
#         break  # No more input
#     index = "-"
#     if tok.type == 'ID':
#         index = Lexer.sTable.index(tok.value)
#     if tok.type == 'Num':
#         index = tok.value
#     fo.write(str(tok.value) + "    " + str(tok.type) + "    " +  str(index) + "\n")
#     print(tok)

y = Yacc()
lexer = Lexer()
y.build().parse(f.read(), lexer.build(), True)

# fo.close()