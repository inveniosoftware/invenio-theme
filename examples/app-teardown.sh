#!/bin/sh

DIR=`dirname "$0"`

cd $DIR
export FLASK_APP=app.py

# clean environment
[ -e "$DIR/static" ] && rm -Rf $DIR/static/
