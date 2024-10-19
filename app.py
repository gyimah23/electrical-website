from flask import Flask, render_template, request, jsonify
import google.generativeai as palm
import os

app = Flask(__name__, template_folder='template')

# Set the Google Cloud Platform API key for Generative AI service
os.environ["GOOGLE_API_KEY"] = "you api"

# Configure the Palm API
palm.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Generation configuration
generation_config = {
    # ... (same configuration as before)
}

# Create the Generative AI model
model = palm.GenerativeModel(
    model_name="gemini-1.5-flash",  # Verify model availability
    generation_config=generation_config,
)

# Create a chat session
chat_session = model.start_chat(history=[])

# Route for generating text
@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['message']
    response = chat_session.send_message(user_input)
    return response.text  # Return plain text

# Main route for displaying chat interface
@app.route('/')
def chat():
    return render_template('s.html')

if __name__ == '__main__':
    app.run(debug=True)
