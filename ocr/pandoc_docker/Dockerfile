FROM ubuntu:latest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y pandoc
RUN apt-get install -y texlive-latex-base
RUN apt-get install -y texlive-fonts-recommended
RUN apt-get install -y texlive-fonts-extra
RUN apt-get install -y texlive-latex-extra
RUN apt-get install -y texlive-xetex

WORKDIR /data

ENTRYPOINT ["/bin/bash"]
