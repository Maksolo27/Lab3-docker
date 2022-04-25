FROM python:3.9

WORKDIR /pythonApp

COPY requirements/requirements.txt requirements/
COPY requirements/backend.in requirements/
COPY build/index.html build/

RUN pip install -r requirements/backend.in
RUN pip install -r requirements/requirements.txt

COPY . .

CMD [ "uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080" ]