# powerpanel-exporter
A prometheus exporter for CyberPower PowerPanel Personal Edition for Linux

Your UPS must be connected to the docker host via USB. Running on Fedora 28, my UPS was registered as `/dev/usb/hiddev0`. Yours may differ.

Run `build.sh` and then `docker-compose up -d` after verifying the USB path and you should be good to go!

Note - This would not build for me on OSX 10.16, but builds successfully on Fedora 28. OSX complains when enabling the pwrstat daemon.
