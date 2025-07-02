# backend_module.py

from dotenv import load_dotenv
from mistralai import Mistral
import base64
import os

load_dotenv()

def encode_image(image_path):
    """Encode the image to base64."""
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_haircut_advice(image_path):
    """Get haircut advice from the model using an image path."""
    base64_image = encode_image(image_path)
    if not base64_image:
        return "L'image n'a pas pu être encodée."

    client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))
    
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Propose moi une coupe de cheuveux"},
                {"type": "image_url", "image_url": f"data:image/jpeg;base64,{base64_image}"}
            ]
        }
    ]

    try:
        chat_response = client.chat.complete(
            model="pixtral-12b-2409",
            messages=messages
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        return f"Erreur lors de la génération de la réponse : {e}"
