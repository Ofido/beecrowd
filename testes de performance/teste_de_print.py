import timeit

horas = 5
minutos = 10
segundos = 40

print(timeit.timeit("''.join([str(x) for x in [horas, ':', minutos, ':', segundos]])",number=100000000,globals={'horas':horas, 'minutos':minutos, "segundos":segundos}))
print(timeit.timeit("str(horas) + ':' + str(minutos) + ':' + str(segundos)",number=100000000,globals={'horas':horas, 'minutos':minutos, "segundos":segundos}))
print(timeit.timeit("f\"{horas} + ':' + {minutos} + ':' + {segundos}\"",number=100000000,globals={'horas':horas, 'minutos':minutos, "segundos":segundos}))