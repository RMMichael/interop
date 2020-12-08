#!/usr/bin/env bash

PATH=$(dirname ${BASH_SOURCE[0]})

set -e

cd $PATH

bash -c "apt -qq update && apt -qq install -y \
            git \
                  "
