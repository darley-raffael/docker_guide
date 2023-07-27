# Exercícios Práticos de Networks Docker

> Os exercícios práticos serão feitos usando o python com a biblioteca Flask

## Network externo com Docker

### Exemplo: _*Api_Python_External*_

## Network Host com Docker

### Exemplo: _*Api_Python_Host*_

- Podemos nos conectar em um container usando um container com o host Docker
- _*Host*_ é uma máquina que está executando no Docker
- Como ip de host utilizamos: `host.docker.internal`
- Podemos usar nosso próprio ip host

## Network entre containers

### Exemplo: _*Api_Python_Containers*_

- Duas imagens distintas rodando em containers separados que precisam de conectar para inserir um dado no banco
- Pra isso é necessário criar uma rede **bridge**, para fazer a conexão;
- No exemplo o contianer de Api Flask Vai inserir dados no banco em Mysql que roda pelo Docker
