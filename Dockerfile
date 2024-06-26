FROM python:3.10.12

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get install curl

WORKDIR /.

COPY ./requirements.txt ./requirements.txt
RUN  pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "main"]