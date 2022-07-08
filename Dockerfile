FROM python:3.9-slim

ENV HOME /usr/src/
WORKDIR $HOME

COPY requirements.txt \
        core \
        $HOME

RUN pip install --upgrade pip && pip install -r requirements.txt

# run and print the output
RUN python -m core.main

RUN python -m core.main --input_file input.txt --output_name output --out txt
