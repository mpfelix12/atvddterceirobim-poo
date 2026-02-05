import streamlit as st
from views import View
import time

class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        op = st.selectbox("Operação", ["Inserir", "Atualizar", "Excluir"])
        if op == "Inserir": ManterProfissionalUI.inserir()
        if op == "Atualizar": ManterProfissionalUI.atualizar()
        if op == "Excluir": ManterProfissionalUI.excluir()
        
    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        fone = st.text_input("Informe o fone")
        if st.button("Inserir"):
            View.profissional_inserir(nome, especialidade, fone)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()
                        
    def atualizar():
        op = st.selectbox("Selecione o profissional", View.profissional_listar())
        nome = st.text_input("Informe o nome", op.get_nome())
        especialidade = st.text_input("Informe a especialidade", op.get_especialidade())
        fone = st.text_input("Informe o fone", op.get_fone())
        if st.button("Atualizar"):
            id = op.get_id()
            View.profissional_atualizar(id, nome, especialidade, fone)
            st.success("Profissional atualizado com sucesso")
            time.sleep(2)
            st.rerun()

    def excluir():
        op = st.selectbox("Selecione o profissional", View.profissional_listar())
        if st.button("Excluir"):
            id = op.get_id()
            View.profissional_excluir(id)
            st.success("Profissional excluído com sucesso")
            time.sleep(2)
            st.rerun()

    