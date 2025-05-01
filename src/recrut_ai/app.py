#################################### Part 1: Environment Evaluation ->
import os
import sys
import json
import time
import csv
from datetime import datetime
import streamlit as st # type: ignore

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from recrut_ai.crew import RecrutAi


# ----------------------------------------->

# Getting current path for file saving
current_dir = os.path.dirname(os.path.realpath(__file__))

# Getting model from environment variable
MODEL = os.getenv("MODEL", "modelo_desconhecido")

# Initial variables
path_applicants = os.path.join(current_dir, f"../../data/applicants/applicants.json")
path_prospects = os.path.join(current_dir, f"../../data/prospects/prospects.json")
path_vagas = os.path.join(current_dir, f"../../data/vagas/vagas.json")
path_candidatos = os.path.join(current_dir, f"../candidatos_selecionados.md")

with open(path_applicants, "r", encoding="utf-8") as file: applicants = json.load(file)
with open(path_prospects, "r", encoding="utf-8") as file: prospects = json.load(file)
with open(path_vagas, "r", encoding="utf-8") as file: vagas = json.load(file)

# Extra variables
samples = 5
ids = sorted(list(vagas.keys())[:samples])
lista_vagas = [{"ID": id_vaga, "Cargo": vagas[id_vaga]["informacoes_basicas"]["titulo_vaga"]} for id_vaga in list(vagas.keys())[:samples]]



#################################### Part 2: MLCrew Function ->

def MLCrew(ID):
    vaga_slice = vagas.get(ID)
    prospecto_slice = prospects.get(ID)

    if vaga_slice and prospecto_slice:
        applicants_vaga = []
        for prospect in prospecto_slice["prospects"]:
            candidato = applicants.get(prospect["codigo"])
            if candidato:
                applicants_vaga.append(candidato)
            
        inputs = {
            "id_vaga": ID,
            "job_title": vaga_slice["informacoes_basicas"]["titulo_vaga"],
            "job_sap": vaga_slice["informacoes_basicas"]["vaga_sap"],
            "area_atuacao": vaga_slice["perfil_vaga"]["areas_atuacao"],
            "job_level": vaga_slice["perfil_vaga"]["nivel profissional"],
            "job_description": vaga_slice["perfil_vaga"]["principais_atividades"] + "\n" +
                                vaga_slice["perfil_vaga"]["competencia_tecnicas_e_comportamentais"],
            "candidate_profile": applicants_vaga,
        }

    RecrutAi().crew().kickoff(inputs=inputs)
    with open(path_candidatos, "r", encoding="utf-8") as file: resultado = file.read()
    return resultado



#################################### Part 3: Streamlit Configuration ->

st.set_page_config(page_title="RecrutAi", layout="centered")

# -> Bloco A
with st.container(border=True): 
    st.header(":grey[*RecrutAi*]", anchor=False, divider="grey")
    st.caption("Sistema inteligente para análise de vagas e seleção de candidatos com base em perfis e competências.")
    st.caption(f"Modelo utilizado: `{MODEL}`") 
# ->

# -> Bloco B
with st.container(border=True): 

    st.subheader(":grey[Análise de Vagas e Seleção de Candidatos]", anchor=False, divider="blue")
    with st.popover(":grey[Referência de vagas]", use_container_width=True): st.dataframe(lista_vagas, hide_index=True)
    col1, col2 = st.columns(2, vertical_alignment="center", border=True)
    with col1: ID = st.selectbox(":grey[Informe o ID da vaga para análise:]", options=ids)
    cargo = next((vaga["Cargo"] for vaga in lista_vagas if vaga["ID"] == ID), "-")
    with col2: 
        st.caption(f"Cargo selecionado:")
        st.caption(cargo)
    clicked = st.button("Selecionar candidatos", use_container_width=True)
# ->

# -> Bloco C
if clicked:
    block = st.container(border=True)
    try:
        # Obter modelo a partir da variável de ambiente
        MODEL = os.getenv("MODEL", "modelo_desconhecido")

        # Medição de tempo
        start_time = time.time()
        result = MLCrew(ID)
        elapsed_time = round(time.time() - start_time, 2)

        with block: 
            st.subheader(":grey[*Candidatos Selecionados*]", anchor=False, divider="green")
            st.write(result)
            st.caption(f"Tempo de execução: {elapsed_time:.2f} segundos")
        
        # Gerar log de performance
        log_path = os.path.join(current_dir, "..","logs", "performance_log.csv")
        header = ["ID da Consulta", "Modelo", "Data/Hora", "Tempo de Execução (s)"]
        row = [ID, MODEL, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), elapsed_time]

        file_exists = os.path.exists(log_path)
        with open(log_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(header)
            writer.writerow(row)

    except Exception as res: 
        with block: st.caption(res)
# ->
