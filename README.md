# NLQ : Natural Language Query for text to SQL converter using LLM

This project is a SQL query generator that uses natural language processing to convert text questions into SQL queries. It's designed to work with Oracle databases and directly apply the changes to the database just from text and utilizes the LangChain library along with the Ollama language model.

## Features

- Convert natural language questions to SQL queries
- Retrieve table schema information from Oracle databases
- Execute SQL queries and display results
- Support for custom language models via Ollama

## Requirements

- Python 3.x
- cx_Oracle
- langchain
- langchain_ollama
- python-dotenv
- Ollama (with a supported model, default is 'gemma')

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/Ayoub-Elkhaiari/NLQ_Natural_language_query.git
   cd NLQ_Natural_language_query
   ```

2. Install the required packages:
   ```
   pip install cx_Oracle langchain langchain_ollama python-dotenv
   ```

3. Set up your Oracle database credentials in a `.env` file:
   ```
   ACCOUNT=your_oracle_account
   PASSWORD=your_oracle_password
   ```

## Usage

1. Run the main script:
   ```
   python main.py
   ```

2. Enter the table name when prompted.

3. Enter your question in natural language.

4. The script will generate and execute the corresponding SQL query, then display the results.

## Project Structure

- `main.py`: The main script that orchestrates the query generation and execution process.
- `Oracle.py`: Contains the `Oracle` class for interacting with the Oracle database.
- `LLM.py`: Defines the `LLM` class for initializing the language model.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Future Improvements

Making it capable for administration purposes (oracle database administration via text)

## Disclaimer

This tool generates SQL queries based on AI model outputs. Always review and validate the generated queries before executing them on production databases.
