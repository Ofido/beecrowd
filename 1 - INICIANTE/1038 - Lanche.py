#https://www.beecrowd.com.br/judge/pt/problems/view/1038

def produto(id) -> float:
    if id == 1:
        return 4
    if id == 2:
        return 4.5
    if id == 3:
        return 5
    if id == 4:
        return 2
    if id == 5:
        return 1.5
    return 0.0

id, qnt = map(int, input().split())
prc = produto(id)
total = prc*qnt
print(f"Total: R$ {total:.2f}")
