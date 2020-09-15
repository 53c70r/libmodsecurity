%global _hardened_build 1
%global debug_package %{nil}

Name:           libmodsecurity
Version:        3.0.4
Release:        3%{?dist}
Summary:        ModSecurity
License:        ASL 2.0
BuildArch:      x86_64
URL:            http://www.modsecurity.org/
Group:          System Environment/Daemons
Source0:        https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
Source1:        https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz.asc
Source2:        LICENSE

Patch0:         cve-2020-15598.patch

BuildRequires:  gcc-c++
BuildRequires:  pcre-devel
BuildRequires:  zlib-devel
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  GeoIP-devel
BuildRequires:  libcurl-devel
BuildRequires:  yajl-devel
BuildRequires:  libxslt-devel
BuildRequires:  ssdeep-devel
BuildRequires:  lua-devel

Requires:       flex
Requires:       yajl
Requires:       curl
Requires:       ssdeep
Requires:       lua
Requires:       libxml2

%description
Libmodsecurity is one component of the ModSecurity v3 project. The library codebase serves as an interface to ModSecurity Connectors taking in web traffic and applying traditional ModSecurity processing. In general, it provides the capability to load/interpret rules written in the ModSecurity SecRules format and apply them to HTTP content provided by your application via Connectors.

%prep
%setup -c -q
%patch0 -p1

%build
./build.sh
./configure
make %{?_smp_mflags}

%install
#%{__install} -p -D -m 644 %{SOURCE2} %{buildroot}%{_datarootdir}/licenses/%{NAME}/LICENSE
%make_install

%files
%defattr (-,root,root)
%license LICENSE
%{_datarootdir}/licenses/%{NAME}/LICENSE
/usr/local/modsecurity/
