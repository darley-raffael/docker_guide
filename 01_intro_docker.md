# 🐳 Introdução ao Docker

## Comandos Básicos

### Iniciando um Container

```shell
docker run <nome do container>
```

## Comandos de Interação com o Container

### Listar os Containers rodando

```shell
docker ps
```

### Listar os fechados

```shell
docker ps -a
```

### Interromper um Container

```shell
docker stop <nome ou id do container>
```

> _Podemos executar o comando somente com a inicial do id_

### Iniciando o container

```shell
docker start <nome ou id do container>
```

> _Podemos executar o comando somente com a inicial do id_

### Escolhendo o nome do container

```shell
docker --name <nome_container>  <imagem_container>
#exemplo
docker --name server_nginx nginx
```

### Rodando Containers em Background (detached)

```shell
docker run -d nginx
```

### Deixando a porta do servidor visível

> No docker todo o conteúdo não tem acesso externo, para acessar externamente precisamos expor uma porta

```bash
docker run -d -p 80:80 nginx
```

Desse modo conseguimos acessar o servidor na porta 80

### Removendo Containers

```bash
docker rm <nome/id do container>
```

OBS: Não dá de remover um container que está rodando, é necessário para o container ou passar a flag `force`

```bash
docker rm <nome/id container> -f
```
