FROM python:3

RUN pip install flask
COPY app.py .

EXPOSE 8000

ENTRYPOINT ["python"]
CMD ["app.py"]