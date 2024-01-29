class Alarme:
    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        self.__estado = valor


alarme = Alarme(True)
print(alarme.get_estado())
alarme.set_estado(False)
print(alarme.get_estado())
