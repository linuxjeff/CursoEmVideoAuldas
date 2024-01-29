galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.clear()
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'temos {totmai} maiores e {totmen} menores de idade.')