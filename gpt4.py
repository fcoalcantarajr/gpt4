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

mensagens = [{
    "role": "system",
    "content": "Hello, you are an assistant model."
}]

def inserir_prompt(prompt):
    global mensagens
    dicionario = {"role": "user", "content": f'{prompt}'}
    mensagens.append(dicionario)


def gpt4(mensagens):
    # Call the GPT-4 model to generate a completion
    completion = client.chat.completions.create(model="gpt-4-1106-preview",
                                                messages=mensagens)
    # Extract the content and role from the generated completion
    content = completion.choices[0].message.content
    role = completion.choices[0].message.role
    # Return the content and role as a list
    dicionario = {"role": role, "content": content}
    return dicionario

def get_multiline_input():
    print(
        "Enter your prompt. Press Ctrl+D (or Ctrl+Z on Windows) when finished:"
    )
    input_lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        input_lines.append(line)

    return "\n".join(input_lines)


def main():
    while True:
        texto = get_multiline_input()
        if texto != 'sair':
            inserir_prompt(texto)
            retorno = gpt4(mensagens)
            print(retorno["content"])
        else:
            print('Saindo...')
            break


if __name__ == '__main__':
    main()
