# Import necessary modules
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env file from the folder
load_dotenv()

# Get the API_KEY environment variable
API_KEY = os.getenv('API_KEY')

# Set the API key for the openai module
client = OpenAI(api_key=API_KEY)

# Define a function to interact with the GPT-4 model
def gpt4(prompt, role_sequel=None, prompt_sequel=None):
    # Define an initial message to start the conversation
    mensagem_inicial = [
            {
                "role": "system",
                "content": "Olá, este é um chatbot com você como o GPT-4 de apoio. Você irá conversar comigo."
            },
            {
                "role": "user",
                "content": f"{prompt}"
            }
        ]
    # Append additional messages if provided
    if prompt_sequel != None:
        mensagem_inicial.append({
            "role": f"{role_sequel}",
            "content": f"{prompt_sequel}"
        })
    # Call the GPT-4 model to generate a completion
    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=mensagem_inicial
    )
    # Extract the content and role from the generated completion
    content = completion.choices[0].message.content
    role = completion.choices[0].message.role
    # Return the content and role as a list
    return [content, role]

# Define a function to call the gpt4 function
def chamar_gpt4(prompt, primeira_chamada=1):
    # Call the gpt4 function for the first time
    if primeira_chamada == 1:
        retorno = gpt4(prompt)
        papel = retorno[1]
        conteudo = retorno[0]
        primeira_chamada += 1
        return conteudo
    # Call the gpt4 function for subsequent times
    else:
        while True:
            retorno = gpt4(prompt, papel, conteudo)
            papel = retorno[1]
            conteudo = retorno[0]
            return conteudo

# Define the main function
def principal(prompt):
    # Call the chamar_gpt4 function to get the response from GPT-4
    conteudo = chamar_gpt4(prompt)
    return conteudo

# Add print statements for debugging
prompt = "Hello, GPT-4!"
print("Prompt:", prompt)

# Call the principal function
response = principal(prompt)
print("Response:", response)