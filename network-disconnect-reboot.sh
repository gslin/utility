#!/bin/bash

TMP_1="$(ping -c 1 -q 1.1.1.1 > /dev/null; echo $?)"
TMP_2="$(ping -c 1 -q 8.8.8.8 > /dev/null; echo $?)"
TMP_3="$(ping -c 1 -q 168.95.1.1 > /dev/null; echo $?)"

mkdir -p /tmp/network-disconnect-reboot
cd /tmp/network-disconnect-reboot

if [ -f 1 ]; then
    mv -f 1 2
else
    echo 0 > 2
fi

if [ -f 0 ]; then
    mv -f 0 1
else
    echo 0 > 1
fi

if [ "${TMP_1}" -ne 0 -a "${TMP_2}" -ne 0 -a "${TMP_3}" -ne 0 ]; then
    echo 1 > 0
else
    echo 0 > 0
fi

if [ "$(cat 0)" -eq 1 -a "$(cat 1)" -eq 1 -a "$(cat 2)" -eq 1 ]; then
    shutdown -r +5
fi
