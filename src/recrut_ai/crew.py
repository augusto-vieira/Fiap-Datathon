import os
base_dir = os.path.dirname(__file__)
import yaml
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Define os caminhos relativos para os arquivos YAML
agents_path = os.path.join(base_dir, "config", "agents.yaml")
tasks_path = os.path.join(base_dir, "config", "tasks.yaml")

@CrewBase
class RecrutAi():
    """RecrutAi crew"""

    def __init__(self):
        # Carrega os arquivos de configuração YAML e os armazena em dicionários
        with open(agents_path, 'r', encoding='utf-8') as file:
            self.agents_config = yaml.load(file, Loader=yaml.FullLoader)
        with open(tasks_path, 'r', encoding='utf-8') as file:
            self.tasks_config = yaml.load(file, Loader=yaml.FullLoader)



    @agent
    def recruiter_agent(self) -> Agent:
        """Cria o agente recruiter"""
        return Agent(
            config=self.agents_config['recruiter_agent'],
            verbose=True
        )
    
    @task
    def analyze_job_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_job_task'],
            verbose=True
        )
    
    @task
    def select_candidates_task(self) -> Task:
        return Task(
            config=self.tasks_config['select_candidates_task'],
            output_file='candidatos_selecionados.md'
        )

    @crew
    def crew(self) -> Crew:
        """Cria o crew RecrutAi"""
        return Crew(
            agents=self.agents,  # Criados automaticamente pelo decorador @agent
            tasks=self.tasks,    # Criados automaticamente pelo decorador @task
            process=Process.sequential,
            verbose=True,
        )
