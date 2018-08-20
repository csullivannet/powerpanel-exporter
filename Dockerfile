FROM fedora

ENV container docker
ENV pp_rpm powerpanel-132-0x86_64.rpm
ENV pp_rpm_url https://dl4jz3rbrsfum.cloudfront.net/software/${pp_rpm}

RUN curl -o ${pp_rpm} ${pp_rpm_url} && \
    rpm -ivh ${pp_rpm} && \
    rm -f ${pp_rpm}

RUN systemctl enable pwrstatd

STOPSIGNAL SIGRTMIN+3

ENTRYPOINT [ "/sbin/init" ]
