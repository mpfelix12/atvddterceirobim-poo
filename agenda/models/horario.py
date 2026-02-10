from datetime import datetime
import json
from models.dao import DAO

class Horario:
    def __init__(self, id, id_servico, id_profissional, data, horario):
        self.__id = id
        self.__id_servico = id_servico
        self.__id_profissional = id_profissional
        self.__data = data
        self.__horario = horario


    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__horario} - {self.__id_profissional} - {self.__id_servico} - {self.__confirmado} - {self.__id_cliente}"
    

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico

    def set_id(self, id): self.__id = id
    def set_data(self, data): self.__data = data
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico


    def to_json(self):
        return {
            "id": self.__id,
            "id_servico": self.__id_servico,
            "id_profissional": self.__id_profissional,
            "data": str(self.__data),
            "horario":str(self.__horario)
        }
    
    @staticmethod
    def from_json(dic):
        return Horario(
            dic["id"],
            dic["id_servico"],
            dic["id_profissional"],
            dic["horario"],
            datetime.strptime(dic["data"], "%d/%m/%Y %H:%M")
        )

class HorarioDAO(DAO):
    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()

        maior_id = 0
        for h in cls.__objetos:
            if h.get_id() > maior_id:
                maior_id = h.get_id()

        obj.set_id(maior_id + 1)
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
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__objetos.remove(aux)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.__objetos.remove(aux)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open("horarios.json", "r") as arquivo:
                lista = json.load(arquivo)
                for dic in lista:
                    cls.__objetos.append(Horario.from_json(dic))
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("horarios.json", "w") as f:
            json.dump([
                {
                    "id": obj.get_id(),
                    "data": obj.get_data().strftime("%d/%m/%Y %H:%M"),
                    "confirmado": obj.get_confirmado(),
                    "id_cliente": obj.get_id_cliente(),
                    "id_servico": obj.get_id_servico(),
                    "id_profissional": obj.get_id_profissional()
                }
                for obj in cls.__objetos
            ], f, indent=4)

