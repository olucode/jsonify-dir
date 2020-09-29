FROM python:3.8

# Add requirements.txt before rest of repo for caching
ADD requirements.txt /app/
WORKDIR /app
RUN pip3 install -r requirements.txt

ADD . /app

EXPOSE 8080 5555

CMD ["bash", "run.sh"]
