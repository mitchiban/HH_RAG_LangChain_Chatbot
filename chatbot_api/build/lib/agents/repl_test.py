#To try it out, you’ll have to navigate into the chatbot_api/src/ folder and start a new REPL session from there.
#


import dotenv
dotenv.load_dotenv()

from agents.hospital_rag_agent import hospital_rag_agent_executor

response = hospital_rag_agent_executor.invoke({"input": "What is the wait time at Wallace-Hamilton?"})