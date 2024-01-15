import os
from openai import OpenAI
import pandas as pd

from inserir import *
from gerar_timestamp import *
from gpt4 import *
from inserir_input import *
from salvar_arquivos import *

API_KEY = os.getenv('API_KEY')


def gerar_mensagens(inicial=None):
    if inicial is None:
        mensagens = [{
            "role": "system",
            "content": "Hello, you are an assistant model."
        }]
    else:
        df = pd.read_csv(inicial, encoding='utf-8-sig')
        mensagens = df.to_dict(orient='records')
    return mensagens


def main():
    """
    Main function that handles the user interaction.

    Returns: None
    """
    client = OpenAI(api_key=API_KEY)
    mensagens = gerar_mensagens()
    arquivo_txt = iniciar_arquivo_txt()
    arquivo_csv = iniciar_arquivo_csv()
    while True:
        texto = get_multiline_input()
        print("Prompt inserido com sucesso!")
        if texto != 'sair':
            inserir_prompt(mensagens, texto)
            retorno = gpt4(client, mensagens)
            inserir_retorno(mensagens, retorno)
            conteudo = retorno["content"]
            print(conteudo)
            escrever_arquivo(arquivo_txt, texto, conteudo)
            salvar_dict(mensagens, arquivo_csv)
        else:
            print('Saindo...')
            break


if __name__ == '__main__':
    main()
