from script_video.script_video import ScriptVideo
from tema.tema import Tema
class ScriptVideoBuilder:
    def __init__(self, script:str) -> None:
        self.script_video = ScriptVideo(script)
    
    def add_tema(self, tema: Tema):
        self.script_video.tema = tema
        
    def build(self) -> ScriptVideo:
        return self.script_video 
