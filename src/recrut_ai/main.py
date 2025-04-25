#!/usr/bin/env python
import sys
import warnings
import json

from datetime import datetime

from recrut_ai.crew import RecrutAi

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """


    with open(r'C:\Users\lucas\OneDrive\Estudos\Datathon\applicants\applicants.json', 'r', encoding='utf-8') as file:
        applicants = json.load(file)

    with open(r'C:\Users\lucas\OneDrive\Estudos\Datathon\prospects\prospects.json', 'r', encoding='utf-8') as file:
        prospecto = json.load(file)

    with open(r'C:\Users\lucas\OneDrive\Estudos\Datathon\vagas\vagas.json', 'r', encoding='utf-8') as file:
        vagas = json.load(file)


    id_analise = '10976' # ID da vaga que queremos analisar
    vaga_slice = vagas.get(id_analise, None) # Trazendo as informações da vaga 10976
    prospecto_slice = prospecto.get(id_analise, None) # Trazendo as informações do prospecto da vaga 10976

    # Criando uma lista com os candidatos que se inscreveram na vaga 10976
    applicants_vaga = []
    for i in prospecto_slice['prospects']:
        applicants_vaga.append(applicants.get(i['codigo'], None))

  


    inputs = {
        'id_vaga': id_analise,
        'job_title': vaga_slice['informacoes_basicas']['titulo_vaga'],
        'job_sap': vaga_slice['informacoes_basicas']['vaga_sap'],
        'area_atuacao': vaga_slice['perfil_vaga']['areas_atuacao'],
        'job_level': vaga_slice['perfil_vaga']['nivel profissional'],
        'job_description': vaga_slice['perfil_vaga']['principais_atividades'] + '\n' + vaga_slice['perfil_vaga']['competencia_tecnicas_e_comportamentais'],
        'candidate_profile': applicants_vaga,
    }

    try:
        # RecrutAi().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs"
    }
    try:
        RecrutAi().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        RecrutAi().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        RecrutAi().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
