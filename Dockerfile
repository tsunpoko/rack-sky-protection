# base-image for python3

# see more about dockerfile templates here https://www.balena.io/docs/reference/base-images/base-images-ref/
FROM balenalib/raspberrypi3-python:3
# package install

RUN apt-get update
RUN apt-get install ffmpeg motion git wget vim

RUN git clone https://github.com/tsunpoko/rack-sky-protection.git
WORKDIR ./rack-sky-protection

RUN pip3 install tweepy

chmod +x run.sh

CMD ["./run.sh"]
