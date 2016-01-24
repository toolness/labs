#! /bin/bash

source /root/.bashrc

cp -R /labs-ro /labs && cd /labs && \
  python setup.py install > /var/log/labs-install.log && \
  cd /labs && $@
