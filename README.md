# 🦜 Chat with SQL Database using LLMs

An interactive **Streamlit + LangChain + Groq (LLaMA 3.1)** powered app that lets you **query your SQL databases using natural language.**  
This project bridges the gap between **LLMs and structured data** — making database analytics conversational and intelligent.

---

## 🚀 Features

✅ **Chat-based Interface** – Ask questions about your SQL database in plain English.  
✅ **Supports Multiple Databases** – Connect to **SQLite (student.db)** or your own **MySQL** instance.  
✅ **LangChain SQL Agent** – Dynamically translates user queries to SQL using LangChain’s `SQLDatabaseToolkit`.  
✅ **Groq LLM (LLaMA 3.1)** – Fast, low-latency inference with `ChatGroq`.  
✅ **Streamlit UI** – Smooth, responsive, and production-ready interface.  
✅ **Safe Query Execution** – Includes query validation and parsing safeguards.  
✅ **Session Memory** – Keeps conversation history across multiple turns.

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Frontend** | [Streamlit](https://streamlit.io/) |
| **LLM Provider** | [Groq API](https://groq.com/) with LLaMA 3.1 |
| **Framework** | [LangChain](https://python.langchain.com/) |
| **Database Layer** | SQLite / MySQL (via SQLAlchemy) |
| **Toolkit** | LangChain SQL Agent Toolkit (`SQLDatabaseToolkit`) |
| **Deployment** | Streamlit Cloud / Local environment |

---

## 🧩 Project Structure

📦 Chat-with-SQL-Database-using-LLMs
│
├── app.py # Main Streamlit app
├── student.db # Sample SQLite database (students table)
├── requirements.txt # Python dependencies
├── sqlite.py # (Optional) Helper for local DB
├── README.md # Project documentation
└── .streamlit/
└── secrets.toml # (For storing API keys securely on Streamlit Cloud)

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SachdevaVansh/Chat-with-SQL-Database-using-LLMs.git
cd Chat-with-SQL-Database-using-LLMs
```
2️⃣ Create and Activate a Virtual Environment
```bash
conda create -n chatbot python=3.10
conda activate chatbot
```
3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
4️⃣ Add Your API Key
You’ll need a Groq API key.

Locally:

```bash
export GROQ_API_KEY="your_groq_api_key_here"
```
Or in Streamlit Cloud:
Add this line in .streamlit/secrets.toml
```toml
GROQ_API_KEY = "your_groq_api_key_here"
```
5️⃣ Run the App
```bash
streamlit run app.py
```
💬 How It Works
The app initializes a LangChain SQL Agent using SQLDatabaseToolkit.

You select the database (SQLite / MySQL).

Enter your Groq API key and connect.

Type any natural language query — e.g.:

Query:
- Show all students with marks above 80.

The LLM:

Interprets the intent

Generates the SQL query

Executes it safely

Displays the results in chat format

🧱 Example Query Flow

User: Show me the average marks per class.

LLM Thought: I need to group students by class and compute their average marks.

SQL Query: SELECT class, AVG(marks) FROM students GROUP BY class;

Result: ...

🧰 Supported Databases
Database	Status	Configuration
SQLite	✅ Default (student.db)	Auto-loaded
MySQL	✅ Supported	Requires host, user, password, db name

🧩 Environment Variables
Variable	Description
- GROQ_API_KEY	Your Groq LLM API key
- MYSQL_HOST	(optional) MySQL hostname
- MYSQL_USER	(optional) MySQL username
- MYSQL_PASSWORD	(optional) MySQL password
- MYSQL_DB	(optional) MySQL database name

📦 Requirements
```bash
streamlit
langchain
langchain-community
langchain-groq
sqlalchemy
mysql-connector-python
```
🛠️ Troubleshooting
❌ Error: ImportError: cannot import name 'AgentType'
✅ Fix: Use the latest langchain-community and pin the LangChain version in requirements.txt.

❌ Error: groq.GroqError: The api_key client option must be set...
✅ Fix: Add your GROQ_API_KEY in secrets or environment variables before running.

❌ Infinite Loop:
✅ Fix: Limit the agent iterations (max_iterations=3) in create_sql_agent().

🌐 Deployment
You can deploy this easily on Streamlit Cloud:

Push your repo to GitHub.

Go to share.streamlit.io.

Connect your repo.

Add your Groq API key in Secrets.

Deploy 🚀

🧑‍💻 Author
👤 Vansh Sachdeva
Data Scientist | AI Engineer | Generative AI Enthusiast

⭐ Acknowledgements
LangChain for the LLM framework

Groq Cloud for ultra-fast inference

Streamlit for rapid app development

💡 Future Enhancements
Add support for PostgreSQL and Snowflake

Integrate LLM-based schema summarization

Add a query visualization dashboard

Implement RAG (Retrieval Augmented Generation) for documentation-based context
