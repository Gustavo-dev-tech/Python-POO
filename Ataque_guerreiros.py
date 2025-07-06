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
        print(f"\n{gue1.nome}, atacou a defesa da {gue2.nome} ")
        print(f"{gue1.nome} = Ataque: {gue1.ataque} | {gue2.nome} = defesa: {gue2.defesa} ")
        gue2.defesa =  gue2.defesa - gue1.ataque # defesa - ataque
        print(f"O novo valor de defesa da {gue2.nome} agora é de {gue2.defesa}")
        if gue2.defesa < 0:
            gue2.vida =  gue2.vida + gue2.defesa # vida.200 - def.-1 = vida.199
            print(f"\nA defesa da {gue2.nome} foi COMPLETAMENTE DESTRUIDA. \nDano a mais causado a defesa, transfirida para sua vida. \nvida atual: {gue2.vida} ")
            gue2.defesa = 0
        # def novo_status(gue2):
        #  print(f"\nO novo valor de defesa da {gue2.nome} agora é de {gue2.defesa}")

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
heroi1.status()
heroi2.status()

#fazendo ataque
heroi1.atacar(heroi2)
heroi2.status()

#while True:
    #num = int(input("Digite: \n1: Mostrar atributos \n2: atacar o Guerreiro 2 \n 3: curar XP"))
        #metodo/função de mostrar atributos
    #if num == 1: