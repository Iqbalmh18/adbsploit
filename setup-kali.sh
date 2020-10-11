#!/usr/bin/bash

sudo apt-get update && sudo apt-get install -y android-tools-adb android-tools-fastboot && sudo apt-get install python3
python3 -m pip install shodan rich prompt_toolkit
cat adbsploit.sh > /usr/bin && chmod +x /usr/bin/adbsploit && adbsploit