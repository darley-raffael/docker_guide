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
  Ex:

```bash
docker run -d -p 80:80 --name php_container --rm -v /Users/darley.raffael/www/Developer_Learn/docker/project_volume:/var/www/html 402a3d1a9060
```

#### Poder Extra do Bing Mounts

- Podemos usar também como forma de manter de pé o nosso container
- Acompanhar a atualização em tempo real do nosso projeto
- Com isso não precisamos fazer o build a cada nova atualização

## Lidando com volumes

### Criando volumes automaticamente

- Podemos criar volumes de modo manual;
- Utilizamos o comando: `docker volume create <nome>`;
- Desta maneira temos um _*named volume*_ criado;
- Podemos atrelar algum container na execução do mesmo;

```bash
# Criando um volume
docker volume  create volume_test

# Iniciando um container com o volume criado
docker run -d -p 80:80 --name php_container --rm -v volume_test:/var/www/html 402a3d1a9060
```

### Listando Volumes

- Comando: `docker volume ls`

### Inspecionando volumes

- Comando: `docker volume inspect`
  Retorno:

```json
[
  {
    "CreatedAt": "2023-07-13T19:22:02Z",
    "Driver": "local",
    "Labels": {},
    "Mountpoint": "/var/lib/docker/volumes/volume_test/_data",
    "Name": "volume_test",
    "Options": {},
    "Scope": "local"
  }
]
```

### Removendo Volumes

- Comando `docker volume rm <nome>`
- OBS: os dados do volume são removidos também

#### Removendo volumes em Massa

- Remover volumes não utilizados;
- Comando:

```bash
docker volume prune
```

- Semelhante ao _*prune*_ que remove imagens e containers

### Volume somente leitura

- Criar volume com permissão _somente leitura_
- Comando:

```bash
docker run -v volume:data:ro
```

- O `:ro` é a abreviação de **read only**
