def origem_destino_iguais(origem, destino, lista_de_erros):
    """Verifica se origem e destino são iguais"""
    if origem == destino:
        lista_de_erros['destino'] = 'Origem e destino não podem ser iguais'


def campo_tem_algum_numero(valor_campo, nome_campo, lista_de_erros):
    """Verifica se há algum número no campo"""
    if any(char.isdigit() for char in valor_campo):
        lista_de_erros[nome_campo] = str(nome_campo) + ': Não inclua números'
