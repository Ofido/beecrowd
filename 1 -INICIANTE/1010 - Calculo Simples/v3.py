#https://www.beecrowd.com.br/judge/pt/problems/view/1009
#0.028s

pecas:list[dict()] = [{}, {}]
for ordem in range(2):
    _, pecas[ordem]['qnt'], pecas[ordem]['valor'] = map(float, input().split())

print(f"VALOR A PAGAR: R$ {(sum([peca['qnt'] * peca['valor'] for peca in pecas])):.2f}")