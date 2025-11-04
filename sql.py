import streamlit as st 
import pathlib as Path 

from langchain.agents import create_sql_agent 
form langchain.agents import AgentExecutor
from langchain.sql_database import SQLDatabase 
from langchain.agents.agent_toolkits import SQLDatabaseToolkit 
from langchain.callbacks import StreamlitCallbackHandler 
from sqlalchemy import create_engine 
import sqlite3
from langcahin_groq import ChatGroq

LOCALDB="USE_LOCALDB"
MYSQL="USE_MYSQL"

radio_opt=["Use sqlite3 database","Connect to your SQL Database"]

selected_opt=st.sidebar.radio(label="Choose from the following",options=radio_opt)

if radio_opt(selected_opt)==1:
    db_uri=MYSQL
    mysql_host=st.sidebar.text_input("Provide MySQL Host")
    mysql_user=st.sidebar.text_input("MySQL user")
    mysql_password=st.sidebar.text_input("MySQL password",type="password")
    mysql_db=st.sidebar.text_input("MYsql databse")
else:
    db_uri=LOCALDB 

api_key=st.sidebar.text_input(label="Groq", type="password")

if not db_uri:
    st.info("Please neter the db info and uri")

if not api_key:
    st.info("Please enter teh groq api_key")

llm=ChatGroq(groq_api_key)

@st.cache_resource(ttl="2h")
def configure_db(db_uri,mysql_host=None,mysql_user=None, mysql_password=None,mysql_db=None):
    if db_uri==LOCALDB:
        dbfilepath=(Path(__file__).parent/"student.db").absolute()
        creator=lambda : sqlite3.connect(f"file{dbfilepath}!mode=ro",uri=True)
        return SQLDatabase(create_engine("sqlite:///",creator=creator))
    elif db_uri==MYSQL:
        if not(mysql_host and mysql_user and mysql_password and mysql_db):
            st.error()
            st.stop()
        return SQLDatabase(create_engine(f"mysql+mysqlconnector://{mysql_user}"))

if db_uri==MYSQL:
    db=configure_db()

toolkit=SQLDatabaseToolkit(db=db,llm=llm)

agent_executor=create_sql_agent(
    llm,
    toolkit,
    verbose,
    agent_type,
    handle_parsing_errors
)

if messages