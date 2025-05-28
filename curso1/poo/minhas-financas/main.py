from categoria import Categoria
from transacao import Transacao
from utilitarios import cadastar_categoria, cadastrar_transacao, salo_total

#categorias
Categoria_receitas = cadastar_categoria('Receitas')
Categoria_contas = cadastar_categoria('Contas Fixas')
Categoria_viagens = cadastar_categoria('Viagens')
Categoria_lazer = cadastar_categoria('Lazer')
#transacoes
cadastrar_transacao(
    descricao='salario abril/2025',
    valor=1000,
    categoria=Categoria_receitas
) 
cadastrar_transacao(
    descricao='Mesada mae',
    valor=50,
    categoria=Categoria_receitas
)
cadastrar_transacao(
    descricao='Ingresso do show',
    valor=-150,
    categoria=Categoria_lazer
) 
cadastrar_transacao(
    descricao='Contas de luz',
    valor=-200,
    categoria=Categoria_contas
)
cadastrar_transacao(
    descricao='Viagem disney',
    valor=-400,
    categoria=Categoria_contas
)
total = salo_total()

print(f'Saldo total: {total}')