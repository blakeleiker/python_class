FROM centos:7.6.1810
MAINTAINER Mike Moore <michael.moore@nasa.gov>

RUN yum install -y epel-release

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm

RUN yum install -y python36u python36u-devel python36u-pip

RUN python3.6 -m pip install --upgrade pip

RUN python3.6 -m pip install virtualenv

COPY requirements.txt requirements.txt

RUN virtualenv -p python3.6 /py_env

RUN source /py_env/bin/activate

RUN pip install -r requirements.txt
