from quixstreams import Application
from tema.tema_director import TemaDirector


def main():

    app_producer = Application(broker_address="localhost:9092", loglevel="DEBUG")

    tema_director = TemaDirector()

    with app_producer.get_producer() as producer:
        while True:
            tema = input("Ingresa un tema \n")
            personaje = input("Ingresa un personaje \n")
            topic = tema_director.build_tema_con_personaje_sin_author(tema, personaje)
            producer.produce(
                topic="temas", key="temas_input_humano", value=str(topic.__dict__)
            )

if __name__ == "__main__":
    main()
