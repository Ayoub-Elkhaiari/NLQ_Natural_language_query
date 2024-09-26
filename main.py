from LLM import LLM
from Oracle import Oracle
from langchain_ollama import OllamaLLM
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()




oracle = Oracle(os.getenv("ACCOUNT"), os.getenv("PASSWORD"))

table = input("Enter the table name: ")

table_info = oracle.get_table_schema(table)


model = LLM()


# Create a prompt template for text-to-SQL conversion
prompt_template = PromptTemplate(
    input_variables=["table_info", "question"],
    template="""
Given the following SQL table:
{table_info}

Generate a SQL query to answer the following question:
{question}

Give just the SQL query, nothing else.

SQL Query:
"""
)

# Create an LLMChain
text_to_sql_chain = LLMChain(llm=model.model, prompt=prompt_template)

question = input("Enter the text here")

# Generate SQL query
query = text_to_sql_chain.run(table_info=table_info, question=question)

# print("Generated SQL Query:")
# print(query)

# print(table_info)
oracle.execute_query(query)
