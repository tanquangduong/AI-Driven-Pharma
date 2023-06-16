"""
@author: Tan Quang Duong
Wel come to Home page
"""
import streamlit as st
from PIL import Image
from transformers import BioGptTokenizer, BioGptForCausalLM


# setting logos in the page
company_logo = Image.open("./figs/AI-driven-Solutions.png")
pharmaGPT_logo = Image.open("./figs/AI-In-Pharma.png")

st.set_page_config(page_title="AI Driven Pharma", page_icon="🚀", layout="centered")
st.sidebar.image(company_logo, use_column_width=True)
st.sidebar.markdown(
    "<h1 style='text-align: center; color: grey;'> Dr. Tan Quang Duong </h1>",
    unsafe_allow_html=True,
)
# st.sidebar.write('**(R) Dr. Quang T. Duong**')

col1, col2, col3, col4, col5 = st.columns(5, gap="large")

with col1:
    st.image(pharmaGPT_logo, width=200)
with col2:
    st.write("")
with col3:
    st.write("")
with col4:
    st.write("")
with col5:
    st.write("")


# Load biogpt tokenizer and model and add them to st.session_state
if "biogpt_tokenizer" not in st.session_state:
    tokenizer = BioGptTokenizer.from_pretrained("microsoft/biogpt")
    st.session_state["biogpt_tokenizer"] = tokenizer

if "biogpt_model" not in st.session_state:
    model = BioGptForCausalLM.from_pretrained("microsoft/biogpt")
    st.session_state["biogpt_model"] = model

st.write("# Welcome to AI In Pharma app! 👋")

# st.sidebar.success("Select a demo above.")

st.markdown(
    """
    # Objective
    This app uses **:green[latest AI-driven solutions]** to **:green[reduce the time needed]** for **:green[edivent generation]**, and **:green[drug approval process]** in pharmaceutical industry. The objectives are multiple:
    - **:green[Text mining and knowledge discovery]** from **biomedical literatures**
    - **:green[Summarizing and tracking]** changing **regulatory documents**, i.e. Food and Drug Administration(**FDA**), European Medicines Agency(**EMA**), etc.
    - **:green[End-to-End relation extraction]** for biomedical entities
    - **:green[Question-Answering]** on biomedical terms
    - **:green[Text generation]** for bimedical documents
    - **:green[Finding insights]** from **real-world evidents**, e.g. **electronic medical records**
    - **:green[Finding trends]** in **drug development**, i.e. **region-specific**, etc
    - **:green[Document classification]** for drug and/or biomedical literatures
    - etc
"""
)
