.PHONY: build up down logs ps exec prune save load images

build:
	docker-compose build --no-cache

up:
	docker-compose up -d --remove-orphans

down:
	docker-compose down

logs:
	docker-compose logs -f

ps:
	docker-compose ps

exec:
	# run a sh in the running web container
	docker-compose exec web sh

prune:
	docker system prune -a --volumes

save:
	# save the web image to tar
	docker save docker-practice/web:latest -o web-image.tar

load:
	docker load -i web-image.tar

images:
	docker images
