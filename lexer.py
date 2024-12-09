import re

def AnalisadorLexico(codigo):
    tokens = []

    # Definindo padrões de tokens
    padrao_identificador = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Identificadores podem começar com _ ou letra
    padrao_numero = r'\d+'  # Números inteiros
    padrao_operadores = r'[+\-*/=@]'  # Operadores aritméticos
    padrao_operadores_logicos = r'&&|\|\||!'  # Operadores lógicos
    padrao_strings = r'"[^"]*"'  # Strings entre aspas
    padrao_comentarios = r'//[^\n]*'  # Comentários de linha
    padrao_tipo = r'\b(int|float|bool)\b'  # Tipos de dados
    padrao_parenteses = r'[\(\)]'  # Parênteses
    padrao_chaves = r'[\{\}]'  # Chaves
    padrao_ponto_virgula = r';'  # Ponto e vírgula
    padrao_palavra_chave = r'\b(if|else|while|return)\b'

    # Remover espaços em branco
    codigo = codigo.strip()

    while codigo:
        codigo = codigo.strip()  # Remove espaços antes de cada iteração

        # Identifica comentários
        match = re.match(padrao_comentarios, codigo)
        if match:
            codigo = codigo[match.end():]  # Ignora o comentário
            continue

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

        # Identifica operadores aritméticos
        match = re.match(padrao_operadores, codigo)
        if match:
            tokens.append(('OPERADOR', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica operadores lógicos
        match = re.match(padrao_operadores_logicos, codigo)
        if match:
            tokens.append(('OPERADOR_LOGICO', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica strings
        match = re.match(padrao_strings, codigo)
        if match:
            tokens.append(('STRING', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica tipos de dados
        match = re.match(padrao_tipo, codigo)
        if match:
            tokens.append(('TIPO', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica parênteses
        match = re.match(padrao_parenteses, codigo)
        if match:
            tokens.append(('PARENTESES', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica chaves
        match = re.match(padrao_chaves, codigo)
        if match:
            tokens.append(('CHAVE', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Identifica ponto e vírgula
        match = re.match(padrao_ponto_virgula, codigo)
        if match:
            tokens.append(('PONTO_VIRGULA', match.group(0)))
            codigo = codigo[match.end():]
            continue

        match = re.match(padrao_palavra_chave, codigo)
        if match:
            tokens.append(('PALAVRA_CHAVE', match.group(0)))
            codigo = codigo[match.end():]
            continue

        # Caso haja algum caractere desconhecido
        raise ValueError(f"Token desconhecido encontrado: {codigo[0]}")

    return tokens