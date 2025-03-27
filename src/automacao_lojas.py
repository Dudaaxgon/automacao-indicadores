
import pandas as pd

# Função para carregar dados (exemplo simples)
def carregar_dados():
    # Suponha que você tenha arquivos CSV com esses dados, ou crie dados fictícios para teste
    emails = pd.DataFrame({
        'Loja': ['Loja1', 'Loja2', 'Diretoria'],
        'Gerente': ['João', 'Maria', 'Carlos'],
        'E-mail': ['joao@email.com', 'maria@email.com', 'carlos@email.com']
    })

    vendas = pd.DataFrame({
        'Loja': ['Loja1', 'Loja2', 'Loja1'],
        'Produto': ['ProdutoA', 'ProdutoB', 'ProdutoC'],
        'Valor Final': [100, 200, 150],
        'Código Venda': [1, 2, 3],
        'data': ['2025-03-25', '2025-03-25', '2025-03-25']
    })

    lojas = ['Loja1', 'Loja2']
    dicionario_lojas = {
        'Loja1': vendas[vendas['Loja'] == 'Loja1'],
        'Loja2': vendas[vendas['Loja'] == 'Loja2']
    }

    # Aqui, você deve definir a data de hoje ou a data que está sendo usada
    dia_indicador = pd.to_datetime('2025-03-25')

    return emails, vendas, lojas, dicionario_lojas, dia_indicador
