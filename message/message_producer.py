import time
from message.message import MessageBuilder, Message
from script_video.script_video_personaje_generator import ScriptVideoPersonajeGenerator

def produce_message(msg_value) -> Message:

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

    if len(message.script) <= 0:
        script_generator = ScriptVideoPersonajeGenerator()
        prompt = script_generator.crear_prompt(message)
        message = script_generator.generar_script_video(prompt, message)
    
    if len(message.tema) <= 0:
        message.tema = f"tema_at_{time.time()}"
    
    return message
    
    