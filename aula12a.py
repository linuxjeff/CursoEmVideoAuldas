# deseja bom dia
# v0.0.1
#   - inicio
#   - Variaveis e if

nome = str(input('Qual é seu nome?\n>>> '))

if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem pupular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(nome))
