FROM python:3.7.9

# set the working directory in the container
WORKDIR /exercise

# copy the dependencies file to the working directory
COPY ./requirements.txt /exercise/requirements.txt

# install dependencies
RUN pip install -r requirements.txt
COPY . /exercise

ENV SERVER_HOST='0.0.0.0' \
    SERVER_PORT='5000'

CMD [ "python", "main.py" ]


