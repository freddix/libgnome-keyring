Summary:	Keep passwords and other user's secrets
Name:		libgnome-keyring
Version:	3.10.1
Release:	2
License:	LGPL v2+/GPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnome-keyring/3.10/%{name}-%{version}.tar.xz
# Source0-md5:	9b7834bf6630160878a0aa7cb5df7dfc
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	gobject-introspection-devel >= 1.38.0
BuildRequires:	libgcrypt-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	vala-vapigen >= 0.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The library libgnome-keyring is used by applications to integrate with
the GNOME keyring system.

%package devel
Summary:	Headers for GNOME keyring library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Headers for GNOME keyring library.

%package apidocs
Summary:	GNOME keyring API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
GNOME keyring API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/libgnome-keyring.so.?
%attr(755,root,root) %{_libdir}/libgnome-keyring.so.*.*.*
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnome-keyring.so
%{_datadir}/gir-1.0/*.gir
%{_includedir}/gnome-keyring-1
%{_pkgconfigdir}/gnome-keyring-1.pc
%{_datadir}/vala/vapi/gnome-keyring-1.vapi

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gnome-keyring

