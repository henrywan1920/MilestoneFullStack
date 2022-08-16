#Dockerfile, Image,  Container
From ultralytics/yolov5:latest

WORKDIR /usr/src/app

ENV PATH="/usr/src/app:${PATH}"

COPY ./static ./static

COPY ./templates ./templates

COPY ./resources ./resources

COPY ./models ./models

COPY requirements.txt .

COPY app.py .

COPY config.py .

COPY prediction.py .

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
