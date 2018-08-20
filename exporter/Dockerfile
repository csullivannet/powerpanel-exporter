FROM powerpanel

WORKDIR /opt/pp-exporter

RUN dnf -y install python python-pip && dnf clean all

RUN pip install --upgrade sultan

COPY server.py server.py

COPY stats.json stats.json

COPY index.html index.html

COPY pyserver.service /lib/systemd/system/pyserver.service 

RUN systemctl enable pyserver