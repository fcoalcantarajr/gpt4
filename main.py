import os
from datetime import datetime

import pytz
from openai import OpenAI

API_KEY = os.getenv('API_KEY')

client = OpenAI(api_key=API_KEY)


def gerar_timestamp():
    """
    Function to generate a timestamp string.

    Returns:
    - A timestamp string in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    timezone = pytz.timezone('America/Fortaleza')
    utc_now = datetime.utcnow()
    utc_now = utc_now.replace(tzinfo=pytz.utc)
    local_now = utc_now.astimezone(timezone)
    timestamp = local_now.strftime('%Y-%m-%d %H:%M:%S')

    return timestamp


mensagens = [{
    "role": "system",
    "content": "Hello, you are an assistant model."
}]


def inserir_prompt(prompt):
    """
    Function to insert a prompt into the 'mensagens' list.

    Args:
    - prompt: The prompt to be inserted.

    Returns: None
    """
    global mensagens
    dicionario = {"role": "user", "content": f'{prompt}'}
    mensagens.append(dicionario)


def gpt4(mensagens):
    """
    Function to call the GPT-4 model and generate a completion.

    Args:
    - mensagens: The list of messages to be passed to the GPT-4 model.

    Returns: A dictionary with the generated content and role.
    """
    # Call the GPT-4 model to generate a completion
    completion = client.chat.completions.create(model="gpt-4-1106-preview",
                                                messages=mensagens)
    # Extract the content and role from the generated completion
    content = completion.choices[0].message.content
    role = completion.choices[0].message.role
    # Return the content and role as a dictionary
    dicionario = {"role": role, "content": content}
    return dicionario


def get_multiline_input():
    """
    Function to get multiline input from the user.

    Returns: A string containing the user's input.
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


def escrever_arquivo(prompt, resposta):
    """
    Function to write the prompt and response to a file.

    Args:
    - prompt: The prompt.
    - resposta: The response.
    - numero: A random number used for the file name.

    Returns: None
    """
    timestamp = gerar_timestamp()
    arquivo = f'output_{timestamp}.txt'
    if os.path.exists(arquivo):
        with open(arquivo, 'a') as file:
            file.write(f'\nPrompt: {prompt}\n')
            file.write(f'\nResposta: {resposta}\n')
    else:
        with open(arquivo, 'w') as file:
            file.write(f'\nPrompt: {prompt}\n')
            file.write(f'\nResposta: {resposta}\n')


def main():
    """
    Main function that handles the user interaction.

    Returns: None
    """
    while True:
        texto = get_multiline_input()
        print("Prompt inserido com sucesso!")
        if texto != 'sair':
            inserir_prompt(texto)
            retorno = gpt4(mensagens)
            conteudo = retorno["content"]
            print(conteudo)
            escrever_arquivo(texto, conteudo)
        else:
            print('Saindo...')
            break


if __name__ == '__main__':
    main()
