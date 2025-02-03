import os
import logging
import ast
import time
from quixstreams import Application
from script_video.script_video_personaje_generator import ScriptVideoPersonajeGenerator
from tema.tema_director import TemaDirector
from dotenv import load_dotenv  


def main():
    load_dotenv()
    tema_director = TemaDirector()
    retry_count = 0 
    
    while retry_count < 5:

        try:

            app_consumer = Application(
                broker_address=os.getenv("KAFKA_BROKER"),
                loglevel="DEBUG",
                consumer_group="temas_reader",
                auto_offset_reset="latest",
            )

            with app_consumer.get_consumer() as consumer:
                consumer.subscribe(["temas"])
                while True:
                    msg = consumer.poll(1)
                    if msg is None:
                        print("Waiting...")
                    elif msg.error() is not None:
                        raise ValueError(msg.error())
                    else:
                        print(msg.value())
                        key = msg.key().decode("utf8")
                        msg_value = msg.value()
                        offset = msg.offset()
                    #   print(f"{offset} {key} {msg_value}")
                        consumer.store_offsets(msg)
                        app_producer = Application(
                            broker_address=os.getenv("KAFKA_BROKER"), loglevel="DEBUG"
                        )
                        with app_producer.get_producer() as producer:

                            msg_value = ast.literal_eval(msg_value.decode("utf-8"))
                            print(msg_value)
                            print("Started producing...")

                            topic = tema_director.build_tema_con_personaje_sin_author(
                                msg_value["tema"], msg_value["personaje"]
                            )
                            script_generator = ScriptVideoPersonajeGenerator()
                            
                            prompt = script_generator.crear_prompt(topic)

                            script_video = script_generator.generar_script_video(
                                prompt, topic.__dict__
                            )
                            producer.produce(
                                topic="scripts_video",
                                key="Ai Scripts",
                                value=str(script_video.__dict__),
                            )
                            logging.info(f"Producing: {script_video.__dict__}")
                            logging.info("Produced. Sleeping..")
        
        except ValueError as ex:
            print(f"Error: {ex}, retrying...")
            retry_count += 1
            time.sleep(5)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
