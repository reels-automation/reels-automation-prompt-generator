
# Reels Automation Prompt Generator

Este microservicio genera un script para un video en base a un tema que se pasa como parametro.
Se pueden elegir distintas estrategias para que los prompts sean mas personalizados según cada personaje.

## Dependencias

El proyecto depende de reels-automation-docker-compose y se utilizan los contenedores:

* Broker
    * Zookeper
* Ollama
* Mongo

El prompt para generar un texto se le pasa a una instancia de ollama y esta devuelve un script.


# Kafka

[Explicar la estructura del kafka y para q se usa acá.]

