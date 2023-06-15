"""
@author: Tan Quang Duong
"""

import streamlit as st
import hydralit_components as hc
from hydralit_components import HyLoader, Loaders
from PIL import Image
import torch
from transformers import set_seed
from aipharma.utils import make_ner


# make it look nice from the start
st.set_page_config(page_title="AI in Pharma", page_icon="🚀", layout="wide")
your_logo = Image.open("./figs/AI-In-Pharma.png")
image_promt_1 = Image.open("./figs/biogpt_prompt_1.png")
image_promt_2 = Image.open("./figs/biogpt_prompt_2.png")

col1, col2, col3, col4, col5 = st.columns(5, gap="large")

with col1:
    st.write("")
with col2:
    st.write("")
with col3:
    st.write("")
with col4:
    st.write("")
with col5:
    st.image(your_logo, width=150)

# specify the primary menu definition
menu_data = [
    {"id": "tab1", "icon": "📚", "label": "About"},
    {"id": "tab2", "icon": "💬", "label": "BioMedical Q/A"},
]

over_theme = {
    "menu_background": "#7BB657",
    "txc_active": "#000000",
    "txc_inactive": "#FFFFFF",
}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    # home_name='Home',
    # login_name='Logout',
    hide_streamlit_markers=False,  # will show the st hamburger as well as the navbar now!
    sticky_nav=True,  # at the top or not
    sticky_mode="pinned",  # jumpy or not-jumpy, but sticky or pinned
)
if "biogpt_tokenizer" in st.session_state:
    tokenizer = st.session_state["biogpt_tokenizer"]
if "biogpt_model" in st.session_state:
    model = st.session_state["biogpt_model"]

with HyLoader("", loader_name=Loaders.pulse_bars):
    if menu_id == "tab1":
        st.markdown(
            """
            ## BioGPT prompt for BioMedical Q/A
            """
        )
        st.image(image_promt_1, caption="Example 1 of BioGPT prompt")
        st.image(image_promt_2, caption="Example 2 of BioGPT prompt")
        st.markdown(
            """
            ## Models and Implementations
            - [**BioGPT**](https://github.com/microsoft/BioGPT) of **Microsoft Research** for biomedical text generation Q/A
            - [**BioGPT implementation**](https://huggingface.co/microsoft/biogpt) by **Transformers** library of **Hugging Face**
            - [**BERN2**](http://bern2.korea.ac.kr) **API** by ***DMIS lab** of Korea University for **Name Entity Recognition**(**NER**) based on the answer of BioGPT
            ## Datasets
            - **[BC5CDR](https://huggingface.co/datasets/tner/bc5cdr)**: dataset for chemical-disease-relation extraction task which consists of 500/500/500 documents as the training/validation/testset
            - **[KD-DTI](https://tdcommons.ai/multi_pred_tasks/dti/)**: dataset for drug-target-interaction,consisting of 12k/1k/1.3k documents as the train/validation/test set
            - **[DDI](https://github.com/isegura/DDICorpus)** dataset for drug-drug-interaction task,consisting of 792 texts selected from the Drug Bank database and other 233 Medline abstracts.
            - [**PubMed**](https://pubmed.ncbi.nlm.nih.gov/): a vast collection of biomedical literature. It is a free resource maintained by 
            the United States National Library of Medicine (NLM) and the National Institutes of Health (NIH). 
            PubMed primarily focuses on scientific research articles in the fields of medicine, healthcare, life sciences, and related disciplines.
                - **[PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/)**: Free full-text articles
                - **[PubMed Health](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3133896/)**: Evidence-based information for consumers and clinicians
                - **[PubMedQA](https://pubmedqa.github.io/)**: A dataset for Biomedical Research Question Answering. It has 1k expert labeled, 61.2k unlabeled and 211.3k artificially generated QA instances.
            - **[HoC](https://github.com/sb895/Hallmarks-of-Cancer/tree/master)**: It consists of 1852 PubMed publication abstracts manually annotated by experts according to a taxonomy. The taxonomy consists of 37 classes in a hierarchy.

            """
        )
    elif menu_id == "tab2":
        # Store the initial value of widgets in session state
        if "visibility" not in st.session_state:
            st.session_state.visibility = "visible"
            st.session_state.disabled = False

        text_input = st.text_input(
            "**Enter your question** 👇",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder="Ask me anything about biomedical",
        )
        if text_input:
            inputs = tokenizer(text_input, return_tensors="pt")
            set_seed(42)
            with torch.no_grad():
                beam_output = model.generate(
                    **inputs,
                    min_length=100,
                    max_length=1024,
                    num_beams=5,
                    early_stopping=True,
                )
            output = tokenizer.decode(beam_output[0], skip_special_tokens=True)
            st.write("**Anwser:**")
            st.write(output)

            if st.button("**NER**"):
                make_ner(output)
