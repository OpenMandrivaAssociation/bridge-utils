%define	name	bridge-utils
%define	version	1.4
%define	rel     7
%define	release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Utilities for configuring the linux ethernet bridge
Group:		Networking/Other
License:	GPL
URL:		http://linux-net.osdl.org/index.php/Bridge
Source0:	http://downloads.sourceforge.net/bridge/%{name}-%{version}.tar.bz2
BuildRequires:	kernel-headers
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

%build
autoconf
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README doc/{FAQ,FIREWALL,HOWTO,WISHLIST}
%{_mandir}/man*/*
%{_sbindir}/*

%files devel
%defattr(-,root,root)
%{_mandir}/man*/*
%{_libdir}/*.a
%{_includedir}/*.h
