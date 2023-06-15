"""
@author: Tan Quang Duong
"""


import os
from pathlib import Path
import numpy as np
import streamlit as st
import hydralit_components as hc
from hydralit_components import HyLoader, Loaders
from PIL import Image
from aipharma.utils import read_pdf, summarize_text

# make it look nice from the start
st.set_page_config(page_title="AI in Pharma", page_icon="🚀", layout="wide")
# show Flowqast logo
your_logo = Image.open("./figs/AI-In-Pharma.png")
image = Image.open("./figs/doc_summary.png")

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
    {"id": "tab2", "icon": "✅", "label": "Document Summary"},
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
            ## Document summary
            """
        )
        st.image(image, caption="Illustration for document summary", width=400)
        st.markdown(
            """
            ## Models and Implementations
            - Model GPT 3.5
            - Implementation using 'openai' library and OpenAI key
            - Limitation of around 4000 token for summarization task
            ## Use-case
            - Regulation document summary
            - Biomedical document summary
            """
        )
    elif menu_id == "tab2":
        # Get dataset (*.csv) path from selection box
        datasource_path = "./datasets/"
        list_file = ["-"] + os.listdir(datasource_path)
        dataset_file = st.selectbox("**Select document**", list_file)
        if dataset_file != "-":
            st.session_state["dataset"] = dataset_file
        if "dataset" in st.session_state:
            dataset_path = os.path.join(datasource_path, st.session_state["dataset"])
            num_pages, text_content = read_pdf(dataset_path)

            # Get & show dataset name
            dataset_name = Path(dataset_path).stem
            st.markdown("**Pdf file name**: **:green[{}]**".format(dataset_name))

            # Get & show dataset extension
            dataset_extension = Path(dataset_path).suffix
            st.markdown(
                "**Dataset Extension**: **:green[{}]**".format(dataset_extension)
            )

            if dataset_path is not None:
                st.markdown("**Page number**: **:green[{}]**".format(num_pages))
                page_list = np.arange(0, num_pages, 1) + 1

                page_number = st.selectbox(
                    "**Which page do you want to summary?**", page_list
                )
                st.write("**The text in the page** **:green[{}]**:".format(page_number))
                st.write(text_content[page_number - 1])
                content_text = text_content[page_number - 1]

                # Save content text of chosen page to st session_state
                st.session_state["content_text"] = content_text

            if "content_text" in st.session_state:
                content_text = st.session_state["content_text"]
                if st.button("**Summary**"):
                    summary = summarize_text(content_text)
                    st.write(summary)
