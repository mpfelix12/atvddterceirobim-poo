import json
from models.dao import DAO

class Profissional:
    def __init__(self, id, nome, especialidade, fone):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_fone(fone)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__especialidade} – {self.__fone}"
    
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_especialidade(self): return self.__especialidade
    def get_fone(self): return self.__fone

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome
    def set_especialidade(self, especialidade): self.__especialidade = especialidade
    def set_fone(self, fone): self.__fone = fone

    def to_json(self):
        return{
            "id": self.__id,
            "nome": self.__nome,
            "especialidade": self.__especialidade,
            "fone": self.__fone
        }

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"],
            dic["especialidade"], dic["fone"])      

        
class ProfissionalDAO(DAO):
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()

        maior_id = 0
        for p in cls.__objetos:
            if p.get_id() > maior_id:
                maior_id = p.get_id()

        obj.set_id(maior_id + 1)

        cls.__objetos.append(obj)

        lista = []
        for p in cls.__objetos:
            lista.append(p.to_json())  # 👈 CONVERTE PARA DICIONÁRIO

        DAO.profissional_salvar(lista)
        

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos
    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("profissionais.json", "r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.__objetos.append(Profissional.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissionais.json", "w") as arquivo:
            json.dump(cls.__objetos, arquivo, default=Profissional.to_json)