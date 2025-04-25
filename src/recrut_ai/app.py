import streamlit as st
import sys
import os
# Adiciona o diretório 'src' ao sys.path para que recrut_ai seja encontrado
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import warnings
import json
from recrut_ai.crew import RecrutAi


st.title("RecrutAi - Análise de Vagas e Seleção de Candidatos")
st.write("Interface gráfica para executar o crew de recrutamento.")

# Upload dos arquivos JSON
# applicants_file = st.file_uploader("Carregar applicants.json", type=["json"])
# prospects_file = st.file_uploader("Carregar prospects.json", type=["json"])
# vagas_file = st.file_uploader("Carregar vagas.json", type=["json"])

with open(os.path.join('data', 'applicants', 'applicants.json'), 'r', encoding='utf-8') as file:
    applicants = json.load(file)

with open(os.path.join('data', 'prospects', 'prospects.json'), 'r', encoding='utf-8') as file:
    prospects = json.load(file)

with open(os.path.join('data', 'vagas', 'vagas.json'), 'r', encoding='utf-8') as file:
    vagas = json.load(file)

# Entrada para o ID da vaga
id_vaga = st.text_input("Digite o ID da vaga que deseja analisar", value="10976")

if id_vaga:
    vaga_slice = vagas.get(id_vaga)
    prospecto_slice = prospects.get(id_vaga)

    if vaga_slice and prospecto_slice:
        # Cria a lista de candidatos inscritos na vaga
        applicants_vaga = []
        for prospect in prospecto_slice['prospects']:
            candidato = applicants.get(prospect['codigo'])
            if candidato:
                applicants_vaga.append(candidato)
        
        # Prepara os inputs para o crew
        inputs = {
            'id_vaga': id_vaga,
            'job_title': vaga_slice['informacoes_basicas']['titulo_vaga'],
            'job_sap': vaga_slice['informacoes_basicas']['vaga_sap'],
            'area_atuacao': vaga_slice['perfil_vaga']['areas_atuacao'],
            'job_level': vaga_slice['perfil_vaga']['nivel profissional'],
            'job_description': vaga_slice['perfil_vaga']['principais_atividades'] + '\n' +
                                vaga_slice['perfil_vaga']['competencia_tecnicas_e_comportamentais'],
            'candidate_profile': applicants_vaga,
        }
        
        if st.button("Executar Análise"):
            try:
                resultado = RecrutAi().crew().kickoff(inputs=inputs)
                st.write("Resultado da Análise:")
                # Ler a saída do crew e exibir
                with open(os.path.join('src', 'candidatos_selecionados.md'), 'r', encoding='utf-8') as file:
                    resultado = file.read()
                st.write(resultado)

            except Exception as e:
                st.error(f"Ocorreu um erro durante a execução: {e}")
    else:
        st.error("Não foi possível encontrar a vaga ou os prospectos para o ID informado.")
