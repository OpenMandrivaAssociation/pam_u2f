%global debug_package %{nil}

Name:		pam_u2f
Version:	1.4.0
Release:	1
Source0:	https://developers.yubico.com/pam-u2f/Releases/pam_u2f-%{version}.tar.gz
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

%package -n pamu2fcfg
Summary:       Configures PAM authentication over U2F
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description -n pamu2fcfg
pamu2fcfg provides a command line tool for configuring PAM authentication
over U2F.

%prep
%autosetup -p1

%files
%doc AUTHORS NEWS README
%license COPYING
%{_mandir}/man8/pam_u2f.8{,.*}
%{_libdir}/security/pam_u2f.so

%files -n pamu2fcfg
%{_bindir}/pamu2fcfg
%{_mandir}/man1/pamu2fcfg.1{,.*}
