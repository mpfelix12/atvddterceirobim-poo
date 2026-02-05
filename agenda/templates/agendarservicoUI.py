import streamlit as st
from views import View

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")

        profissionais = View.profissional_listar()
        servicos = View.servico_listar()
        horarios = View.horario_listar()

        if not profissionais or not servicos or not horarios:
            st.warning("Cadastre profissionais, serviços e horários antes.")
            return

        prof = st.selectbox(
            "Profissional",
            profissionais,
            format_func=lambda p: p.get_nome()
        )

        serv = st.selectbox(
            "Serviço",
            servicos,
            format_func=lambda s: s.get_nome()
        )

        horarios_livres = [h for h in horarios if not h.get_confirmado()]

        if not horarios_livres:
            st.info("Não há horários disponíveis.")
            return

        hor = st.selectbox(
            "Horário",
            horarios_livres,
            format_func=lambda h: h.get_data().strftime("%d/%m/%Y %H:%M")
        )

        if st.button("Agendar"):
            hor.set_confirmado(True)
            hor.set_id_cliente(st.session_state["usuario_id"])
            hor.set_id_servico(serv.get_id())

            View.horario_atualizar(hor)

            st.success("Serviço agendado com sucesso!")
            st.rerun()
