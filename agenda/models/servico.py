import json
from models.dao import DAO

class Servico:
    def __init__(self, id, descricao, valor):
        if descricao == "": raise ValueError("Descrição inválida")
        if valor < 0: raise ValueError("Valor inválido")
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor
        
    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R$ {self.__valor:.2f}"
    
    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor
    
    def set_id(self, id):
        self.__id = id

    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição inválida")
        self.__descricao = descricao

    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor inválido")
        self.__valor = valor
        
    def to_json(self):
        dic = {"id":self.__id, "descricao":self.__descricao,
            "valor":self.__valor}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])
        
class ServicoDAO(DAO):
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        novo_id = 0
        for aux in cls.__objetos:
            if aux.get_id() > novo_id:
                novo_id = aux.get_id()
        obj.set_id(novo_id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        antigo = cls.listar_id(obj.get_id())
        if antigo:
            cls.__objetos.remove(antigo)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        antigo = cls.listar_id(obj.get_id())
        if antigo:
            cls.__objetos.remove(antigo)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("servicos.json", "r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.__objetos.append(Servico.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", "w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Servico.to_json)