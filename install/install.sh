#! /bin/bash

# install the requirements
sudo chown -R ubuntu:ubuntu /home/ubuntu/
pip3 install flask
pip3 install pymongo

# download the apply
mkdir /home/ubuntu/src
cd /home/ubuntu/src
git clone https://github.com/norhe/simple-client.git

# systemd

cat <<EOF | sudo tee /lib/systemd/system/web_client.service
[Unit]
Description=client.py - Client service API
After=network.target

[Service]
Type=simple
User=ubuntu
ExecStart=/usr/local/bin/envconsul -prefix web_client_conf /usr/bin/python3 /home/ubuntu/src/simple-client/client.py
Restart=always
SyslogIdentifier=web_client

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl daemon-reload
sudo systemctl enable web_client.service
sudo systemctl start web_client.service

echo "Setting up Nginx to listen on 80..."

DEBIAN_FRONTEND=noninteractive sudo apt-get --yes install nginx-light
sudo rm /etc/nginx/sites-enabled/default

cat <<EOF | sudo tee /etc/nginx/sites-available/web-client
server {
    listen 80;
    location / {
        proxy_pass         "http://127.0.0.1:8080";
    }
}
EOF

sudo ln -s /etc/nginx/sites-available/web-client /etc/nginx/sites-enabled/web-client

sudo systemctl restart nginx

