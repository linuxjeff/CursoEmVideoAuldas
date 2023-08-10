Nota1 = float(input('Digite a primeira nota: '))
Nota2 = float(input('Digite a segunda nota: '))
Media = (Nota1 + Nota2)/2
print('A sua méida foi {:.1f}'.format(Media))
if Media >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
