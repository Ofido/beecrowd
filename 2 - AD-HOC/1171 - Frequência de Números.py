#https://www.beecrowd.com.br/judge/pt/problems/view/2896
# 0.152s

qnt = input()
apperars = {}
for _ in range(int(qnt)):
    aux = int(input())
    if apperars.get(aux, ""):
        apperars[aux] += 1
    else:
        apperars[aux] = 1

for keys in sorted(apperars):
    print(f"{keys} aparece {apperars[keys]} vez(es)")