FROM python:3.9
WORKDIR /app
COPY . /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5055
CMD ["rasa", "run", "actions"]