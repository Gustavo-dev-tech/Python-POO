class Guerreiro:

    #Inicializar
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        

    def status(self):
        print(f"\nAtributos do guerreiro {self.nome}:\n Vida: {self.vida}\n Ataque: {self.ataque} \n Defesa: {self.defesa}")

    #função de ataque ao outro jogador
    def atacar(gue1,gue2):
        print(f"\n{gue1.nome}, atacou {gue2.nome} ")
            
            #se a defesa do outro jogador ainda existir:
        if gue2.defesa > 0:
            print(f"{gue1.nome} = Ataque: {gue1.ataque} | {gue2.nome} = defesa: {gue2.defesa} ")
            gue2.defesa =  gue2.defesa - gue1.ataque # defesa - ataque
            print(f"O novo valor de defesa da {gue2.nome} agora é de {gue2.defesa}")
            if gue2.defesa < 0:
                gue2.vida =  gue2.vida + gue2.defesa # vida.200 - def.-1 = vida.199
                print(f"\nA defesa de {gue2.nome} foi COMPLETAMENTE DESTRUIDA. \nDano a mais causado a defesa, transfirida para sua vida. \nvida atual: {gue2.vida} ")
                gue2.defesa = 0
                if gue2.vida <= 0:
                    print(f" {gue2.nome} virou Pó... \n     FIM DE JOGO.")

            #se a defesa ja se foi, e a vida ainda é maior que 0    
        elif gue2.defesa <= 0 and gue2.vida > 0:
            print(f"A defesa de {gue2.nome} se foi... agora ele usara sua vida como ultima defesa \n")
            print(f"{gue1.nome} = Ataque: {gue1.ataque} | {gue2.nome} = vida: {gue2.vida} ")
            gue2.vida =  gue2.vida - gue1.ataque # defesa - ataque
            print(f"O novo valor de vida de {gue2.nome} agora é de {gue2.vida}")
            if gue2.vida <= 0:
                print(f" {gue2.nome} virou Pó... \n     FIM DE JOGO.")   

    def aumentarxp(gue):
        print(f"A vida do jogador {gue.nome} é de: {gue.vida}.")
        gue.vida += (gue.vida / 100) * 25
        print(f"Com o aumento de 25% sua vida agora é de: {gue.vida}. ")

    #heroi1
print("Digite os atributos do Heroi 1:")
nome1 = input("Nome: ")
vida1 = int(input("Vida: "))
ataque1 = int(input("Ataque: "))
defesa1 = int(input("Defesa: "))

#heroi2
print("\nDigite os atributos do Heroi 2:")
nome2 = input("Nome: ")
vida2 = int(input("Vida: "))
ataque2 = int(input("Ataque: "))
defesa2 = int(input("Defesa: "))

#Criando um objeto da classe criada e passando atributos
heroi1 = Guerreiro(nome1, vida1, ataque1, defesa1 )
heroi2 = Guerreiro(nome2, vida2, ataque2,defesa2  )


#mostrando atributos
#heroi1.status()
#heroi2.status()

#fazendo ataque
#heroi1.atacar(heroi2)
#heroi2.status()

#Aumentando vida
#heroi1.aumentarxp()
#heroi2.aumentarxp()

vez = "heroi1"
while vez == "heroi1" or vez == "heroi2":
    #Rodada do jogador 1
    while vez == "heroi1":
        print(f"\n\nRodada do Guerreiro {heroi1.nome}.")
        num = int(input(f"\n\nEscolha: \n1: Mostrar atributos \n2: atacar a/o {heroi2.nome} \n3: curar XP. \n\n Digite:"))
        if num == 1:
            heroi1.status()
            heroi2.status()
        elif num == 2:
            heroi1.atacar(heroi2)
            break
        elif num == 3:
            heroi1.aumentarxp()
            break
    if heroi1.vida < 1:
        vez = "FIM"
        print(f" {heroi1.nome} virou Pó... \n     FIM DE JOGO.")
        break
    else:
        vez = "heroi2"
    #rodado do jogador 2
    while vez == "heroi2":
        print(f"\n\nRodada do Guerreiro {heroi2.nome}.")
        num = int(input(f"\n\nEscolha: \n1: Mostrar atributos \n2: atacar o {heroi1.nome} \n3: curar XP. \n Digite:"))
        if num == 1:
            heroi1.status()
            heroi2.status()
            #atacar jogador 1
        elif num == 2:
            heroi2.atacar(heroi1)
            break
            #aumentar 25% da vida
        elif num == 3:
            heroi2.aumentarxp()
            break
    if heroi1.vida < 1:
        vez = "FIM"
        print(f" {heroi1.nome} virou Pó... \n     FIM DE JOGO.")
        break
    if heroi1.vida < 2:
        vez = "FIM"
        print(f" {heroi2.nome} virou Pó... \n     FIM DE JOGO.")
        break
    else:
        vez = "heroi1"