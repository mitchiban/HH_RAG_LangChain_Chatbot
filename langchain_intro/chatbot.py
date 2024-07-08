import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)


#demo - launch via ipython in repl
from langchain.schema.messages import HumanMessage, SystemMessage
from langchain_intro.chatbot import chat_model

messages = [
    SystemMessage(content="""You're an assistant knowledgeable about healthcare. Only answer healthcare-related questions. 
                  But do so in poem verse, start with roses are red, violets are blue"""),
    HumanMessage(content="What is Medicaid managed care?"), ]

chat_model.invoke(messages)

messages_1 = [
    SystemMessage(content="""You're an assistant knowledgeable about healthcare. Only answer healthcare-related questions."""),
    HumanMessage(content="How do I change a tire?"), ]

chat_model.invoke(messages_1)
