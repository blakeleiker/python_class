FROM centos7.6.1810
MAINTAINER Mike Moore <michael.moore@nasa.gov>

RUN yum install https://centos7.iuscommunity.org/ius-release.rpm

RUN yum install python36u python36u-devel python36u-pip

RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install virtualenv

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
