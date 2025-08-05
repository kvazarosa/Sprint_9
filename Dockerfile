FROM python:3.9
WORKDIR /app/environments/.github/Sprint_9
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["pytest", "--alluredir", "allure-results"]
