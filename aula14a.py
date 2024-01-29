n = 1

par = impar = 0

while n != 0:
    n = int(input('Digite um valor.\n>>> '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1

print('Você digitou {} números pare(s) e digitou {} números ímpar(es).'.format(par, impar))
