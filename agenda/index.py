import streamlit as st
from views import View

from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.agendarservicoUI import AgendarServicoUI


class IndexUI:

    # --------------------------------------------------
    # Criar admin automaticamente
    # --------------------------------------------------
    @staticmethod
    def criar_admin_padrao():
        for c in View.cliente_listar():
            if c.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "0000-0000", "1234")

    # --------------------------------------------------
    # MENU VISITANTE
    # --------------------------------------------------
    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox(
            "Menu",
            ["Entrar no Sistema", "Abrir Conta"]
        )

        if op == "Entrar no Sistema":
            LoginUI.main()
        elif op == "Abrir Conta":
            AbrirContaUI.main()

    # --------------------------------------------------
    # MENU CLIENTE
    # --------------------------------------------------
    @staticmethod
    def menu_cliente():
        op = st.sidebar.selectbox(
            "Menu",
            ["Meus Dados", "Agendar Serviço"]
        )

        if op == "Meus Dados":
            PerfilClienteUI.main()
        elif op == "Agendar Serviço":
            AgendarServicoUI.main()

    # --------------------------------------------------
    # MENU ADMIN
    # --------------------------------------------------
    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox(
            "Menu",
            [
                "Cadastro de Clientes",
                "Cadastro de Profissionais",
                "Cadastro de Serviços",
                "Cadastro de Horários"
            ]
        )

        if op == "Cadastro de Clientes":
            ManterClienteUI.main()

        elif op == "Cadastro de Profissionais":
            ManterProfissionalUI.main()

        elif op == "Cadastro de Serviços":
            ManterServicoUI.main()

        elif op == "Cadastro de Horários":
            ManterHorarioUI.main()

    # --------------------------------------------------
    # LOGOUT
    # --------------------------------------------------
    @staticmethod
    def logout():
        if st.sidebar.button("Sair do Sistema"):
            st.session_state.clear()
            st.rerun()

    # --------------------------------------------------
    # SIDEBAR PRINCIPAL
    # --------------------------------------------------
    @staticmethod
    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            st.sidebar.write(
                f"Bem-vindo(a), {st.session_state['usuario_nome']}"
            )

            if st.session_state["usuario_nome"] == "admin":
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()

            IndexUI.logout()

    # --------------------------------------------------
    # MAIN
    # --------------------------------------------------
    @staticmethod
    def main():
        st.set_page_config(page_title="Sistema de Agendamento")
        st.title("Sistema de Agendamento")

        IndexUI.criar_admin_padrao()
        IndexUI.sidebar()


# Executa o sistema
if __name__ == "__main__":
    IndexUI.main()
