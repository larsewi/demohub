#!/usr/bin/env bash

cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name HUB --role hub
cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name UBUNTU --role client
cf-remote spawn --platform debian-9-x64 --count 1 --name DEBIAN --role client
cf-remote spawn --platform rhel-8-x64 --count 1 --name RHEL --role client
cf-remote spawn --platform centos-7-x64 --count 1 --name CENTOS --role client

cf-remote install --package "cfengine-nova-hub_3.22.0a.3f67ca765_25996.ubuntu22_amd64.deb" --demo --bootstrap HUB --hub HUB
cfbs build
cf-remote deploy --hub HUB

cf-remote install --package "cfengine-nova_3.22.0a.3f67ca765_25996.ubuntu22_amd64.deb" --demo --bootstrap HUB --clients UBUNTU
cf-remote install --package "cfengine-nova_3.22.0a.3f67ca765_25996.debian9_amd64.deb" --demo --bootstrap HUB --clients DEBIAN
cf-remote install --package "cfengine-nova-3.22.0a.3f67ca765-25996.el8.x86_64.rpm" --demo --bootstrap HUB --clients RHEL
cf-remote install --package "cfengine-nova-3.22.0a.3f67ca765-25995.el7.x86_64.rpm" --demo --bootstrap HUB --clients CENTOS

cf-remote run --hosts HUB "sudo systemctl restart cf-hub"

cf-remote info --hosts HUB
