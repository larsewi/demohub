#!/usr/bin/env bash

cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name hub --role hub
cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name ubuntu --role client
cf-remote spawn --platform debian-9-x64 --count 1 --name debian --role client
cf-remote spawn --platform rhel-8-x64 --count 1 --name rhel --role client
cf-remote spawn --platform centos-7-x64 --count 1 --name centos --role client

cf-remote install --demo --bootstrap hub --hub hub
cf-remote deploy --hub hub

cf-remote install --demo --bootstrap hub --clients ubuntu
cf-remote install --demo --bootstrap hub --clients debian
cf-remote install --demo --bootstrap hub --clients rhel
cf-remote install --demo --bootstrap hub --clients centos

cf-remote info --hosts hub

