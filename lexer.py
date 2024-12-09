import re

def AnalisadorLexico(codigo):
    tokens = []
    erros = []  # Lista para capturar erros

    # Definindo padrões de tokens
    padrao_identificador = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Identificadores podem começar com _ ou letra
    padrao_numero = r'\d+'  # Números inteiros
    padrao_operadores = r'[+\-*/=]'  # Operadores aritméticos
    padrao_operadores_logicos = r'(\|\||&&|!)'  # Operadores lógicos (||, &&, !)
    padrao_strings = r'"[^"]*"'  # Strings entre aspas
    padrao_comentarios = r'//[^\n]*'  # Comentários de linha
    padrao_tipo = r'\b(int|float|bool|double)\b'  # Tipos de dados
    padrao_parenteses = r'[\(\)]'  # Parênteses
    padrao_ponto_virgula = r';'  # Ponto e vírgula
    padrao_palavra_chave = r'\b(if|else|while|return|do)\b'
    padrao_comparacao = r'(==|!=|<=|>=)'  # Comparações == e !=
    padrao_delimitadores = r'[\{\}:]'  # Delimitadores: {, }, :
    padrao_booleano = r'\b(true|false)\b'  # Booleanos

    # Remover espaços em branco
    codigo = codigo.strip()
    posicao = 0  # Posição inicial do analisador

    while codigo:
        codigo = codigo.strip()
        match = None

        # Testa cada padrão
        for padrao, tipo in [
            (padrao_comentarios, 'COMENTARIOS'),
            (padrao_numero, 'NUMERO'),
            (padrao_comparacao, 'COMPARACAO'),
            (padrao_operadores, 'OPERADOR'),
            (padrao_operadores_logicos, 'OPERADOR_LOGICO'),
            (padrao_strings, 'STRING'),
            (padrao_tipo, 'TIPO'),
            (padrao_parenteses, 'PARENTESES'),
            (padrao_ponto_virgula, 'PONTO_VIRGULA'),
            (padrao_palavra_chave, 'PALAVRA_CHAVE'),
            (padrao_booleano, 'BOOLEANO'),
            (padrao_identificador, 'IDENTIFICADOR'),
            (padrao_delimitadores, 'DELIMITADOR')
        ]:
            match = re.match(padrao, codigo)
            if match:
                if tipo:  # Apenas adiciona tokens relevantes
                    tokens.append((tipo, match.group(0), posicao))
                break

        if match:
            posicao += match.end()
            codigo = codigo[match.end():]
        else:
            erros.append(f"Token desconhecido '{codigo[0]}' na posição {posicao}")
            codigo = codigo[1:]
            posicao += 1

    if erros:
        raise ValueError("\n".join(erros))

    return tokens