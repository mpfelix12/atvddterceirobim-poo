class Servico:
    def __init__(self, id, descricao, valor):
        if descricao == "": raise ValueError("Descrição inválida")
        if valor < 0: raise ValueError("Valor inválido")
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor


    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição inválida")
        self.__descricao = descricao

    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor inválido")
        self.__valor = valor