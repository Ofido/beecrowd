# Código gerado através da resolução por blocos

retorno = None
A = None
C = None
D = None
B = None
valores = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


retorno = True
valores = read_line().split(" ")
A = int((valores.pop(0)))
B = int((valores.pop(0)))
C = int((valores.pop(0)))
D = int((valores.pop(0)))
if B > C:
  if D > A:
    if C + D > A + B:
      if D >= 0:
        if C >= 0:
          if (A % 2) == 0:
            retorno = False
            print("Valores aceitos")
if retorno:
  print("Valores nao aceitos")
