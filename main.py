from random import randint

nome = input("Olá, como você se chama? ")
print(f"Certo! {nome}, estou escolhendo um número de 1 até 50. Você consegue saber qual é? ")
numero_advinhado = randint(1 , 25)
tentativas = 5

for tentativa in range(1, tentativas +1):
    numero_escolhido = int(input("Escolha um número: "))
    if numero_escolhido == numero_advinhado:
        print(f"PARABÉNS, Voce ACERTOU em {tentativa} tentativas!")
        break
    elif numero_escolhido > numero_advinhado:
        print("Tente um número menor!")
    else:
        print("Tente um número MAIOR!")
print(f"O número sorteado era {numero_advinhado}. Obrigado por jogar!")