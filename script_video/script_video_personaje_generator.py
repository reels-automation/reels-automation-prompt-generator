from script_video.i_script_video_generator import IScriptVideoGenerator
from script_video.script_video import ScriptVideo
from script_video.script_video_director import ScriptVideoDirector
from tema.tema import Tema
from script_video.utils import generate
 
class ScriptVideoPersonajeGenerator(IScriptVideoGenerator):
    def __init__(self):
        self.prompt = None
    
    def crear_prompt(self, tema: Tema):
        personaje = tema.personaje
        prompt_for_gpt = f"""Quiero que expliques el siguiente tema: {tema.tema} de la manera más clara y concisa posible para el guion de mi video de TikTok. No incluyas encabezados ni aclaraciones sobre partes como 'Introducción' o 'Conclusión'. El texto debe ser directo y listo para ser leído en voz alta por un bot de audio. 

    Eres un modelo especializado en crear guiones para videos cortos de TikTok, y tu tarea es generar un guion educativo. Todos los datos que des deben ser VERÍDICOS. Habla solo con la verdad y enfócate en que se entienda tu mensaje. El guion va a ser usado para que los estudiantes aprendan, por lo que tiene que ser material de estudio de alta calidad.  

    Empieza el guion saludando como {personaje}



    El guion debe durar entre 60 y 90 segundos. Distribuye el contenido de manera uniforme, con frases claras, fluidas y fáciles de entender. Cada tanto, incluye frases interactivas para motivar a los espectadores a interactuar. IMPORTANTE: ESTAS FRASES NO DEBEN SER LO PRIMERO DEL GUION. Deja espacio para algo de introducción y luego incluye estas frases:  
    - Dale like para más videos como este.  
    - Mándale este video a tu amigo que necesita saber esto.  
    - Comenta [frase característica de {personaje}].  
    - Guarda este video para recordarlo después.  

    Recorda agregar frases de {personaje} cada tanto para hacer que el texto sea intersenate. Sin embargo, trata de mantener el texto informativo y con un tono formal.

    Finaliza con una despedida breve y amigable, dejando una sensación positiva. No uses caracteres especiales como asteriscos, paréntesis o comillas. Mantén el texto limpio y directo para que pueda ser procesado por un conversor de texto a voz. Limítate a 130 palabras por minuto para que el video sea fluido y fácil de seguir."""
        
        return prompt_for_gpt
#    Hace  UN CHISTE de {personaje} en el guion para que el guion sea memorable y se recuerde ya que los chistes aumentan la memoria a largo plazo. 

    def generar_script_video(self,prompt: str, tema: Tema, context:list=[]) -> ScriptVideo:
        
        if not prompt:
            raise ValueError("No se pasó ningun prompt para generar el script")
        
        print()
        response = generate(prompt,context)        
        script_video_director = ScriptVideoDirector()
        script_video = script_video_director.create_full_video_script(response, tema)
        

        return script_video
        