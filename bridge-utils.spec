Summary:	Utilities for configuring the linux ethernet bridge
Name:		bridge-utils
Version:	1.7.1
Release:	2
Group:		Networking/Other
License:	GPL
Url:		https://linux-net.osdl.org/index.php/Bridge
Source0:	http://downloads.sourceforge.net/bridge/%{name}-%{version}.tar.gz
BuildRequires:	kernel-headers
Obsoletes:	%{name}-devel < 1.5-4

%description
This package contains utilities for configuring the linux ethernet
bridge. The linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%prep
%autosetup -p1

%build
autoconf
%configure
%make_build -j1

%install
%make_install

%files
%doc ChangeLog README doc/{FAQ,FIREWALL,HOWTO,WISHLIST}
%doc %{_mandir}/man*/*
%{_sbindir}/*
