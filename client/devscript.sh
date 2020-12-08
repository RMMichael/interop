#!/usr/bin/env bash
# Utility scripts.

CLIENT=$(dirname ${BASH_SOURCE[0]})
REPO=${CLIENT}/..

# Quit on any error.
set -e

# Run commands from context of client directory.
cd $CLIENT

if [ "$1" == "rundev" ]
then
bash -c "cd /interop/client && \
        python3 -m venv --system-site-packages venv && \
        source venv/bin/activate && \
        pip3 install -r requirements.txt && \
        deactivate"

bash -c "cd /interop/client && \
        source venv/bin/activate && \
        python3 setup.py install && \
        deactivate"

bash --init-file configure.sh
#source venv/bin/activate

fi

if [ "$1" == "venv" ]
then
bash --init-file configure.sh
fi
