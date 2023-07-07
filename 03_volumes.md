# Introdução a Volumes

> Introduzindo Volumes aos Containers

## O que São Volumes?

- Uma forma prática de persistir dados em aplicações e não depender de containers para isso;
- Todo dado criado em um container é salvo nele, quando o container é removido os dados se perdem;
- Os volumes servem para gerenciar os dados e também fazer backups de forma mais simples;

## Tipos de Containers

- **Anônimos (anonymous)**: Diretórios criados pela flag `-v`, porém com um nome aleatório;
- **Nomeados (named)**: volumes com nomes, mais fácil de se referir a eles dentro do ambiente;
- **Bind Mounts**: forma de salvar os dados em nossa máquina, sem o gerenciamento do docker;

### Volumes Anônimos

- Podemos criar um volume a anônimo (`anonymous`) com o comando

```bash
docker run -v /data
```

- Onde `/data` será o diretório que contêm o volume anônimo
- Este container será atrelado ao volume anônimo
- Com o comando `docker volume ls`, podemos ver todos os volumes do ambiente

EX:

> Para rodar o testar o volume no diretório `project_volume`

```bash
docker run -d -p 80:80 --name php_container --rm -v /data 402
```

> Vendo os volume criado podemos utilizar o comando

```bash
docker volume ls
```

### Volumes nomeados (`named`)

- Podemos criar um volume nomeado do seguinte modo:

```bash
docker run -v nomevolume:/data
```

- Com o nome o volume pode ser facilmente referenciado
- Quando usamos o comando `docker volume ls` podemos identificar o container nomeado
- O volume assume a mesma funcionalidade: armazenar arquivos
- O diretório tem que ser o mesmo presente no _WORKDIR_ do **Dockerfile**
  EX:

```bash
docker run -d -p 80:80 --name php_container --rm -v phpvolume:/var/www/html/messages 402
```

### Bind Mounts

- Também é um volume, fica em um diretório que nós especificamos;
- Um volume não é criado em si, **_apenas apontamos um diretório_**;
- O comando para criar um bind mount: `docker run /dir/data:/data`;
- Desse modo o diretório `dir/data` no nosso computador, será o volume do container;
