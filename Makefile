app/run:
	poetry run python ./list_products/main.py

app/api:
	poetry run python ./list_products/flask_main.py

bot/run:
	poetry run python ./list_products/bot_main.py


app/test/unit:
	poetry run pytest
