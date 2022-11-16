# 🐳Translator app using Docker and REST APIs 🐳

This repo contains dockerized version of the translator module used in [Subtitle Translation Project](https://github.com/Razwand/subtitle_translation).
The goal is to build a simple app to translate text from Spanish to English, so this is a simplified version of the original project.

## Requirements
- Docker

### Start docker container on a given port.

```console
app_translator_with_docker>docker build image <img_name> .

```
```console
app_translator_with_docker>docker run -d -p <port>:5000 --name <container_name> <img_name>

```
### Call from console (APP USAGE)

```console
app_translator_with_docker>curl -X POST localhost:<port>/translate -H "Content-Type:application/json" -d "{\"text\":\"Hola esto es una prueba del traductor\"}"

```


