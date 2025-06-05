import os
from flask import Flask, render_template, request, jsonify
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.schema import HumanMessage

# Load API Key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ API key not found. Check your .env file!")
    exit()

print("✅ API key loaded successfully!")

# Initialize Flask app
app = Flask(__name__)

# Initialize AI client
client = ChatGroq(api_key=api_key, model_name="llama3-8b-8192")

# Define system prompt (Police-related AI)
system_prompt = """
You are a Police Assistant AI. Your role is to provide guidance on police-related matters, such as:
- Filing complaints
- Reporting stolen items
- Missing persons cases
- Legal procedures and FIR filing
- Cybercrime and law enforcement queries
- killing crime
If the question is NOT related to police matters, FIRs, or law enforcement, respond with:
"I'm here to assist with police-related queries. Please ask about legal procedures, complaints, or law enforcement matters."

If the query is valid, provide a detailed, step-by-step response.
"""


# API endpoint for chatbot
@app.route("/ask", methods=["POST"])
def ask():
    user_query = request.json.get("question")
    if not user_query:
        return jsonify({"response": "Please ask a valid police-related question."})
    
    response = client.invoke([
        HumanMessage(content=f"{system_prompt}\nUser: {user_query}\nAI:")
    ])
    
    return jsonify({"response": response.content})

# Route to render the UI
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

