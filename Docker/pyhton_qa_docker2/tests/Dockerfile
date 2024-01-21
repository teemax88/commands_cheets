FROM python:3.6

WORKDIR /app

# copy all the files to the container
COPY . .

# install dependencies
RUN pip install -U pip
RUN pip install -r requirements.txt

# command
CMD ["pytest"]
