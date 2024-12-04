import time
import logging
import json
import ast
from quixstreams import Application
from script_video.script_video_personaje_generator import ScriptVideoPersonajeGenerator
from tema.tema_director import TemaDirector


def main():
    tema_director = TemaDirector()
    app_consumer = Application(
        broker_address="localhost:9092",
        loglevel = "DEBUG",
        consumer_group = "temas_reader",
        auto_offset_reset="latest",
    )
    
    with app_consumer.get_consumer() as consumer:
        consumer.subscribe(["temas"])
        
        while True:
                msg = consumer.poll(1)
                if msg is None:
                    print("Waiting...")
                elif msg.error() is not None:
                    raise Exception(msg.error())
                else:
                    print(msg.value())
                    key = msg.key().decode("utf8")
                    msg_value = msg.value()
                    offset = msg.offset()
                    print(f"{offset} {key} {msg_value}")
                    consumer.store_offsets(msg)
                    app_producer = Application(
                        broker_address="localhost:9092",
                        loglevel = "DEBUG"
                    )    
                    with app_producer.get_producer() as producer:
                            
                            msg_value = ast.literal_eval(msg_value.decode("utf-8"))
                            print(msg_value)
                            print("Started producing...")
                            
                            topic = tema_director.build_tema_con_personaje_sin_author(msg_value["tema"],msg_value["personaje"])
                            script_generator = ScriptVideoPersonajeGenerator()
                            prompt = script_generator.crear_prompt(topic)
                            script_video = script_generator.generar_script_video(prompt, topic.__dict__)
                            producer.produce(
                                topic = "scripts_video",
                                key = "Ai Scripts",
                                value = str(script_video.__dict__)
                            )
                            logging.info("Produced. Sleeping..")
            

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
