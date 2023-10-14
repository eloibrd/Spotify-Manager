FROM apache/airflow:2.7.2-python3.10

LABEL org.opencontainers.image.source=https://github.com/eloibrd/Spotify-Manager

COPY ./requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
