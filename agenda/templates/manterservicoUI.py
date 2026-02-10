import streamlit as st
import time
from views import View

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        op = st.selectbox("Operação", ["Inserir", "Atualizar", "Excluir"])
        if op == "Inserir": ManterServicoUI.inserir()
        if op == "Atualizar": ManterServicoUI.atualizar()
        if op == "Excluir": ManterServicoUI.excluir()
    def inserir():
        st.subheader("Inserir Serviço")
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor (R$)")
        if st.button("Inserir"):
            try:
                View.servico_inserir(descricao, float(valor))
                st.success("Serviço inserido com sucesso")
            except ValueError as erro:
                st.error("Valor inválido.")
            st.rerun()
                        
    def atualizar():
        lista = View.servico_listar()

        if len(lista) == 0:
            st.warning("Nenhum serviço cadastrado.")
            return

        op = st.selectbox("Selecione o serviço", lista)

        if op is not None:
            descricao = st.text_input("Informe a descrição", op.get_descricao())
            valor = st.text_input("Informe o valor", op.get_valor())

            if st.button("Atualizar"):
                try:
                    valor = valor.replace(",", ".")
                    View.servico_atualizar(op.get_id(), descricao, float(valor))
                    st.success("Serviço atualizado com sucesso!")
                except:
                    st.error("Valor inválido.")

    def excluir():
        op = st.selectbox("Selecione o serviço", View.servico_listar())
        if st.button("Excluir"):
            try:
                id = op.get_id()
                View.servico_excluir(id)
                st.success("Serviço excluído com sucesso")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()