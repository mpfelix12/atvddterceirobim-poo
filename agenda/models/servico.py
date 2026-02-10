import json

class Servico:
    def __init__(self, id, descricao, valor):

        if descricao is None or descricao.strip() == "":
            raise ValueError("Descrição inválida")

        valor = float(valor)

        if valor < 0:
            raise ValueError("Valor inválido")

        self.__id = id
        self.__descricao = descricao.strip()
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
        return{
            "id": self.get_id(),
            "descricao": self.get_descricao(),
            "valor": self.get_valor()
        }
    
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])
        
class ServicoDAO:

    __objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        obj.set_id(len(cls.__objetos) + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    # ✅ MÉTODO QUE ESTAVA FALTANDO
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
        import json
        cls.__objetos = []
        try:
            with open("servicos.json", "r") as f:
                lista = json.load(f)

                for item in lista:
                    descricao = item.get("descricao", "").strip()
                    valor = float(item.get("valor", 0))
                    id = item.get("id", 0)

                    if descricao != "":
                        s = Servico(id, descricao, valor)
                        cls.__objetos.append(s)

        except FileNotFoundError:
            cls.__objetos = []



    @classmethod
    def salvar(cls):
        import json
        with open("servicos.json", "w") as f:
            json.dump([obj.to_json() for obj in cls.__objetos], f, indent=4)
