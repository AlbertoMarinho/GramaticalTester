from lark import Lark, UnexpectedInput

grammar = r"""
    start: program
    program: command*
    command: assignment | if_stmt | while_stmt | do_while_stmt | return_stmt
    assignment: identifier "=" expression ";"
    expression: term (("+"|"-") term)*
    term: factor (("*"|"/") factor)*
    factor: identifier | number | "true" | "false" | "(" expression ")" | string
    if_stmt: "if" expression block else_block?
    else_block: "else" block
    block: "{" program "}"
    while_stmt: "while" expression block
    do_while_stmt: "do" block "while" expression ";"
    return_stmt: "return" expression ";"
    identifier: /[a-zA-Z_][a-zA-Z0-9_]*/
    number: /\d+/
    string: /"[^"]*"/
    %ignore /\/\/[^\n]*/
    %ignore /[ \t\r\n]+/  // Ignora espaços em branco e novas linhas
"""





parser = Lark(grammar, start="start", parser="lalr")

test_sentences = [
    "a = b + c;",  # Válida
    "if true { a = 1; } else { b = 2; }",  # Válida
    "while x { y = y * 2; }",  # Válida
    "do { x = x - 1; } while x;",  # Válida
    "return a + b * c;",  # Válida
    "a = 42 + ;",  # Inválida: operador sem operando à direita
    "if (x == 10) { y = y + 1; } else ;",  # Inválida: bloco else vazio
    "x = 10 + * 2;",  # Inválida: dois operadores consecutivos sem operando
    "while { x = x / 2; }",  # Inválida: condição de loop while ausente
    "do { x = x - 1; while x;",  # Inválida: falta de fechamento do bloco do while
    "return ;",  # Inválida: falta de expressão após return
    "if true { a = 1 }"  # Inválida: falta de ponto e vírgula após o comando
]


for sentence in test_sentences:
    try:
        print(f"Testando: {sentence}")
        tree = parser.parse(sentence)
        print("Valido!\n")
    except UnexpectedInput as e:
        print(f"Erro: {e}")
