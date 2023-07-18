# Networks - Conectando Containers

**_O Que são networks?_**

> - Uma forma de gerenciar a conexão do Docker com outras plataformas
> - Os Networks são criados separados dos containers
> - Uma rede deixa mais simples a conexão entre containers

---

## Tipos de conexão

- **Externa**: conexão de uma api com um servidor remoto;
- **Com o host**: comunicação com a máquina que está executando o docker;
- **Entre containers**: comunicação que utiliza o driver bridge e permite a comunicação entre dois ou mais containers;

## Tipos de rede(drivers)

- **Bredge**: default do Docker, utilizado quando containers precisam se conectar entre si;
- **host**: permite conexão entre um container a máquina que está hosteando o Docker;
- **macvlan**: permite a conexão de rede de um container;
- **plugins**: permite a extensões de terceiros para criar outras redes;

### Listando redes

- Algumas redes já estão criadas, fazem parte da configuração do Docker;
- Comando:

```bash
docker network ls
```

### Criando Redes

- Para criar uma rede usamos o comando:

```bash
docker network create <nome>
```

- Está rede será do tipo **bridge**, que é mais utilizado;
- É possível criar diversas redes;
