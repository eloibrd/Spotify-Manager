poetry export --without-hashes --format=requirements.txt > requirements.txt

docker build -t ghcr.io/eloibrd/spotify-manager-airflow:latest -f docker/airflow.Dockerfile .

docker push ghcr.io/eloibrd/spotify-manager-airflow:latest

rm requirements.txt
