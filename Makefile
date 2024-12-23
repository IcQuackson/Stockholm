
SRC_DIR = ./src
CONTAINER_NAME = linux

all: $(SRC_DIR)/docker-compose.yml $(SRC_DIR)/dockerfile
	sudo docker compose -f $(SRC_DIR)/docker-compose.yml up --build -d 

restart:
	sudo docker compose restart

rerun: clean all

clean:
	- sudo docker compose down
	- sudo docker system prune -a

connect:
	sudo docker exec -it $(CONTAINER_NAME) bash