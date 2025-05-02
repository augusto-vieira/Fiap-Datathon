#!/bin/bash

echo "🧹 Limpando containers e recursos do projeto FIAP Datathon..."

# Parar os containers do projeto
docker stop api_agent_ai ollama 2>/dev/null

# Remover os containers do projeto
docker rm api_agent_ai ollama 2>/dev/null

# Remover volume associado
docker volume rm ollama_data 2>/dev/null

# (Opcional) Remover imagens específicas (apenas se quiser forçar rebuild)
# docker rmi fiap-datathon-app ollama/ollama 2>/dev/null

# (Opcional) Limpar recursos não utilizados
docker image prune -f
docker volume prune -f

echo "✅ Projeto limpo com sucesso!"
