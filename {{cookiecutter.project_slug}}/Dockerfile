FROM python:3.11.4-alpine

WORKDIR /app/

COPY . /app

RUN pip install --upgrade pip
# Install dependencies
RUN pip install -r requirements.txt

# Other configurations