#!bin/bash

if [ ! -d "./target" ] && [ ! -d "./data" ]; then
    echo "Execute o install.sh!!!!!."
    exit 1
fi

python3 regen_pdf.py