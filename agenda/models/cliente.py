import json
from models.dao import DAO

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"

    # GETTERS
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha

    # SETTERS
    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_email(self, email): self.__email = email
    def set_fone(self, fone): self.__fone = fone
    def set_senha(self, senha): self.__senha = senha

    # JSON
    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "senha": self.__senha
        }

    @staticmethod
    def from_json(dic):
        return Cliente(
            dic["id"],
            dic["nome"],
            dic["email"],
            dic["fone"],
            dic["senha"]
        )


class ClienteDAO(DAO):
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
    def autenticar(cls, email, senha):
        cls.abrir()
        for c in cls.__objetos:
            if c.get_email() == email and c.get_senha() == senha:
                return c
        return None

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
            with open("clientes.json", "r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.__objetos.append(Cliente.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("clientes.json", "w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Cliente.to_json)
