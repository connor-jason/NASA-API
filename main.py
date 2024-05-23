from ollamaTesting import ollama_chat 
from nasaapi import nasa_APOD

# pull NASA's Image of the Day
nasa_APOD()

# Give the image to Ollama and print the response
print(ollama_chat('./image.png'))
