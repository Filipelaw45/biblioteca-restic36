# Biblioteca ResTIC36

Este projeto é uma aplicação de biblioteca desenvolvida em Python, utilizando Class-Based Views (CBVs), Paginação, Busca e Ordenação. O objetivo é facilitar a gestão e consulta de livros, autores e categorias.

## Funcionalidades

- **Class-Based Views**: Estrutura modular e reutilizável para as views da aplicação.
- **Paginação**: Navegação eficiente através de listas de livros, permitindo que os usuários visualizem um número limitado de itens por página.
- **Busca**: Funcionalidade de busca para encontrar livros, autores ou categorias específicas.
- **Ordenação**: Capacidade de ordenar os resultados com base em diferentes critérios, como título, autor e data de publicação.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **DRF**: Framework utilizado para desenvolvimento da API.
- **SQLite**: Banco de dados utilizado para armazenamento de dados.

## Instalação

1. Clone o repositório:

  ```bash
  git clone https://github.com/filipelaw45/biblioteca-restic36.git
  cd biblioteca-restic36
  ```

2. Crie um ambiente virtual:

  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  .\venv\Scripts\activate  # Windows
  ```

3. Instale as dependências:

  ```bash
  pip install -r requirements.txt
  ```

5. Execute as migrações do banco de dados

  ```bash
  cd biblioteca
  python manage.py migrate
  ```

6. Popule o banco de dados com dados de exemplo:

  ```bash
  python manage.py seed_db
  ```

7. Inicie o servidor de desenvolvimento:

  ```bash
  python manage.py runserver
  ```

