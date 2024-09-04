import google.generativeai as genai

def cliente_gemini(modelo):
    KEY_API = "AIzaSyAoR0Jm03syGRjfidzU-4EpdL4mRJsOeBI"

    genai.configure(api_key=KEY_API)

    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(f'Crie uma descrição em uma linha do modelo de bicicleta {modelo}')
    return response.text
