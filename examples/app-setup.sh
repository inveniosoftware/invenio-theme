#!/bin/sh

# quit on errors:
set -o errexit

# quit on unbound symbols:
set -o nounset

DIR=`dirname "$0"`

cd $DIR
export FLASK_APP=app.py

# Install requirements
npm install -g node-sass clean-css clean-css-cli requirejs uglify-js

# Collect npm, requirements from registered bundles
flask npm

# Now install npm requirements (requires that npm is already installed)
cd static ; npm install ; cd ..

# Next, we copy the static files from the Python packages into the Flask
# application's static folder
flask collect -v

# Finally, we build the webassets bundles
flask assets build
