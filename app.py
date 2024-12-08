from lexer import AnalisadorLexico

def testeAnalisadorLexico():
    #Teste de tokens

    codigo = input("Digite o Código a ser testado\n")
    tokens = AnalisadorLexico(codigo)

    print("Testando tokens")
    print("Tokens:", tokens)

    #Teste de erro

    try:
        codigoInvalido = "a = 5 + 3 @ b"
        tokensInvalidos = AnalisadorLexico(codigoInvalido)
        print("\nTokens inválidos: ", tokensInvalidos)
    except ValueError as error:
        print("\nErro esperado:", error)



testeAnalisadorLexico()