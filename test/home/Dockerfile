FROM python:2.7

RUN apt-get update
RUN apt-get install -y openssh-client

RUN pip install argh

# http://serverfault.com/a/132973
RUN printf \
  'StrictHostKeyChecking=no\nLogLevel=ERROR\n' >> /etc/ssh/ssh_config

COPY bashrc /root/.bashrc
COPY id_rsa id_rsa.pub /root/.ssh/
RUN chmod 0700 /root/.ssh && chmod 0600 /root/.ssh/* && \
  git config --global user.email "root@example.com" && \
  git config --global user.name "Root"
