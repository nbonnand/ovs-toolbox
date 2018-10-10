#!/bin/bash

#Nicolas Bonnand, 2018

apt-get install -y software-properties-common apt-transport-https > /tmp/startup_script_log  2>&1

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - >> /tmp/startup_script_log  2>&1

add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" >> /tmp/startup_script_log  2>&1

apt-get update >> /tmp/startup_script_log 2>&1

apt-get install -y docker-ce openvswitch-switch plotnetcfg >> /tmp/startup_script_log  2>&1

