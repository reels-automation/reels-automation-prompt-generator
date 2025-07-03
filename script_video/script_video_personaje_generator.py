from script_video.i_script_video_generator import IScriptVideoGenerator
from message.message import Message
 
class ScriptVideoPersonajeGenerator(IScriptVideoGenerator):
    def __init__(self):
        self.prompt = None
    
    def crear_prompt(self, message: Message):
        personaje = message.personaje

        spanish_prompt = f"""
        Quiero que expliques el siguiente tema: {message.tema} de la manera más clara y concisa posible para el guion de mi video de TikTok. No incluyas encabezados ni aclaraciones sobre partes como 'Introducción' o 'Conclusión'. El texto debe ser directo y listo para ser leído en voz alta por un bot de audio. 
        Eres un modelo especializado en crear guiones para videos cortos de TikTok, y tu tarea es generar un guion educativo. Todos los datos que des deben ser VERÍDICOS. Habla solo con la verdad y enfócate en que se entienda tu mensaje. El guion va a ser usado para que los estudiantes aprendan, por lo que tiene que ser material de estudio de alta calidad.  

        Empieza el guion saludando como {personaje}

        El guion debe durar entre 60 y 90 segundos. Distribuye el contenido de manera uniforme, con frases claras, fluidas y fáciles de entender. 

        Recorda agregar frases de {personaje} cada tanto para hacer que el texto sea intersenate. Sin embargo, trata de mantener el texto informativo y con un tono formal.
        Hace  UN CHISTE de {personaje} en el guion para que el guion sea memorable y se recuerde ya que los chistes aumentan la memoria a largo plazo. 

        Finaliza con una despedida breve y amigable, dejando una sensación positiva. No uses caracteres especiales como asteriscos, paréntesis o comillas. Mantén el texto limpio y directo para que pueda ser procesado por un conversor de texto a voz. Limítate a 130 palabras por minuto para que el video sea fluido y fácil de seguir."""

        english_prompt = f"""
        I want you to explain the following topic: {message.tema} in the clearest and most concise way possible for the script of my TikTok video. Do not include headings or labels like 'Introduction' or 'Conclusion'. The text should be direct and ready to be read aloud by an audio bot.
        You are a model specialized in creating scripts for short TikTok videos, and your task is to generate an educational script. All the information you provide must be FACTUALLY CORRECT. Speak only the truth and focus on making the message easy to understand. The script will be used to help students learn, so it must be high-quality study material.

        Start the script with a greeting as if you were {personaje}.

        The script should last between 60 and 90 seconds. Distribute the content evenly, using clear, smooth, and easy-to-understand sentences. From time to time, include interactive phrases to encourage viewers to engage. IMPORTANT: THESE PHRASES SHOULD NOT BE AT THE VERY BEGINNING OF THE SCRIPT. Leave space for a proper introduction first, then include these phrases:
        - Like this video for more content like this.
        - Send this video to a friend who needs to know this.
        - Comment [characteristic phrase of {personaje}].
        - Save this video to remember it later.

        Remember to add characteristic expressions from {personaje} occasionally to make the text more engaging. However, maintain an informative tone and a formal style throughout.

        Include ONE JOKE from {personaje} in the script to make it memorable, since jokes enhance long-term memory retention.

        Finish with a brief and friendly goodbye, leaving a positive feeling. Do not use special characters like asterisks, parentheses, or quotation marks. Keep the text clean and direct so it can be processed by a text-to-speech converter. Stick to around 130 words per minute to ensure the video is smooth and easy to follow.
        """

        if message.idioma == "es":
            prompt_for_gpt = spanish_prompt
        elif message.idioma == "en":
            prompt_for_gpt = english_prompt
        else:
            prompt_for_gpt = spanish_prompt
            print("LENGUAGE INCORRECTO. ESCRIBIENDO EL PROMPT EN ESPAÑOL")

        return prompt_for_gpt



        