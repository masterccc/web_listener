#!/bin/bash

echo "Start installing fakeweb ..."

USERN="$USER"

rm -fr venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# ---  Root is used below this line --- #

sudo -v

sudo cp fakeweb.service /etc/systemd/system/
sudo sed -i 's/###USERNAME###/'${USERN}'/g' /etc/systemd/system/fakeweb.service
sudo systemctl daemon-reload
sudo systemctl enable fakeweb.service

echo "Fakeweb installation succeed"