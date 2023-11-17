# Import the necessary modules
from flask import Flask, render_template, request
import gpt4
import time

# Create a Flask web application
app = Flask(__name__)

# List to store chat messages
messages = []

# Define the route for the home page
@app.route('/')
def index():
    # Render the index.html template and pass the messages list to it
    print("Rendering index.html")
    return render_template('index.html', messages=messages)

# Define the route for sending a message
@app.route('/send_message', methods=['POST'])
def send_message():
    # Get the user's message from the form
    user_message = request.form['user_message']
    
    # Check if the user wants to exit the application
    if user_message == 'sair':
        print("Aplicação será encerrada em 30 segundos...")
        time.sleep(30)
        exit()
    else:
        # Append the user's message to the messages list
        messages.append(('User', user_message))
        print(f"User message: {user_message}")
        
        # Generate a response using the gpt4 module
        resposta = gpt4.principal(user_message)
        
        # Append the generated response to the messages list
        messages.append(('GPT-4', f'{resposta}'))
        print(f"GPT-4 response: {resposta}")
        
        # Render the index.html template and pass the messages list to it
        print("Rendering index.html")
        return render_template('index.html', messages=messages)


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)