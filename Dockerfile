FROM python:3.10

WORKDIR /app

EXPOSE 8501

COPY ./requirements/requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

CMD ["streamlit", "run", "0_🏠_Home.py"]