FROM python:3.8

# Install necessary packages
RUN apt-get update    &&\
    apt-get install -y  \
    libldap2-dev        \
    libsasl2-dev        \
    ldap-utils          \
    xmlsec1             \
    lcov                \
    python3-dev

RUN python3 -m pip install --upgrade pip
RUN pip3 install poetry==1.0.9
RUN poetry config virtualenvs.create false

# Copy poetry files
COPY pyproject.toml /tmp/mnt/pyproject.toml
COPY poetry.lock /tmp/mnt/poetry.lock

# Install dependencies
RUN cd /tmp/mnt && poetry install

CMD ["/bin/sh"]
