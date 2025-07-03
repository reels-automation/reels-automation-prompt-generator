import os
import logging
import ast
import time
from quixstreams import Application
from script_video.script_video_personaje_generator import ScriptVideoPersonajeGenerator
from script_video.script_video_messi_generator import ScriptVideoMessiGenerator
from tema.tema_director import TemaDirector
from message.message import MessageBuilder
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

                print(msg.value())
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
                    print("Msg Value:", msg_value)
                    print("Started producing...")

                    message_builder = MessageBuilder(msg_value["tema"])

                    message = (
                        message_builder
                        .add_usuario(msg_value["usuario"])
                        .add_idioma(msg_value["idioma"])
                        .add_personaje(msg_value["personaje"])
                        .add_script(msg_value["script"])
                        .add_audio_item(msg_value["audio_item"])
                        .add_subtitle_item(msg_value["subtitle_item"])
                        .add_author(msg_value["author"])
                        .add_gameplay_name(msg_value["gameplay_name"])
                        .add_background_music(msg_value["background_music"])
                        .add_images(msg_value["images"])
                        .add_random_images(msg_value["random_images"])
                        .add_random_amount_images(msg_value["random_amount_images"])
                        .add_gpt_model(msg_value["gpt_model"])
                        .build()
                    )

                    script_generator = ScriptVideoPersonajeGenerator()

                    if len(message.script) <= 0:
                        prompt = script_generator.crear_prompt(message)
                        message = script_generator.generar_script_video(prompt, message)

                    if len(message.tema) <= 0:
                        message.tema = f"tema_at_{time.time()}"

                    producer.produce(
                        topic="scripts_video",
                        key="Ai Scripts",
                        value=str(message.to_dict()),
                    )

                    logging.info(f"Producing: {message.to_dict()}")
                    logging.info("Produced. Sleeping..")

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
