%global _hardened_build 1
%global debug_package %{nil}

Name:           nginx-libmodsecurity
Version:        3.0.4
Release:        8%{?dist}
Summary:        ModSecurity
License:        ASL 2.0
BuildArch:      x86_64
URL:            http://www.modsecurity.org/
Group:          System Environment/Daemons
Source0:        https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
Source1:        https://github.com/SpiderLabs/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz.asc
Source2:        LICENSE
Source100:      modsecurity.gpg
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
BuildRequires:  gnupg2
Obsoletes:      libmodsecurity
Obsoletes:      libmodsecurity-devel
Obsoletes:      libmodsecurity-static
Requires:       flex
Requires:       yajl
Requires:       curl
Requires:       ssdeep
Requires:       libxml2


%description
Libmodsecurity is one component of the ModSecurity v3 project. The library codebase serves as an interface to ModSecurity Connectors taking in web traffic and applying traditional ModSecurity processing. In general, it provides the capability to load/interpret rules written in the ModSecurity SecRules format and apply them to HTTP content provided by your application via Connectors.

%prep
cat %{SOURCE100} > %{_builddir}/modsecurity.gpg
%{gpgverify} --keyring='%{_builddir}/modsecurity.gpg' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n modsecurity-v%{VERSION}
%patch0 -p1

%build
./build.sh
./configure
make %{?_smp_mflags}

%install
%make_install
%{__install} -p -D -m 0644 %{SOURCE2} %{buildroot}%{_datarootdir}/licenses/%{NAME}/LICENSE

%files
%defattr (-,root,root)
/usr/local/modsecurity/
%{_datarootdir}/licenses/%{NAME}/LICENSE
