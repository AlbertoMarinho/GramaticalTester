from lexer import AnalisadorLexico

def testeAnalisadorLexico():
    # Teste de tokens
    codigo = input("Digite o código a ser testado:\n")
    try:
        tokens = AnalisadorLexico(codigo)
        print("\nTokens válidos:")
        for token in tokens:
            print(token)
    except ValueError as error:
        print("\nErros encontrados:")
        print(error)

    # Teste de erro
    print("\nTeste com código inválido:")
    try:
        codigoInvalido = "a = 5 + 3 @ b"
        tokensInvalidos = AnalisadorLexico(codigoInvalido)
        print("Tokens inválidos:", tokensInvalidos)
    except ValueError as error:
        print("Erro esperado:", error)


testeAnalisadorLexico()

