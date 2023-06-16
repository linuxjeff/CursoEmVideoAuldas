# Variáveis
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# Execução

print('A soma é {}, \no produto é {} e a divisão é {:.2f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
