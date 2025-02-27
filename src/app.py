import streamlit as st
import sqlite3
import openai
from query_generator import generate_sql, load_db_schema
from sql_validator import validate_sql, execute_test_query

st.title("LLM-Based SQL Query Generator")

st.sidebar.header("Project Settings")
db_path = st.sidebar.text_input("Database Path","data/spider_data/database/coffee_shop/coffee_shop.sqlite")

natural_language_query = st.text_area("Enter your natural language query: ", "")


# Initialize session state for sql_query if not set
if "sql_query" not in st.session_state:
    st.session_state["sql_query"] = ""

if st.button("Generate SQL"):
    if natural_language_query.strip():
        st.session_state["sql_query"] = generate_sql(load_db_schema(db_path),natural_language_query)
    else:
        st.session_state["sql_query"] = ""
        st.warning("Please enter a query.")
        

st.subheader("Generated SQL Query")
# Always display the stored SQL query
if st.session_state["sql_query"]:
    st.code(st.session_state["sql_query"], language="sql")


if st.button("Validate & Execute"):
    if  st.session_state["sql_query"]:
        is_valid, validation_msg = validate_sql(st.session_state["sql_query"])
        if is_valid:
            st.success("✅ SQL is valid!")
            success, result = execute_test_query(st.session_state["sql_query"],db_path)
            if success:
                st.dataframe(result)
            else:
                st.error(f"Execution Error: {result}")
        else:
            st.error(f"Invalid SQL: {validation_msg}")
    else:
        st.warning("Generate a query first!")