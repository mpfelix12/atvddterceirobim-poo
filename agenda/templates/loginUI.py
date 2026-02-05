import streamlit as st
from views import View

class LoginUI:

    @staticmethod
    def main():
        st.header("Login")

        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")

        if st.button("Entrar"):
            c = View.cliente_autenticar(email, senha)

            if c is None:
                st.error("Email ou senha inválidos")
            else:
                st.session_state["usuario_id"] = c.get_id()
                st.session_state["usuario_nome"] = c.get_nome()
                st.success("Login realizado com sucesso")
                st.rerun()
