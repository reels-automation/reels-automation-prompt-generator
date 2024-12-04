"""Builder de la clase Tema"""
from tema.tema import Tema
 
class TemaBuilder():
    def __init__(self,tema:str) -> None:
        """_summary_

        Args:
            tema (str): _description_
        """
        self.tema = Tema(tema)

    def add_personaje(self, personaje: str):
        self.tema.personaje = personaje
    
    def add_author(self, author: str):
        self.tema.author = author
    
    def build(self) -> Tema:
        return self.tema
