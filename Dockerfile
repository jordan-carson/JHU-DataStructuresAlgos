FROM python:3.9-slim

ENV HOME /usr/src/
WORKDIR $HOME

COPY requirements.txt \
        core \
        $HOME

RUN pip install --upgrade pip && pip install -r requirements.txt

# run and output program results from filename input parameter.
RUN python -m core.main --filename input.txt
