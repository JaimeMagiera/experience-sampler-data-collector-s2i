# experience-sampler-data-collector-builder
FROM registry.redhat.io/rhel8/httpd-24

LABEL maintainer="Jaime Magiera <jaimelm@umich.edu>"
ENV BUILDER_VERSION 1.0
LABEL io.k8s.description="Platform for building the Experience Sampler Data Collector" \
      io.k8s.display-name="Builder for Experience Sampler Data Collector" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,Experience Sampler, Data Collector"

COPY ./<builder_folder>/ /opt/app-root/
COPY ./s2i/bin/ /usr/libexec/s2i
RUN chown -R 1001:1001 /opt/app-root
USER 1001
RUN sed -i 's#/opt/rh/httpd24/root/var/www/cgi-bin#/opt/app-root/src/cgi-bin#g' /etc/httpd/conf/httpd.conf
CMD ["/usr/libexec/s2i/usage"]
