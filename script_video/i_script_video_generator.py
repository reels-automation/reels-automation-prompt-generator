from abc import ABC
from tema.tema import Tema
from message.message import Message
from script_video.utils import generate

class IScriptVideoGenerator(ABC):
    
    
    def crear_contexto(self, tema: Tema):
        """Crea un prompt para pasarselo a algun modelo de lenguaje que lo pueda procesar
        Args:
            tema (Tema): _description_
        """
        pass
    
    def generar_script_video(self, prompt:str, message:Message) -> Message:
        
        """Genera un script en base a un prompt

        Args:
            prompt (str): El prompt que se le pasa a ollama para que devuelva una respuesta
            message (Message): 

        Raises:
            ValueError: _description_

        Returns:
            Message: Genera un mensaje con el tema agregado
        """

        if not prompt:
            raise ValueError("No se pasó ningun prompt para generar el script")
        
        print()
        response = generate(prompt=prompt, model=message.gpt_model, context=[])
            
        message.script = response
       
        return message