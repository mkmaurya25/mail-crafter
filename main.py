import streamlit as st
from chains import Chain
from portfolio import Portfolio
from utils import clean_text
from langchain_community.document_loaders import WebBaseLoader

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

def create_streamlit_app():
    st.title("📧 Cold Mail Crafter")
    # Input for API key (hidden with password field)
    api_key = st.sidebar.text_input("Enter your GROQ API Key", 
                                    type="password", placeholder="your api key")
    # st.sidebar.button("Submit")
    # If API key is not provided, show a warning message
    if not api_key:
        st.sidebar.warning("Please enter your GROQ API Key to proceed.")
    else:
        st.sidebar.success("API Key entered successfully!")
    # api_key = st.text_input("Enter your Groq API key:", type="password")
    # url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-33460")
    url_input = st.text_input("Enter a URL:", placeholder="Type or paste your URL here")
    submit_button = st.button("Submit")

    if submit_button and api_key:
        try:
            chain = Chain(api_key)
            portfolio = Portfolio()
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = chain.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = chain.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")
    elif not api_key:
        st.error("Please enter your API key")

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app()
