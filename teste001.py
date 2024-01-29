# Importando Libs
from random import randint
###
# Variáveis iniciais
Numeros = list()
###
# Código para receber os números.
Casou = int(0)
Contador = int(0)
while Contador != 6:
    NovoNumero = randint(1, 60)
    for Duplicado in Numeros:
        if Duplicado == NovoNumero:
            Casou = Duplicado
    if Casou != NovoNumero:
        Numeros.append(NovoNumero)
        Contador += 1
###
# Mostrar resultado ordenado
Numeros.sort()
for Sena in Numeros:
      print(Sena, end=' ')
###