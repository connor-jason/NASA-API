import ollama

def ollama_chat(image_path: str):
	res = ollama.chat(
		model="llava",
		messages=[
			{
				'role': 'user',
				'content': 'What do you see in this image? How does it make you feel?',
				'images': [image_path]
			}
		]
	)

	return res['message']['content']