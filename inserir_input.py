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
