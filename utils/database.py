from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from config import DATABASE_URI, OPENAI_API_KEY

db = SQLDatabase.from_uri(DATABASE_URI)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=OPENAI_API_KEY)

def create_sql_agent():
    return create_sql_agent(llm=llm, db=db, agent_type="openai-tools", verbose=True)

agent_executor = create_sql_agent()
