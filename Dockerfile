FROM centos:7

WORKDIR /root/rpmbuild/
RUN mkdir ./BUILD ./BUILDROOT ./RPMS ./SOURCES ./SPECS ./SRPMS
COPY ./app-1 ./SOURCES/app-1
COPY ./app-1.spec ./SPECS/
RUN cd ./SOURCES/ && tar -cvzf app-1.tar.gz app-1 && cd /root/rpmbuild/ && \
yum -y install rpmdevtools rpm-build && \
rpmbuild -v -bb ./SPECS/app-1.spec
