FROM python:2.7

RUN apt-get update
RUN apt-get install -y openssh-server

RUN pip install argh

RUN mkdir /var/run/sshd

# http://askubuntu.com/a/94067
RUN adduser --home /home/varmaa --disabled-password --gecos "" varmaa

COPY test/labs/authorized_keys /home/varmaa/.ssh/

RUN chmod 0700 /home/varmaa/.ssh && chmod 0600 /home/varmaa/.ssh/* && \
  mkdir /home/varmaa/git
RUN chown -R varmaa.varmaa /home/varmaa

RUN printf "GatewayPorts clientspecified\n" >> /etc/ssh/sshd_config

COPY setup.py /labs/
COPY labs /labs/labs/
RUN cd /labs && python setup.py develop

EXPOSE 22
