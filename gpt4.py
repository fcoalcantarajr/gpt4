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

# Define a list to store messages
mensagens = [{
    "role": "system",
    "content": "Hello, you are an assistant model."
}]

def inserir_prompt(prompt):
    """
    Function to insert a prompt into the messages list.

    Args:
        prompt (str): The user prompt to be inserted into the messages list.
    """
    global mensagens
    dicionario = {"role": "user", "content": f'{prompt}'}
    mensagens.append(dicionario)

def gpt4(mensagens):
    """
    Function to call the GPT-4 model and generate a completion.

    Args:
        mensagens (list): The list of messages.

    Returns:
        dict: A dictionary containing the generated completion's content and role.
    """
    completion = client.chat.completions.create(model="gpt-4-1106-preview",
                                                messages=mensagens)
    content = completion.choices[0].message.content
    role = completion.choices[0].message.role
    dicionario = {"role": role, "content": content}
    return dicionario

def get_multiline_input():
    """
    Function to get multiline input from the user.

    Returns:
        str: The multiline input provided by the user.
    """
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
    """
    Main function that runs the program.
    """
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