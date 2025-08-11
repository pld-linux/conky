#
# TODO: fix build with lua. Now when lua enabled conky requires tolua++-devel when installing
#
# Conditional build:
%bcond_with	lua_cairo	# without lua cairo bindings
%bcond_with	lua_imlib2	# without lua imlib2 bindings
#
Summary:	A light-weight system monitor
Summary(pl.UTF-8):	Monitor systemu dla środowiska graficznego
Name:		conky
Version:	1.22.2
Release:	1
License:	Distributable (see COPYING doc)
Group:		X11/Applications
Source0:	https://github.com/brndnmtthws/conky/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	4dc1856729caf13812423882a5b6b2f2
Source1:	https://github.com/brndnmtthws/conky/releases/download/v%{version}/%{name}.1.gz
# Source1-md5:	032d5220afc460796c8d9611e709f0a2
URL:		https://github.com/brndnmtthws/conky/
BuildRequires:	alsa-lib-devel
%{?with_lua_cairo:BuildRequires:	cairo-devel}
BuildRequires:	cmake
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	imlib2-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	lua51-devel >= 5.1
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sed >= 4.0
BuildRequires:	sqlite3-devel
%if %{with lua_cairo} || %{with lua_imlib2}
BuildRequires:	tolua++-devel >= 1.0.90
%endif
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

%package lua-cairo
Summary:	Lua Cairo bindings for Conky
Summary(pl.UTF-8):	Dowiązania Lua Cairo dla Conky
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description lua-cairo
Lua Cairo bindings for Conky.

%description lua-cairo -l pl.UTF-8
Dowiązania Lua Cairo dla Conky.

%package lua-imlib2
Summary:	Lua Imlib2 bindings for Conky
Summary(pl.UTF-8):	Dowiązania Lua Imlib2 dla Conky
Group:		Development/Languages
Requires:	%{name} = %{version}-%{release}

%description lua-imlib2
Lua Imlib2 bindings for Conky.

%description lua-imlib2 -l pl.UTF-8
Dowiązania Lua Imlib2 dla Conky.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DBUILD_CURL=ON \
	-DBUILD_IMLIB2=ON \
	-DBUILD_WLAN=ON \
	-DBUILD_RSS=ON \
	%{cmake_on_off lua_cairo BUILD_LUA_CAIRO} \
	%{cmake_on_off lua_imlib2 BUILD_LUA_IMLIB2} \
	-DDOC_PATH=%{_sysconfdir}/%{name} \
	-DLIB_INSTALL_DIR=%{_libdir}/%{name}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_mandir}/man1/
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/

rm $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/convert.lua

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# COPYING must be added (see COPYING file)
%doc AUTHORS COPYING README.md
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_sysconfdir}/conky
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conky/%{name}.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conky/%{name}_no_x11.conf
%dir %{_libdir}/conky
%attr(755,root,root) %{_libdir}/%{name}/libtcp-portmon.so
%{_desktopdir}/conky.desktop
%{_iconsdir}/hicolor/scalable/apps/conky-logomark-violet.svg
%{_mandir}/man1/%{name}.1*

%if %{with lua_cairo}
%files lua-cairo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/conky/libcairo.so.*.*.*
%{_libdir}/conky/libcairo.so
%endif

%if %{with lua_imlib2}
%files lua-imlib2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/conky/libimlib2.so.*.*.*
%{_libdir}/conky/libimlib2.so
%endif
