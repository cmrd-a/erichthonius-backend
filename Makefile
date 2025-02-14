dbqu:
	docker-compose up --build db queue
uv:
	uvicorn app.main:app --reload --reload-dir ./app

wc:
	watchmedo auto-restart --directory=./app/ --pattern=*.py --recursive -- celery worker -A app.worker -l info -Q main-queue -c 4

gt:
	gnome-terminal -- bash -c "make dbqu"
	gnome-terminal -- bash -c "make uv"
	gnome-terminal -- bash -c "make wc"