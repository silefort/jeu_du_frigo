# Nom de l'image et du conteneur
IMAGE_NAME=jeu-frigo
CONTAINER_NAME=jeu-frigo-container
PORT=5000

# Builder l'image Docker
build:
	docker build -t $(IMAGE_NAME) .

# Lancer le conteneur en arrière-plan
run:
	docker run -d --rm --name $(CONTAINER_NAME) -p $(PORT):5000 $(IMAGE_NAME)

# Arrêter le conteneur
stop:
	docker stop $(CONTAINER_NAME) || true

# Ouvrir un tunnel public avec localtunnel
# -> nécessite que 'lt' soit installé en global : npm install -g localtunnel
tunnel:
	@echo "mot de passe local tunnel: $$(curl -s https://loca.lt/mytunnelpassword)"
ifeq ($(SUBDOMAIN),)
	lt --port $(PORT)
else
	lt --port $(PORT) --subdomain $(SUBDOMAIN)
endif

# Lancer tout : build + run + tunnel
all: stop build run tunnel
