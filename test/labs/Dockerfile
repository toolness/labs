FROM python:2.7

RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# http://askubuntu.com/a/94067
RUN adduser --home /home/varmaa --disabled-password --gecos "" varmaa

COPY authorized_keys /home/varmaa/.ssh/

RUN chmod 0700 /home/varmaa/.ssh && chmod 0600 /home/varmaa/.ssh/* && \
  mkdir /home/varmaa/git
RUN chown -R varmaa.varmaa /home/varmaa

EXPOSE 22
