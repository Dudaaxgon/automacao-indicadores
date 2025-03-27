from processar_dados import carregar_dados

# Chama a função para carregar os dadoss
emails, vendas, lojas, dicionario_lojas, dia_indicador = carregar_dados()

# Exibir os primeiros registros de cada DataFrame
print("\nPrimeiros registros dos e-mails:")
print(emails.head())

print("\nPrimeiros registros das vendas:")
print(vendas.head())

print("\nDicionário de lojas criado com sucesso!")
print(f"Temos dados de {len(dicionario_lojas)} lojas.")
