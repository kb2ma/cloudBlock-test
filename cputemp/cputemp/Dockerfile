FROM balenalib/genericx86-64-ext-alpine-python:3.8-build as build  

RUN mkdir /install
WORKDIR /install

COPY requirements.txt /requirements.txt
ENV PATH=/root/.local/bin:$PATH
RUN pip3 install --user -r /requirements.txt

FROM balenalib/genericx86-64-ext-alpine-python:3.8-run 
COPY --from=build /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

WORKDIR /usr/src/app
COPY . ./

RUN install_packages nano

CMD ["python", "-u", "main.py"]

