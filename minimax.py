from random import randrange

class Jogador:
    def __init__(self):
        nome = str(input("Diga seu nome:\t")).capitalize()
        self.nome = nome

        while True:
            try:
                letra = str(input('Escolha "X" ou "O":\t')).upper()
                self.letra = letra[0]
            except self.letra != "X" and self.letra != "O":
                print("Letra invalida")
            else:
                break

def mostrarQuadro(quadro):
    print(quadro[1] + '|' + quadro[2] + '|' + quadro[3])
    print('-+-+-')
    print(quadro[4] + '|' + quadro[5] + '|' + quadro[6])
    print('-+-+-')
    print(quadro[7] + '|' + quadro[8] + '|' + quadro[9])
    print("\n")


def livre(pos):
    if quadro[pos] == ' ':
        return True
    else:
        return False


def inserir(letra, pos):
    if livre(pos):
        quadro[pos] = letra
        mostrarQuadro(quadro)
        if (empate()):
            print("Empate!")
            file = open("log.txt", "a")
            file.write(f'{jogador.nome} empatou com o computador usando "{jogador.letra}"!\n')
            exit()
        if vitoria():
            if letra != jogador.letra:
                print("Computador venceu!")
                file = open("log.txt", "a")
                file.write(f'{jogador.nome} perdeu para o computador usando "{jogador.letra}"!\n')
                exit()
            else:
                print(f"{jogador.nome} venceu!")
                file = open("log.txt", "a")
                file.write(f'{jogador.nome} ganhou do computador usando "{jogador.letra}"!\n')
                exit()

        return


    else:
        print("Posicao invalida!")
        pos = int(input("Diga outra posicao:  "))
        inserir(letra, pos)
        return


def vitoria():
    if (quadro[1] == quadro[2] and quadro[1] == quadro[3] and quadro[1] != ' '):
        return True
    elif (quadro[4] == quadro[5] and quadro[4] == quadro[6] and quadro[4] != ' '):
        return True
    elif (quadro[7] == quadro[8] and quadro[7] == quadro[9] and quadro[7] != ' '):
        return True
    elif (quadro[1] == quadro[4] and quadro[1] == quadro[7] and quadro[1] != ' '):
        return True
    elif (quadro[2] == quadro[5] and quadro[2] == quadro[8] and quadro[2] != ' '):
        return True
    elif (quadro[3] == quadro[6] and quadro[3] == quadro[9] and quadro[3] != ' '):
        return True
    elif (quadro[1] == quadro[5] and quadro[1] == quadro[9] and quadro[1] != ' '):
        return True
    elif (quadro[7] == quadro[5] and quadro[7] == quadro[3] and quadro[7] != ' '):
        return True
    else:
        return False


def pVitoria(p):
    if (quadro[1] == quadro[2] and quadro[1] == quadro[3] and quadro[1] == p):
        return True
    elif (quadro[4] == quadro[5] and quadro[4] == quadro[6] and quadro[4] == p):
        return True
    elif (quadro[7] == quadro[8] and quadro[7] == quadro[9] and quadro[7] == p):
        return True
    elif (quadro[1] == quadro[4] and quadro[1] == quadro[7] and quadro[1] == p):
        return True
    elif (quadro[2] == quadro[5] and quadro[2] == quadro[8] and quadro[2] == p):
        return True
    elif (quadro[3] == quadro[6] and quadro[3] == quadro[9] and quadro[3] == p):
        return True
    elif (quadro[1] == quadro[5] and quadro[1] == quadro[9] and quadro[1] == p):
        return True
    elif (quadro[7] == quadro[5] and quadro[7] == quadro[3] and quadro[7] == p):
        return True
    else:
        return False


def empate():
    for key in quadro.keys():
        if (quadro[key] == ' '):
            return False
    return True


def jogadorMovi():
    pos = int(input("Entre uma posicao:  "))
    inserir(jogador.letra, pos)
    return


def computadorMovi():
    mPont = -800
    mMovi = 0
    for key in quadro.keys():
        if (quadro[key] == ' '):
            quadro[key] = computador
            pont = minimax(quadro, 0, False)
            quadro[key] = ' '
            if (pont > mPont):
                mPont = pont
                mMovi = key

    inserir(computador, mMovi)
    return


def minimax(quadro, prof, max):
    if (pVitoria(computador)):
        return 1
    elif (pVitoria(jogador.letra)):
        return -1
    elif (empate()):
        return 0

    if (max):
        mPont = -800
        for key in quadro.keys():
            if (quadro[key] == ' '):
                quadro[key] = computador
                pont = minimax(quadro, prof + 1, False)
                quadro[key] = ' '
                if (pont > mPont):
                    mPont = pont
        return mPont

    else:
        mPont = 800
        for key in quadro.keys():
            if (quadro[key] == ' '):
                quadro[key] = jogador.letra
                pont = minimax(quadro, prof + 1, True)
                quadro[key] = ' '
                if (pont < mPont):
                    mPont = pont
        return mPont


quadro = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

mostrarQuadro(quadro)
print("Segue as posicoes:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")

jogador = Jogador()
if jogador.letra == "X":
    computador = "O"
else:
    computador = "X"

sorteio = randrange(0,3)
if sorteio == 1:
    while not vitoria():
        jogadorMovi()
        computadorMovi()
else:
    while not vitoria():
        computadorMovi()
        jogadorMovi()
