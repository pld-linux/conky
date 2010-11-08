%bcond_without	lua_cairo	# without lua cairo bindings
#
Summary:	A light-weight system monitor
Summary(pl.UTF-8):	Monitor systemu dla środowiska graficznego
Name:		conky
Version:	1.8.1
Release:	3
License:	Distributable (see COPYING doc)
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/conky/%{name}-%{version}.tar.bz2
# Source0-md5:	366dc6a5c2ebebfbe6f53da25061b5d6
URL:		http://conky.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
%{?with_lua_cairo:BuildRequires:	tolua++-devel >= 1.0.90}
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Conky is a light-weight system monitor based on the torsmo code. Conky
can display arbitrary information (such as the date, CPU temperature
from i2c, MPD info, and anything else you desire) to the root window
in X11.

%description -l pl.UTF-8
Conky jest niewielkim monitorem systemu opartym na kodzie torsmo. Może
wyświetlać takie informacje, jak:
- data
- temperatura CPU
- ilość miejsca na dysku itp.

%prep
%setup -q
%{__sed} -i 's,lua5.1,lua51,' configure.ac

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	CFLAGS="%{rpmcflags} `pkg-config ncurses --cflags`" \
	LIBS="-ltinfo" \
	%{?with_lua_cairo:--enable-lua-cairo}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING must be added (see COPYING file)
%doc AUTHORS ChangeLog COPYING README TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_sysconfdir}/conky
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conky/%{name}.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conky/%{name}_no_x11.conf
%dir %{_libdir}/conky
%if %{with lua_cairo}
%{_libdir}/conky/libcairo.so.*.*.*
%ghost %{_libdir}/conky/libcairo.so.0
%endif
%{_mandir}/man1/%{name}.1*
