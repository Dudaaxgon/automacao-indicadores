
import pandas as pd
from gerar_ranking import gerar_ranking, gerar_ranking_ano, gerar_ranking_dia


def gerar_ranking(vendas):
    """
    Função que gera o ranking de lojas com base em faturamento,
    para o dia ou para o ano, dependendo dos dados fornecidos.
    """
    # Suponha que 'vendas' seja um DataFrame com os dados de vendas
    # Agrupar por loja e calcular o faturamento
    faturamento_lojas=vendas.groupby('Loja')['Valor Final'].sum()

    # Ordenar o faturamento de forma decrescente (da maior para a menor)
    faturamento_lojas_ordenado=faturamento_lojas.sort_values(ascending = False)

    return faturamento_lojas_ordenado


def gerar_ranking_ano(vendas, ano):
    """
    Função que gera o ranking anual de lojas com base no faturamento.
    """
    # Filtrar vendas pelo ano
    vendas_ano=vendas[pd.to_datetime(vendas['data']).dt.year == ano]

    # Chamar a função de ranking
    return gerar_ranking(vendas_ano)


def gerar_ranking_dia(vendas, dia):
    """
    Função que gera o ranking diário de lojas com base no faturamento.
    """
    # Filtrar vendas pelo dia
    vendas_dia=vendas[pd.to_datetime(vendas['data']).dt.date == dia]

    # Chamar a função de ranking
    return gerar_ranking(vendas_dia)

    # Gerar ranking do dia
    ranking_dia = gerar_ranking_dia(vendas, dia_indicador.date())

    # Gerar ranking do ano
    ranking_ano = gerar_ranking_ano(vendas, dia_indicador.year)
