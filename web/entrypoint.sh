#!/bin/sh

python3 manage.py migrate --noinput
python3 manage.py loaddata datadump.json
python3 manage.py collectstatic --noinput && chmod 775 -R /static
