# lab-1-ot-security/Dockerfile
FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y git python3
RUN git clone https://github.com/thiagoralves/OpenPLC_v3.git
WORKDIR /OpenPLC_v3
RUN ./install.sh docker
# Port 8080 untuk Web UI, 502 untuk Modbus
EXPOSE 8080 502
CMD ["/usr/bin/python3", "webserver/webserver.py"]