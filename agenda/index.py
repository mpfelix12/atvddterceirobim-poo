from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.agendarservicoUI import AgendarServicoUI
from templates.manterprofissionalUI import ManterProfissionalUI
from views import View
import streamlit as st


class IndexUI:

    @staticmethod
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "fone", "1234")

    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox(
            "Menu", 
            ["Entrar no Sistema", "Abrir Conta"]
        )
        if op == "Entrar no Sistema":
            LoginUI.main()
        else:
            AbrirContaUI.main()

    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox(
            "Menu", 
            ["Meus Dados", "Agendar Serviço"]
        )
        if op == "Meus Dados":
            PerfilClienteUI.main()
        else:
            AgendarServicoUI.main()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu", 
            [
                "Cadastro de Clientes",
                "Cadastro de Serviços",
                "Cadastro de Horários",
                "Cadastro de Profissionais"
            ]
        )

        if op == "Cadastro de Clientes":
            ManterClienteUI.main()
        elif op == "Cadastro de Serviços":
            ManterServicoUI.main()
        elif op == "Cadastro de Horários":
            ManterHorarioUI.main()
        else:
            ManterProfissionalUI.main()

    @staticmethod
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    @staticmethod
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            st.sidebar.write(
                "Bem-vindo(a), " + st.session_state["usuario_nome"]
            )
            admin = st.session_state["usuario_nome"] == "admin"
            if admin:
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    @staticmethod
    def main():
        st.title("Sistema de Agendamento")
        IndexUI.cliente_criar_admin()
        IndexUI.sidebar()


if __name__ == "__main__":
    IndexUI.main()
