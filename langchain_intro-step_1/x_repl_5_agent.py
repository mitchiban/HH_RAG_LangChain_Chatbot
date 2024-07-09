from langchain_intro.chatbot import hospital_agent_executor
#context_1
hospital_agent_executor.invoke({"input": "What is the current wait time at hospital C?"})

#context_2
hospital_agent_executor.invoke({"input": "What have patients said about their comfort at the hospital?"})