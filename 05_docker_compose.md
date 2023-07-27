# Gerenciando Múltiplos containers com o Docker Compose

## O que é o Docker Compose

- É uma ferramenta para rodar múltiplos containers
- Possui somente um arquivo de configuração, que orquestra totalmente os containers
- É uma forma de rodar múltiplos builds e runs com um comando
- Essencial em projetos maiores

## Criando um arquivo Docker-Compose

- Criar um arquivo: `docker-compose.yaml`
- O arquivo vai coordenar os containers e imagens, possui chaves muito utilizados
- `version`: versão do Compose - formato do aquivo **_docker-compose.yaml_**
- `services`: Containers/serviços que vão rodar nessa aplicação
- `volumes`: Possível adição de volumes
