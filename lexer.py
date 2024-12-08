import re

def AnalisadorLexico(codigo):
    tokens = []

    # Definindo padrões de tokens
    padrao_identificador = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Identificadores podem começar com _ ou letra
    padrao_numero = r'\d+'  # Números
    padrao_operadores = r'[+\-*/=]'  # Operadores aritméticos
    padrao_parenteses = r'[\(\)]'  # Parênteses
    padrao_ponto_virgula = r';'  # Ponto e vírgula

    # Remover espaços em branco
    codigo = codigo.strip()

    while codigo:
        codigo = codigo.strip()  # Remove espaços antes de cada iteração

        # Identifica identificadores
        match = re.match(padrao_identificador, codigo)
        if match:
            tokens.append(('IDENTIFICADOR', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica números
        match = re.match(padrao_numero, codigo)
        if match:
            tokens.append(('NUMERO', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica operadores
        match = re.match(padrao_operadores, codigo)
        if match:
            tokens.append(('OPERADOR', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica parênteses
        match = re.match(padrao_parenteses, codigo)
        if match:
            tokens.append(('PARENTESES', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica ponto e vírgula
        match = re.match(padrao_ponto_virgula, codigo)
        if match:
            tokens.append(('PONTO_VIRGULA', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Caso haja algum caractere desconhecido
        raise ValueError(f"Token desconhecido encontrado: {codigo[0]}")

    return tokens
