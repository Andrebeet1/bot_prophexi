import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_prediction(username):
    prompt = f"Tu es un ancien prophète mystique. Fais une prédiction étrange et poétique pour l'utilisateur nommé {username}."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Tu es un prophète mystérieux."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.9
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return "❌ Je ne peux pas voir ton avenir pour le moment."
