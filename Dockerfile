FROM python:3.9-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./api.py /code/api.py
COPY ./Clr /code/Clr

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

EXPOSE 7860

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"] 