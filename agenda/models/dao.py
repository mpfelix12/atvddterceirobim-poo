import json
import os

class DAO:

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    @staticmethod
    def caminho(nome):
        return os.path.join(DAO.BASE_DIR, nome)

    # -------------------------
    # CLIENTE
    # -------------------------
    @staticmethod
    def cliente_listar():
        try:
            with open(DAO.caminho("clientes.json"), "r") as f:
                return json.load(f)
        except:
            return []

    @staticmethod
    def cliente_salvar(lista):
        with open(DAO.caminho("clientes.json"), "w") as f:
            json.dump(lista, f, indent=4)

    # -------------------------
    # PROFISSIONAL
    # -------------------------
    @staticmethod
    def profissional_listar():
        try:
            with open(DAO.caminho("profissionais.json"), "r") as f:
                return json.load(f)
        except:
            return []

    @staticmethod
    def profissional_salvar(lista):
        with open(DAO.caminho("profissionais.json"), "w") as f:
            json.dump(lista, f, indent=4)

    # -------------------------
    # SERVIÇO
    # -------------------------
    @staticmethod
    def servico_listar():
        try:
            with open(DAO.caminho("servicos.json"), "r") as f:
                return json.load(f)
        except:
            return []

    @staticmethod
    def servico_salvar(lista):
        with open(DAO.caminho("servicos.json"), "w") as f:
            json.dump(lista, f, indent=4)

    # -------------------------
    # HORÁRIO
    # -------------------------
    @staticmethod
    def horario_listar():
        try:
            with open(DAO.caminho("horarios.json"), "r") as f:
                return json.load(f)
        except:
            return []

    @staticmethod
    def horario_salvar(lista):
        with open(DAO.caminho("horarios.json"), "w") as f:
            json.dump(lista, f, indent=4)
