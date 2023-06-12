FROM python:3.9
WORKDIR /app
COPY . /app
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5005
CMD ["rasa", "run", "-m", "models/20230516-070654-teal-albariño.tar.gz", "--enable-api", "--cors", "*", "--debug"]