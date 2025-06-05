import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.schema import HumanMessage

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("❌ API key not found. Check your .env file!")
    exit()

print("✅ API key loaded successfully!")

# Initialize AI client
client = ChatGroq(api_key=api_key, model_name="llama3-8b-8192")

# Define system prompt (ensures AI only answers police-related queries)
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

def get_police_assistant_response(user_query):
    response = client.invoke([
        HumanMessage(content=f"{system_prompt}\nUser: {user_query}\nAI:")
    ])
    return response.content

# Continuous loop to take input from CMD
while True:
    user_query = input("\n🔹 Ask your police-related question (or type 'exit' to quit): ")
    
    if user_query.lower() in ["exit", "quit"]:
        print("🚔 Exiting Police AI Assistant. Stay safe!")
        break

    ai_response = get_police_assistant_response(user_query)
    print(f"\n🤖 AI: {ai_response}")


















voice input feature



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Police AI Assistant</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: linear-gradient(135deg, #000000, #1a1a1a, #2b2b2b);
            color: white;
            font-family: Arial, sans-serif;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
            padding: 0;
        }

        .chat-container {
            width:80%;
            max-width: 350px;
            height: 95vh;
            display: flex;
            flex-direction: column;
            border-radius: 30px;
            background: white;
            color: rgb(210, 12, 12);
            overflow: hidden;
            border: 2px solid black;
            position: relative;
        }

        .chat-header {
            text-align: center;
            font-size: 15px;
            font-weight: bold;
            padding: 12px;
            border-bottom: 2px solid rgb(36, 34, 34);
        }

        .chat-box {
            flex-grow: 1;
            padding: 12px;
            overflow-y: auto;
            scrollbar-width: thin;
            display: flex;
            flex-direction: column;
            scroll-behavior: smooth;
        }

        .message {
            padding: 8px;
            border-radius: 12px;
            margin: 4px 0;
            font-size: 12px;
            display: inline-block;
            max-width: 75%;
            word-wrap: break-word;
            transition: all 0.3s ease-in-out;
        }

        .user-message {
            background: linear-gradient(45deg, #bae8f0, #5447e7);
            color: white;
            align-self: flex-end;
            text-align: right;
            cursor: pointer;
        }

        .ai-message {
            background: linear-gradient(45deg, #f9f9f9, #caecc0);
            color: black;
            align-self: flex-start;
            white-space: pre-line;
        }
        .ai-message img {
            max-width: 100%;
            border-radius: 8px;
            margin-top: 8px;
        }
        .typing-indicator {
            background: gray;
            color: white;
            padding: 8px;
            border-radius: 12px;
            font-size: 12px;
            align-self: flex-start;
        }

        .input-group {
            display: flex;
            gap: 8px;
            padding: 10px;
            background: white;
            border-top: 2px solid black;
            border-radius: 0 0 30px 30px;
        }

        input {
            flex: 1;
            padding: 10px;
            border-radius: 25px;
            border: 1px solid black;
            outline: none;
            font-size: 12px;
        }
        .ask-btn {
            background: green;
            color: white;
            padding: 10px 16px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.2s ease-in-out;
        }
        .ask-btn:hover {
            background: #1f7d1f;
        }

        .ask-btn, .mic-btn {
            padding: 10px;
            border-radius: 30px;
            border: none;
            cursor: pointer;
            font-size: 12px;
            transition: all 0.2s ease-in-out;
        }

        .ask-btn {
            background: green;
            color: white;
        }

        .ask-btn:hover {
            background: #1f7d1f;
        }

        .mic-btn {
            background: #e74c3c;
            color: white;
        }

        .mic-btn:hover {
            background: #c0392b;
        }
        .menu-bar {
    position: absolute;
    top: 0;
    left: 0;
    width: 250px;
    height: 100%;
    background: rgba(9, 9, 9, 0.9);
    color: white;
    display: flex;
    flex-direction: column;
    transform: translateX(-100%);
    transition: all 0.3s ease-in-out;
    overflow-y: auto; /* Enables scrolling for the entire menu */
    scrollbar-width: thin;
    max-height: 100vh;
}
.menu-bar.open {
            transform: translateX(0);
        }
        .menu-header {
            font-size: 16px;
            font-weight: bold;
            padding: 12px;
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            position: sticky;
            top: 0;
            z-index: 10;
        }
         .menu-content {
    width: 100%;
    height: auto;
    background: rgb(255, 255, 255);
    color: black;
    border-radius: 12px;
    padding: 10px;
    overflow-y: auto; /* Enables scrolling for past questions */
    scrollbar-width: thin;
    max-height: 80vh; /* Adjust this height to fit content properly */
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
}


        .menu-item {
            font-size: 12px;
            padding: 8px;
            border-bottom: 1px solid gray;
            cursor: pointer;
            transition: background 0.2s;
            white-space: normal;
            word-wrap: break-word;
            overflow-wrap: break-word;
            max-width: 100%;
        }

        .menu-item:hover {
            background: rgba(255, 255, 255, 0.2);
        }

        .menu-toggle {
            position: absolute;
            top: 7px;
            left: 7px;
            background: linear-gradient(45deg, #d6d6d2, #8b5cf6);
            color: black;
            border-radius: 50%;
            width: 35px;
            height: 35px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-weight: bold;
            transition: background 0.2s, transform 0.2s;
        }
        .message-time {
    display: block;
    font-size: 10px;
    color: rgb(27, 27, 27);
    margin-top: 2px;
}

    </style>
</head>
<body>
<div class="chat-container">
        <div class="chat-header">   𝐀𝐈-𝐏𝐎𝐋𝐈𝐂𝐄 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓🤖 </div>
        <div class="menu-bar" id="menu-bar">
            <div class="menu-header">📜 Past Questions</div>
            <div id="menu-content"></div>
        </div>
        <div class="menu-toggle" onclick="toggleMenu()">☰</div>
        <div class="chat-box" id="chat-history"></div>
        <div class="input-group">
            <input type="text" id="user-input" placeholder="Ask a police-related question...">
            <button class="ask-btn" onclick="sendMessage()">Ask</button>
            <button class="mic-btn" id="mic-button" onclick="startVoiceRecognition()">🎤</button>
        </div>
    </div>
    

    <script>
    let pastQuestions = [];

    function sendMessage() {
        let userInput = document.getElementById("user-input").value.trim();
        if (!userInput) return;

        let chatHistory = document.getElementById("chat-history");
        let currentTime = new Date().toLocaleTimeString();

        let userMessage = document.createElement("div");
        userMessage.className = "message user-message";
        userMessage.innerHTML = `👤 ${userInput} <br><span class="message-time">${currentTime}</span>`;
        chatHistory.appendChild(userMessage);

        document.getElementById("user-input").value = "";

        let typingIndicator = document.createElement("div");
        typingIndicator.className = "message typing-indicator";
        typingIndicator.innerText = "🤖 Typing...";
        chatHistory.appendChild(typingIndicator);

        chatHistory.scrollTop = chatHistory.scrollHeight;

        fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question: userInput })
        })
        .then(response => response.json())
        .then(data => {
            chatHistory.removeChild(typingIndicator);
            let aiMessage = document.createElement("div");
            aiMessage.className = "message ai-message";
            let aiTime = new Date().toLocaleTimeString();

             if (data.image_url) {
            aiMessage.innerHTML = `<img src="${data.image_url}" alt="Generated Image"><br>🤖 ${data.response} <br><span class="message-time">${aiTime}</span>`;
        } else {
            aiMessage.innerHTML = `🤖 ${data.response} <br><span class="message-time">${aiTime}</span>`;
        }
            
            chatHistory.appendChild(aiMessage);
            chatHistory.scrollTop = chatHistory.scrollHeight;
        });

        pastQuestions.unshift(userInput);
          updateMenu();
    }
    function updateMenu() {
    let menuContent = document.getElementById("menu-content");
    menuContent.innerHTML = ""; // Clear old list

    pastQuestions.forEach(question => {
        let menuItem = document.createElement("div");
        menuItem.className = "menu-item";
        menuItem.innerText = question;
        menuItem.onclick = () => reAskQuestion(question);
        menuContent.appendChild(menuItem);
    });

    // Ensure the scroll bar stays at the top for the latest question
    menuContent.scrollTop = 0;
}


    function toggleMenu() {
        document.getElementById("menu-bar").classList.toggle("open");
    }

    function reAskQuestion(question) {
        document.getElementById("user-input").value = question;
        sendMessage();

    function startVoiceRecognition() {
        let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = "en-US";
        recognition.interimResults = false;
        recognition.maxAlternatives = 1;

        recognition.onstart = function () {
            document.getElementById("mic-button").innerText = "🎙️ Listening...";
        };

        recognition.onresult = function (event) {
            let spokenText = event.results[0][0].transcript;
            document.getElementById("user-input").value = spokenText;
            sendMessage(); // Auto send message after recognition
        };

        recognition.onerror = function () {
            document.getElementById("mic-button").innerText = "🎤";
            alert("Voice recognition failed. Try again.");
        };

        recognition.onend = function () {
            document.getElementById("mic-button").innerText = "🎤";
        };

        recognition.start();
    }

    </script>
</body>
</html>

























