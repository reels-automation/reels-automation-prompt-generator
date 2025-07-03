import os
import logging
import ast
import time
from quixstreams import Application
from script_video.script_video_personaje_generator import ScriptVideoPersonajeGenerator
from script_video.script_video_messi_generator import ScriptVideoMessiGenerator
from tema.tema_director import TemaDirector
from message.message import MessageBuilder
from message.message_producer import produce_message
from settings import KAFKA_BROKER
from errors.errors import PromptError

def main():
    
    app_consumer = Application(
        broker_address=KAFKA_BROKER,
        loglevel="DEBUG",
        consumer_group="temas_reader",
        auto_offset_reset="latest",
    )

    with app_consumer.get_consumer() as consumer:
        consumer.subscribe(["temas"])
        print("Consumidor creado")

        while True:
            try:
                msg = consumer.poll(1)
                if msg is None:
                    print("Waiting...")
                    continue
                elif msg.error() is not None:
                    raise ValueError(msg.error())

                key = msg.key().decode("utf8")
                msg_value = msg.value()
                offset = msg.offset()

                consumer.store_offsets(msg)

                app_producer = Application(
                    broker_address=KAFKA_BROKER,
                    loglevel="DEBUG"
                )

                with app_producer.get_producer() as producer:
                    
                    msg_value = ast.literal_eval(msg_value.decode("utf-8"))
                    logging.info("Msg Value: %{msg_value}")
                    print("Started producing...")


                    message = produce_message(msg_value)
                    
                    producer.produce(
                        topic="scripts_video",
                        key="Ai Scripts",
                        value=str(message.to_dict()),
                    )

                    logging.info("Produced a message. Sleeping")

            except PromptError as ex:
                logging.error(ex)
            except KeyboardInterrupt:
                logging.info("Closing...")
                break
            except Exception as ex:
                logging.error(f"[Unhandled Exception] {ex}")

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
