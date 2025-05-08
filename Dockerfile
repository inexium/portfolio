FROM debian

ENV DEBIAN_FRONTEND=noninteractive
ENV DEBIAN_PRIORITY=critical
ENV DEBCONF_NOWARNINGS=yes

RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y \
	pipx \
	gcc \
	python3-dev \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /opt/cv
COPY . /opt/cv

RUN usermod -d /opt/cv nobody
RUN chown -R nobody /opt/cv
USER nobody

RUN pipx install uv
RUN ./.local/bin/uv sync
RUN ./.local/bin/uv run python manage.py collectstatic
RUN chmod u+x /opt/cv/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/opt/cv/entrypoint.sh"]
