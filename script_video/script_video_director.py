from script_video.script_video_builder import ScriptVideoBuilder
from tema.tema import Tema


class ScriptVideoDirector:
    @staticmethod
    def create_full_video_script(script:str,tema:Tema):
        script_video_builder =ScriptVideoBuilder(script)
        script_video_builder.add_tema(tema)
        return script_video_builder.build()

    @staticmethod
    def create_video_no_tema(script:str):
        script_video_builder = ScriptVideoBuilder(script)
        return script_video_builder.build()