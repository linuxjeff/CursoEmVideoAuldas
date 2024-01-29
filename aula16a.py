from random import randint

Fuzileiro = ('Fuzileiro', 20, 8, 'Fuzil', 1, 6)
Engenheiro = ('Engenheiro', 18, 10, 'Pistola', 2, 3)
# Armas Especiais
Granada = (25, 3, 8)
DanoGranada = Granada[0]
NumerosGranadas = Granada[1]
PAGranada = Granada[2]
###

RGranada = randint(1, 3)

Classeplayer = str('')
Vida = int(0)
PontoDeAcao = int(0)
Arma = str('')
Dano = int(0)
Hit = int(0)

Ganua = ('Ganua', 16, 10, 'Garra', 3, 2)
Hulk = ('Hulk', 20, 5, 'Soco Forte', 5, 3)
Enemy = ()
EPAMinimo = int(0)
EscolhaInimigo = randint(1, 2)

if EscolhaInimigo == 1:
    Enemy = Ganua
elif EscolhaInimigo == 2:
    Enemy = Hulk

NomeCerto = str('')

Player = str(input('Qual seu nome?\n>>> ')).capitalize().strip()

while NomeCerto != 'S':
    NomeCerto = str('')
    NomeCerto = str(input(f'O nome digitado foi {Player}.'
                          f'\nVocê quer este nome mesmo?\n[S/N]\n>>> ')).upper().strip()[0]
    if NomeCerto == 'N':
        Player = str(input('Qual seu nome?\n>>> ')).capitalize().strip()

while True:
    Classe = str(input('Qual a sua classe?\n1 - Fuzileiro\n2 - Engenheiro\n>>> '))

    if Classe == '1' or Classe == '2':
        Classe = int(Classe)
    else:
        print('Voce escolheu uma classe invalida!\nTente novamente')

    if Classe == 1:
        Classeplayer = Fuzileiro[0]
        Vida = Fuzileiro[1]
        PontoDeAcao = Fuzileiro[2]
        Arma = Fuzileiro[3]
        Dano = Fuzileiro[4]
        Hit = Fuzileiro[5]
        break
    elif Classe == 2:
        Classeplayer = Engenheiro[0]
        Vida = Engenheiro[1]
        PontoDeAcao = Engenheiro[2]
        Arma = Engenheiro[3]
        Dano = Engenheiro[4]
        Hit = Engenheiro[5]
        break
    print(Vida)


print(Vida)
Vida = Fuzileiro[1]
print(Vida)

ENome = Enemy[0]
EVida = Enemy[1]
EPA = Enemy[2]
EArma = Enemy[3]
Edano = Enemy[4]
EHit = Enemy[5]

PontoAcaoInicial = PontoDeAcao
EPAinicial = EPA

while Vida > 0 and EVida > 0:
    print(f'Vida {Player} = HP: {Vida} | Vida {ENome} = HP: {EVida}')
    print(f'Você tem {RGranada} Granadas.\n Cada Arma especial gasta 8 PA.')
    print(f'Seu PA: {PontoDeAcao}')
    EscolhaTurno = int(input(f'Escolha Ação ↓\n1 - Atacar = {Arma}\n2 - Granada\n3 - Pular turno\n>>> '))
    if EscolhaTurno == 1:
        if PontoDeAcao <= 0:
            print('Seu PA acabou, aguarde um turno para recaregar.')
        elif PontoDeAcao > 0:
            PontoDeAcao -= 1
            DanoReal = randint(0, Dano)
            HitReal = randint(0, Hit)
            DanoE = DanoReal * HitReal
            EVida -= DanoE
            print(f'Você causou {DanoE} ao {ENome}')
    elif EscolhaTurno == 3:
        RecargaDePA = randint(1, 3)
        PontoDeAcao += RecargaDePA
        if PontoDeAcao >= PontoAcaoInicial:
            PontoDeAcao = PontoAcaoInicial
    elif EscolhaTurno == 2:
        if PontoDeAcao <= 7:
            print('Você não tem PA para usar a Arma especial.')
        else:
            DanoReal = randint(1, DanoGranada)
            DanoE = DanoReal
            RGranada -= 1
            PontoDeAcao -= 8
            EVida -= DanoE
            print(f'Você jogou uma granada que casou o dano de {DanoE} ao {ENome}')

    if EPA > EPAMinimo:
        EPA -= 1
        Edanoreal = randint(0, Edano)
        Ehitreal = randint(0 , EHit)
        DanoP = Edanoreal * Ehitreal
        Vida -= DanoP
        print(f'O {ENome} casou {DanoP} dano em você.')
    elif EPA <= 0:
        ERecargaPA = randint(1, 3)
        EPA += ERecargaPA
        if EPA >= EPAinicial:
            EPA = EPAinicial

if Vida <= 0:
    print(f'O {Classeplayer} {Player} morreu em batalha para o {ENome}! :(')
elif EVida <= 0:
    print('Você ganohu!')
