%global _hardened_build 1

Name:           libmodsecurity-nginx
Version:        3.0.7
Release:        2%{?dist}
Summary:        ModSecurity
License:        ASL 2.0
URL:            http://www.modsecurity.org/
Group:          System Environment/Daemons
Source0:        https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
Source1:        https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz.asc
Source100:      modsecurity.gpg

BuildRequires: gcc-c++
BuildRequires: automake
BuildRequires: make
BuildRequires: flex
BuildRequires: bison
BuildRequires: git-core
BuildRequires: ssdeep-devel
BuildRequires: gnupg
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(yajl)
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(geoip)
BuildRequires: pkgconfig(libpcre)
BuildRequires: pkgconfig(lmdb)

Conflicts:      libmodsecurity
Conflicts:      libmodsecurity-devel
Conflicts:      libmodsecurity-static

%description
Libmodsecurity is one component of the ModSecurity v3 project.
The library codebase serves as an interface to ModSecurity Connectors
taking in web traffic and applying traditional ModSecurity processing.
In general, it provides the capability to load/interpret rules written
in the ModSecurity SecRules format and apply them to HTTP content provided
by your application via Connectors.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package static
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description static
The %{name}-static package contains static libraries for developing
applications that use %{name}.

%prep
cat %{SOURCE100} > %{_builddir}/modsecurity.gpg
%{gpgverify} --keyring='%{_builddir}/modsecurity.gpg' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -n modsecurity-v%{VERSION} -S git

%build
# removed --with-lmdb
%configure --libdir=%{_libdir}
%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%doc README.md AUTHORS
%{_libdir}/*.so.*
%{_bindir}/*
%license LICENSE

%files devel
%doc README.md AUTHORS
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig
%license LICENSE

%if 0%{?fedora} == 35
%files static
%{_libdir}/*.a
%{_libdir}/*.la
%endif

%if 0%{?fedora} == 36
%files static
%{_libdir}/*.a
%endif
