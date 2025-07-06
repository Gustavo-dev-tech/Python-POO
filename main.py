# Criando uma classe chamada Heroi
class Heroi:
    
    # __init__ é um método especial que inicializa os atributos do herói
    def __init__(self, nome, genero, life, xp):
        # self.nome cria um atributo chamado nome e recebe o valor passado
        self.nome = nome
        self.genero = genero  # Armazena o gênero do herói
        self.life = life      # Armazena a vida do herói
        self.xp = xp          # Armazena a experiência do herói

    # Método que mostra o gênero do herói
    def sexo(self):
        print(f"O genero do heroi {self.nome} é {self.genero} ")

# Criando um objeto da classe Heroi com valores iniciais
goku = Heroi("Goku", "Masculino", "100", "4000")

# Acessando os atributos do objeto e imprimindo na tela
print(goku.nome)    # Exibe o nome do herói
print(goku.genero)  # Exibe o gênero
print(goku.life)    # Exibe a vida
print(goku.xp)      # Exibe a experiência

# Chamando o método sexo() do objeto goku
goku.sexo()  # Exibe: O genero do heroi Goku é Masculino
