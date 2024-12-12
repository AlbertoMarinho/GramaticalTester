import re

def AnalisadorLexico(codigo):
    tokens = []
    erros = []

    padroes = {
        'NUMERO': re.compile(r'\d+'),
        'COMPARACAO': re.compile(r'(==|!=|<=|>=)'),
        'OPERADOR': re.compile(r'[+\-*/=]'),
        'OPERADOR_LOGICO': re.compile(r'(\|\||&&|!)'),
        'STRING': re.compile(r'"[^"]*"'),
        'TIPO': re.compile(r'\b(int|float|bool|double)\b'),
        'PARENTESES': re.compile(r'[\(\)]'),
        'PONTO_VIRGULA': re.compile(r';'),
        'PALAVRA_CHAVE': re.compile(r'\b(if|else|while|return|do)\b'),
        'BOOLEANO': re.compile(r'\b(true|false)\b'),
        'IDENTIFICADOR': re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*'),
        'DELIMITADOR': re.compile(r'[\{\}:]')
    }

    codigo = codigo.strip()
    posicao = 0

    while codigo:
        codigo = codigo.strip()
        match = None

        for tipo, padrao in padroes.items():
            match = padrao.match(codigo)
            if match:
                tokens.append((tipo, match.group(0), posicao))
                break

        if match:
            posicao += match.end()
            codigo = codigo[match.end():]
        else:
            erros.append(f"Token desconhecido '{codigo[0]}' na posição {posicao}")
            codigo = codigo[1:]
            posicao += 1

    tokens.append(('EOF', '', posicao))

    if erros:
        raise ValueError("\n".join(erros))

    return tokens