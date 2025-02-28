# 🦾 LLM-Based SQL Query Generator

## 📌 Project Overview
This project is an AI-powered SQL Query Generator that translates natural language queries into SQL statements using **GPT-4**. It helps users generate, validate, and execute SQL queries against a specified database schema.

## 🎯 Features
- **Natural Language to SQL**: Uses OpenAI's GPT-4 to generate SQL queries.
- **Query Validation**: Ensures generated queries are syntactically correct.
- **Database Execution**: Runs SQL queries against an SQLite database.
- **Custom Schema Support**: GPT generates SQL based on your database schema.
- **User-Friendly UI**: Built with **Streamlit** for ease of use.
- **Secure API Key Management**: Users can input their **OpenAI API Key** manually or load it from a `.env` file.

## 🛠️ Tech Stack
- **Backend**: Python, OpenAI API, SQLite
- **Frontend**: Streamlit
- **Libraries**: LangChain, SQL Parsing, python-dotenv

## 🚀 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/llm-sql-query-generator.git
cd llm-sql-query-generator
```

### 2️⃣ Create and Activate a Virtual Environment (Optional but Recommended)
```bash
# On macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up the `.env` File
Create a `.env` file in the root directory and add your **OpenAI API Key**:
```ini
OPENAI_API_KEY=your_openai_api_key_here
```

### 5️⃣ Run the Streamlit App
```bash
streamlit run src/ui.py
```

## 🛠️ Usage
1. Enter your **OpenAI API Key** in the **Project Settings** section or let it load from `.env`.
2. Provide the **database path** to your SQLite file.
3. Enter a natural language query (e.g., "Show all employees who joined after 2020").
4. Click **Generate SQL** to get the SQL query.
5. Validate & Execute the query to see the results.

## 📁 Project Structure
```plaintext
📂 llm-sql-query-generator
├── 📂 src
│   ├── ui.py  # Streamlit UI
│   ├── sql_generator.py  # Generates SQL using GPT-4
│   ├── sql_validator.py  # Validates & executes SQL queries
├── .env  # API key (ignored in .gitignore)
├── schema.sql  # Sample database schema
├── imdb.sqlite  # Example SQLite database
├── requirements.txt  # Dependencies
└── README.md  # Project documentation
```

## 🏗️ Future Enhancements
- **Fine-Tune Open-Source LLM**: Replace GPT-4 with **Code Llama** for better query accuracy.
- **Support for More Databases**: Extend support to PostgreSQL and MySQL.
- **Query Optimization**: Improve generated queries for efficiency.
- **User Authentication**: Secure access to query execution.

## 🛡️ License
This project is licensed under the **MIT License**.

## 🤝 Contributing
Pull requests are welcome! If you’d like to contribute, please open an issue first to discuss your changes.

## 📬 Contact
For questions or collaborations, reach out via [your-email@example.com] or open an issue on GitHub. 🚀

