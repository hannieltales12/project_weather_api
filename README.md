# Weather API Project

O seguinte projeto consta com uma API de clima que realiza a coleta de dados via web scraping utilizando request, armazena-os em um banco de dados PostgreSQL e utiliza o Django e o Django Rest Framework para criar uma landing page que exibe as informações coletadas. O projeto está contido em containers Docker para fácil configuração e execução.

## Funcionalidades

- **CRUD Completo**: Criação, leitura, atualização e exclusão de dados de clima.
- **Busca por Nome da Cidade**: Permite buscar dados de clima pelo nome da cidade.
- **Landing Page**: Exibe os dados de clima em uma tabela, com botões para atualização e exclusão.
- **Endpoints Internos**: Uma aba na landing page exibe os endpoints internos do projeto.

## Pré-requisitos

- Docker
- Docker Compose
- Git

## Instalação

### Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/project-weather-api.git
cd project-weather-api

```
### Criação do arquivo .env
### Exemplo:

SECRET_KEY='sua-chave-secreta'
DEBUG=True
ALLOWED_HOSTS="127.0.0.1, localhost"
POSTGRES_DB='weatherdb'
POSTGRES_USER='weatheruser'
POSTGRES_PASSWORD='weatherpassword'
POSTGRES_HOST='db'
POSTGRES_PORT='5432'


## Subir os containers
```bash
docker-compose build
docker-compose up
```

## Considerações
- O projeto não consta com todos os requisitos solicitados pelo teste. Resolvi desenvolvê-lo mesmo incompleto pois seria um desafio visto nunca ter utilizado o Django. Ao todo esse projeto foi desenvolvido em 7 horas sofridas kkkkk distribuídas ao longo da semana, devido ter uma rotina de trabalho das 8hrs as 18h e depois faculdade até as 22h.

- Além disso ele carece um tanto em documentação, pelo menos em relação ao padrão de documentação que tento manter nos meus códigos.

- Na pasta .temp se encontra a visualização de como ficou o projeto.

