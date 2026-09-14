FROM python:3.12-alpine

WORKDIR /lab
COPY requirements-dev.txt /lab/requirements-dev.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY tests /lab/tests
COPY course /lab/course
COPY attacker-tools /lab/attacker-tools
COPY solutions /lab/solutions
COPY docker-compose.yml /lab/docker-compose.yml
COPY docker-compose.hardened.yml /lab/docker-compose.hardened.yml
COPY pytest.ini /lab/pytest.ini

CMD ["python", "-m", "pytest"]
