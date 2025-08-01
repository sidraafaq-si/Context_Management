# Context_Management
This project builds an intelligent, context-aware agent that uses tools and dynamic instructions to answer user queries like their name or roll number, based on stored context. It leverages the agents framework and OpenAI's API.

🚀 Features
✅ Dynamic instruction generation based on user context
✅ Custom tool integration using decorators
✅ Sync execution of agents
✅ Powered by OpenAI's GPT models (configurable)
🛠️ Requirements
Python 3.9+
openai
pydantic
python-dotenv
rich
agents framework (custom or internal library)
📦 Installation
Clone the repository:

git clone https://github.com/yourusername/ai-agent-user-info.git
cd ai-agent-user-info
Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Create a .env file with your API key:

OPENAI_API_KEY=your-openai-api-key
🧪 Usage
Run the main script:

python main.py
You should see a response like:

pgsql
Copy
Edit
User roll no is abc12345000 and name is Nida
📁 Project Structure
bash
Copy
Edit
.
├── main.py             # Main script with agent definition and execution
├── .env                # Environment file for API keys
├── README.md           # Project overview
└── requirements.txt    # Python dependencies
🧩 How it Works
Context Definition:
User_Info (a Pydantic model) holds user attributes like name, age, and roll number.

Dynamic Instructions:
The dynamic_ins() function modifies how the agent behaves based on current context.

Tooling:
User_information() is a custom function-tool the agent can call when asked about user details.

Agent Execution:
The Runner.run_sync() method runs the agent synchronously with user input and context.

🧠 Example Prompt
"What is the name of user? and what is his roll no?"

Agent will respond using the registered tool with contextual information
