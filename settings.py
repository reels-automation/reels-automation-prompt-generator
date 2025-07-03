import os
from dotenv import load_dotenv  
load_dotenv()
KAFKA_BROKER = os.getenv("KAFKA_BROKER")
OLLAMA_IP = os.getenv("OLLAMA_IP")
