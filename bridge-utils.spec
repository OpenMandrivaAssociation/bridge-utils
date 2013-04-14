%define	name	bridge-utils
%define	version	1.5
%define	rel     3
%define	release	%{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Utilities for configuring the linux ethernet bridge
Group:		Networking/Other
License:	GPL
URL:		http://linux-net.osdl.org/index.php/Bridge
Source0:	http://downloads.sourceforge.net/bridge/%{name}-%{version}.tar.gz
Patch1:		bridge-utils-1.5-kernel-headers.patch
BuildRequires:	kernel-headers

%description
This package contains utilities for configuring the linux ethernet
bridge. The linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%package	devel
Summary:	Libraries for the linux ethernet bridge programs
Group:		Development/C

%description	devel
This package contains the header and object files necessary for
developing programs which use 'libbridge', the interface to the linux
kernel ethernet bridge.

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
%defattr(-,root,root)
%doc ChangeLog README doc/{FAQ,FIREWALL,HOWTO,WISHLIST}
%{_mandir}/man*/*
%{_sbindir}/*

%files devel
%defattr(-,root,root)





%changelog
* Sun Jul 31 2011 tv <tv> 1.5-1.mga2
+ Revision: 131051
- fix file list
- new release
