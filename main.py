import os
import logging
import ast
import time
from quixstreams import Application
from script_video.script_video_personaje_generator import ScriptVideoPersonajeGenerator
from tema.tema_director import TemaDirector
from dotenv import load_dotenv  
from message.message import MessageBuilder

def main():
    load_dotenv()
    tema_director = TemaDirector()
    retry_count = 0 
    
    environment = os.getenv("ENVIRONMENT")
    
    if environment == "DEVELOPMENT":
        KAFKA_BROKER = os.getenv("KAFKA_BROKER")
    else:
        KAFKA_BROKER = os.getenv("KAFKA_BROKER_DOCKER")


    while retry_count < 5:

        try:

            app_consumer = Application(
                broker_address=KAFKA_BROKER,
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
                            broker_address=KAFKA_BROKER, loglevel="DEBUG"
                        )
                        with app_producer.get_producer() as producer:

                            msg_value = ast.literal_eval(msg_value.decode("utf-8"))
                            print("Msg Value: " , msg_value)
                            print("Started producing...")

                            message_builder = MessageBuilder(msg_value["tema"])

                            message = (message_builder
                            .add_personaje(msg_value["personaje"])
                            .add_script(msg_value["script"])
                            .add_tts_audio_name(msg_value["tts_audio_name"])
                            .add_tts_audio_bucket(msg_value["tts_audio_bucket"])
                            .add_subtitles_name(msg_value["subtitles_name"])
                            .add_subtitles_bucket(msg_value["subtitles_bucket"])
                            .add_author(msg_value["author"])
                            .add_pitch(msg_value["pitch"])
                            .add_tts_voice(msg_value["tts_voice"])
                            .add_tts_rate(msg_value["tts_rate"])
                            .add_pth_voice(msg_value["pth_voice"])
                            .add_gameplay_name(msg_value["gameplay_name"])
                            .build()
                        )

                            script_generator = ScriptVideoPersonajeGenerator()
                            
                            prompt = script_generator.crear_prompt(message)

                            message = script_generator.generar_script_video(
                                prompt, message
                            )
                            producer.produce(
                                topic="scripts_video",
                                key="Ai Scripts",
                                value=str(message.to_dict()),
                            )
                            logging.info(f"Producing: {message.to_dict()}")
                            logging.info("Produced. Sleeping..")
        
        except Exception as ex:
            print(f"Error: {ex}, retrying...")
            retry_count += 1
            time.sleep(5)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()
