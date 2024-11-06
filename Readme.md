# Edpassare Advanced Class AI Website Project

This project is a Flask-based web application that interacts with the Groq AI model to provide chatbot responses (Voice and Text). Users can submit questions or prompts through an HTML form, and the application processes the input with Groq's API to generate an intelligent response.

## Features

- Interactive chatbot interface
- Responsive AI-based answers powered by Groq's Llama3 model
- Simple and user-friendly HTML form for submitting questions

## Prerequisites

- Python 3.x
- Groq API key (required for API access)
- Flask and other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
   ```

2. **Create a virtual environment (optional but recommended)**:

   ```bash
    python3 -m venv myenv
    source myenv/Scripts/activate   # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**:

   ```bash
    pip install -r requirements.txt
    ```

4. **Set up your Groq API key:**:
    ```
        - Replace "your_groq_api_key_here" in client = Groq(api_key="your_groq_api_key_here") with your actual Groq API key.
    ```

## File Structure

- main.py: Main application file that defines routes and chatbot response logic.
- templates/: Contains *chat.html*, which is the HTML form for submitting messages.


## Running the Application


1. **Start the Flask application:**:

   ```bash
    python main.py
    ```

2. **Access the application:**:

    - Open your browser and go to http://127.0.0.1:5000.

3. **Interacting with the Chatbot:**:

    - Enter a message in the text field and click "Send".
    - The chatbot will respond with an AI-generated answer by default with a text and  voice response.
    - Clear button - clears the current conversation screen
    - Toggle Voice - Activates the voice response ON/OFF

## API Endpoint

The chatbot API has a single endpoint:

- POST /ask: Accepts a messageText parameter from the form data and returns a  JSON response with a generated answer.

1. **Example Request**:

   ```html
    <form action="/ask" method="POST">
        <input type="text" name="messageText" placeholder="Type your question...">
        <button type="submit">Ask</button>
    </form>

    ```

2. **Example Response**:

   ```json
    {
    "status": "OK",
    "answer": "This is the AI-generated response."
    }
    ```

## License

    This project is licensed under the MIT License.