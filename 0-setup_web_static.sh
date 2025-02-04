#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static.
sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
hbnb_static="\\\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}\n"
sudo sed -i "35i $hbnb_static" /etc/nginx/sites-available/default
sudo service nginx restart
