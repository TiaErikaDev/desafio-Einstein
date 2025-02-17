import pandas as pd

df = pd.read_csv('dataAnalysis/vendas_simuladas.csv')


# Cálculo do faturamento do produto
df['faturamento'] = df['quantidade'] * df['preco_unitario']

# Agrupando o faturamento por produtos
faturamento_por_produto = df.groupby("produto", as_index=False)["faturamento"].sum()


# Encontrando o produto com maior e menor faturamento
produto_maior_faturamento = faturamento_por_produto.loc[faturamento_por_produto['faturamento'].idxmax()]
produto_menor_faturamento = faturamento_por_produto.loc[faturamento_por_produto['faturamento'].idxmin()]

print("Faturamento total por produto:\n", faturamento_por_produto)

print(f"\nProduto com MAIOR faturamento: {produto_maior_faturamento.produto} - R$ {produto_maior_faturamento.faturamento:.2f}")
print(f"Produto com MENOR faturamento: {produto_menor_faturamento.produto} - R$ {produto_menor_faturamento.faturamento:.2f}")