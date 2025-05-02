import os
import requests

def get_ollama_models():
    """
    Lista os nomes dos modelos disponíveis no contêiner Ollama.

    Returns:
        list: Lista de nomes de modelos disponíveis ou uma lista vazia em caso de erro.
    """
    try:
        print("Iniciando requisição para Ollama...")
        # Use o nome do serviço Docker como hostname
        response = requests.get("http://ollama:11434/api/tags")
        print(f"Status Code: {response.status_code}")
        print(f"Resposta da API: {response.text}")  
        if response.status_code == 200:
            data = response.json()
            if "models" in data and isinstance(data["models"], list):
                # Extrai apenas os nomes dos modelos, removendo o sufixo após ":"
                models = [f"ollama/{model['name'].split(':')[0]}" for model in data["models"]]
                print(f"Modelos extraídos: {models}")
                return models
            else:
                print("Formato inesperado da resposta:", data)
                return []
        else:
            print(f"Erro ao acessar Ollama: {response.status_code} - {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar à API do Ollama: {e}")
        return []

def get_model_default(env_file=".env"):
    """
    Lê o valor da variável MODEL do arquivo .env.

    Args:
        env_file (str): Caminho para o arquivo .env.

    Returns:
        str: O valor da variável MODEL ou None se não for encontrado.
    """
    try:
        with open(env_file, "r") as file:
            for line in file:
                if line.startswith("MODEL="):
                    return line.strip().split("=", 1)[1]
    except FileNotFoundError:
        print(f"Arquivo {env_file} não encontrado.")
    return None

