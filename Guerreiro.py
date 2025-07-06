class Guerreiro:

    #Inicializar
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
    #metodos
    def status(self):
        print(f"Atributos do guerreio {self.nome}:\n Vida: {self.vida}\n Ataque: {self.ataque} \n Defesa: {self.defesa}")

#Criando um objeto da classe criada
heroi = Guerreiro("Gustavo", 100, 20, 10 )
heroi.status()