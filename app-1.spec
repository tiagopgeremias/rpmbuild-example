Name:           app
Version:        1
Release:        0
Summary:        Example of creating RPM packages.
 
License:        GPL
URL:            https://github.com/tiagopgeremias/rpmbuild-example
Source0:        app-1.tar.gz
 
BuildArch:    noarch
BuildRoot:    %{_tmppath}/%{name}-buildroot
 
%description
This repository serves as a basis for creating RPM packages.
All content is for testing purposes only.
 
%prep
/usr/bin/getent passwd pyapp || /usr/sbin/useradd -r -s /sbin/nologin pyapp
%setup -q
 
%install
mkdir -p $RPM_BUILD_ROOT/var/log/pyapp/
mkdir -p $RPM_BUILD_ROOT
cp -R * $RPM_BUILD_ROOT
 
%files
%defattr(-,pyapp,pyapp,-)
/opt/app/
/var/log/pyapp/