#!/bin/sh

# quit on errors:
set -o errexit

# quit on unbound symbols:
set -o nounset

DIR=`dirname "$0"`

cd $DIR
export FLASK_APP=app.py


# Next, we copy the static files from the Python packages into the Flask
# application's static folder
flask collect -v

flask webpack buildall

