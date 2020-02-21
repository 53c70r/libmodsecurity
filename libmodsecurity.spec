%global _hardened_build 1
%global debug_package %{nil}

Name:           libmodsecurity
Epoch:          1
Version:        3.0.4
Release:        1%{?dist}
Summary:        LibModSecurity
License:        ASL 2.0
URL:            http://www.modsecurity.org/
Group:          System Environment/Daemons
Source0:        https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
Source1:        https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz.asc

BuildRequires:  gcc-c++
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  GeoIP-devel
BuildRequires:  libcurl-devel
BuildRequires:  yajl-devel
BuildRequires:  lmdb-devel
BuildRequires:  libxslt-devel

%description
Libmodsecurity is one component of the ModSecurity v3 project. The library codebase serves as an interface to ModSecurity Connectors taking in web traffic and applying traditional ModSecurity processing. In general, it provides the capability to load/interpret rules written in the ModSecurity SecRules format and apply them to HTTP content provided by your application via Connectors.

%prep
%setup -q -n modsecurity-v%{version}

%build
./build.sh
./configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr (-,root,root)
/usr/local/modsecurity/
