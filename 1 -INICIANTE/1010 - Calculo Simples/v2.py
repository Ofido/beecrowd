#https://www.beecrowd.com.br/judge/pt/problems/view/1009
#0.024s

_, primeira_peca_qnt, primeira_peca_valor = map(float, input().split())
_, segunda_peca_qnt , segunda_peca_valor  = map(float, input().split())

valor_final = (primeira_peca_qnt * primeira_peca_valor) + (segunda_peca_qnt * segunda_peca_valor)

print(f"VALOR A PAGAR: R$ {valor_final:.2f}")