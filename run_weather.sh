#!/bin/bash
APP_DIR=$(dirname "$(readlink -f "$0")")
cd "$APP_DIR"
PYTHON_PATH=$(which python3)
if [ -z "$PYTHON_PATH" ]
    then
        PYTHON_PATH="$HOME/miniconda3/bin/python"
    fi
"$PYTHON_PATH" main.py >> cron_debug.log 2>&1