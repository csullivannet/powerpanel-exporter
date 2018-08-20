docker build --tag powerpanel .
docker run -d -p 8081:8080 --name powerpanel -ti --tmpfs /run --tmpfs /tmp -v /sys/fs/cgroup:/sys/fs/cgroup:ro --device /dev/usb/hiddev0  http