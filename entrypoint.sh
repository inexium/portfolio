#!/bin/bash

set -e

echo "Starting UWSGI"
./.local/bin/uv run uwsgi --ini uwsgi.ini