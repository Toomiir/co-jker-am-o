from openai import OpenAI
from env import API_KEY

client = OpenAI(api_key=API_KEY)

def corregir_gramatica(texto_a_corregir):
    prompt = f"Corrige la siguiente frase gramaticalmente:\n{texto_a_corregir}\nCorrección:"

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user",
        "content": prompt
      }
    ],
        max_tokens=150
    )

    correccion_gramatical = response.choices[0].message.content  

    return correccion_gramatical

if __name__ == "__main__":
    texto_original = "Hoy hace mucho calor y me gustaria ir a la playa."
    texto_corregido = corregir_gramatica(texto_original)
    
    print("Texto original:", texto_original)
    print("Texto corregido:", texto_corregido)