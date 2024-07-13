from langchain_intro.chatbot import review_chain

question = """Has anyone complained about
...            communication with the hospital staff?"""

review_chain.invoke(question)