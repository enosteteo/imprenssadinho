import random

vida = 0
# Configurar o jogo:
# Mensagem Vitórida / Derrota
msg_ganhar = "Parabéns! você ganhou!"
msg_perder = "Que pena! Você perdeu.. Tente novamente"

# Alterar o intervalo do jogo
intervalo = [0, 100]

###
# Níveis do jogo
# obs deve-se alterar o input de nível_escolhido com as novas modificações para informar o usuário final.
###
nivel = [["fácil", 10], ["difícil", 5]]

# Gera o número secreto
num_secreto = random.randint(intervalo[0], intervalo[1])
fim = False

# Garante uma dificuldáde válida
while not fim:
    nivel_escolhido = input("Escolha a dificuldade...\nFácil - 10 tentativas\nDifícil - 5 tentativas:\n").lower()
    # Varre os níveis para alocar a qntde de vidas conformeo nível escolhido
    for n in nivel:
        if nivel_escolhido in n[0]:
            vida = n[1]
            break
    if vida != 0:
        fim = True
    else:
        print("Dificuldade inválida, por favor, escolha uma dentre as opções")

# Jogo começa
fim = False
while not fim:
    num = int(input("Insira um número: "))

    # Acertou -> ganhou
    # Errou -> perde vida
    if num == num_secreto:
        fim = True
        print(msg_ganhar)
    else:
        vida -= 1

    # vida chegou a 0? fim de jogo
    # ainda não? continue
    if vida == 0:
        fim = True
        print(msg_perder)
    else:
        if intervalo[0] < num < num_secreto:
            intervalo[0] = num
        elif intervalo[1] > num > num_secreto:
            intervalo[1] = num
        print("O novo intervalo é: %i " % intervalo[0] + "à %i" % intervalo[1])