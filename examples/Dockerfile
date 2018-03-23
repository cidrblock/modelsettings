FROM python:3.6.4-alpine

RUN apk add -U \
	ca-certificates \
 && rm -rf /var/cache/apk/* \
 && pip install --no-cache-dir --upgrade pip

WORKDIR /usr/src/app/
ADD model_settings.yml .
ADD app.py .
ADD requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]
