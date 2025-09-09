# Jeu du Frigo

## TL;DR
```
make all SUBDOMAIN=mondomainepublic
```

## En plus long

### Pré-requis

Pour faire tourner le jeu en local, docker devrait suffire puis `make build && make run`

### Exposer le jeu sur les internets

Pour exposer le jeu sur internet, `localtunnel` est nécessaire, pour l'installer :
```
npm install -g localtunnel
```
Puis `make tunnel SUBDOMAIN=mondomainepublic`

Cela va créer un tunnel entre votre port 5000 en local et le domaine `https://mondomainepublic.loca.lt`
Le 'mot de passe' à rentrer sur la page exposée est une adresse IP retournée directement par la commande `make tunnel`
