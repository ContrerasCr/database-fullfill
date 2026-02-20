FROM python:3.13-slim

#ARG DB_URI

SHELL ["/bin/bash", "-c"]

RUN apt-get update 

WORKDIR /app

COPY . .

RUN  pip install -r requeriments.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]