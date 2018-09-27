FROM python:3.6

# install requirements
ADD requirements*.txt setup.cfg ./
RUN pip install --no-cache-dir -r requirements.txt

# install asserts
ADD assets/ /opt/resource/
ADD test/ /opt/resource-tests/

RUN /opt/resource-tests/test.sh
