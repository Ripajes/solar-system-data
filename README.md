# solar-system-data
Solar system data with https://api.le-systeme-solaire.net/ api
Run with python:
    - Install requirements.txt
    - run it:
        python ingest_data.py
Run with docker:
- Build the image:
    docker build -t solar_system_ingest .
- Run the image
    docker run -it -v ${PWD}/data:/app/data solar_system_ingest
