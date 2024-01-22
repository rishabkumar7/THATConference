import streamlit as st
import main as pets_name
import os

#Load .env file
from dotenv import load_dotenv
load_dotenv()

st.title("🐶 Pets Name Generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Dog", "Cat", "Hamster", "Rat", "Snake", "Lizard", "Cow"))

animal_labels = {
    "Dog": "What color is your dog?",
    "Cat": "What color is your cat?",
    "Hamster": "What color is your hamster?",
    "Rat": "What color is your rat?",
    "Snake": "What color is your snake?",
    "Lizard": "What color is your lizard?",
    "Cow": "What color is your cow?",
}

pet_color = st.sidebar.text_area(
    label=animal_labels[animal_type],
    max_chars=25
)

if pet_color:
    response = pets_name.generate_pet_name(animal_type, pet_color, os.getenv("OPENAI_API_KEY"))
    st.text(response['text'])