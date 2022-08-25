import timeit

soma_de_lista_com_if = '''
def foo(bar):
    if bar%2:
        return {'is_impar': False, 'value': bar}
    return {}
output = []
for i in range(10000):
    value = foo(i)
    if value:
        output += [value]
'''
soma_de_lista_inline_if = '''
def foo(bar):
    if bar%2:
        return {'is_impar': False, 'value': bar}
    return {}
output = []
for i in range(10000):
    value = foo(i)
    output += [value] if value else []
'''
append_de_lista_com_if = '''
def foo(bar):
    if bar%2:
        return {'is_impar': False, 'value': bar}
    return {}
output = []
for i in range(10000):
    value = foo(i)
    if value:
        output.append(value)
'''

print(timeit.timeit(soma_de_lista_com_if,number=1000)) # 4.9563971
print(timeit.timeit(soma_de_lista_inline_if,number=1000)) # 5.1483522
print(timeit.timeit(append_de_lista_com_if,number=1000)) # 4.384740300000001
