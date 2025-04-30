#!/bin/bash

# Utilize este script para limpar o seu ambiente de teste/desenvolvimento.

# Parar todos os contêineres em execução
echo "Parando todos os contêineres em execução..."
docker stop $(docker ps -q)

# Remover todos os contêineres
echo "Removendo todos os contêineres..."
docker rm $(docker ps -a -q)

# Remover todas as imagens
echo "Removendo todas as imagens..."
docker rmi $(docker images -q)

# Remover volumes não utilizados (opcional)
echo "Removendo volumes não utilizados..."
docker volume rm $(docker volume ls -q)

# Remover redes não utilizadas (opcional)
# echo "Removendo redes não utilizadas..."
# docker network rm $(docker network ls -q)

# Limpeza geral (opcional)
echo "Realizando limpeza geral do sistema..."
docker system prune -a --volumes -f

echo "Limpeza completa do Docker concluída!"
