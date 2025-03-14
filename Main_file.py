from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
import streamlit as st

import prompt_mod
import vector_mod

load_dotenv()

def create_streamlit_app():
    st.title("🤖 Product Recommender")
    search_req = st.text_input("""Enter the valid product: below are the example queries
     Examples :
          - "Find the best wireless headphones under $100.
          - "Suggest a reliable smartphone with a great camera."
          - "Where can I buy a budget-friendly ergonomic office chair?"
    - """)
    submit_button = st.button("Submit")

    if submit_button:
        try:
            llm = ChatGroq(
                model="mixtral-8x7b-32768",
                temperature=0.4,
                groq_api_key=os.getenv("GROQ_API_KEY")
            )

            context = vector_mod.vector_func(search_req)
            prompt = prompt_mod.prompt_return()

            chain = prompt | llm

            res = chain.invoke({"context": context, "user_query": search_req})
            st.code(res.content, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Product Recommender", page_icon="🤖")
    create_streamlit_app()



