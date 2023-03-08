#!/usr/bin/env bash

cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name HUB --role hub
cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name UBUNTU --role client
cf-remote spawn --platform debian-9-x64 --count 1 --name DEBIAN --role client
cf-remote spawn --platform rhel-8-x64 --count 1 --name RHEL --role client
cf-remote spawn --platform centos-7-x64 --count 1 --name CENTOS --role client

cf-remote install --demo --bootstrap HUB --hub HUB
cf-remote deploy --hub HUB

cf-remote install --demo --bootstrap HUB --clients UBUNTU
cf-remote install --demo --bootstrap HUB --clients DEBIAN
cf-remote install --demo --bootstrap HUB --clients RHEL
cf-remote install --demo --bootstrap HUB --clients CENTOS

cf-remote info --hosts HUB
