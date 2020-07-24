FROM python:3.8.3-alpine3.12

COPY ./requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV APP_HOME /LayaHand

RUN mkdir $APP_HOME

WORKDIR $APP_HOME

COPY . $APP_HOME

CMD ["python", "main.py"]