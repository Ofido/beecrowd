import timeit

print(timeit.timeit("''.join([str(x) for x in [horas, ':', minutos, ':', segundos]])",number=1000000))
print(timeit.timeit("str(horas) + ':' + str(minutos) + ':' + str(segundos)",number=1000000))