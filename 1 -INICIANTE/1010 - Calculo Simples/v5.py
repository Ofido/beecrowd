#https://www.beecrowd.com.br/judge/pt/problems/view/1009
#0.030s

pecas:list[dict()] = [{}, {}]
for ordem in range(2):
    _, pecas[ordem]['qnt'], pecas[ordem]['valor'] = map(float, input().split())

final_value = sum([peca['qnt'] * peca['valor'] for peca in pecas])

print(f"VALOR A PAGAR: R$ {(final_value):.2f}")