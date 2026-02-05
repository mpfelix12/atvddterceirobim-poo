import streamlit as st
from views import View
import time

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        profissionais = View.profissional_listar()

        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Selecione o Profissional", profissionais)
            horarios_disponiveis = View.agendar_horario(profissional.get_id())

            if len(horarios_disponiveis) == 0:
                st.write("Nenhum horário disponível para este profissional")
            else:
                op_horario = st.selectbox("Selecione o Horário", horarios_disponiveis)
                servicos = View.servico_listar()
                op_servico = st.selectbox("Selecione o Serviço", servicos)

                if st.button("Agendar Serviço"):
                    id_cliente = st.session_state['usuario_id']
                    View.horario_atualizar(op_horario.get_id(), op_horario.get_data(), True, id_cliente, op_servico.get_id())
                    st.success("Serviço agendado com sucesso")
                    time.sleep(2)
                    st.rerun()