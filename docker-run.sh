docker run \
  -e KAFKA_BROKER=broker:9092 \
  -e OLLAMA_MODEL=mistral:latest \
  -e OLLAMA_IP=http://localhost:11434/api/generate \
  -e OLLAMA_IP_DOCKER=http://ollama:7869/api/generate \
  -e KAFKA_BROKER_DOCKER=broker:9092 \
  prompt-generator
