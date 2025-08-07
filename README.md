# Test task for secunda

## <a id="quick_start">Quick start</a> 🚀
- Create a virtual environment using the command: `python -m venv venv`
- Activate virtual environment
    - For Windows, you need to run the following command: `venv\Scripts\activate`
    - For Linux systems, you need to run the following command: `source venv/bin/activate`
- Check pip: `pip list`
- Next you need to install poetry: `pip install poetry`
- Next download all libraries: `poetry install`

### Setting up environment variables:
**.env**
```
MODE=DEV
DB_USER=user
DB_PASS=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=test-db
API_KEY=5252
```

**.test.env**

```
MODE=TEST
DB_USER=postgres
DB_PASS=postgres
DB_HOST=localhost
DB_PORT=5432
DB_NAME=test_db
```

### Launching the application
  - Using docker-compose: `docker-compose up`
  - Using docker compose: `docker compose up`

### Alembic commands:
  - `alembic init -t async alembic`
  - `alembic revision --autogenerate -m 'initial'`
  - `alembic upgrade head`
  - `alembic downgrade -1`

### Pytest commands:
  - `pytest --maxfail=1 -vv -p no:warnings`
  - `pytest --maxfail=1 -vv -p no:warnings -k 'TestCaseName'`
  - `pytest --maxfail=1 -vv -p no:warnings --ignore=PathName`
  - `make test`

### Ruff commands:
  - `ruff check . --config=pyproject.toml`
  - `make lint`

### Make commands:
```bash
make api
```
```bash
make lint
```
```bash
make test
```