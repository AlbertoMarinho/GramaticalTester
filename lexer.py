import re

PADROES_TOKENS = [
    ('PALAVRA_CHAVE', r'\b(if|while|for)\b'),  # Palavras-chave
    ('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*'),  # Identificadores
    ('NUMERO', r'\d+'),  # Números
    ('OPERADOR', r'[+\-*/=]'),  # Operadores aritméticos
    ('PARENTESES', r'[\(\)]'),  # Parênteses
    ('PONTO_VIRGULA', r';'),  # Ponto e vírgula
    ('STRING', r'(["\'])(?:\\.|[^\\])*?\1'),  # Strings com aspas simples ou duplas
    ('ESPACO', r'\s+'),  # Espaços em branco
    ('COMENTARIO', r'#.*'),  # Comentários
]

def obterToken(codigo):
    """
    Tenta encontrar o próximo token no código.
    """
    for tipo, padrao in PADROES_TOKENS:
        match = re.match(padrao, codigo)
        if match:
            # Retorna tipo, valor do token, e tamanho correspondente
            return tipo, match.group(0), match.end()
    return None, None, None

def AnalisadorLexico(codigo):
    """
    Analisa o código fornecido e retorna uma lista de tokens.
    """
    tokens = []
    posicao = 0
    while codigo:
        codigo = codigo.lstrip()  # Remove espaços em branco iniciais
        tipo, valor, tamanho = obterToken(codigo)
        if tipo is None:
            raise ValueError(f"Token desconhecido '{codigo[0]}' na posição {posicao}")
        if tipo not in ['ESPACO', 'COMENTARIO']:  # Ignorar espaços e comentários
            tokens.append((tipo, valor))
        posicao += tamanho
        codigo = codigo[tamanho:]  # Avança no código analisado
    return tokens