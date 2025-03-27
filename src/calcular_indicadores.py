import pathlib
import win32com.client as win32
from processar_dados import carregar_dados

# Carregar dados
emails, vendas, lojas, dicionario_lojas, dia_indicador = carregar_dados()

# Definir caminho de backup antes de usá-lo
caminho_backup = pathlib.Path('outputs')

# Definição de metas
meta_faturamento_dia = 1000
meta_faturamento_ano = 1650000
meta_qtdeprodutos_dia = 4
meta_qtdeprodutos_ano = 120
meta_ticketmedio_dia = 500
meta_ticketmedio_ano = 500

for loja in dicionario_lojas:
    vendas_loja = dicionario_lojas[loja]
    vendas_loja_dia = vendas_loja.loc[vendas_loja['data'] == dia_indicador, :]

    # Faturamento
    faturamento_ano = vendas_loja['Valor Final'].sum()
    faturamento_dia = vendas_loja_dia['Valor Final'].sum()

    # Diversidade de produtos
    qtde_produtos_ano = len(vendas_loja['Produto'].unique())
    qtde_produtos_dia = len(vendas_loja_dia['Produto'].unique())

    # Ticket médio
    valor_venda = vendas_loja.groupby('Código Venda').sum()
    ticket_medio_ano = valor_venda['Valor Final'].mean()
    valor_venda_dia = vendas_loja_dia.groupby('Código Venda').sum()
    ticket_medio_dia = valor_venda_dia['Valor Final'].mean()

    # Enviar o e-mail
    outlook = win32.Dispatch('outlook.application')

    # Verifica se a loja está no DataFrame de emails
    if loja in emails['Loja'].values:
        nome = emails.loc[emails['Loja'] == loja, 'Gerente'].values[0]
        email_destino = emails.loc[emails['Loja'] == loja, 'E-mail'].values[0]
    else:
        print(f"A loja {loja} não foi encontrada no DataFrame de e-mails.")
        continue  # Pula para a próxima loja se não encontrar no DataFrame

    mail = outlook.CreateItem(0)
    mail.To = email_destino
    mail.Subject = f'OnePage Dia {dia_indicador.day}/{dia_indicador.month} - Loja {loja}'

    # Determinação das cores com base nas metas
    cor_fat_dia = 'green' if faturamento_dia >= meta_faturamento_dia else 'red'
    cor_fat_ano = 'green' if faturamento_ano >= meta_faturamento_ano else 'red'
    cor_qtde_dia = 'green' if qtde_produtos_dia >= meta_qtdeprodutos_dia else 'red'
    cor_qtde_ano = 'green' if qtde_produtos_ano >= meta_qtdeprodutos_ano else 'red'
    cor_ticket_dia = 'green' if ticket_medio_dia >= meta_ticketmedio_dia else 'red'
    cor_ticket_ano = 'green' if ticket_medio_ano >= meta_ticketmedio_ano else 'red'

    mail.HTMLBody = f'''
    <p>Bom dia, {nome}</p>

    <p>O resultado de ontem <strong>({dia_indicador.day}/{dia_indicador.month})</strong> da <strong>Loja {loja}</strong> foi:</p>

    <table>
      <tr>
        <th>Indicador</th>
        <th>Valor Dia</th>
        <th>Meta Dia</th>
        <th>Cenário Dia</th>
      </tr>
      <tr>
        <td>Faturamento</td>
        <td style="text-align: center">R${faturamento_dia:.2f}</td>
        <td style="text-align: center">R${meta_faturamento_dia:.2f}</td>
        <td style="text-align: center"><font color="{cor_fat_dia}">◙</font></td>
      </tr>
      <tr>
        <td>Diversidade de Produtos</td>
        <td style="text-align: center">{qtde_produtos_dia}</td>
        <td style="text-align: center">{meta_qtdeprodutos_dia}</td>
        <td style="text-align: center"><font color="{cor_qtde_dia}">◙</font></td>
      </tr>
      <tr>
        <td>Ticket Médio</td>
        <td style="text-align: center">R${ticket_medio_dia:.2f}</td>
        <td style="text-align: center">R${meta_ticketmedio_dia:.2f}</td>
        <td style="text-align: center"><font color="{cor_ticket_dia}">◙</font></td>
      </tr>
    </table>
    <br>
    <table>
      <tr>
        <th>Indicador</th>
        <th>Valor Ano</th>
        <th>Meta Ano</th>
        <th>Cenário Ano</th>
      </tr>
      <tr>
        <td>Faturamento</td>
        <td style="text-align: center">R${faturamento_ano:.2f}</td>
        <td style="text-align: center">R${meta_faturamento_ano:.2f}</td>
        <td style="text-align: center"><font color="{cor_fat_ano}">◙</font></td>
      </tr>
      <tr>
        <td>Diversidade de Produtos</td>
        <td style="text-align: center">{qtde_produtos_ano}</td>
        <td style="text-align: center">{meta_qtdeprodutos_ano}</td>
        <td style="text-align: center"><font color="{cor_qtde_ano}">◙</font></td>
      </tr>
      <tr>
        <td>Ticket Médio</td>
        <td style="text-align: center">R${ticket_medio_ano:.2f}</td>
        <td style="text-align: center">R${meta_ticketmedio_ano:.2f}</td>
        <td style="text-align: center"><font color="{cor_ticket_ano}">◙</font></td>
      </tr>
    </table>

    <p>Segue em anexo a planilha com todos os dados para mais detalhes.</p>

    <p>Qualquer dúvida estou à disposição.</p>
    <p>Att., Lira</p>
    '''

    # Anexos (pode colocar quantos quiser):
    attachment = pathlib.Path.cwd() / caminho_backup / loja / f'{dia_indicador.month}_{dia_indicador.day}_{loja}.xlsx'
    mail.Attachments.Add(str(attachment))

    mail.Send()
    print(f'E-mail da Loja {loja} enviado')
