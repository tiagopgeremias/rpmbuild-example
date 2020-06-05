# RPMBUILD-Example
Small example for creating RPM packages, for testing purposes.


## Create RPM
    docker build -t rpm_package .

    docker run -itd --name my_rpm_package rpm_package

    docker cp my_rpm_package:/root/rpmbuild/RPMS/noarch/app-1-0.noarch.rpm .