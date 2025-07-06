class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.quant_vendas = 0

    def vendeu(self, quant_vendas):
        self.quant_vendas = quant_vendas

    def bateu_meta(self, meta):
        if self.quant_vendas > meta:
            print(self.nome, 'Bateu meta')
        else:
            print(self.nome, 'Não bateu meta')

vendedor1 = Vendedor("Henrique")
vendedor1.vendeu(100)
vendedor1.bateu_meta(200)

vendedor2 = Vendedor("Teixeira")
vendedor2.vendeu(402)
vendedor2.bateu_meta(400)