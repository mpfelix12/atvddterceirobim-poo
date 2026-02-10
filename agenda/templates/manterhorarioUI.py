import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime


class ManterHorarioUI:

    @staticmethod
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterHorarioUI.listar()

        with tab2:
            ManterHorarioUI.inserir()

        with tab3:
            ManterHorarioUI.atualizar()

        with tab4:
            ManterHorarioUI.excluir()

    # -----------------------------
    @staticmethod
    def listar():
        lista = View.horario_listar()
        dados = []

        for h in lista:
            dados.append({
                "ID": h.get_id(),
                "Data": h.get_data(),
                "Hora": h.get_hora(),
                "Profissional": h.get_profissional().get_nome(),
                "Serviço": h.get_servico().get_descricao()
            })

        if len(dados) > 0:
            df = pd.DataFrame(dados)
            st.dataframe(df)
        else:
            st.info("Nenhum horário cadastrado.")

    # -----------------------------
    @staticmethod
    def inserir():
        st.subheader("Inserir Horário")

        servicos = View.servico_listar()
        profissionais = View.profissional_listar()

        if len(servicos) == 0 or len(profissionais) == 0:
            st.warning("Cadastre serviços e profissionais primeiro.")
            return

        servico = st.selectbox("Selecione o serviço", servicos)
        profissional = st.selectbox("Selecione o profissional", profissionais)

        data = st.date_input("Data")
        hora = st.time_input("Hora")

        if st.button("Inserir"):
            id_servico = servico.get_id()
            id_profissional = profissional.get_id()

            data_hora = datetime.combine(data, hora)
            View.horario_inserir(id_servico, id_profissional, data_hora)


            st.success("Horário cadastrado com sucesso!")
            st.rerun()

    # -----------------------------
    @staticmethod
    def atualizar():
        horarios = View.horario_listar()

        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            clientes = View.cliente_listar()
            servicos = View.servico_listar()

            op = st.selectbox("Atualização de Horários", horarios)

            data = st.text_input(
                "Informe a nova data e horário do serviço",
                op.get_data().strftime("%d/%m/%Y %H:%M")
            )

            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())

            id_cliente = None if op.get_id_cliente() in [0, None] else op.get_id_cliente()
            id_servico = None if op.get_id_servico() in [0, None] else op.get_id_servico()

            cliente = st.selectbox(
                "Informe o novo cliente",
                clientes,
                next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), 0)
            )

            servico = st.selectbox(
                "Informe o novo serviço",
                servicos,
                next((i for i, s in enumerate(servicos) if s.get_id() == id_servico), 0)
            )

            if st.button("Atualizar"):
                id_cliente = cliente.get_id() if cliente else None
                id_servico = servico.get_id() if servico else None

                View.horario_atualizar(
                    op.get_id(),
                    datetime.strptime(data, "%d/%m/%Y %H:%M"),
                    confirmado,
                    id_cliente,
                    id_servico
                )

                st.success("Horário atualizado com sucesso")
                st.rerun()

    # -----------------------------
    @staticmethod
    def excluir():
        horarios = View.horario_listar()

        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", horarios)

            if st.button("Excluir"):
                View.horario_excluir(op.get_id())
                st.success("Horário excluído com sucesso")
                time.sleep(1)
                st.rerun()
