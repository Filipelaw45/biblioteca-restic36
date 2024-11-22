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

8. Logue com 'admin' senha 'admin123'

9. Execute os testes:

  ```bash
  pytest core/tests/
  ```

10. Documentação em localhost:8000/redoc

11. Swagger em localhost:8000/docs

