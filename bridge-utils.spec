%define	name	bridge-utils
%define	version	1.2
%define	rel	3
%define	release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Utilities for configuring the linux ethernet bridge
Group:		Networking/Other
License:	GPL
URL:		http://linux-net.osdl.org/index.php/Bridge
Source0:	http://downloads.sourceforge.net/bridge/%{name}-%{version}.tar.bz2
Source1:	README.urpmi
Source2:    bash-completion
BuildRequires:	kernel-headers
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package contains utilities for configuring the linux ethernet
bridge. The linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%description -l	pl
Ten pakiet zawiera narzêdzia przeznaczone do konfigurowania linuxowego
ethernet bridge (inteligentny switch). Linux ethernet bridge mo¿e byæ
u¿yty do ³±czenia kilku ethernetowych interfejsów sieciowych w jeden.
Po³±czenie jest w pe³ni prze¼roczyste; hosty przy³±czone po jednej
stronie widz± hosty z drugiej strony bezpo¶rednio.

%package	devel
Summary:	Libraries for the linux ethernet bridge programs
Summary(pl):	Biblioteki u¿ywane do sterowania linuxowym bridge
Group:		Development/C

%description	devel
This package contains the header and object files necessary for
developing programs which use 'libbridge', the interface to the linux
kernel ethernet bridge.

%description	devel -l pl
Ten pakiet zawiera pliki nag³ówkowe i bibliotekê konieczn± do rozwoju
programów u¿ywaj±cych 'libbridge' - interfejs do linuxowego ethernet
bridge.

%prep
%setup -q

%build
autoconf
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
install -m 644 %{SOURCE1} README.update.urpmi

# bash completion
install -m 755 -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -m 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/bash_completion.d/bridge-utils

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README README.update.urpmi doc/{FAQ,FIREWALL,HOWTO,WISHLIST}
%{_mandir}/man*/*
%{_sbindir}/*
%{_sysconfdir}/bash_completion.d/bridge-utils

%files devel
%defattr(-,root,root)
%{_mandir}/man*/*
%{_libdir}/*.a
%{_includedir}/*.h
