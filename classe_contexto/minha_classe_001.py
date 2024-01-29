class MinhaClasse:
    def __init__(self, att):
        self.meu_atributo = 'Olá Mundo!'
        self.meu_atributo2 = att
    def meu_metodo(self):
        print('Estou no método!')
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, num, mult):
        return num * mult


objeto = MinhaClasse('String passada ao instânciar o objeto através da classe MinhaClasse')
objeto.meu_metodo()
result = objeto.meu_metodo2(3, 2)
print(result)
