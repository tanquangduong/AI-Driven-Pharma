import os
import requests
import streamlit as st
from text_highlighter import text_highlighter
import PyPDF2
import openai
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")

# Set your OpenAI API key
openai.api_key = os.environ.get("OPENAI_KEY", "")


def query_plain(text, url="http://bern2.korea.ac.kr/plain"):
    out = requests.post(url, json={"text": text.replace(";", ",")})
    return out.json()


def read_pdf(pdf_path):
    # creating a pdf file object
    pdfFileObj = open(pdf_path, "rb")

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # printing number of pages in pdf file
    pages_num = len(pdfReader.pages)

    # Extract the text content from the PDF file
    text_content = []
    for page in pdfReader.pages:
        text = ""
        text += page.extract_text()
        text_content.append(text)

    # closing the pdf file object
    pdfFileObj.close()

    return pages_num, text_content


def summarize_text(text_content):
    # Reduce the length of text_content
    shortened_text = text_content[:4000]  # Adjust the desired length

    # Make the API call with the shortened text
    # print("Making API call with text:", shortened_text)  # Print the shortened text
    response = openai.Completion.create(
        engine="text-davinci-003", prompt=shortened_text, max_tokens=500
    )

    # Extract the generated summary from the response
    summary = response.choices[0].text.strip()

    # print("Generated summary:", summary)  # Print the generated summary
    return summary


color_list = [
    ("gene", "#DFFF00"),
    ("disease", "#FFBF00"),
    ("chemical", "#FF7F50"),
    ("species", "#DE3163"),
    ("mutation", "#9FE2BF"),
    ("cell_line", "#40E0D0"),
    ("cell_type", "#6495ED"),
    ("DNA", "#CCCCFF"),
    ("RNA", "#BFC9CA"),
    ("drug", "#F08080"),
]


def make_ner(input_text):
    ner_output = query_plain(input_text)
    # ner_dict = {'mention': [],
    #             'label': [],
    #             'prob': []
    #             }
    # for idx, ner in enumerate(ner_output['annotations']):
    #     ner_dict['mention'].append(ner['mention'])
    #     ner_dict['label'].append(ner['obj'])
    #     ner_dict['prob'].append(ner['prob'])
    # df_ner = pd.DataFrame(ner_dict)
    # df_ner = df_ner.sort_values('label')

    annotation_ner = []
    for idx, ner in enumerate(ner_output["annotations"]):
        d = {
            "start": ner["span"]["begin"],
            "end": ner["span"]["end"],
            "tag": ner["obj"],
        }
        annotation_ner.append(d)

    st.write("**NER**: 👇")
    result = text_highlighter(
        text=input_text,
        labels=color_list,
        # Optionally you can specify pre-existing annotations:
        annotations=annotation_ner,
    )
