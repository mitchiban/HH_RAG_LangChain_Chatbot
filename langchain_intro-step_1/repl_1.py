import dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)


#Chat model demo - launch via ipython in repl
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

chat_model.invoke("What is blood pressure?")


#Prompt Template demo - launch via ipython in repl
## A
from langchain.prompts import ChatPromptTemplate
review_template_str = """Your job is to use patient
... reviews to answer questions about their experience at a hospital.
... Use the following context to answer questions. Be as detailed
... as possible, but don't make up any information that's not
... from the context. If you don't know an answer, say you don't know.
...
... {context}
...
... {question}
... """
review_template = ChatPromptTemplate.from_template(review_template_str)
context = "I had a great stay!"
question = "Did anyone have a positive experience?"
review_template.format(context=context, question=question)

"""
Response
"Human: Your job is to use patient\nreviews to answer questions about
 their experience at a hospital.\nUse the following context to
 answer questions. Be as detailed\nas possible, but don't make
 up any information that's not\nfrom the context. If you don't
 know an answer, say you don't know.\n\nI had a great
 stay!\n\nDid anyone have a positive experience?\n"
 """


## B
from langchain.prompts import (
...     PromptTemplate,
...     SystemMessagePromptTemplate,
...     HumanMessagePromptTemplate,
...     ChatPromptTemplate,
... )

review_system_template_str = """Your job is to use patient
... reviews to answer questions about their experience at a
... hospital. Use the following context to answer questions.
... Be as detailed as possible, but don't make up any information
... that's not from the context. If you don't know an answer, say
... you don't know.
...
... {context}
... """

review_system_prompt = SystemMessagePromptTemplate(
...     prompt=PromptTemplate(
...         input_variables=["context"], template=review_system_template_str
...     )
... )

review_human_prompt = HumanMessagePromptTemplate(
...     prompt=PromptTemplate(
...         input_variables=["question"], template="{question}"
...     )
... )

messages = [review_system_prompt, review_human_prompt]
review_prompt_template = ChatPromptTemplate(
...     input_variables=["context", "question"],
...     messages=messages,
... )
context = "I had a great stay!"
question = "Did anyone have a positive experience?"

review_prompt_template.format_messages(context=context, question=question)

"""
[SystemMessage(content="Your job is to use patient\nreviews to answer
 questions about their experience at a\nhospital. Use the following context
 to answer questions.\nBe as detailed as possible, but don't make up any
 information\nthat's not from the context. If you don't know an answer, say
 \nyou don't know.\n\nI had a great stay!\n"), HumanMessage(content='Did anyone
 have a positive experience?')]
"""