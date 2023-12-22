
def gpt4(client, mensagens):
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
