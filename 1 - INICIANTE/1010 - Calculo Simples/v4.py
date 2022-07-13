#https://www.beecrowd.com.br/judge/pt/problems/view/1009
#0.075s

pecas:list[dict()] = [{}, {}]
for ordem in range(2):
    _, pecas[ordem]['qnt'], pecas[ordem]['valor'] = map(float, input().split())

final_list = [peca['qnt'] * peca['valor'] for peca in pecas]

print(f"VALOR A PAGAR: R$ {(sum(final_list)):.2f}")