import json
import requests
import os 
import unicodedata
import re

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
#model = os.environ.get("OLLAMA_VERSION") 
model = "codellama:latest"

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
    

def generate(prompt:str, context:list[str]) -> str:
    """Genera un prompt de Ollama

    Args:
        prompt (str): El prompt que se le pasa al modelo de lenguaje
        context (list[str]): El contexto que se tiene de otros mensajes

    Returns:
        Response(str): El texto que generó el modelo de lenguaje
    """
    r = requests.post('http://localhost:7869/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=True, timeout=100)
    
    r.raise_for_status()

    full_response = ""  # To store the concatenated text response

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        # the response streams one token at a time, print that as we receive it
        print(response_part, end='', flush=True)

        # Append each part of the response to the full text
        full_response += response_part

        if 'error' in body:
            raise Exception(body['error']) 

        if body.get('done', False):
            full_response = sanitize_attribute(full_response)
            return full_response  # Return the full response as text

