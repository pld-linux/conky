Summary:	A light-weight system monitor
Summary(pl):	Monitor systemu dla �rodowiska graficznego
Name:		conky
Version:	1.4.4
Release:	1
License:	Distributable (see COPYING doc)
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/conky/%{name}-%{version}.tar.bz2
# Source0-md5:	c856556d4372226f99cf7e9a888e9118
URL:		http://conky.sourceforge.net/
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conky is a light-weight system monitor based on the torsmo code. Conky
can display arbitrary information (such as the date, CPU temperature
from i2c, MPD info, and anything else you desire) to the root window
in X11.

%description -l pl
Conky jest niewielkim monitorem systemu opartym na kodzie torsmo. Mo�e
wy�wietla� takie informacje, jak:
- data
- temperatura CPU
- ilo�� miejsca na dysku itp.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#COPYING must be added (see COPYING file)
%doc AUTHORS ChangeLog COPYING README TODO doc/conkyrc.sample
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
