# Introdução a Volumes

> Introduzindo Volumes aos Containers

## O que São Volumes?

- Uma forma prática de persistir dados em aplicações e não depender de containers para isso;
- Todo dado criado em um container é salvo nele, quando o container é removido os dados se perdem;
- Os volumes servem para gerenciar os dados e também fazer backups de forma mais simples;

### Tipos de Containers

- **Anônimos (anonymous)**: Diretórios criados pela flag `-v`, porém com um nome aleatório;
- **Nomeados (named)**: volumes com nomes, mais fácil de se referir a eles dentro do ambiente;
- **Bind Mounts**: forma de salvar os dados em nossa máquina, sem o gerenciamento do docker;

## Criando uma aplicação
