from flask import Flask, render_template, request, jsonify
import os
from groq import Groq


app = Flask(__name__) 
client =  Groq(api_key="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")

def groq_model_response(content): 
    chat_response = client.chat.completions.create(messages=[{"role": "system","content":("A conversational ChatBot that gives short and precise response")}, {"role": "user", "content":content}], model = "llama3-70b-8192")
    return chat_response.choices[0].message.content

@app.route("/")
def hello_world():
    return render_template("Chat.html")
    #return('ChatBot Project')

@app.route("/ask", methods=["POST"])
def ask():
   message = request.form["messageText"]
   response = groq_model_response(message)
   return jsonify ({
        "status": "OK",
        "answer": response
    
    })

if __name__ == "__main__":
    app.run(debug=True)
    