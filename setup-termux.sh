#!~/../usr/bin/bash

apt update && apt install -y python wget
python3 -m pip install shodan rich prompt_toolkit
wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh -q && bash InstallTools.sh
cat adbsploit.sh  > ~/../usr/bin/adbsploit && chmod +x ~/../usr/bin/adbsploit && adbsploit