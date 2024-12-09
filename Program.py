from Lexer import AnalisadorLexico

def main():
    print("Bem-vindo ao analisador léxico!")
    codigo = input("Digite o código a ser analisado:\n")
    try:
        tokens = AnalisadorLexico(codigo)
        print("\nTokens gerados:")
        for tipo, valor in tokens:
            print(f"{tipo}: {valor}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == '__main__':
    main()