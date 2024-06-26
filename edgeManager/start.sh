#!/usr/bin/env bash

RELATIVE_DIR=`dirname "$0"`
cd $RELATIVE_DIR

echo $1
ENV=$1
echo "ENV is $ENV"

if [ "$ENV" == "run" ]; then
    cd backend

    python3 run.py
    if [ $? -ne 0 ]; then
        echo ">>> python run fail, try to pip install"
        python3 -m pip install -r requirements.txt
    fi
    python3 run.py

elif [ "$ENV" == "start" ]; then
    cd frontend

    npm start
    if [ $? -ne 0 ]; then
        echo ">>> npm start fail, try to npm install"
        npm run clean
        if [ $? -eq 0 ]; then
            npm install --legacy-peer-deps
        fi
    fi
    npm start

elif [ "$ENV" == "clean" ]; then
    cd frontend

    npm run clean

elif [ "$ENV" == "build" ]; then
    cd frontend

    npm run build
    if [ $? -ne 0 ]; then
        echo ">>> npm build fail, try to npm install"
        npm run clean
        if [ $? -eq 0 ]; then
            npm install --legacy-peer-deps
        fi
    fi

    if [ $? -eq 0 ]; then
        npm run build
        if [ $? -eq 0 ]; then
            tar -zcf build.tar build

        else
            echo ">>> npm install and build fail"
        fi
    fi

elif [ "$ENV" == "apply" ]; then
    cd frontend
    rm -rf build

    tar -xvf build.tar

elif [ "$ENV" == "test" ]; then
    cd frontend

    npm run build
    if [ $? -ne 0 ]; then
        echo ">>> npm build fail, try to npm install"
        npm run clean
        if [ $? -eq 0 ]; then
            npm install --legacy-peer-deps
        fi
    fi

    if [ $? -eq 0 ]; then
        npm run build
        if [ $? -eq 0 ]; then
            cd ../backend

            python3.9 run.py
            if [ $? -ne 0 ]; then
                echo ">>> python run fail, try to pip install"
                python3.9 -m pip install -r requirements.txt
            fi
            python3.9 run.py

        else
            echo ">>> npm install and build fail"
        fi
    fi

fi
