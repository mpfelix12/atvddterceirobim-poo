from models.cliente import Cliente, ClienteDAO
from models.horario import Horario, HorarioDAO
from models.servico import Servico, ServicoDAO
from models.profissional import Profissional, ProfissionalDAO
from datetime import datetime, timedelta

class View:

    # ---------- CLIENTE ----------
    @staticmethod
    def cliente_listar():
        r = ClienteDAO.listar()
        r.sort(key=lambda obj: obj.get_nome())
        return r

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)

    @staticmethod
    def cliente_autenticar(email, senha):
        return ClienteDAO.autenticar(email, senha)

    # ---------- SERVIÇO ----------
    @staticmethod
    def servico_inserir(descricao, valor):
        for obj in View.servico_listar():
            if obj.get_descricao() == descricao:
                raise ValueError("Serviço já cadastrado")
        s = Servico(0, descricao, valor)
        ServicoDAO.inserir(s)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        for obj in View.servico_listar():
            if obj.get_id() != id and obj.get_descricao() == descricao:
                raise ValueError("Descrição já cadastrada")
        s = Servico(id, descricao, valor)
        ServicoDAO.atualizar(s)

    @staticmethod
    def servico_listar():
        r = ServicoDAO.listar()
        r.sort(key=lambda obj: obj.get_descricao())
        return r

    @staticmethod
    def servico_excluir(id):
        for h in View.horario_listar():
            if h.get_id_servico() == id:
                raise ValueError("Serviço já agendado")
        s = Servico(id, "", 0)
        ServicoDAO.excluir(s)

    # ---------- HORÁRIO ----------
    @staticmethod
    def horario_inserir(id_servico, id_profissional, data, hora):
        obj = Horario(0, id_servico, id_profissional, data, hora)
        HorarioDAO.inserir(obj)



    @staticmethod
    def horario_listar():
        r = HorarioDAO.listar()
        r.sort(key=lambda obj: obj.get_data())
        return r

    @staticmethod
    def horario_filtrar_profissional(id_profissional):
        return [
            h for h in View.horario_listar()
            if h.get_id_profissional() == id_profissional
        ]

    @staticmethod
    def horario_abrir_agenda(data, hinicio, hfinal, intervalo, id_profissional, id_servico):

        dt = datetime.strptime(data, "%d/%m/%Y")

        if dt.date() < datetime.now().date():
            raise ValueError("Data não pode estar no passado")

        if intervalo > 120:
            raise ValueError("Intervalo máximo de 120 minutos")

        hora_inicio = datetime.strptime(hinicio, "%H:%M")
        hora_fim = datetime.strptime(hfinal, "%H:%M")

        atual = dt.replace(hour=hora_inicio.hour, minute=hora_inicio.minute)
        limite = dt.replace(hour=hora_fim.hour, minute=hora_fim.minute)

        while atual < limite:
            View.horario_inserir(
                id_servico,
                id_profissional,
                atual.date(),
                atual.time()
            )
            atual += timedelta(minutes=intervalo)


    @staticmethod
    def agendar_horario(id_profissional):
        agora = datetime.now()
        r = []
        for h in View.horario_listar():
            if (
                h.get_data() >= agora
                and not h.get_confirmado()
                and h.get_id_cliente() is None
                and h.get_id_profissional() == id_profissional
            ):
                r.append(h)
        return r

    @staticmethod
    def horario_atualizar(id, id_servico, id_profissional, data, hora, confirmado, id_cliente):

        h = Horario(id, id_servico, id_profissional, data, hora)
        h.set_confirmado(confirmado)
        h.set_id_cliente(id_cliente)

        HorarioDAO.atualizar(h)


    @staticmethod
    def horario_excluir(id):
        h = HorarioDAO.listar_id(id)
        if h:
            HorarioDAO.excluir(h)


    # ---------- PROFISSIONAL ----------
    @staticmethod
    def profissional_listar():
        r = ProfissionalDAO.listar()
        r.sort(key=lambda obj: obj.get_nome())
        return r

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO.listar_id(id)

    @staticmethod
    def profissional_inserir(nome, especialidade, fone):
        from models.profissional import Profissional
        from models.profissional import ProfissionalDAO

        obj = Profissional(0, nome, especialidade, fone)
        ProfissionalDAO.inserir(obj)


    @staticmethod
    def profissional_atualizar(id, nome, especialidade, fone):
        p = Profissional(id, nome, especialidade, fone)
        ProfissionalDAO.atualizar(p)

    @staticmethod
    def profissional_excluir(id):
        p = Profissional(id, "", "", "")
        ProfissionalDAO.excluir(p)
