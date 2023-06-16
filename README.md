# AI driven Pharma
:tada:  Build AI-driven NLP application for pharmaceutical industry

# Objective
This app uses **latest AI-driven solutions** to **reduce the time needed** for **edivent generation**, and **drug approval process** in pharmaceutical industry. The objectives are multiple:
- **Text mining and knowledge discovery** from **biomedical literatures**
- **Summarizing and tracking** changing **regulatory documents**, i.e. Food and Drug Administration(**FDA**), European Medicines Agency(**EMA**), etc.
- **End-to-End relation extraction** for biomedical entities
- **Question-Answering** on biomedical terms
- **Text generation** for bimedical documents
- **Finding insights** from **real-world evidents**, e.g. **electronic medical records**
- **Finding trends** in **drug development**, i.e. **region-specific**, etc
- **Document classification** for drug and/or biomedical literatures
- etc

## :white_check_mark: Setup
- Create Python environment\
`conda create -n env_name python=3.10`\
`conda activate env_name`
- Install required packages for production\
`pip install -r .\path_to_requirements\requirements.txt`
- Install required packages for developement\
`pip install -r .\path_to_requirements\requirements-dev.txt`
- Create **your own OPENAI KEY** and add to **.env.local** for text summary feature
- Run app on terminal. **Note** that The first time you run the app, it will take a few minutes to load the model.
`streamlit run 0_🏠_Home.py`


## :white_check_mark: Build and run Docker image
```
# build docker image
docker build . -t ai-pharma-app

# run docker image
docker run -p 8501:8501 -d ai-pharma-app 
```

## :white_check_mark: Build with docker-compse
```
# Run docker-compose
docker-compse up --build -d

# Stop app
docker-compse down
```

## :white_check_mark: Models and Implementations
- [**BioGPT**](https://github.com/microsoft/BioGPT) of **Microsoft Research** for biomedical text generation Q/A
- [**BioGPT implementation**](https://huggingface.co/microsoft/biogpt) by **Transformers** library of **Hugging Face**
- [**BERN2**](http://bern2.korea.ac.kr) **API** by ***DMIS lab** of Korea University for **Name Entity Recognition**(**NER**) based on the answer of BioGPT
- [**NCBI**](https://www.ncbi.nlm.nih.gov) (National Center for Biotechnology Information) API for query biomedical liturature 
- [**NCBI API implementation**](https://github.com/cakmakaf/fetch_PubMed_abstracts_by_keyword) using 'bio' library
- OpenAI API 
  - Model GPT 3.5
  - Limitation of around 4000 token for summarization task
            
## :white_check_mark: Datasets
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
- [**NCBI**](https://www.ncbi.nlm.nih.gov): Access to biomedical and genomic information
  - [**MeSH**](https://www.ncbi.nlm.nih.gov/mesh/): The NLM controlled vocabulary thesaurus used for indexing articles for PubMed.
  - [**Gene**](https://www.ncbi.nlm.nih.gov/gene/): Gene integrates information from a wide range of species. A record may include nomenclature, Reference Sequences (RefSeqs), maps, pathways, variations, phenotypes, and links to genome-, phenotype-, and locus-specific resources worldwide.
  - etc
