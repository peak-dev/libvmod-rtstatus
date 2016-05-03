Summary: rtstatus VMOD for Varnish
Name: vmod-rtstatus
Version: 1.0
Release: 1%{?dist}
License: BSD
Group: System Environment/Daemons
Source0: libvmod-rtstatus.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: varnish >= 4.0.2
Requires: varnish-libs >= 4.0.2
BuildRequires: make
BuildRequires: python-docutils
BuildRequires: varnish >= 4.0.2
BuildRequires: varnish-libs-devel >= 4.0.2

%description
Real Time status page for Varnish.

%prep
%setup -n libvmod-rtstatus-%{version}


%build
%configure --prefix=/usr/
%{__make} %{?_smp_mflags}
%{__make} %{?_smp_mflags} check

%install
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
[ %{buildroot} != "/" ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/varnis*/vmods/
%doc /usr/share/doc/lib%{name}/*
%{_mandir}/man?/*

%changelog
* Tue Nov 14 2012 Lasse Karstensen <lasse@varnish-software.com> - 0.1-0.20121114
- Initial version.