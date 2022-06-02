#https://www.beecrowd.com.br/judge/pt/problems/view/1238
#

for _ in int(input()):
    string_1, string_2 = input().split(' ')
    menor = len(string_1) if len(string_1) >= len(string_1) else len(string_2)
    string_1_mais_2 = ''
    for x in range(menor):
        string_1_mais_2 += ''
