FROM python:3

RUN pip install flask
COPY app.py .

EXPOSE 80

ENTRYPOINT ["python"]
CMD ["app.py"]