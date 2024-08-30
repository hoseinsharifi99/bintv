up:
	docker-compose up -d

run:
	python3 manage.py runserver

up-celery:
	celery -A blog_project worker --loglevel=info

migrate:
	python3 manage.py migrate

makemigrations:
	python3 manage.py makemigrations

requirements:
	python3 -m pip freeze > requirements.txt