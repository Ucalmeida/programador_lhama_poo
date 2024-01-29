class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self) -> None:
        print(f'{self.nome} está correndo')

    def beber(self, bebida: str) -> None:
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print(f'{self.nome} está bebendo...')

    def __apresentar_documento(self) -> None:
        print(f'CPF: {self.__cpf}')


ronaldo = Pessoa('Ronald', 42, '987654321')
print(ronaldo.nome)
print(ronaldo.idade)
ronaldo.beber('cerveja')
ronaldo.beber('coca-cola')
