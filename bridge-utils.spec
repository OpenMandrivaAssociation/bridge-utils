Summary:	Utilities for configuring the linux ethernet bridge
Name:		bridge-utils
Version:	1.5
Release:	6
Group:		Networking/Other
License:	GPL
Url:		http://linux-net.osdl.org/index.php/Bridge
Source0:	http://downloads.sourceforge.net/bridge/%{name}-%{version}.tar.gz
Patch1:		bridge-utils-1.5-kernel-headers.patch
BuildRequires:	kernel-headers
Obsoletes:	%{name}-devel < 1.5-4

%description
This package contains utilities for configuring the linux ethernet
bridge. The linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%prep
%setup -q
%patch1 -p1

%build
autoconf
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc ChangeLog README doc/{FAQ,FIREWALL,HOWTO,WISHLIST}
%{_mandir}/man*/*
%{_sbindir}/*

