FROM python:3.11-alpine

RUN adduser --system www-data
RUN mkdir -p /srv/app
RUN mkdir -p /srv/uploads
RUN chown www-data:www-data /srv/uploads

WORKDIR /srv/app

USER www-data

RUN python3 -m pip install --disable-pip-version-check --no-cache-dir -r requirements.txt

EXPOSE 8066

CMD ["python3", "app.py"] 