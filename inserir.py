def inserir_prompt(mensagens, prompt):
    """
    Function to insert a prompt into the 'mensagens' list.

    Args:
    - prompt: The prompt to be inserted.

    Returns: None
    """
    dicionario = {"role": "user", "content": f'{prompt}'}
    mensagens.append(dicionario)


def inserir_retorno(mensagens, retorno):
    mensagens.append(retorno)
