#Amanda Aiko dos Santos Hiraide - Análise e desenvolvimento de sistemas PUCPR
#Projeto zumbie dice, segunda parte

import random
from time import sleep

print("Bem vindo ao zombie dice!! coma quantos cérebros conseguir!!")


num_jogadores = 0
# Quantidade de jogadores
while (num_jogadores < 2):


    num_jogadores = int(input("Informe a quantidade de jogadores: "))


    if (num_jogadores < 2):
        print("Para jogar é necessário pelo menos 2 jogadores!!")
 #Nome dos jogadores
lista_jogadores = []

for c in range (0, num_jogadores):


    nome = input(f'Digite o nome do {c + 1}° jogador: ').upper()
    lista_jogadores.append(nome)

# Sorteio de dados
def dado_verde():
    dadoVerde = ("C", "P", "C", "T", "P", "C")
    return dadoVerde

def dado_amarelo():
    dadoAmarelo = ("T", "P", "C", "T", "P", "C")
    return dadoAmarelo

def dado_vermelho():
    dadoVermelho = ("T", "P", "T", "C", "P", "T")
    return dadoVermelho

lista_dados = [
    dado_verde(), dado_verde(), dado_verde(), dado_verde(), dado_verde(), dado_verde(),
    dado_amarelo(), dado_amarelo(), dado_amarelo(), dado_amarelo(),
    dado_vermelho(), dado_vermelho(), dado_vermelho()
]



print("---INICIANDO PARTIDA---")

jogador_atual = 0
dados_sorteados = []
tiros = 0
cerebros = 0
passos = 0
pontos = []


#loop

for i in range(0, num_jogadores):
    pontos.append(0)

def sorteamento_dados (cor_dado = ()):
    for n in range (0, 3):
        num_sorteado = random.randrange(13)
        dado_sorteado = lista_dados[num_sorteado]
        if dado_sorteado == dado_verde():
            cor_dado = "VERDE"
        elif dado_sorteado == dado_amarelo():
            cor_dado = "AMARELO"
        elif dado_sorteado == dado_vermelho():
            cor_dado = "VERMELHO"

        print("O dado sorteado foi", cor_dado)
        dados_sorteados.append(dado_sorteado)
        sleep(1)


#Sorteio de dados
while True:

    print('É a vez do jogador: ', lista_jogadores[jogador_atual])

    sorteamento_dados()

    for dado_sorteado in dados_sorteados:
        num_faces = random.randint(0, 5)
        if dado_sorteado[num_faces] == "C":
            print('+1 Você comeu um cérebro')
            cerebros += 1

        elif dado_sorteado[num_faces] == "T":
            print('Você tomou um tiro!')
            tiros += 1

        else:
            print('CUIDADO!! passos!!')
            passos += 1
    sleep(1)


    print("---Pontuação---")
    print("Cérebros: ", cerebros)
    print("Tiros: ", tiros)


    if tiros > 2:
        print(' Você perdeu essa rodada! você levou, ', tiros, ' tiros')
        tiros = 0
        cerebros = 0
        passos = 0
        dados_sorteados = []
        jogador_atual += 1

        if jogador_atual == len(lista_jogadores):
            jogador_atual = 0
            print('Próxima rodada: ', lista_jogadores[jogador_atual])

    else:
        continuar_turno = str(input('Continuar jogando? (S/N) ')).strip().upper()[0]

        if (continuar_turno == "S"):
            pontos[jogador_atual] += cerebros
            jogador_atual += 1
            dados_sorteados = []
            tiros = 0
            cerebros = 0
            passos = 0


            if (jogador_atual == len(lista_jogadores)):
                jogador_atual = 0

        if (continuar_turno == "N"):
            jogador_atual = 0
            print('---ATÉ A PRÓXIMA---')
            break
