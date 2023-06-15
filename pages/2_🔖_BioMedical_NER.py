"""
@author: Tan Quang Duong
"""

import streamlit as st
import hydralit_components as hc
from hydralit_components import HyLoader, Loaders
from PIL import Image
from Bio import Entrez
from Bio import Medline
from aipharma.utils import make_ner


# make it look nice from the start
st.set_page_config(page_title="AI in Pharma", page_icon="🚀", layout="wide")
# show Flowqast logo
your_logo = Image.open("./figs/AI-In-Pharma.png")
image = Image.open("./figs/NER-demo-BERN2.png")

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
    {"id": "tab2", "icon": "🔖", "label": "BioMedical NER"},
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


with HyLoader("", loader_name=Loaders.pulse_bars):
    if menu_id == "tab1":
        st.markdown(
            """
            ## BioMedical NER (Name Entity Recognition)
            """
        )
        st.image(image, caption="NER illustration for biomedical literature")
        st.markdown(
            """
            ## Models and Implementations
            - [**BERN2**](http://bern2.korea.ac.kr) API by DMIS lab of Korea University for **Name Entity Recognition**(**NER**) based on the answer of BioGPT
            - [**NCBI**](https://www.ncbi.nlm.nih.gov) (National Center for Biotechnology Information) API for query biomedical liturature 
            - [**NCBI API implementation**](https://github.com/cakmakaf/fetch_PubMed_abstracts_by_keyword) using 'bio' library
            ## Datasets
            - [**NCBI**](https://www.ncbi.nlm.nih.gov): Access to biomedical and genomic information
                - [**PubMed**](https://pubmed.ncbi.nlm.nih.gov/): a vast collection of biomedical literature. It is a free resource maintained by 
                the United States National Library of Medicine (NLM) and the National Institutes of Health (NIH). 
                PubMed primarily focuses on scientific research articles in the fields of medicine, healthcare, life sciences, and related disciplines.
                    - **[PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/)**: Free full-text articles
                    - **[PubMed Health](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3133896/)**: Evidence-based information for consumers and clinicians
                    - **[PubMedQA](https://pubmedqa.github.io/)**: A dataset for Biomedical Research Question Answering. It has 1k expert labeled, 61.2k unlabeled and 211.3k artificially generated QA instances.
                - [**MeSH**](https://www.ncbi.nlm.nih.gov/mesh/): The NLM controlled vocabulary thesaurus used for indexing articles for PubMed.
                - [**Gene**](https://www.ncbi.nlm.nih.gov/gene/): Gene integrates information from a wide range of species. A record may include nomenclature, Reference Sequences (RefSeqs), maps, pathways, variations, phenotypes, and links to genome-, phenotype-, and locus-specific resources worldwide.
                - etc
            """
        )
    elif menu_id == "tab2":
        input_mode = st.radio(
            "**NER from BioMedical literature or abstracts**",
            ("Add Text", "Query from NCBI"),
            horizontal=True,
        )
        # ner for manually add text
        if input_mode == "Add Text":
            text_input = st.text_area("Type your text here:", height=200)
            if text_input:
                make_ner(text_input)

        # ner for querry from
        elif input_mode == "Query from NCBI":
            # Store the initial value of widgets in session state
            if "visibility" not in st.session_state:
                st.session_state.visibility = "visible"
                st.session_state.disabled = False

            # get bio_term from user input
            bio_term = st.text_input(
                "**Enter biomedical term / topic** 👇",
                label_visibility=st.session_state.visibility,
                disabled=st.session_state.disabled,
                placeholder="Add your terms here.",
            )

            # show db results based on bio_term
            if bio_term:
                Entrez.email = "tquangbk@gmail.com"  # Always tell NCBI who you are
                handle = Entrez.egquery(term=bio_term)
                record = Entrez.read(handle)
                db_result = []
                for row in record["eGQueryResult"]:
                    db_result.append((row["DbName"], row["Count"]))
                db_term = st.selectbox("**Select database for your term**", db_result)

                # show id lists of articles from db_term
                NUM_ARTICLE = 10
                db_name = db_term[0]
                db_count = db_term[1]
                handle = Entrez.esearch(db=db_name, term=bio_term, retmax=NUM_ARTICLE)
                record = Entrez.read(handle)
                handle.close()
                idlist = record["IdList"]

                handle = Entrez.efetch(
                    db=db_name, id=idlist, rettype="medline", retmode="text"
                )
                records = Medline.parse(handle)
                records = list(records)

                # get article_list
                article_list = []
                for idx, record in enumerate(records):
                    article_list.append(
                        (idlist[idx], record.get("DP", "?"), record.get("TI", "?"))
                    )

                # select articles
                selected_article = st.selectbox("**Select article**", article_list)
                idx_chosen = idlist.index(selected_article[0])
                st.markdown(
                    "**Title**: **:green[{}]**".format(
                        records[idx_chosen].get("TI", "?")
                    )
                )
                st.markdown(
                    "**Author**: **:green[{}]**".format(
                        records[idx_chosen].get("AU", "?")
                    )
                )
                st.markdown(
                    "**Publication Date**: **:green[{}]**".format(
                        records[idx_chosen].get("DP", "?")
                    )
                )
                st.markdown(
                    "**Keywords**: **:green[{}]**".format(
                        records[idx_chosen].get("OT", "?")
                    )
                )
                st.markdown("**Abstract**:")
                abstract = records[idx_chosen].get("AB", "?")
                st.write(abstract)

                make_ner(abstract)
