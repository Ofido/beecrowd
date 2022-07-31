#https://www.beecrowd.com.br/judge/pt/problems/view/1013
#tempo limite atingido

A, B, C = list(map(int, input().split()))

while True:
    if A > C and A > B:
        print(f'{A} é o maior')
        break

    if B > C:
        print(f'{B} é o maior')
        break

    print(f'{C} é o maior')