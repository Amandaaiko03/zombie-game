#Amanda Aiko dos Santos Hiraide - PUCPR - Análise e desenvolvimento de sistemas

# entrada do jogo
print("Bem vindo ao zombie dice!! coma quantos cérebros conseguir!!")

numberPlayers = 0
while (numberPlayers < 2):
	numberPlayers = int(input("informe número de jogadores:"))
	# quantidade de jogadores
	if numberPlayers < 2:
		print("Para jogar é necessário pelo menos 2 jogadores!!\n")
else:
	print("Iniciar partida!\n")

ListaPlayers = []
for i in range (numberPlayers):
	nome = input("Insira o nome do zombie" + str ( i + 1 ) + ":")
	ListaPlayers.append(nome)

#números randomicos
import random
# Dados verdes (6 dados)
dadoVerde = "CPCTPC"
dado1 = "CPCTPC"
dado2 = "CPCTPC"
dado3 = "CPCTPC"
dado4 = "CPCTPC"
dado5 = "CPCTPC"
dado6 = "CPCTPC"
# Dados amarelos (4 dados)
dadoAmarelo = "TPCTPC"
dado7 = "TPCTPC"
dado8 = "TPCTPC"
dado9 = "TPCTPC"
dado10 = "TPCTPC"
# Dados vermelhos (3 dados)
dadoVermelho = "TPTCPT"
dado11 = "TPTCPT"
dado12 = "TPTCPT"
dado13 = "TPTCPT"

listaDados = [ 'dadoVerde','dadoVerde','dadoVerde','dadoVerde','dadoVerde','dadoVerde',
'dadoAmarelo','dadoAmarelo','dadoAmarelo','dadoAmarelo',
'dadoVermelho','dadoVermelho','dadoVermelho' ]


#sorteio de dados
for i in range(6):
	listaDados.append(dadoVerde)

for i in range(4):
	listaDados.append(dadoAmarelo)

for i in range(3):
	listaDados.append(dadoVermelho)


print("...INICIANDO JOGO...")
playerAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0
corDado = ''

# Loop infinito do jogo
while True:
	print('Turno do jogador {}:'.format(ListaPlayers[playerAtual]))

	# Soteando os dados a serem pegos
	for i in range(3):
		numSorteado = random.randint(0, 12)
		dadoSorteado = listaDados[numSorteado]

		if (dadoSorteado == 'CPCTPC'):
			corDado = 'Verde'
		elif (dadoSorteado == 'TPCTPC'):
			corDado = 'Amarelo'
		else:
			corDado = 'Vermelho'

		print('Dado sorteado: {}\n'.format(corDado))

		dadosSorteados.append(dadoSorteado)

#Sorteio dos dados
	print('As faces sorteadas foram:\n')

	for dadosSorteado in dadosSorteados:
		numFaceDado = random.randint(0,5)

		if dadosSorteado[numFaceDado] == 'C':
			print(' +1 Você comeu um cérebro')
			cerebros += 1
		elif dadosSorteado[numFaceDado] == 'T':
			print('Você tomou um tiro')
			tiros += 1
		else:
			print("Passos!!")
			passos += 1

	print('Pontuação:')
	print('Cérebros:{}'.format(cerebros))
	print('Tiros:{}'.format(tiros))
	print('Passos:{}'.format(passos))

	ContinuarTurno = input("Continuar jogando?(Sim/Não)")
	if (ContinuarTurno == 'Sim'):
		playerAtual += 1
		dadosSorteados = []
		cerebros = 0
		tiros = 0
		passos = 0
	if (playerAtual == len(ListaPlayers)):
		print('Fim de jogo!')
		break
	else:
		print('Iniciando partida!!')
		dadosSorteados=[]







