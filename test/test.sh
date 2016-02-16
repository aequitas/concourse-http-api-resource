#!/bin/sh

# fail if one command fails
set -e

# install requirements
pip install --no-cache-dir -r requirements_dev.txt

# test
pylama /opt/resource /opt/resource-tests/
py.test -l --tb=short -r fE /opt/resource-tests

# cleanup
rm -fr /tmp/*
pip uninstall -y -r requirements_dev.txt
