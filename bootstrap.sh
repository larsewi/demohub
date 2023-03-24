#!/bin/bash

# Hub
cf-remote save --hosts vagrant@192.168.56.10 --role hub --name hub
cf-remote --version master install --demo --bootstrap hub --hub hub
cfbs build
cf-remote deploy --hub hub

# Client
cf-remote save --hosts vagrant@192.168.56.11 --role client --name client
cf-remote --version master install --demo --bootstrap hub --clients client
