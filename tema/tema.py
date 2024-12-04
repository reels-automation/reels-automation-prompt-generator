"""Class para la logica de los tema"""

import unicodedata
import re
from typing import Any

class Tema:
    """_summary_
    """
    def __init__(self, tema:str, personaje: str=None, author:str=None) -> None:
        """_summary_

        Args:
            tema (str): _description_
            personaje (str, optional): _description_. Defaults to None.
            author (str, optional): _description_. Defaults to None.
        """
        self.tema = self.__sanitize_attribute(tema)
        self.personaje = self.__sanitize_attribute(personaje)
        self.author = self.__sanitize_attribute(author)
    
    def __sanitize_attribute(self,attribute:str):
        """Sanitiza un input para que no contenga caracteres que no puedan ser parseados

        Args:
            attribute (str):

        Returns:
            (str):
        """
        if attribute != None:
            result = unicodedata.normalize('NFKD', attribute).encode('ASCII', 'ignore').decode('ASCII')
            result = re.sub(r'[^a-zA-Z0-9_-]', ' ', result)
            result = result.strip()
            return result
        return None
