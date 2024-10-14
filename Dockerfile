FROM python:3.10.12-slim

RUN mkdir -p /app

COPY . main.py /app/

WORKDIR /app

RUN python -m nltk.downloader punkt punkt_tab
RUN python -m textblob.download_corpora
RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "main.py" ]

ENTRYPOINT [ "python" ]
