FROM python:3

RUN pip install flask
COPY app.py .

ARG myBuildArgs
RUN echo ${myBuildArgs}

RUN echo ${myJsonEnv}

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["app.py"]
