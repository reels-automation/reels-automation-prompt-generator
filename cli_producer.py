from quixstreams import Application
from message.message import MessageBuilder

def main():

    app_producer = Application(broker_address="localhost:9092", loglevel="DEBUG")

    with app_producer.get_producer() as producer:
        while True:
            tema = input("Ingresa un tema \n")
            personaje = input("Ingresa un personaje \n")

            message_builder = MessageBuilder(tema)
            message = (message_builder.add_personaje(personaje).build()) 

            print(message.to_dict())

            producer.produce(
                topic="temas", key="temas_input_humano", value=str(message.to_dict())
            )

if __name__ == "__main__":
    main()
