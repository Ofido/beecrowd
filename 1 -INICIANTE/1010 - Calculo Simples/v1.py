#https://www.beecrowd.com.br/judge/pt/problems/view/1009
#0.046s
#0.110s -> vide doc

_, primeira_peca_qnt, primeira_peca_valor = map(float, input().split())
_, segunda_peca_qnt , segunda_peca_valor  = map(float, input().split())

print(f"VALOR A PAGAR: R$ {((primeira_peca_qnt * primeira_peca_valor) + (segunda_peca_qnt * segunda_peca_valor)):.2f}")