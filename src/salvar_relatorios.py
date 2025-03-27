import pathlib

def salvar_relatorios(dicionario_lojas, dia_indicador):
    """Salva os relatórios de vendas das lojas em pastas organizadas por loja."""

    # Criar diretório de backup se não existir
    caminho_backup = pathlib.Path("Backup Arquivos Lojas")
    caminho_backup.mkdir(exist_ok=True)

    for loja, dados_loja in dicionario_lojas.items():
        # Criar pasta da loja se não existir
        pasta_loja = caminho_backup / loja
        pasta_loja.mkdir(exist_ok=True)

        # Criar nome do arquivo com data
        nome_arquivo = f"{dia_indicador.month}_{dia_indicador.day}_{loja}.xlsx"
        local_arquivo = pasta_loja / nome_arquivo

        # Salvar o arquivo Excel
        dados_loja.to_excel(local_arquivo, index=False)

        print(f"Relatório salvo: {local_arquivo}")

