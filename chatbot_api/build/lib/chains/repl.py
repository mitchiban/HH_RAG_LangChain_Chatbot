import dotenv
dotenv.load_dotenv()

from chatbot_api.src.chains.hospital_review_chain import (reviews_vector_chain)

query = """What have patients said about hospital efficiency?
            Mention details from specific reviews."""

response = reviews_vector_chain.invoke(query)

response.get("result")



# 2nd part
import dotenv
dotenv.load_dotenv()
from chatbot_api.src.chains.hospital_cypher_chain import (hospital_cypher_chain)
question = """What is the average visit duration for emergency visits in North Carolina?"""
response = hospital_cypher_chain.invoke(question)



question = """Which state had the largest percent increase in Medicaid visits from 2022 to 2023?"""
response = hospital_cypher_chain.invoke(question)

question = """Where did Scotto park his car?"""
response = hospital_cypher_chain.invoke(question)

question = """Does Alice like peas?"""
response = hospital_cypher_chain.invoke(question)

question = """Does Alice dislike peas?"""
response = hospital_cypher_chain.invoke(question)