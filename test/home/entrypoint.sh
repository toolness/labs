#! /bin/bash

source /root/.bashrc

cd /labs && python setup.py develop > /var/log/labs-install.log && \
  cd /labs/test && $@
