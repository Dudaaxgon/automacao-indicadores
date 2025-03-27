import pandas as pd
from pathlib import Path

def carregar_dados():
    """Carrega os arquivos de dados (Emails, Vendas e Lojas) e organiza por loja."""

    # Definir caminho da pasta base do projeto
    base_path = Path(__file__).parent.parent / "data"

    # Importar bases de dados
    emails = pd.read_excel(base_path / "Emails.xlsx")
    lojas = pd.read_csv(base_path / "Lojas.csv", encoding="latin1", sep=";")
    vendas = pd.read_excel(base_path / "Vendas.xlsx")

    # Adicionar o nome da loja na tabela de vendas
    vendas = vendas.merge(lojas, on="ID Loja")

    # Criar um dicionário para separar os dados por loja
    dicionario_lojas = {loja: vendas[vendas["Loja"] == loja] for loja in lojas["Loja"]}

    # Identificar o dia mais recente nos dados de vendas
    dia_indicador = vendas["Data"].max()
    data_formatada = f"{dia_indicador.day}/{dia_indicador.month}"
    print(f"Data mais recente nos dados: {data_formatada}")

    return emails, vendas, lojas, dicionario_lojas, dia_indicador
