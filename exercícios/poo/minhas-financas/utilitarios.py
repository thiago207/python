from categoria import Categoria
from transacao import Transacao

lista_categorias = []
lista_transacao = []

def cadastar_categoria(nome):
    nova_categoria = Categoria(nome=nome)

    lista_categorias.append(nova_categoria)

    return nova_categoria

def cadastrar_transacao(descricao,valor,categoria):
    nova_transacao = Transacao(
        descricao=descricao,
        valor=valor,
        categoria=categoria,
    )

    lista_transacao.append(nova_transacao)

    return nova_transacao

def salo_total():
    total = 0
    for t in lista_transacao:
        total += t.valor

    return total