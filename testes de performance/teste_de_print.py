import timeit
from datetime import datetime

horas:int = 5
minutos:int = 10
segundos:int = 40

variables:dict[str, int] = {
    'horas':horas,
    'minutos':minutos,
    "segundos":segundos
}
quantidade_de_testes:list[int] = [1]
total_time:list[int] = [1]

tests:dict[str, list[float]] = {
    "''.join([str(x) for x in [horas, ':', minutos, ':', segundos]])"                           : [],
    "str(horas) + ':' + str(minutos) + ':' + str(segundos)"                                     : [],
    "f\"{horas}:{minutos}:{segundos}\""                                                         : [],
    "\"{horas}:{minutos}:{segundos}\".format(horas=horas, minutos=minutos, segundos=segundos)"  : [],
    "(\"{0}:{1}:{2}\").format(horas, minutos, segundos)"                                        : [],
    "(\"{}:{}:{}\").format(horas, minutos, segundos)"                                           : [],
    "\"%s:%s:%s\" % (horas, minutos, segundos)"                                                 : [],
}

print("validação")
for test in list(tests): # executando os testes
    eval(f"print({test})")

resultado:list[str] = []

rodada:int = 0
tempo_total:datetime = datetime.now() # inicia o timer geral de contagem de tempo

while True:

    # verificando se ainda existem testes para rodar
    if len(tests) == 1:
        for test in list(tests):
            tempo_do_teste = sum(tests[test])
            resultado.append(f"{test} - tempo total: {tempo_do_teste} - tempo da ultima execução: {tests[test][-1]} - rodada: {rodada} - quantidade_de_testes: {quantidade_de_testes}")
        break

    tempo_inicio:datetime = datetime.now() # inicia o timer

    for test in list(tests): # executando os testes
        tests[test].append(timeit.timeit(test,number=quantidade_de_testes[rodada],globals=variables))

    # lidando com o tempo da rodada e o tempo parcial
    tempo_fim = datetime.now()
    final = tempo_fim - tempo_inicio
    final_parcial = tempo_fim - tempo_total

    # print da rodada
    print(f"rodada - {rodada} - tempo da rodada: {final} - tempo total parcial: {final_parcial} - numero de testes {quantidade_de_testes[rodada]}")
    print(f"validação {final.total_seconds()}")
    if final.total_seconds() > 5: # se o tempo for maior que 10 minutos remove o pior de todos e mantêm o mesmo número de testes;
        pior_tempo = 0
        excluir = ''

        for test in list(tests):
            tempo_total_do_teste = sum(tests[test])
            if tempo_total_do_teste > pior_tempo:
                pior_tempo, excluir, ultima_rodada = tempo_total_do_teste, test, tests[test][-1]

        resultado.append(f"{excluir} - tempo total: {pior_tempo} - tempo da ultima execução: {ultima_rodada} - rodada: {rodada} - quantidade_de_testes: {quantidade_de_testes.copy()}")
        print(f"{excluir} - tempo total: {pior_tempo} - tempo da ultima execução: {ultima_rodada} - rodada: {rodada} - quantidade_de_testes: {quantidade_de_testes.copy()}")
        del tests[excluir]
        # usando continue para não incrementar mais o numero de testes
        continue

    # acrescentado o numero de testes e a variável rodada
    quantidade_de_testes.append(quantidade_de_testes[rodada] * 10)
    rodada = len(quantidade_de_testes) - 1

tempo_final = datetime.now()
tempo_total_final = tempo_final - tempo_total

print(f"O teste demorou {tempo_total_final}")
print('\n'.join(resultado))
print(quantidade_de_testes)
