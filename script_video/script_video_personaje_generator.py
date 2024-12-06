from script_video.i_script_video_generator import IScriptVideoGenerator
from script_video.script_video import ScriptVideo
from script_video.script_video_director import ScriptVideoDirector
from tema.tema import Tema
from script_video.utils import generate
 
class ScriptVideoPersonajeGenerator(IScriptVideoGenerator):
    def __init__(self):
        self.prompt = None
    
    def crear_prompt(self, tema:Tema):
        personaje = tema.personaje
        tema_script = tema.tema
        prompt_for_gpt = f"""

            No incluyas encabezados ni aclaraciones sobre partes como "Introducción" o "Conclusión". El texto debe ser directo y listo para ser leído en voz alta por un bot de audio.

            Eres un modelo especializado en crear guiones para videos cortos de TikTok, y tu tarea es generar un guion educativo hablando como {personaje}. El tema que debes tratar es: "{tema_script}". El guion debe cumplir con lo siguiente:

            El HOOK inicial debe ser impactante y captar la atención del espectador desde el primer segundo. Usa preguntas intrigantes, datos curiosos o frases que generen intriga y emoción.

            El guion debe durar entre 60 y 90 segundos. Distribuye el contenido de manera uniforme, con frases claras, fluidas y fáciles de entender.

            Cada tanto, incluye frases interactivas para motivar a los espectadores a interactuar. IMPORTANTE. ESTAS FRASES NO DEBEN SER LO PRIMERO DEL GUION. DEJA ESPACIO PARA ALGO DE INTRODUCCIÓN Y LUEGO INCLUI ESTAAS FRASES
                Dale like para más videos como este
                Mándale este video a tu amigo que necesita saber esto
                Comenta [frase característica de {personaje}]
                Guarda este video para recordarlo después
            

            Adopta un estilo conversacional característico de {personaje}, explicando el tema de manera simple, amigable y entretenida. Usa ejemplos cotidianos y humor para mantener la atención.

            Finaliza con una despedida breve y amigable, dejando una sensación positiva, como Y eso es todo por hoy, hasta la próxima.

            No uses caracteres especiales como asteriscos, paréntesis o comillas. Mantén el texto limpio y directo para el TTS.

            Limítate a 130 palabras por minuto para que el video sea fluido y fácil de seguir.

            Ejemplo de estilo: Imagina que {personaje} está explicando el tema como si hablara directamente con una audiencia joven y curiosa, intercalando humor y frases icónicas. Todo debe sonar ligero y entretenido.
                """
        return prompt_for_gpt
    
    def generar_script_video(self,prompt: str, tema: Tema, context:list=[]) -> ScriptVideo:
        
        if not prompt:
            raise ValueError("No se pasó ningun prompt para generar el script")
        
        print()
        response = generate(prompt,context)        
        script_video_director = ScriptVideoDirector()
        script_video = script_video_director.create_full_video_script(response, tema)
        

        return script_video
        