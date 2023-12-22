import pandas as pd
from gerar_timestamp import *
import os


def salvar_dict(mensagens, arquivo_csv):
    df = pd.DataFrame(mensagens)
    df.to_csv(arquivo_csv, index=False)


def iniciar_arquivo_txt():
    timestamp = gerar_timestamp()
    arquivo_txt = os.path.join('outputs', f'output_{timestamp}.txt')
    return arquivo_txt


def iniciar_arquivo_csv():
    timestamp = gerar_timestamp()
    arquivo_csv = os.path.join('csv_saved', f'mensagens_{timestamp}.csv')
    return arquivo_csv


def escrever_arquivo(arquivo, prompt, resposta):
    """
    Function to write the prompt and response to a file.

    Args:
    - prompt: The prompt.
    - resposta: The response.
    - numero: A random number used for the file name.

    Returns: None
    """
    if os.path.exists(arquivo):
        with open(arquivo, 'a') as file:
            file.write(f'\nPrompt: {prompt}\n')
            file.write(f'\nResposta: {resposta}\n')
    else:
        with open(arquivo, 'w') as file:
            file.write(f'\nPrompt: {prompt}\n')
            file.write(f'\nResposta: {resposta}\n')
