import unicodedata
import re

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