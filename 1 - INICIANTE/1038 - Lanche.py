#https://www.beecrowd.com.br/judge/pt/problems/view/1038

def produto(id):
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

id, qnt = input().split()
prc = produto(int(id))
total = prc*int(qnt)
print(f"Total: R$ {total:.2f}")