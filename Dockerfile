#Dockerfile, Image,  Container
FROM python:3.7.13

WORKDIR /usr/src/app

ENV PATH="/usr/src/app:${PATH}"

COPY ./static ./static

COPY ./templates ./templates

COPY requirements.txt .

COPY server.py .

COPY config.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
