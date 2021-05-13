FROM balenalib/genericx86-64-ext-python:3.8-stretch-build

RUN install_packages nano

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . ./
CMD ["python", "-u", "main.py"]
