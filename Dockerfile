FROM python:3.10.12-slim

RUN mkdir -p /app

COPY . main.py /app/

WORKDIR /app

RUN pip install --no-cache-dir nltk && \
    python -m nltk.downloader punkt punkt_tab
RUN pip install -r requirements.txt
RUN pip install httpx
RUN python -m textblob.download_corpora

EXPOSE 8000

CMD [ "main.py" ]

ENTRYPOINT [ "python" ]
