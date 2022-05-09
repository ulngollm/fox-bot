env:
	cp .env.example .env
build:
	docker build . -t foxbot

run:
	docker run -v $(CURDIR):/usr/src/app foxbot