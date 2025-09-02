# CSV Data Manipulation Exercise

Este repositório apresenta um exercício de manipulação de dados em CSV usando Python.

---
##  Descrição

O script `DataManipulation.py` processa o arquivo de vendas `sales_data.csv` para responder a três consultas analíticas:

1. **Resumo por categoria**  
   - Soma o total de vendas por categoria.  
   - Gera o arquivo: `resumo_categoria.csv`.

2. **Top 5 produtos mais vendidos por categoria**  
   - Agrega as vendas por produto dentro de cada categoria.  
   - Identifica os cinco produtos com maior faturamento em cada categoria.  
   - Salva o resultado em: `mais_vendidos.csv`.

3. **Mês com maior faturamento**  
   - Agrupa faturamento por mês de venda.  
   - Identifica o mês com maior valor total de vendas.  
   - Armazena o resultado em: `mes_campeao.csv`.

---

##  Estrutura de Arquivos

- `sales_data.csv` — Base de dados original contendo colunas como Produto, Categoria, Preço Unitário, Quantidade Vendida, Total de Vendas e Data da Venda.
- `DataManipulation.py` — Script Python que realiza a leitura, processamento e gravação conforme descrito.
- Saídas geradas pelo script:
  - `resumo_categoria.csv`
  - `mais_vendidos.csv`
  - `mes_campeao.csv`
