# Trabalho de Programação para Web
Professor HERCULES CARDOSO DA SILVA

## Resume

SHOULD I PUT A LONG DESCRIPTION HERE? OR MAYBE SHORT? I DON'T KNOW
<br>
<br>

## Run locally
### Requirements
- Docker
- Docker Compose

<br>

### Environmental variables

- Copy the `.env.dev` to a new file `.env` and update the variables.

<br>

### Build

```
docker-compose build
```
<br>

### Execute

```
docker-compose up
```

<br>

### Finish execution

```
docker-compose down
```

The data is kept in volumes and to clean the database is necessary to remove the `postgres-data` directory.

```
rm -Rf postgres-data
```
<br>
