Name:       Dashboard
Summary:    A HTML HelloTizen application
Version:    1.0
Release:    1
Group:      Applications/System
License:    ASL 2.0
URL:        http://www.tizen.org2
Source0:    %{name}-%{version}.tar.bz2

#BuildRequires:  common
BuildRequires:  pkgmgr
BuildRequires:  zip
BuildRequires:  desktop-file-utils

%description
A proof of concept pure html5 UI

%prep
%setup -q -n %{name}-%{version}

%build
make %{?_smp_mflags} wgtPkg

%install
make %{?_smp_mflags} wgtPkg
pkgcmd -i -t wgt -p DNA_Dashboard.wgt

%files
%defattr(-,root,root,-)

