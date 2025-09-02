import csv
from collections import defaultdict
from datetime import datetime


entrada = 'sales_data.csv'

dados = []
with open (entrada, 'r', encoding='utf-8') as f:
    leitor = csv.DictReader(f, delimiter=',')
    for linha in leitor:
        produto = linha["Produto"]
        categoria = linha["Categoria"]
        preco = float(linha["Preço Unitário (R$)"])
        qtd = int(linha["Quantidade Vendida"])
        total = float(linha["Total de Vendas (R$)"])
        data = linha["Data da Venda"]
        dados.append({
            "produto": produto,
            "categoria": categoria,
            "preco": preco,
            "qtd": qtd,
            "total": total,
            "data": data
        })

# Resumo por Categoria
resumo_categoria = defaultdict(float)
for item in dados:
    resumo_categoria[item["categoria"]] += item["total"]

with open('resumo_categoria.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Categoria', 'Total Vendido (R$)'])
    for categoria, total in resumo_categoria.items():
        writer.writerow([categoria, f'{total:.2f}'])

print(resumo_categoria)


