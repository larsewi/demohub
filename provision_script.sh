#!/usr/bin/env bash

cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name hub1 --role hub
cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name hub2 --role hub
cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name hub3 --role hub
cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name hub4 --role hub
cf-remote spawn --platform ubuntu-22-04-x64 --count 1 --name hub5 --role hub

sleep 30

cf-remote install --package "cfengine-nova-hub_3.22.0a.3f67ca765_25996.ubuntu22_amd64.deb" --demo --bootstrap hub1 --hub hub1
rm -f def.json
cp def1.json def.json
cfbs build
cf-remote deploy --hub hub1
cf-remote run --hosts hub1 "sudo systemctl restart cf-hub"

cf-remote install --package "cfengine-nova-hub_3.22.0a.3f67ca765_25996.ubuntu22_amd64.deb" --demo --bootstrap hub2 --hub hub2
rm -f def.json
cp def2.json def.json
cfbs build
cf-remote deploy --hub hub2
cf-remote run --hosts hub2 "sudo systemctl restart cf-hub"

cf-remote install --package "cfengine-nova-hub_3.22.0a.3f67ca765_25996.ubuntu22_amd64.deb" --demo --bootstrap hub3 --hub hub3
rm -f def.json
cp def3.json def.json
cfbs build
cf-remote deploy --hub hub3
cf-remote run --hosts hub3 "sudo systemctl restart cf-hub"

cf-remote install --package "cfengine-nova-hub_3.22.0a.3f67ca765_25996.ubuntu22_amd64.deb" --demo --bootstrap hub4 --hub hub4
rm -f def.json
cp def4.json def.json
cfbs build
cf-remote deploy --hub hub4
cf-remote run --hosts hub4 "sudo systemctl restart cf-hub"

cf-remote install --package "cfengine-nova-hub_3.22.0a.3f67ca765_25996.ubuntu22_amd64.deb" --demo --bootstrap hub5 --hub hub5
rm -f def.json
cp def5.json def.json
cfbs build
cf-remote deploy --hub hub5
cf-remote run --hosts hub5 "sudo systemctl restart cf-hub"
