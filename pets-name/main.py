#Imports
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

#Load .env file
from dotenv import load_dotenv
load_dotenv()

# Generate Pet Name Function
def generate_pet_name(animal_type, pet_color):
  llm = OpenAI(temperature=0.7)

  
  prompt_template = PromptTemplate(
    input_variables=["animal_type", "pet_color"],
    template =  "I have {animal_type} pet and I want a cool name for it, it is {pet_color} color. Suggest me five cool names for my pet"
  )

  name_chain = prompt_template | llm

  response = name_chain.invoke({"animal_type":animal_type, "pet_color":pet_color})

  return response

if __name__ == "__main__":
  print(generate_pet_name("Cat", "White"))