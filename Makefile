include .env
export

make install:
	poetry install
	poetry run python ./scripts/create_db.py

make start:
	poetry run python -m src.echo_bot
