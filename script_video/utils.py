import json
import requests
import os 
import unicodedata
import re
from dotenv import load_dotenv  

load_dotenv()
environment = os.getenv("ENVIRONMENT")
    
if environment == "DEVELOPMENT":
        OLLAMA_IP = os.getenv("OLLAMA_IP")
else:
        OLLAMA_IP = os.getenv("OLLAMA_IP_DOCKER")

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
    r = requests.post(OLLAMA_IP,
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=True, timeout=100)
    
    r.raise_for_status()

    full_response = ""  

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        print(response_part, end='', flush=True) # Muestra token x token el texto. 

        full_response += response_part

        if 'error' in body:
            raise Exception(body['error']) 

        if body.get('done', False):
            return full_response  

