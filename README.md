# PharmaGPT
:tada:  Build AI-driven NLP application for pharmaceutical industry


## :white_check_mark: Setup
- Create Python environment\
`conda create -n env_name python=3.10`\
`conda activate env_name`
- Create Python environment\
`pip install -r .\path_to_requirements\requirements.txt`
- Run *.py in Pycharm with Interpreter Option:\
`-m streamlit run`
or on terminal
`streamlit run 0_🏠_Home.py`

## Build and run Docker image
```
# build docker image
docker build . -t ai-pharma-app

# run docker image
docker run -p 8501:8501 -d ai-pharma-app 
```

## Build with docker-compse
```
# Run docker-compose
docker-compse up --build -d

# Stop app
docker-compse down
```