# Documentação do Projeto

## Arquitetura

Este projeto segue a arquitetura **MVC (Model-View-Controller)**, que é uma abordagem comum para aplicações web. A arquitetura MVC separa a aplicação em três componentes principais:

- **Model**: Responsável pela lógica de dados e interação com o banco de dados.
- **View**: Responsável pela interface do usuário e apresentação dos dados.
- **Controller**: Responsável por lidar com as requisições HTTP, processar os dados do modelo e retornar as respostas apropriadas.

## Estrutura de Diretórios

Abaixo está a estrutura de diretórios do projeto e as responsabilidades de cada diretório:

```
__pycache__/
.env
.gitignore
app/
    __init__.py
    __pycache__/
    controllers/
        routes/
            __pycache__/
            rotas_de_adm.py
            rotas_de_agendamento.py
    models.py
    static/
        css/
            styles.css
        img/
            exemple
        js/
            exemple
    templates/
        index.html
        tela_inicial.html
config.py
migrations/
    exemple
requirements.txt
run.py
tests/
    exemple
```

### Descrição dos Diretórios

- **app/**: Diretório principal da aplicação.
  - **\_\_init\_\_.py**: Arquivo de inicialização da aplicação Flask.
  - **controllers/**: Contém os controladores que lidam com as requisições HTTP.
    - **routes/**: Contém os arquivos de rotas específicas.
      - **rotas_de_adm.py**: Rotas relacionadas à administração.
      - **rotas_de_agendamento.py**: Rotas relacionadas ao agendamento.
  - **models.py**: Arquivo onde os modelos de dados são definidos.
  - **static/**: Contém arquivos estáticos como CSS, JavaScript e imagens.
    - **css/**: Arquivos de estilo CSS.
      - **styles.css**: Arquivo de estilos principal.
    - **img/**: Imagens utilizadas na aplicação.
    - **js/**: Arquivos JavaScript.
  - **templates/**: Contém os arquivos HTML que são renderizados como resposta.
    - **index.html**: Página inicial da aplicação.
    - **tela_inicial.html**: Outra página da aplicação.
- **config.py**: Arquivo de configuração da aplicação.
- **migrations/**: Diretório para arquivos de migração do banco de dados.
- **requirements.txt**: Lista de dependências do projeto.
- **run.py**: Ponto de entrada da aplicação. Inicializa e executa a aplicação Flask.
- **tests/**: Diretório para arquivos de teste.

## Comandos Úteis

### Docker Compose

- **Subir os contêineres**:

  ```sh
  docker-compose up -d
  ```

- **Desmontar os contêineres**:

  ```sh
  docker-compose down
  ```

- **Listar os contêineres em execução**:

  ```sh
  docker ps
  ```

- **Verificar os logs de um contêiner específico**:
  ```sh
  docker logs <nome_do_container>
  ```

### Executar o Projeto

- **Rodar a aplicação Flask**:
  ```sh
  python run.py
  ```

### Variáveis de Ambiente

Certifique-se de que o arquivo `.env` esteja configurado corretamente com as variáveis de ambiente necessárias:

```env
POSTGRES_USER=usuarioLocal
POSTGRES_PASSWORD=senhaLocal
POSTGRES_DB=bancoLocal
POSTGRES_PORT=5432
```

### Instalar Dependências

- **Instalar dependências do projeto**:
  ```sh
  pip install -r requirements.txt
  ```

## Como Executar

Para executar a aplicação, siga os passos abaixo:

1. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

2. Execute a aplicação:
   ```sh
   python run.py
   ```

## Contribuição

Esta documentação fornece uma visão geral da arquitetura do projeto, a estrutura de diretórios e comandos úteis para gerenciar os contêineres Docker e executar a aplicação. Certifique-se de seguir as instruções para configurar corretamente o ambiente de desenvolvimento.
