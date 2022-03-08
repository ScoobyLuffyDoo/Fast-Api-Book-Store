# DockerFile, Image, Container

FROM python:3.10.2

COPY ./resources



ADD index.py .

RUN pip install fastapi 
RUN pip install pydantic
RUN pip install resources
RUN pip install requests
RUN pip install staty

CMD [ "python","./index.py" ]