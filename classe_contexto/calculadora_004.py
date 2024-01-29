class Calculadora:
    def calcular(self, op, num1: float, num2: float) -> float:
        if op == '+':
            return self.__adicionar(num1, num2)
        elif op == '-':
            return self.__subtracao(num1, num2)
        else:
            print('Operação inválida')

    def __adicionar(self, num1: float, num2: float) -> float:
        return num1 + num2

    def __subtracao(self, num1: float, num2: float) -> float:
        return num1 - num2


calculadora = Calculadora()
print(calculadora.calcular('+', 4, 6))
print(calculadora.calcular('-', 4, 6))
