%global debug_package %{nil}

Name:		pam_u2f
Version:	1.4.0
Release:	4
Source0:	https://developers.yubico.com/pam-u2f/Releases/pam_u2f-%{version}.tar.gz
Source1:	u2f-required.pam
Source2:	u2f-sufficient.pam
Summary:	Pluggable Authentication Module (PAM) for U2F and FIDO2
URL:		https://github.com/yubico/pam-u2f
License:	BSD-2-Clause
Group:		System/Library

BuildSystem:	cmake

BuildRequires: asciidoc
BuildRequires: gnupg2
BuildRequires: pkgconfig(pam)
BuildRequires: pkgconfig(libfido2)
BuildRequires: a2x
%description
This module implements PAM over U2F and FIDO2, providing an easy way to integrate the YubiKey (or other U2F/FIDO2 compliant authenticators) into your existing infrastructure.

%package -n pam-u2f
Summary:       Configures PAM authentication over U2F


%description -n pam-u2f
This module implements PAM over U2F and FIDO2, providing an easy way to integrate the YubiKey (or other U2F/FIDO2 compliant authenticators) into your existing infrastructure.

%package -n pamu2fcfg
Summary:       Configures PAM authentication over U2F
Requires:      pam-u2f%{?_isa} = %{version}-%{release}

%description -n pamu2fcfg
pamu2fcfg provides a command line tool for configuring PAM authentication
over U2F.

%prep
%autosetup -p1

%check
mkdir -p %{buildroot}%{_sysconfdir}/pam.d/
cp %{S:1} %{buildroot}%{_sysconfdir}/pam.d/u2f-required
cp %{S:2} %{buildroot}%{_sysconfdir}/pam.d/u2f-sufficient

%files -n pam-u2f
%doc AUTHORS NEWS README
%license COPYING
%{_sysconfdir}/pam.d/u2f*
%{_mandir}/man8/pam_u2f.8{,.*}
%{_libdir}/security/pam_u2f.so

%files -n pamu2fcfg
%{_bindir}/pamu2fcfg
%{_mandir}/man1/pamu2fcfg.1{,.*}
