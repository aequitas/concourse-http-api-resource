FROM python:3

# install requirements
ADD requirements*.txt setup.cfg ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements_dev.txt

ADD assets/ /opt/resource/
ADD test/ /opt/resource-tests/

ENTRYPOINT RESOURCE_DEBUG=1 py.test -l --tb=short -r fE /opt/resource-tests
