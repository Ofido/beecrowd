#https://www.beecrowd.com.br/judge/pt/problems/view/1103
#

while True:
    hora_que_dormiu, minuto_que_dormiu, hora_de_acordar, minuto_de_acordar = list(map(int, input().split()))

    if hora_que_dormiu + minuto_que_dormiu + hora_de_acordar + minuto_de_acordar == 0:
        break

    tempo_de_sono = 0
    tempo_que_dormiu = minuto_que_dormiu + hora_que_dormiu*60
    tempo_de_acordar = minuto_de_acordar + hora_de_acordar*60

    tempo_dormido = tempo_de_acordar - tempo_que_dormiu

    if tempo_dormido <= 0:
        tempo_dormido += (60 + 23*60)

    print(tempo_dormido)