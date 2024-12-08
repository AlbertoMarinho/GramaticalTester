import re

def AnalisadorLexico(codigo):
    tokens = []

    # Definindo padrões de tokens
    padraoIdentificador = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Identificadores podem começar com _ ou letra
    padraoNumero = r'\d+'  # Números
    padraoOperadores = r'[+\-*/=]'  # Operadores aritméticos
    padraoParenteses = r'[\(\)]'  # Parênteses
    padraoPontoVirgula = r';'  # Ponto e vírgula

    # Remover espaços em branco
    codigo = codigo.strip()

    while codigo:
        codigo = codigo.strip()  # Remove espaços antes de cada iteração

        # Identifica identificadores
        match = re.match(padraoIdentificador, codigo)
        if match:
            tokens.append(('IDENTIFICADOR', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica números
        match = re.match(padraoNumero, codigo)
        if match:
            tokens.append(('NUMERO', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica operadores
        match = re.match(padraoOperadores, codigo)
        if match:
            tokens.append(('OPERADOR', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica parênteses
        match = re.match(padraoParenteses, codigo)
        if match:
            tokens.append(('PARENTESES', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica ponto e vírgula
        match = re.match(padraoPontoVirgula, codigo)
        if match:
            tokens.append(('PONTO_VIRGULA', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Caso haja algum caractere desconhecido
        raise ValueError(f"Token desconhecido encontrado: {codigo[0]}")

    return tokens
