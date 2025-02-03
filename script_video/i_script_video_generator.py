from abc import ABC
from tema.tema import Tema
from script_video.script_video import ScriptVideo

class IScriptVideoGenerator(ABC):
    
    def generar_script_video(self, tema: Tema) -> ScriptVideo:
        pass
    
    def crear_contexto(self, tema: Tema):
        """Crea un prompt para pasarselo a algun modelo de lenguaje que lo pueda procesar
        Args:
            tema (Tema): _description_
        """
        pass
    
    