# PharmaGPT
:tada:  Build AI-driven NLP application for pharmaceutical industry


## :white_check_mark: Setup
- Create Python environment\
`conda create -n env_name python=3.10`\
`conda activate env_name`
- Install required packages for production\
`pip install -r .\path_to_requirements\requirements.txt`
- Install required packages for developement\
`pip install -r .\path_to_requirements\requirements-dev.txt`
- Create your own OPENAI KEY and add to .env.local
- Run app on terminal
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