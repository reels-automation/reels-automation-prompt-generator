import json
import requests
import os 
import unicodedata
import re
from settings import OLLAMA_IP
from errors.errors import PromptError

def sanitize_attribute(attribute: str):
    """Sanitiza un input para que no contenga caracteres que no puedan ser parseados
    Args:
        attribute (str):
    Returns:
        (str):
    """
    if attribute != None:
        result = (
            unicodedata.normalize("NFKD", attribute)
            .encode("ASCII", "ignore")
            .decode("ASCII")
        )
        result = re.sub(r"[^a-zA-Z0-9_-]", " ", result)
        result = result.strip()
        return result
    return None
    

def generate(prompt:str, context:list[str], model:str) -> str:
    """Genera un prompt de Ollama

    Args:
        prompt (str): El prompt que se le pasa al modelo de lenguaje
        context (list[str]): El contexto que se tiene de otros mensajes

    Returns:
        Response(str): El texto que generó el modelo de lenguaje
    """
    try:
        r = requests.post(OLLAMA_IP,
                            json={
                                'model': model,
                                'prompt': prompt,
                                'context': context,
                            },
                            stream=True, timeout=100)
    except requests.RequestException as ex:
        raise PromptError(
            mensaje="Error al conectarse al endpoint de Ollama",
            status_code=400,
            error_log=ex
        )
    
    if r.status_code != 200:
        error = r.json()['error']
        raise PromptError(mensaje="Error al generar un respuesta en la api de ollama", status_code=r.status_code, error_log=error)


    full_response = ""  

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        print(response_part, end='', flush=True) 

        full_response += response_part
     

        if body.get('done', False):
            return full_response  

