FROM python:3.9 as base

ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y aptitude
RUN aptitude install -y gdal-bin libgdal-dev
RUN pip install pipenv



FROM base as dependencies

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --dev



FROM dependencies as runtime

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

RUN mkdir code
WORKDIR /home/appuser/code
COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]