Summary:	A light-weight system monitor
Summary(pl):	Monitor systemu dla ¶rodowiska graficznego
Name:		conky
Version:	1.3.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/conky/%{name}-%{version}.tar.gz
URL:		http://conky.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conky is a light-weight system monitor based on the torsmo code. Conky
can display arbitrary information (such as the date, CPU temperature
from i2c, MPD info, and anything else you desire) to the root window
in X11.

%description -l pl
Conky jest niewielkim monitorem systemu opartym na kodzie torsmo. Mo¿e
wy¶wietlaæ takie informacje, jak:
- data
- temperatura CPU
- ilo¶æ miejsca na dysku itp.

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
%doc AUTHORS COPYING NEWS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.1*
