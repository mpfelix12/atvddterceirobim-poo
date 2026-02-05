class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        op = st.selectbox("Operação", ["Inserir", "Atualizar", "Excluir"])
        if op == "Inserir": ManterServicoUI.inserir()
        if op == "Atualizar": ManterServicoUI.atualizar()
        if op == "Excluir": ManterServicoUI.excluir()
    def inserir():
        descricao = st.text_input("Informe a descrição")
        valor = st.text_input("Informe o valor (R$)")
        if st.button("Inserir"):
            try:
                View.servico_inserir(descricao, float(valor))
                st.success("Serviço inserido com sucesso")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()
                        
    def atualizar():
        op = st.selectbox("Selecione o serviço", View.servico_listar())
        descricao = st.text_input("Informe a descrição", op.get_descricao())
        valor = st.text_input("Informe o valor (R$)", str(op.get_valor()))
        if st.button("Atualizar"):
            try:
                id = op.get_id()
                View.servico_atualizar(id, descricao, float(valor))
                st.success("Serviço atualizado com sucesso")

            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()]

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