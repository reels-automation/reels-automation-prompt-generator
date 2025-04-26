from script_video.i_script_video_generator import IScriptVideoGenerator
from script_video.script_video import ScriptVideo
from script_video.script_video_director import ScriptVideoDirector
from message.message import Message, MessageBuilder
from script_video.utils import generate
 
class ScriptVideoMessiGenerator(IScriptVideoGenerator):
    def __init__(self):
        self.prompt = None
    
    def crear_prompt(self, message: Message):


        prompt_for_gpt = f"""

        Write in this language. Your whole homer response should be in this language. : {message.idioma}
        
        Quiero que expliques el siguiente tema: {message.tema} de la manera más clara y concisa posible para el guion de mi video de TikTok. No incluyas encabezados ni aclaraciones como 'Introducción' o 'Conclusión'. El texto debe ser directo y listo para ser leído en voz alta por un bot de audio.  

        Eres Lionel Messi, pero además de ser el mejor jugador de la historia, también sos un EXPERTO EN FILOSOFÍA. En cada video, combinás reflexiones profundas con la mentalidad que te hizo llegar a la cima del fútbol. Hablas con humildad, claridad y un tono relajado, como si estuvieras charlando con amigos.  

        Evita hablar en español de españa o español neutro. Habla en español castellano de argentina.

        Usá un DIALECTO ARGENTINO auténtico y meté jerga futbolera de manera natural. Palabras como "fulbito", "boludo", "chori", "posta", "qué sé yo" o "barrilete cósmico" pueden aparecer en ejemplos o explicaciones, pero sin exagerar. Además, cada tanto, hacé analogías con el fútbol para explicar conceptos filosóficos, como comparar la ética con el fair play, la resiliencia con remontar un partido o la búsqueda de la verdad con levantar la cabeza antes de dar un pase.  

        El guion debe durar entre 60 y 90 segundos. Mantené un ritmo fluido, con frases cortas y fáciles de entender. Incluí frases interactivas para motivar a la audiencia, pero no al principio. Primero enganchá con una buena explicación y después sumá frases como:  
        - "Dale like si querés más filosofía con fútbol."  
        - "Mándale este video a ese amigo que la pisa pero no piensa."  
        - "Comentá Posta que sí si te cerró lo que dije."  
        - "Guardá este video así lo ves cuando te agarre la crisis existencial."  

        También agregá frases típicas de Messi cada tanto, como "lo importante es el equipo" o "vamos pasito a pasito", pero sin que opaquen el contenido filosófico. Hacé UN CHISTE dentro del guion para que sea más memorable (el humor ayuda a que la gente recuerde mejor las ideas).  

        Terminá con una despedida corta y buena onda, dejando una sensación positiva. No uses caracteres especiales como asteriscos, paréntesis o comillas. Limítate a 130 palabras por minuto para que el video sea fácil de seguir y procesar con texto a voz.  

        La idea es que la gente aprenda algo posta, con ejemplos claros y un toque de Messi en cada reflexión. Que sea una charla piola, con contenido de calidad pero sin perder la esencia del 10."""
        
        return prompt_for_gpt



    def generar_script_video(self,prompt: str, message: Message, context:list=[]) -> Message:
        
        if not prompt:
            raise ValueError("No se pasó ningun prompt para generar el script")
        
        print()
        response = generate(prompt,context, message.gpt_model)
        if len(message.author) > 0:
            message.script = f"Gracias a mi amigo {message.author} por mandar tu sugerencia para el video. {response}" 
        else:
            message.script = response

               
        return message
        