#Imports
import streamlit as st
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

#Load .env file
from dotenv import load_dotenv
load_dotenv()

# Generate Pet Name Function
def generate_pet_name(animal_type, pet_color, openai_api_key):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

  template = """
  I have {animal_type} pet and I want a cool name for it, it is {pet_color} color. Suggest me five cool names for my pet
  Answer: Here are five names for your pet:
  """

  prompt_template= PromptTemplate(template=template, input_variables=["animal_type", "pet_color"])
  #prompt_template = PromptTemplate.from_template("I have {animal_type} pet and I want a cool name for it, it is {pet_color} color. Suggest me five cool names for my pet"
  #)

  #name_chain = prompt_template | llm
  name_chain = LLMChain(llm=llm, prompt=prompt_template)

  response = name_chain.invoke({"animal_type":animal_type, "pet_color":pet_color})

  return response

if __name__ == "__main__":
  print(generate_pet_name("Cat", "White", os.getenv("OPENAI_API_KEY")))