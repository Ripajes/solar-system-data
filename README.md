# solar-system-data
Downloads solar system planets data from https://api.le-systeme-solaire.net/ api and saves it in data folder.
### Run it with python3:
- Install requirements.txt
- Run it:
    <code>python ingest_data.py</code>
### Run it with docker:
- Build the image:
    <code>docker build -t solar_system_ingest . </code>
- Run the container:
    <code>docker run -it -v ${PWD}/data:/app/data solar_system_ingest</code>
