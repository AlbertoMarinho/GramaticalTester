from lark import Lark, UnexpectedInput

grammar = r"""
    start: program
    program: command*
    command: assignment | ifstmt | while_stmt | do_while_stmt | return_stmt
    assignment: identifier "=" expression ";"
    expression: term (("+"|"-") term)*
    term: factor ((""|"/") factor)
    factor: identifier | number | "true" | "false" | "(" expression ")" | string
    if_stmt: "if" expression block else_block?
    else_block: "else" block
    block: "{" program "}"
    while_stmt: "while" expression block
    do_while_stmt: "do" block "while" expression ";"
    return_stmt: "return" expression ";"
    identifier: /[a-zA-Z][a-zA-Z0-9_]/
    number: /\d+/
    string: /"[^"]"/
    %ignore ///[^\n]/
    %ignore /[ \t\r\n]+/  // Ignora espaços em branco e novas linhas
"""



parser = Lark(grammar, start="start", parser="lalr")

test_sentences = [
    "a = b + c;",
    "if true { a = 1; } else { b = 2; }",
    "while x { y = y 2; }",
    "do { x = x - 1; } while x;",
    "return a + b * c;"
]


for sentence in test_sentences:
    try:
        print(f"Testando: {sentence}")
        tree = parser.parse(sentence)
        print("Valido!")
    except UnexpectedInput as e:
        print(f"Erro: {e}")