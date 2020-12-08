#!/usr/bin/env bash

DIR=$(dirname ${BASH_SOURCE[0]})


set -e

cd $DIR
#download packages for interop server
bash -c "apt -qq update && apt -qq install -y \
            git \
            nginx \
            npm \
            postgresql-client \
            protobuf-compiler \
            python3  \
            python3-matplotlib \
            python3-numpy \
            python3-pip \
            python3-psycopg2 \
            python3-pyproj"

bash -c "pip3 install -r ../server/config/requirements.txt"

bash -c "npm install -g yuglify"



