FROM apache/airflow:2.7.1-python3.10

LABEL org.opencontainers.image.source=https://github.com/eloibrd/Spotify-Manager

COPY ./requirements.txt ./requirements.txt

USER airflow

RUN pip install --no-cache-dir -r ./requirements.txt
